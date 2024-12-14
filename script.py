import json

# File paths
input_coco_file = "Months-Digits-5.v4i.coco/train/_annotations.coco.json"  # Replace with your file name if different
output_bulk_file = "bulk_annotations.json"

# Load COCO JSON
with open(input_coco_file, "r") as file:
    coco_data = json.load(file)

# Map category IDs to names
category_mapping = {cat["id"]: cat["name"] for cat in coco_data["categories"]}

# Prepare Elasticsearch bulk data
bulk_data = []
index_name = "passport_labeled_images_ziad_mahmoud"  # Elasticsearch index name

for annotation in coco_data["annotations"]:
    # Get the corresponding image
    image = next(img for img in coco_data["images"] if img["id"] == annotation["image_id"])

    # Create document
    document = {
        "image_id": annotation["image_id"],
        "file_name": image["file_name"],
        "image_width": image["width"],
        "image_height": image["height"],
        "category": category_mapping[annotation["category_id"]],
        "bbox": annotation["bbox"],
        "area": annotation["area"]
    }

    # Add Bulk API format
    action = {"index": {"_index": index_name, "_id": annotation["id"]}}
    bulk_data.append(action)
    bulk_data.append(document)

# Write to output file
with open(output_bulk_file, "w") as file:
    for entry in bulk_data:
        file.write(json.dumps(entry) + "\n")

print(f"Bulk annotations saved to {output_bulk_file}")
