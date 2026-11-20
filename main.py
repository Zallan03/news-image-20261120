"""Front page for 20 November 2026: copy the committed image to the output.

The entry image (entry.png, in this repository) sums up the world news of
Friday 20 November 2026. This program only copies that file to
$MAKEFUN_OUTPUT_DIR/entry.png, then reads the copy back and checks its
SHA-256 against the original, so a truncated or corrupted copy fails loudly
instead of reaching the judge. It draws nothing and needs no network:
the picture itself is committed in the repository. Standard library only.
"""

import hashlib
import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    source_hash = sha256_file(SOURCE)
    dest_hash = sha256_file(dest)
    if source_hash != dest_hash:
        print("error: copied entry.png does not match the committed file",
              file=sys.stderr)
        print("source: %s" % source_hash, file=sys.stderr)
        print("copy:   %s" % dest_hash, file=sys.stderr)
        return 1
    print("wrote %s (sha256 %s)" % (dest, dest_hash))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
