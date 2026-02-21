CTAS = [
    "Start your plan",
    "Get my meal plan",
    "Try it free",
    "Build my week",
    "Plan in 60 seconds",
    "See my options",
    "Generate my meals",
    "Make this easier",
    "Start eating better",
    "Skip the stress",
]

def generate_ctas(n: int = 10):
    return [f"{i+1:02d}. {CTAS[i % len(CTAS)]}" for i in range(n)]
