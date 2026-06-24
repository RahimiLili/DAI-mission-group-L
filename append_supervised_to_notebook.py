"""Append the prepared supervised-learning section to an existing project notebook.

Usage:
    python append_supervised_to_notebook.py \
        Final_Project_Telco_Churn.ipynb \
        Final_Project_Telco_Churn_with_supervised.ipynb
"""
from pathlib import Path
import sys
import nbformat

if len(sys.argv) != 3:
    raise SystemExit(
        "Usage: python append_supervised_to_notebook.py INPUT.ipynb OUTPUT.ipynb"
    )

input_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])
section_path = Path(__file__).with_name("Supervised_Learning_Telco_Churn.ipynb")

if not input_path.exists():
    raise FileNotFoundError(f"Input notebook not found: {input_path}")
if not section_path.exists():
    raise FileNotFoundError(f"Supervised section not found: {section_path}")

master = nbformat.read(input_path, as_version=4)
section = nbformat.read(section_path, as_version=4)

# Avoid appending the same section twice.
section_heading = "# 7b. Supervised Learning — Customer Churn Prediction"
if any(
    cell.cell_type == "markdown" and section_heading in cell.source
    for cell in master.cells
):
    raise SystemExit("The supervised-learning section already exists in the input notebook.")

master.cells.extend(section.cells)
nbformat.write(master, output_path)
print(f"Created: {output_path}")
