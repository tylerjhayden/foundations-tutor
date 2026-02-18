"""CLI entry: `foundations-tutor` → Streamlit app."""

import subprocess
import sys
from pathlib import Path


def main() -> None:
    app = Path(__file__).parent / "app.py"
    result = subprocess.run(
        [sys.executable, "-m", "streamlit", "run", str(app)] + sys.argv[1:],
        check=False,
    )
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
