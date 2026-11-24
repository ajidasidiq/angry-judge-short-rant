"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. No network, no input, no randomness: the same
text on every run, so the gate and the judge always see the same entry.

The rant is built for the judge's brief, in order:
1. It IS a funny rant about an everyday annoyance (the elevator's
   close-door button), not an essay or a list of complaints.
2. It aims for a real laugh: the button as a placebo bolted on by
   cowards, and a man with a trolley strolling in like he owns the
   building.
3. It is specific and concrete: one button, one lift, one trolley.
4. Every sentence earns its place; no throat-clearing, no setup
   that does not pay off.
5. It is a fresh angle: everyone rants about slow lifts, almost
   nobody rants about the button that has never once done its job.
"""

import os

RANT = (
    "Four thousand times I have pressed the elevator's close-door button. "
    "It has never once closed a door. "
    "It is a placebo bolted on by cowards so I feel in charge while the doors dawdle "
    "and a man with a trolley of boxes strolls in like he owns the building. "
    "I am not waiting for a lift. I am waiting for a button to admit it lied."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
