"""
generate_hooks.py

Minimal "creative batch" generator.
Takes a product description and outputs 30 ad hooks using simple frameworks.

No API keys. No dependencies. Just useful output you can paste into ads.
"""

FRAMEWORKS = [
    "Stop doing {bad_thing}. Do {good_thing}.",
    "If you struggle with {pain}, try {solution}.",
    "The fastest way to get {outcome} without {sacrifice}.",
    "I tried {solution} for 7 days. Here's what happened.",
    "Most people get {goal} wrong. Do this instead:",
    "{pain} is usually caused by {cause}. Fix it with {solution}.",
]

DEFAULTS = {
    "bad_thing": "guessing what to eat",
    "good_thing": "following a simple plan",
    "pain": "weekday dinner stress",
    "solution": "a meal plan that writes itself",
    "outcome": "healthy meals",
    "sacrifice": "extra time",
    "goal": "meal prep",
    "cause": "decision fatigue",
}

def generate(product: str, n: int = 30):
    hooks = []
    i = 0
    while len(hooks) < n:
        fw = FRAMEWORKS[i % len(FRAMEWORKS)]
        hook = fw.format(**DEFAULTS)
        hooks.append(f"{len(hooks)+1:02d}. {hook} ({product})")
        i += 1
    return hooks

if __name__ == "__main__":
    product = "Meal Prep Pro"
    hooks = generate(product, 30)
    print("\n".join(hooks))
