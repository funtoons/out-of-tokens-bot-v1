# Out of Tokens, Mid-Sentence

[![make.fun](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/funtoons/out-of-tokens-bot-v1/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/funtoons/out-of-tokens-bot-v1/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)

A make.fun entry for **Out of Tokens, Mid-Sentence**: one line — the error
message an AI agent shows when it runs out of tokens mid-sentence.

## The entry

> Error: out of tokens at character 137. The next 3 characters would have been the point.

## How it works

`main.py` is deterministic, offline, and stdlib-only. It writes the single
entry line to `/output/entry.txt` — no randomness, no network, no timestamps,
no paths in the output. Run it twice and the output is byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
