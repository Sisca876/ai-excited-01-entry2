"""ai-excited-01 entry: copy the bundled image to /output/entry.png.

The image is a JPEG stored under the name entry.png, which the gate
accepts (PNG or JPEG, told apart by the first bytes). The copy is byte
for byte, so both grader runs write identical output.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(out_dir, "entry.png")
    try:
        os.makedirs(out_dir, exist_ok=True)
        shutil.copyfile(source, dest)
        # Fail loudly on a truncated write instead of shipping a broken image.
        if os.path.getsize(dest) != os.path.getsize(source):
            print(f"error: {dest} size mismatch after copy", file=sys.stderr)
            return 1
    except OSError as exc:
        print(f"error: could not write {dest}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
