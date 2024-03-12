import os
import json

def list_files(directory):
    """
    List all files in a directory recursively.
    """
    raw_file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            raw_file_list.append(os.path.relpath(os.path.join(root, file), directory))
    return sorted(raw_file_list)

def create_json_file(raw_file_list, output_file):
    """
    Create a JSON file with the given file list.
    """
    with open(output_file, 'w') as json_file:
        json.dump(raw_file_list, json_file, indent=4)

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cards_dir = os.path.join(script_dir, "cards")

    if not os.path.exists(cards_dir):
        print("Folder 'cards' not found in the script directory.")
        return

    raw_file_list = list_files(cards_dir)
    json_file = "raw_file_list.json"
    create_json_file(raw_file_list, json_file)
    print("JSON file created successfully.")

    # Sort the file list alphabetically
    raw_file_list_sorted = sorted(raw_file_list)
    print("File list sorted alphabetically:")
    for file in raw_file_list_sorted:
        print(file)

if __name__ == "__main__":
    main()
