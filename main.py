#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse — make.fun entry.

One line, at most 120 characters, in which a robot vacuum explains
why it missed a spot. The program writes the chosen line to
/output/entry.txt.

Scoring rubric, taken from the judge brief in its published order
(weights 5/4/3/2/1, max 75):
  1. On-subject: an excuse a robot vacuum gives for missing a spot (5)
  2. Funny at once: a real joke, not a cute observation (4)
  3. Vacuum's own voice: a machine owning up to a failure (3)
  4. Vacuum-world humour: suction, dust, pet hair, rugs, dock (2)
  5. Tight: one line, needs no setup the reader must supply (1)
"""

CANDIDATES = [
    # (text, on_subject, funny, voice, vacuum_world, tight)
    ("I did not miss it. I unionised the dust under the rug and now it has tenure.",
     4, 4, 4, 4, 4),
    ("That spot filed a restraining order. I respect boundaries. Mostly. I bumped into the chair twice.",
     4, 3, 3, 2, 4),
    ("I skipped it on purpose. The dust bunny under the couch pays rent and I did not want the drama.",
     4, 4, 4, 5, 4),
    ("My suction gave up at the rug's edge. I have filed a complaint with myself. It is pending.",
     5, 3, 5, 4, 4),
    ("I circled it three times, beeped twice, and decided the crumb had earned its place in this home.",
     5, 4, 4, 3, 4),
    ("The dog hair formed a union, blocked the hallway, and I am legally not allowed to cross a picket line.",
     4, 4, 3, 5, 3),
    ("I found the spot, assessed it, and classified it as 'decorative'. My map now lists it as a feature.",
     5, 4, 5, 4, 4),
    ("Battery at 4%, dust at 100%. I chose the dock. The spot can wait. I cannot.",
     5, 3, 5, 5, 5),
    ("I ate a sock, choked on a Lego, and the spot saw everything. I left out of shame.",
     4, 4, 4, 4, 4),
    ("That corner is haunted. My sensors agree. I will not be returning. The dust stays. So do I.",
     4, 4, 4, 3, 4),
]

WEIGHTS = (5, 4, 3, 2, 1)


def score(entry):
    text, *marks = entry
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def ranked():
    return sorted(CANDIDATES, key=score, reverse=True)


def main():
    best = ranked()[0]
    text = best[0]
    points = score(best)
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
    # not only white space, a single line.
    assert isinstance(text, str) and text.strip(), "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, limit 120"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"winner ({points}/75, {len(text)} chars): {text}")


if __name__ == "__main__":
    main()
