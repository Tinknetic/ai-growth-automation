import argparse
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
    # --- CLI args (the upgrade) ---
    parser = argparse.ArgumentParser(description="Generate a creative batch for a product.")
    parser.add_argument("product", nargs="?", default="Meal Prep Pro", help="Product name, e.g. 'Meal Prep Pro'")
    parser.add_argument("--persona", choices=PERSONAS.keys(), default="busy_professional",
                        help="Persona key")
    parser.add_argument("--angle", choices=[label for (label, _) in ANGLES], default="time",
                        help="Angle label")
    parser.add_argument("--out", default=None, help="Optional output filepath")
    args = parser.parse_args()
    # -----------------------------

    product_name = args.product
    persona = PERSONAS[args.persona]

    angle_map = {label: desc for (label, desc) in ANGLES}
    angle_label = args.angle
    angle_desc = angle_map[angle_label]

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

    if args.out:
        outfile = args.out
    else:
        slug = product_name.lower().replace(" ", "-")
        outfile = f"sample_outputs/{slug}_{date.today().isoformat()}.txt"

    write_output(outfile, text)

    print(text)
    print(f"\nSaved to: {outfile}")


if __name__ == "__main__":
    main()
