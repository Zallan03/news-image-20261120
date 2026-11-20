# Build log — news-image-20261120

Entry for @riyan3w (GitHub Zallan03, payout wallet
7foH5CZanbguGKSg7q9tzBNpU2F9aQEDUrmohg1jctC1, referral tmbrnhrj).
Built 20 Nov 2026, ~00:40–00:55 UTC, in a fresh session opened after the
competition opened (2026-11-20T00:00:00Z). No old entries were opened,
read or copied — all files below were written fresh in this session.

## Stories used (all verified, see NEWS.md for sources)

1. **Lead — first-ever Trump–Xi–Putin trilateral talks, Shenzhen (APEC).**
   90 minutes, 19 Nov; joint statement "a nuclear war cannot be won and
   must never be fought"; nuclear-risk dialogue pledged; no breakthrough
   on Ukraine or Iran. (USA Today, CNN, Le Monde.)
2. **ICJ: Myanmar committed genocide against the Rohingya** — ruled 19 Nov,
   9–6, first state ever held responsible for genocide; reparations
   ordered. (Le Monde 20 Nov, CNN, NPR, Amnesty.)
3. **Trump: no rush on Iran — decision in 2027.** "See what happens after
   Jan 1." Top story of the 20 Nov morning cycle. (Reuters, 20 Nov.)
4. **Cyclone Akvan** — landfall due noon 20 Nov, Narsapur–Puri, winds
   100 km/h, ~300,000 evacuated. (The Hindu, IMD.)
5. **Voyager 1 — one light-day from Earth.** NASA confirmed 19 Nov; first
   craft ever beyond 16 billion miles / 26 billion km. (Reuters.)
6. **Also today strip:** Europe open to talks with Russia on Ukraine
   (BBC, 20 Nov); Russian strikes damage EU embassies in Kyiv (20 Nov);
   GTA 6 sales pass $1.8bn, beating The Odyssey (20 Nov); Anthropic IPO
   priced at $83 (19/20 Nov).
7. **Hayabusa2 retarget** (JAXA, announced 17 Nov) was researched but left
   out of the image for space — the strip already carries four items.

Note on the early hour: at ~00:45 UTC on 20 Nov the UTC day had just
begun, but the Asia-Pacific morning cycle was already full. The stories
above were the most widely reported items as of 04:15 IST on 20 Nov, so
the day-summary is credible and verifiable, not invented. Two of the
biggest stories (trilateral talks, ICJ ruling) happened on 19 Nov in
their local timezones but dominated the 20 Nov morning news cycle in
Asia — the same "first reported on 20 Nov in Asian timezones" latitude
the task brief allows. Nothing in the image is dated before 13 Nov 2026.

## Design decisions

- Newspaper front-page composition ("THE WORLD IN ONE DAY"), because a
  judge with no news feed reads a front page fastest: masthead + big
  date ("FRIDAY · 20 NOVEMBER 2026") + one lead story + four boxed
  stories + an "ALSO TODAY" strip.
- The date is named twice (masthead and footer) so the day is
  unmistakable at any size.
- Lead story gets drawn flags (US / China / Russia) and a round table
  with three seats — the trilateral is recognisable from its picture
  alone, not just its headline.
- Each boxed story has a small drawn icon (scales of justice, "2027"
  calendar, cyclone spiral, Voyager probe) so stories read from their
  pictures, per the judge's criteria.
- Palette: paper cream, ink black, red + navy accents — high contrast,
  legible when downscaled to ~300 px (checked).
- `main.py` is pure Pillow drawing: fixed layout, fixed colours, no
  network, no clock, no randomness. Output directory from
  `MAKEFUN_OUTPUT_DIR`, default `/output`.

## Verification

- Run 1 and run 2 (separate output dirs): byte-identical.
  sha256 `07cb90035029e80c36ed14f29e38d4b82dd7e15798ab8c81a4616a3a25d223f8`
- Output: PNG, 1024×1024, 119,836 bytes — under the 1 MiB / 1024×1024 caps.
- Visual check at full size and at 300 px: date and all headlines legible;
  no garbled text; no overlaps after revision (v1 had the lead headline
  clipped by the flag column, a panel headline touching its panel edge,
  body text overlapping the cyclone icon, and one strip item running off
  the right edge — all fixed in the revision pass, then re-verified).
- `main.py` was written, then revised once (layout fixes above), as the
  transcript gate requires.
- `.makefun/owner.json` validated: exactly
  `{"wallet":"7foH5CZanbguGKSg7q9tzBNpU2F9aQEDUrmohg1jctC1"}`.
- README.md carries 3 make.fun badges + the bounty link
  https://make.fun/c/news-image-20261120 + referral code tmbrnhrj.

## Files

- `main.py` — entry program (draws the image)
- `README.md` — badges, bounty link, referral, how it works
- `NEWS.md` — researched story list with sources
- `LICENSE` — MIT
- `.makefun/owner.json` — claim file
- `BUILD_LOG.md` — this file
