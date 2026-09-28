# Public Relations — Belajar dari Kasus

Study app interaktif untuk mata kuliah **Public Relations** (W1–W6): materi dibedah lewat kasus, bank konsep, latihan PG dengan pembahasan, essay bocoran UTS, dan simulasi ujian ber-timer.

**Live:** https://melvernmogens.github.io/pr-prep/

## Cakupan materi

| Week | Topik | Fokus UTS |
|---|---|---|
| W1 | Public Relations in Corporations | definisi PR, RACE/ROSIE |
| W2 | Internal PR | **Realistic Job Preview** (essay pasti) |
| W3 | History of PR | rhetorical theory (ethos/pathos/logos) |
| W4 | Public Opinion | **Fear Appeal** (essay pasti) |
| W5 | PR Research | metode riset PR |
| W6 | Media Writing | **Press Release** (essay pasti) |

Format UTS (bocoran): **25 PG + 4 essay**. Simulasi ujian app mengikuti format ini.

## Struktur repo

```
pr-prep/
├── content/            # SEMUA KONTEN (DSL)
│   ├── w1.md … w6.md   # materi per week + @slide (gambar slide asli)
│   ├── quiz_w*.md      # bank soal PG per week
│   └── kasus_uts.md    # 4 essay bocoran UTS + rubrik
├── src/                # engine SPA (fork relmat-prep — jangan disentuh)
├── assets/slides/      # gambar slide dosen (di-embed saat build, gitignore? tidak — di-commit utk CI)
├── build/              # parse.py (DSL+@check), build.py (inline), texcheck.js, deploy.sh
├── docs/CONTENT-SPEC.md
├── sources/            # PPTX asli (gitignore)
└── src_txt/            # teks per slide (gitignore)
```

## Format konten (DSL)

Sama seperti relmat-prep — lihat `docs/CONTENT-SPEC.md`. Tambahan: `@slide w4-06` menempel gambar slide dosen (level `@topic` setelah `@intro`, atau level `@example`).

## Build & deploy

```bash
uv run python build/parse.py          # gate: semua @check harus PASS
uv run python build/build.py          # inline → out/index.html (satu file offline)
bash build/deploy.sh                  # push ke gh-pages
```

## QA & verifikasi

- Semua angka/klaim slide diverifikasi `@check` saat build.
- Bank PG diaudit: 0 bias "jawaban benar = opsi terpanjang".
- Audit independen konten vs transkrip slide.
- Mobile-first, audit overflow 390px.

## Stack

Vanilla JS SPA single-file offline (hash router + localStorage `prprep.v1`), KaTeX + font embed. Fork dari [relmat-prep](https://github.com/MelvernMogens/relmat-prep).
