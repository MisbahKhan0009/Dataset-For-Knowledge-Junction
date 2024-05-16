import json

def get_id(name, map_data, field_name):
    for item in map_data:
        if item['Name'] == name:
            return item[field_name]
    return None

# Load the original JSON file
original_json_path = "/Users/misbah/Downloads/Dataset/BookUnclearned_v2.json"
with open(original_json_path, 'r') as f:
    original_data = json.load(f)

# Load the map files
publisher_map_path = "/Users/misbah/Downloads/Dataset/Cleaned data/publisher_id_map.json"
author_map_path = "/Users/misbah/Downloads/Dataset/Cleaned data/author_id_map.json"
category_map_path = "/Users/misbah/Downloads/Dataset/Cleaned data/category_id_map.json"

with open(publisher_map_path, 'r') as f:
    publisher_map_data = json.load(f)

with open(author_map_path, 'r') as f:
    author_map_data = json.load(f)

with open(category_map_path, 'r') as f:
    category_map_data = json.load(f)

# Update the original data with IDs
for book in original_data:
    # Get PublisherID
    publisher_name = book.get('Publisher')
    if publisher_name:
        publisher_id = get_id(publisher_name, publisher_map_data, 'PublisherID')
        if publisher_id is not None:
            book['PublisherID'] = publisher_id
            del book['Publisher']
    
    # Get AuthorID
    author_name = book.get('Author')
    if author_name:
        author_id = get_id(author_name, author_map_data, 'AuthorID')
        if author_id is not None:
            book['AuthorID'] = author_id
            del book['Author']
    
    # Get CategoryID
    category_name = book.get('Category')
    if category_name:
        category_id = get_id(category_name, category_map_data, 'CategoryID')
        if category_id is not None:
            book['CategoryID'] = category_id
            del book['Category']

# Save the updated data back to the original JSON file
with open(original_json_path, 'w') as f:
    json.dump(original_data, f, indent=4)
