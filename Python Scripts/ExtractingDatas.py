import json

# Read the existing JSON file
json_file_path = "/Users/misbah/Downloads/Dataset/BookUnclearned_v2.json"
with open(json_file_path, 'r') as f:
    books_data = json.load(f)

# Extract unique values for Author, Publisher, Language, and Category
unique_authors = set(book['Author'] for book in books_data)
unique_publishers = set(book['Publisher'] for book in books_data)
# Assuming Language and Category are present in the JSON data
unique_languages = set(book['Language'] for book in books_data)
unique_categories = set(book['Category'] for book in books_data)

# Create dictionaries to map unique values to IDs
author_id_map = [{'AuthorID': idx + 1, 'Name': author} for idx, author in enumerate(unique_authors)]
publisher_id_map = [{'PublisherID': idx + 1, 'Name': publisher} for idx, publisher in enumerate(unique_publishers)]
language_id_map = [{'LanguageID': idx + 1, 'Name': language} for idx, language in enumerate(unique_languages)]
category_id_map = [{'CategoryID': idx + 1, 'Name': category} for idx, category in enumerate(unique_categories)]

# Write mappings to separate JSON files
with open('author_id_map.json', 'w') as f:
    json.dump(author_id_map, f, indent=4)

with open('publisher_id_map.json', 'w') as f:
    json.dump(publisher_id_map, f, indent=4)

with open('language_id_map.json', 'w') as f:
    json.dump(language_id_map, f, indent=4)

with open('category_id_map.json', 'w') as f:
    json.dump(category_id_map, f, indent=4)
