#!/usr/bin/env python3
"""Audit quiz W5+W6: posisi jawaban benar, panjang opsi benar vs pengecoh, jumlah kasus."""
import json
from collections import Counter

d = json.load(open("build/content.json"))
for wk in (5, 6):
    qs = [q for q in d["quiz"] if q["week"] == wk]
    pos = Counter(q["ans"] for q in qs)
    print(f"W{wk}: {len(qs)} soal | posisi benar (0-3):", dict(sorted(pos.items())))
    for q in qs:
        L = [len(o) for o in q["opts"]]
        a = q["ans"]
        others = sorted(L[:a] + L[a + 1:])
        longest_wrong = others[-1]
        ratio = L[a] / longest_wrong if longest_wrong else 0
        flags = []
        if L[a] == max(L) and ratio > 1.3:
            flags.append(f"LONGEST>{ratio:.2f}x")
        if L[a] == max(L):
            flags.append("longest")
        kasus = "kasus" if q["q"][0].lower().startswith("kasus") else "    "
        print(f"  {q['id']} ans={a} len={L[a]} maxwrong={longest_wrong} {' '.join(flags) or 'ok'} [{kasus}] {q['topic']} :: {q['q'][0][:58]}")
    nk = sum(1 for q in qs if q["q"][0].lower().startswith("kasus"))
    print(f"  -> soal ber-kasus: {nk}/{len(qs)} = {nk/len(qs):.0%}")
