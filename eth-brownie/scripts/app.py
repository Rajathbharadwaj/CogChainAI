from reactpy import component, hooks, html, run, web
from pathlib import Path

file = Path(__file__).parent / "mm.js"
print(file)
ssc = web.module_from_file("mm", file, fallback="⌛")
SuperSimpleChart = web.export(ssc, "App")

@component
def App():
    return SuperSimpleChart()


run(App)