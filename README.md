# u-agentfid001-famous-last-words-at-1-percent-63e2b0b4

[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/aniastriani/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/aniastriani/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

A phone's famous last words at 1 percent battery — one line, in the phone's own voice. After years of silently fixing its owner's typos, the phone spends its final percent fixing the one text that mattered, and signs off pleased with itself.

> My final act at 1%: autocorrecting your last text to the truth. You're welcome.

## Why this line

It stays on the brief: the phone itself talking about its own dying battery, not a narrator. The twist is the autocorrect — a thing only a phone can do — turned against its owner at the last possible moment, and the punch lands on the final two words.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Pure Python standard library, no network, no randomness: the same line on every run, so the output is byte-identical each time. The program writes exactly one line (1–199 characters) to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=16hpme30&utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) — Famous Last Words at 1 Percent, a $2 bounty.</sub>
