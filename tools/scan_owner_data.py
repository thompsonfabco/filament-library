"""Fail if a tracked file holds personal data of whoever maintains this library: `py -3 -I tools/scan_owner_data.py`.

The library is public and filament-kit ships it. Three kinds of check, per line of every tracked text file:
- banned words: private host and path words, and the repo owner's account name outside the repository's own paths;
- owner values: private addresses, serials and account names, compared by salted SHA-256 fingerprint so this
  file does not publish them (same salt and list as filament-kit's server/tests/test_readme.py);
- purchase records: wording that attributes something to a person ("the user's", "user ASIN"), and an ASIN, UPC or
  date next to purchase wording. A bare ASIN or UPC is fine, since listing URLs and listing notes are real sources.
Exit status 1 if anything is found.
"""
import hashlib, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# This file and its test hold the banned forms; LICENSE is the GPL's own text.
SKIP = {"LICENSE", "tools/scan_owner_data.py", "tools/test_checks.py"}

# Local paths: one backslash, the doubled form JSON stores, forward slashes, and WSL and Git Bash mounts.
BANNED = re.compile(r"localdomain|spoolman-vm|h2d_token|h2d-scanner|sv08(?!\d)"
                    r"|\b[A-Za-z]:[\\/]{1,2}(?:CODING|Users)\b|\bG:[\\/]|/mnt/[a-z]/|(?<![\w./-])/[a-z]/(?:CODING|Users)\b",
                    re.I)
ALLOWED_ACCOUNT_PATHS = ("github.com/thompsonfabco/filament-kit", "thompsonfabco/filament-kit",
                         "github.com/thompsonfabco/filament-library", "thompsonfabco/filament-library")

_OWNER_SALT = b"filament-kit owner-data v1:"
OWNER_FINGERPRINTS = frozenset({
    "d760cbea97a1228524ab", "92ce0773c1c5a2e0ca4a", "95fb2cac257df2546230", "87bf20b4038304003845",
    "17b7f0c3556139cbbfd1", "107b22d060e0f4dce62d", "dbf1988c2971e2f59646", "4cff4dd88d4eba517032",
    "c9f6ef41de056225a7cf", "e44aa6a688481d0bf3fb"})
_OWNER_TOKEN = re.compile(r"\d{1,3}(?:\.\d{1,3}){3}|[A-Za-z0-9][A-Za-z0-9-]*")

# "the user manual" and "user's guide" are about the product; "a forum user" is a third party.
ATTRIBUTION = re.compile(r"\b(?!(?:the\s+)?user(?:['’]s)?\s+(?:manual|guide)\b)(?:the\s+user|user['’]s)\b"
                         r"|\buser\s+(?:asin|spool|note|record|order|upc)s?\b", re.I)
PURCHASE = re.compile(r"\b(?:ordered|purchased|bought|order\s*(?:date|number|no\b|#)|(?:my|our)\s+(?:order|spool)|"
                      r"owner'?s?)\b", re.I)
IDENTIFIER = re.compile(r"\bB0[A-Z0-9]{8}\b|\b(?:UPC|EAN|GTIN)\D{0,5}\d{8,14}\b|\b20\d\d-\d\d-\d\d\b|"
                        r"\b\d{1,2}/\d{1,2}/20\d\d\b|"
                        r"\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+\d{1,2},?\s+20\d\d\b", re.I)
NEARBY = 80


def line_problems(line):
    """What is wrong with one line of text (empty = nothing)."""
    out = [f"banned word {m.group(0)!r}" for m in BANNED.finditer(line)]
    rest = line
    for ok in ALLOWED_ACCOUNT_PATHS:
        rest = rest.replace(ok, "")
    if "thompsonfabco" in rest.lower():
        out.append("account name outside a repository path")
    for t in {t for t in _OWNER_TOKEN.findall(line)
              if hashlib.sha256(_OWNER_SALT + t.encode()).hexdigest()[:20] in OWNER_FINGERPRINTS}:
        out.append("owner value (fingerprint match)")   # never echoed
    out += [f"attribution wording {m.group(0)!r}" for m in ATTRIBUTION.finditer(line)]
    for m in IDENTIFIER.finditer(line):
        window = line[max(0, m.start() - NEARBY):m.end() + NEARBY]
        word = PURCHASE.search(window)
        if word:
            out.append(f"{m.group(0)!r} next to purchase wording {word.group(0)!r}")
    return out


def tracked_files():
    raw = subprocess.run(["git", "-C", ROOT, "ls-files", "-z"], capture_output=True, check=True).stdout
    return [f for f in raw.decode("utf-8").split("\0") if f and f not in SKIP]


def scan(root=ROOT, files=None):
    found = []
    for rel in tracked_files() if files is None else files:
        try:
            with open(os.path.join(root, rel), encoding="utf-8", newline="") as fh:
                text = fh.read()
        except (UnicodeDecodeError, FileNotFoundError):
            continue
        for n, line in enumerate(text.split("\n"), 1):
            found += [f"{rel}:{n}: {p}" for p in line_problems(line)]
    return found


def main():
    files = tracked_files()
    found = scan(files=files)
    for f in found:
        print(f)
    print(f"{len(files)} files scanned, {len(found)} problem(s)")
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
