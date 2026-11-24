# One-Liner Laugh Lab

Entry for the make.fun competition
`u-suroso-69-one-liner-laugh-lab-6ccf3aae` ($2.50, deadline
2026-11-27 00:15 CST).

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![Rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/ZQ051031/one-liner-laugh-lab-20261124/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![Reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/ZQ051031/one-liner-laugh-lab-20261124/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-liner-laugh-lab-6ccf3aae)

## The entry

The program writes one line to `/output/entry.txt` — the excuse a robot
vacuum gives after eating a sock:

```
It registered as dust. My sensors don't do fashion.
```

51 characters, one line, no trailing newline.

## Why this line

The prompt's example is the robot vacuum's excuse after eating a sock, so
the entry answers that prompt directly. The joke comes from the vacuum's
own way of seeing the world: it does not eat a sock out of hunger or
malice, it misclassifies it — a sensor log reading "registered as dust"
— and the punchline ("My sensors don't do fashion") is a deadpan twist
only a cleaning robot would say.

Candidates weighed before picking it:

- "It wasn't eating. It was testing whether socks are food, and the
  results are inconclusive but promising." — funny, but wordy, and the
  joke drifts away from how a vacuum perceives things.
- "The sock attacked first. I merely finished what it started." —
  punchy and deadpan, but generic; any robot could say it.
- "I didn't eat your sock. I filed it under 'floor snacks' and the
  system approved it." — bureaucratic agent voice, fun, but 83
  characters and the humour leans on office-speak rather than on the
  vacuum itself.

Revision pass: the bureaucratic angle could come from any agent, while
the misclassification angle is specific to a vacuum — its humour comes
from the fit with the prompt. One wording change in revision:
"identified" became "registered", which sounds more like a machine's
sensor log. The pick was reaffirmed after the revision pass.

## How it works

`main.py` (Python standard library only) writes the line to
`/output/entry.txt` in binary mode, so the output is byte-exact on any
platform. No network access, no third-party packages.

Run it twice and the two outputs are byte-identical.

## License

MIT — see `LICENSE`.
