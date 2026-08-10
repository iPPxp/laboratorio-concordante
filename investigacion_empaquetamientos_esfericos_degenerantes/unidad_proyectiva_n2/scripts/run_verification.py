"""Regenera el resultado computado n=2 dentro del directorio de investigación."""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "src"))

from projective_n2 import verification_report


def main() -> None:
    output = PROJECT / "data" / "results_n2.json"
    output.write_text(
        json.dumps(verification_report(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"RESULTADO_COMPUTADO={output}")


if __name__ == "__main__":
    main()
