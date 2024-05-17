import json

# Function to convert date format
def convert_date_format(date_str):
    # Assuming the date string is in the format 'MM/DD/YYYY'
    month, day, year = date_str.split('/')
    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

# File path
json_file_path = "/Users/misbah/Documents/Dataset/Cleaned data/book.json"

# Read JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Iterate over each book entry and update PublicationDate
for book in data:
    book["PublicationDate"] = convert_date_format(book["PublicationDate"])

# Write updated data back to JSON file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Date format converted successfully.")
