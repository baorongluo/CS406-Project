import argparse
import json
import os
from jinja2 import Environment, FileSystemLoader

def main():
    parser = argparse.ArgumentParser(description="Render Jinja2 templates with variables.")
    parser.add_argument("template", help="Path to the Jinja2 template file")
    parser.add_argument("variables", help="Path to the JSON variable file")
    parser.add_argument("-o", "--output", help="Output HTML file", default="output.html")
    args = parser.parse_args()
  
    if not os.path.isfile(args.template):
        print(f"Template file not found: {args.template}")
        return
    if not os.path.isfile(args.variables):
        print(f"Variables file not found: {args.variables}")
        return

    with open(args.variables, 'r', encoding='utf-8') as f:
        variables = json.load(f)

    env = Environment(loader=FileSystemLoader(searchpath='templates'))

    # Get the template from template.html
    template = env.get_template(os.path.basename(args.template))

    # Render the template with the variables
    output = template.render(**variables)

    # Write the rendered output to output file
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Output written to {args.output}")

if __name__ == "__main__":
    main()
