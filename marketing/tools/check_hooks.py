#!/usr/bin/env python3
"""Controlla che gli hook di una settimana siano tutti diversi tra loro e dal registro.

Uso: check_hooks.py <hooks-settimana.md> [hooks-registry.md] [--soglia 0.6]
Formato righe: `qualcosa | file | hook` (le righe senza `|` sono ignorate).
Esce con codice 1 se trova hook uguali o troppo simili.
"""
import re
import sys
from difflib import SequenceMatcher

STOP = {"the", "a", "an", "to", "of", "in", "on", "for", "and", "is", "it", "this", "that", "you", "your", "our", "we"}


def load(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            parts = [p.strip() for p in line.strip().strip("|").split("|")]
            if len(parts) < 3 or set(parts[-1]) <= set("-: ") or parts[-1].lower() == "hook":
                continue
            rows.append((parts[-2], parts[-1]))
    return rows


def norm(text):
    return re.sub(r"[^a-z0-9 ]+", " ", text.lower()).split()


def similarity(a, b):
    wa, wb = norm(a), norm(b)
    seq = SequenceMatcher(None, " ".join(wa), " ".join(wb)).ratio()
    sa, sb = set(wa) - STOP, set(wb) - STOP
    jac = len(sa & sb) / len(sa | sb) if sa | sb else 1.0
    return max(seq, jac)


def opening(text):
    return " ".join(norm(text)[:2])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    soglia = 0.6
    if "--soglia" in sys.argv:
        soglia = float(sys.argv[sys.argv.index("--soglia") + 1])
        args.remove(sys.argv[sys.argv.index("--soglia") + 1])
    if not args:
        sys.exit(__doc__)
    week = load(args[0])
    registry = load(args[1]) if len(args) > 1 else []
    if not week:
        sys.exit(f"Nessun hook trovato in {args[0]}")

    problems = []
    for i, (fa, ha) in enumerate(week):
        for fb, hb in week[i + 1:]:
            s = similarity(ha, hb)
            if s >= soglia:
                problems.append(f"TROPPO SIMILI ({s:.2f}): {fa}: \"{ha}\"  <->  {fb}: \"{hb}\"")
            elif opening(ha) == opening(hb):
                problems.append(f"STESSO INIZIO: {fa}: \"{ha}\"  <->  {fb}: \"{hb}\"")
        for fb, hb in registry:
            s = similarity(ha, hb)
            if s >= soglia:
                problems.append(f"GIA' USATO ({s:.2f}): {fa}: \"{ha}\"  <->  registro {fb}: \"{hb}\"")

    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problemi su {len(week)} hook.")
        sys.exit(1)
    print(f"OK: {len(week)} hook, tutti diversi.")


if __name__ == "__main__":
    main()
