# Public Relations — Belajar dari Kasus

**Study app interaktif untuk mata kuliah Public Relations (W1–W6): materi dibedah lewat kasus, bank konsep, latihan PG dengan pembahasan, essay bocoran UTS, dan simulasi ujian ber-timer.**

Dibuat untuk persiapan UTS. Satu file HTML offline, mobile-first, progres tersimpan di browser.

**Live:** https://melvernmogens.github.io/pr-prep/

## Isi

| | Jumlah |
|---|---|
| Topik materi (W1–W6 + studi kasus) | 30 |
| Contoh kasus dengan langkah pengerjaan | 76 |
| Konsep di bank konsep | 118 |
| Soal PG dengan pembahasan (9 per week) | 54 |
| Essay bocoran UTS + jawaban model per poin rubrik | 4 |
| Gambar slide dosen yang ditempel ke materi | 29 |

| Week | Topik | Fokus UTS |
|---|---|---|
| W1 | Public Relations in Corporations | definisi PR, RACE/ROSIE |
| W2 | Internal PR | **Realistic Job Preview** (essay pasti) |
| W3 | History of PR | rhetorical theory (ethos/pathos/logos) |
| W4 | Public Opinion | **Fear Appeal** (essay pasti) |
| W5 | PR Research | metode riset PR |
| W6 | Media Writing | **Press Release** (essay pasti) |

Format UTS (bocoran): **25 PG + 4 essay**. Simulasi ujian mengikuti format ini.

## Fitur

- **Materi** per week dan per topik, dengan intro, contoh kasus, jebakan umum, dan gambar slide asli (`@slide`).
- **Bank konsep** — semua konsep dalam satu halaman, tiap konsep terhubung ke topiknya.
- **Latihan PG** — tiap soal punya pembahasan kenapa jawaban benar dan kenapa pengecoh salah.
- **Studi kasus / essay UTS** — 4 essay dengan rubrik langkah dan jawaban model.
- **Simulasi ujian** ber-timer.
- Navigasi: Beranda · Materi · Konsep · Latihan · Ujian. Progres disimpan di `localStorage` (`prprep.v1`).

## Cara kerja

Semua konten ditulis sebagai Markdown dengan DSL sederhana (`@topic`, `@example`, `@q`, `@why`, `@slide`, `@check`, …) di `content/`. `build/parse.py` mem-parse konten dan menjalankan semua `@check` (klaim/angka yang diverifikasi) sebagai gate. `build/build.py` meng-inline engine, konten, KaTeX, font, dan gambar slide menjadi satu file `out/index.html`.

Spesifikasi format: [docs/CONTENT-SPEC.md](docs/CONTENT-SPEC.md).

## Build & deploy

Butuh Python 3.12+ (atau [uv](https://docs.astral.sh/uv/)) dan Node.js 22 untuk pengecekan.

```bash
uv run python build/parse.py      # gate: semua @check harus PASS
uv run python build/build.py      # inline -> out/index.html (satu file offline)
node build/texcheck.js            # cek semua string KaTeX
bash build/deploy.sh              # build ulang lalu push out/ ke branch gh-pages
```

Tanpa uv, `python3 build/parse.py` dan `python3 build/build.py` juga jalan (tanpa dependensi). CI menjalankan parse, build, `node --check` dan texcheck di setiap push ke `main`.

## Struktur

```
content/            semua konten (DSL)
  w1.md … w6.md     materi per week
  quiz_w*.md        bank soal PG per week
  kasus_uts.md      4 essay bocoran UTS + rubrik
src/                engine SPA (vanilla JS, hash router), fork dari relmat-prep
assets/             KaTeX, font embed, assets/slides/ (gambar slide dosen)
build/              parse.py, build.py, texcheck.js, deploy.sh
docs/CONTENT-SPEC.md
```

## QA

- Semua angka/klaim slide diverifikasi `@check` saat build (22 check).
- Bank PG diaudit: tidak ada bias "jawaban benar = opsi terpanjang".
- Konten diaudit ulang terhadap transkrip slide.
- Mobile-first, dicek overflow di lebar 390px.

## Kredit

Engine diambil dari [relmat-prep](https://github.com/MelvernMogens/relmat-prep). Gambar slide milik dosen pengampu mata kuliah, dipakai untuk belajar.

Built by [Melvern Mogens](https://github.com/MelvernMogens).
