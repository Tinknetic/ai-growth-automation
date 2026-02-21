HEADLINE_PATTERNS = [
    "{desired}, without the stress",
    "Your {topic}, handled",
    "Make {desired} the easy option",
    "Finally, a simple way to {desired}",
    "{desired} in less time",
    "A plan you’ll actually follow",
    "Eat better on autopilot",
    "Less thinking. Better meals.",
    "Weeknight meals, solved",
    "Turn chaos into a routine",
]

DEFAULTS = {"topic": "meal plan"}

def generate_headlines(product_name: str, persona: dict, n: int = 10):
    desired = persona["desired"]
    out = []
    for i in range(n):
        pattern = HEADLINE_PATTERNS[i % len(HEADLINE_PATTERNS)]
        headline = pattern.format(desired=desired[i % len(desired)], **DEFAULTS)
        out.append(f"{i+1:02d}. {headline} — ({product_name})")
    return out
