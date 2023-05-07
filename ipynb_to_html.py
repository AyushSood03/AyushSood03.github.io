import sys
import nbconvert

input_file = "FinalTutorial.ipynb"
output_file = "index.html"
exporter = nbconvert.HTMLExporter()
output, resources = exporter.from_filename(input_file)

with open(output_file, 'w', encoding="utf-8") as f:
    f.write(output)
print(f"Notebook {input_file} was converted to HTML and saved to {output_file}")