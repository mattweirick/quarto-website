# YAML Author/Editor Formatter

This script reformats the `author` and `editor` fields in a YAML file so that each name is listed as "Given Family".

## How to Use

1. Place your original YAML file in the same directory and name it `test.yaml`.
2. Run the script using Python 3:

   python format_yaml.py

3. The formatted YAML will be saved as `formatted_test.yaml`.
4. Delete references: from the top of the yaml file.

## Notes

- Only entries with both `given` and `family` fields will be reformatted.
- The script preserves all other metadata in the YAML file.
