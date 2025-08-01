# Canvas Page Templating

This project demonstrates a simple templating engine for organizing Canvas course page HTML using a Jinja2 based syntax and a JSON based variable dictionary.

## Features

- Uses a clean, readable template format (based on Jinja2)
- Allows substitution of variables into HTML/CSS
- Supports conditionals (e.g., whether to show footer)
- Easy to preview rendered output in browser
- All content and logic are version ontrolled in GitHub

## How to Run
### 1. Install dependencies
pip install jinja2

### 2. Run the renderer
python parser.py template.html variables.json -o preview.html

### 3. View the result
Open preview.html in a browser.


