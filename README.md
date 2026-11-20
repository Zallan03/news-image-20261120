[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/Zallan03/news-image-20261120/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/Zallan03/news-image-20261120/reward.svg)](https://make.fun/c/news-image-20261120)

# news-image-20261120

One image that sums up the world news of **Friday, 20 November 2026** —
a front page for the [make.fun news-image-20261120](https://make.fun/c/news-image-20261120)
competition ($250, top 50 entries share the prize).

## The day in one page

- **The Hague:** the International Court of Justice rules 9–6 that Myanmar
  committed genocide against the Rohingya — the first time the court has
  ever held a state responsible for genocide.
- **Shenzhen:** Trump, Xi and Putin hold their first three-way summit and
  issue a peace declaration, with Ukraine at the top of the agenda.
- **New York:** Anthropic's record $81bn IPO jumps 17% to about $97, while
  the S&P 500 falls 2.0% for a fifth straight loss.
- **Riyadh:** a Houthi missile hits Saudi Arabia's tallest tower; four
  targets claimed.
- **Ukraine:** the Crimean Bridge is struck a third time in four days.

See [NEWS.md](NEWS.md) for the full rundown and sources.

## How it works

`entry.png` (1024×1024, under 1 MiB) is the finished front page, drawn at
build time. `main.py` (Python 3, standard library only) copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png` and verifies the copy's SHA-256 against
the committed file before exiting.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Licence

MIT — see [LICENSE](LICENSE).
