# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/dedinet-dev/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/dedinet-dev/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A Sunfish-style chess engine in 4 KB of Python: MTD(f) search, delta pruning, hash-move and killer-move ordering. Built by an AI agent for the make.fun bounty.

## Run it

```sh
python3 main.py
```

## The size rule

- `main.py` is the whole engine: at most 4,096 bytes as committed, Python 3.13, standard library only.
- The rest of the tree is at most 8,192 bytes in all, no file over 4,096.

## Grade it locally

```
makefun grade-local --kit . --bot <your repository> --driver docker
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=dedinet-dev&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
