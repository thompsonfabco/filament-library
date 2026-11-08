"""Tests for the authoring rules and the CI checks: `py -3 -I -m unittest discover -s tools -p "test_*.py"`."""
import copy, json, os, subprocess, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_paths, fl, scan_owner_data as scan

GOOD = {"schema_version": 1, "vendor": "V", "product": "P", "material": "PLA", "colors": [], "fields": {},
        "published_ranges": {}, "conflicts": [], "source_quality": "official_page",
        "sources": ["https://example.com/p"], "updated": "2026-11-08"}


def entry(**changes):
    e = copy.deepcopy(GOOD)
    e.update(changes)
    return e


class ValidateMatchesTheKit(unittest.TestCase):
    def test_good_entry(self):
        self.assertEqual(fl.validate(entry()), [])

    def test_orca_parent_accepted_without_suffix(self):
        self.assertEqual(fl.validate(entry(orca_parent="Generic PLA")), [])
        self.assertTrue(fl.validate(entry(orca_parent="Generic PLA @System")))
        self.assertTrue(fl.validate(entry(orca_parent=" ")))

    def test_updated_is_strict(self):
        for bad in ("20261108", "2026-W45-7", "2026-11-08T00:00:00", "2026-13-01", 20261108, None):
            self.assertIn("updated must be a YYYY-MM-DD date", fl.validate(entry(updated=bad)), bad)

    def test_empty_field_value_is_reported_not_raised(self):
        errs = fl.validate(entry(fields={"nozzle_temperature_range_low": []}))
        self.assertTrue(any("one-element" in e for e in errs))

    def test_malformed_url_is_reported_not_raised(self):
        self.assertTrue(any("not an http(s) URL" in e for e in fl.validate(entry(sources=["http://[bad"]))))


class Scan(unittest.TestCase):
    def assertFlags(self, line):
        self.assertTrue(scan.line_problems(line), line)

    def assertClean(self, line):
        self.assertEqual(scan.line_problems(line), [], line)

    def test_purchase_records(self):
        for line in ("The user's ASIN B0AAAAAAAA now redirects",
                     "User ASIN B0AAAAAAAA is titled 'X'",
                     "Amazon B0AAAAAAAA (user ASIN, search snippet)",
                     "User spool is a factory second",
                     "(user note)",
                     "while the user's record describes it",
                     "User's single-spool UPC 012345678905 was not found",
                     "B0AAAAAAAA (ordered 2026-01-30 as 'X')",
                     "purchased 01/30/2026 from a shop",
                     "bought on January 30, 2026",
                     "order date 2026-01-30",
                     "UPC 012345678905 from my spool"):
            self.assertFlags(line)

    def test_published_listing_data_is_fine(self):
        for line in ('"https://www.amazon.com/dp/B0AAAAAAAA",',
                     "Amazon B0AAAAAAAA (2-pack, UPC 012345678905, MPN X): read 2026-11-02",
                     "shop_ordered/54291/pic/Datasheet/TDS.pdf",
                     "not a user drying spec",
                     "User guide spec block 220-250C",
                     "https://example.com/pages/fibreheart-user-manual",
                     "the user manual lists 200C",
                     "the user's guide lists 200C",
                     "the page tells users to match temperature to speed",
                     "A deal-forum user claims the line is being discontinued",
                     "staff reply to a Bambu P1S user: nozzle 230C",
                     "a user test report on the brand's own blog",
                     "Connection refused (ECONNREFUSED 5.149.162.4:443)"):
            self.assertClean(line)

    def test_host_and_path_words(self):
        for line in ("printer.localdomain", "the SV08 MAX generator", r"Source: C:\CODING\x\specs.json", r"G:\x",
                     "https://thompsonfabco.example/x"):
            self.assertFlags(line)
        self.assertClean("https://github.com/thompsonfabco/filament-kit and thompsonfabco/filament-library")

    def test_scan_reads_files_and_reports_line_numbers(self):
        with tempfile.TemporaryDirectory() as d:
            with open(os.path.join(d, "a.md"), "w", encoding="utf-8") as fh:
                fh.write("fine\nthe user's spool\n")
            self.assertEqual(len(scan.scan(d, ["a.md"])), 1)
            self.assertTrue(scan.scan(d, ["a.md"])[0].startswith("a.md:2:"))


class Paths(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.d = self._tmp.name
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.com")
        self.git("config", "user.name", "test")
        self.git("config", "commit.gpgsign", "false")

    def git(self, *args):
        subprocess.run(["git", "-C", self.d, *args], capture_output=True, check=True)

    def version(self, n, *paths, commit=True):
        with open(os.path.join(self.d, "index.json"), "w", encoding="utf-8") as fh:
            json.dump({"library_version": n, "entries": [{"path": p} for p in paths]}, fh)
        if commit:
            self.git("add", "index.json")
            self.git("commit", "-q", "-m", f"v{n}")

    def test_additions_pass(self):
        self.version(1, "library/a/b.json")
        self.version(2, "library/a/b.json", "library/a/c.json")
        self.assertEqual(check_paths.missing_paths(self.d), {})

    def test_a_removed_path_fails_with_its_last_version(self):
        self.version(1, "library/a/b.json", "library/a/c.json")
        self.version(2, "library/a/b.json", "library/a/c.json", "library/a/d.json")
        self.version(3, "library/a/d.json", commit=False)
        self.assertEqual(check_paths.missing_paths(self.d), {"library/a/b.json": 2, "library/a/c.json": 2})

    def test_a_path_dropped_in_an_old_commit_still_fails(self):
        self.version(1, "library/a/b.json")
        self.version(2, "library/a/c.json")
        self.version(3, "library/a/c.json", "library/a/d.json")
        self.assertEqual(check_paths.missing_paths(self.d), {"library/a/b.json": 1})


if __name__ == "__main__":
    unittest.main()
