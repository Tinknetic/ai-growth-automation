import os
from datetime import date

from generators.personas import PERSONAS
from generators.angles import ANGLES
from generators.hooks import generate_hooks
from generators.headlines import generate_headlines
from generators.ctas import generate_ctas


def write_output(path: str, text: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    product_name = "Meal Prep Pro"  # change this when needed

    # Pick one persona to generate a full batch for (fast + focused).
    persona_key = "busy_professional"
    persona = PERSONAS[persona_key]

    # Pick one “primary angle” for hooks (keeps output coherent).
    angle_label, angle_desc = ANGLES[0]  # time

    hooks = generate_hooks(product_name, persona, angle_label, angle_desc, n=30)
    headlines = generate_headlines(product_name, persona, n=10)
    ctas = generate_ctas(n=10)

    angles = [f"{i+1:02d}. [{label}] {desc}" for i, (label, desc) in enumerate(ANGLES)]
    personas = [f"- {p['name']}: pains={p['pains']}; desired={p['desired']}" for p in PERSONAS.values()]

    output = []
    output.append(f"# Creative Batch — {product_name}")
    output.append(f"Date: {date.today().isoformat()}")
    output.append("")
    output.append("## Personas")
    output.extend(personas)
    output.append("")
    output.append("## Angles")
    output.extend(angles)
    output.append("")
    output.append(f"## Hooks (30) — Persona: {persona['name']} | Angle: {angle_label} ({angle_desc})")
    output.extend(hooks)
    output.append("")
    output.append("## Headlines (10)")
    output.extend(headlines)
    output.append("")
    output.append("## CTAs (10)")
    output.extend(ctas)
    output.append("")

    text = "\n".join(output)

    outfile = f"sample_outputs/{product_name.lower().replace(' ', '-')}_{date.today().isoformat()}.txt"
    write_output(outfile, text)

    print(text)
    print(f"\nSaved to: {outfile}")


if __name__ == "__main__":
    main()
