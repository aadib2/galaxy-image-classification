import json
import os

notebook_path = "Project_Notebook.ipynb"  # change this to your filename

# Load notebook
with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

widgets = nb.get("metadata", {}).get("widgets", {})
widget_state = widgets.get("application/vnd.jupyter.widget-state+json", {})

# If "state" is missing, wrap the current content inside "state"
if "state" not in widget_state:
    nb["metadata"]["widgets"]["application/vnd.jupyter.widget-state+json"] = {
        "state": widget_state
    }
    print("✅ Fixed: Added 'state' key to widgets metadata.")
else:
    print("ℹ️ Notebook already has valid widget metadata.")

# Save the notebook
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1)

print(f"📁 Saved fixed notebook to: {os.path.abspath(notebook_path)}")