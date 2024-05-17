import json

# Path to the JSON file
json_file_path = "/Users/misbah/Documents/Dataset/Cleaned data/book.json"

# Function to adjust date format
def adjust_date_format(date_str):
    parts = date_str.split('-')
    return f"{parts[1]}-{parts[2]}-{parts[0]}"

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Adjust date format for each entry
for entry in data:
    if 'PublicationDate' in entry:
        entry['PublicationDate'] = adjust_date_format(entry['PublicationDate'])

# Write the updated data back to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Date format adjusted successfully!")
