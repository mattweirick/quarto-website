import yaml

# Load the original YAML file
with open("test.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# Function to reformat names in a list of dictionaries
def reformat_names(name_list):
    return [f"{entry['given']} {entry['family']}" for entry in name_list if 'given' in entry and 'family' in entry]

# Process each reference entry
for ref in data.get("references", []):
    if "author" in ref and isinstance(ref["author"], list):
        ref["author"] = reformat_names(ref["author"])
    if "editor" in ref and isinstance(ref["editor"], list):
        ref["editor"] = reformat_names(ref["editor"])

# Save the formatted YAML to a new file
with open("formatted_test.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True, sort_keys=False)
