import json
import random

# Path to the JSON file
json_file_path = "/Users/misbah/Documents/Dataset/Cleaned data/book.json"

# Function to generate a random ISBN
def generate_random_isbn():
    new_isbn = str(random.randint(10000000, 99999999))
    while new_isbn.startswith('9'):
        new_isbn = str(random.randint(10000000, 99999999))
    return int(new_isbn)

# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Create a set to store seen ISBNs
seen_isbns = set()

# Iterate over each entry in the JSON data
for entry in data:
    isbn = entry.get('ISBN')
    if isbn in seen_isbns:
        new_isbn = generate_random_isbn()
        while new_isbn in seen_isbns:
            new_isbn = generate_random_isbn()
        entry['ISBN'] = new_isbn
    else:
        seen_isbns.add(isbn)

# Write the updated data back to the JSON file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Duplicate ISBNs replaced successfully!")
