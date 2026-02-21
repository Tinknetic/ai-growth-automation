FRAMEWORKS = [
    "Stop {pain}. Start {desired}.",
    "If you struggle with {pain}, try {solution}.",
    "The fastest way to get {desired} without {sacrifice}.",
    "I tried {solution} for 7 days—here’s what happened.",
    "Most people mess up {topic}. Do this instead:",
    "{pain} is usually caused by {cause}. Fix it with {solution}.",
    "What if {desired} was the default?",
    "A simple way to get {desired} even when {constraint}.",
]

DEFAULTS = {
    "solution": "a meal plan that’s done for you",
    "sacrifice": "spending Sunday meal-prepping",
    "topic": "meal planning",
    "cause": "decision fatigue",
    "constraint": "you’re busy",
}

def generate_hooks(product_name: str, persona: dict, angle_label: str, angle_desc: str, n: int = 30):
    pains = persona["pains"]
    desired = persona["desired"]
    hooks = []
    i = 0

    while len(hooks) < n:
        fw = FRAMEWORKS[i % len(FRAMEWORKS)]
        hook = fw.format(
            pain=pains[i % len(pains)],
            desired=desired[i % len(desired)],
            **DEFAULTS
        )
        hooks.append(f"{len(hooks)+1:02d}. [{persona['name']}] [{angle_label}] {hook} — ({product_name})")
        i += 1

    return hooks
