

# COCO Annotations to Elasticsearch Bulk Format

This script converts COCO-style annotations into a bulk format suitable for ingestion into Elasticsearch. It reads a COCO JSON file, processes the annotations, and generates a bulk insert JSON file for Elasticsearch.

## Requirements

- Python 3.x
- `json` module (included by default in Python)

## Script Overview

This script does the following:

1. Loads a COCO-format annotation JSON file.
2. Maps category IDs to category names based on the COCO categories.
3. Extracts relevant information from the annotations and images.
4. Converts the data into Elasticsearch bulk API format.
5. Saves the processed data into a new JSON file that can be directly used for Elasticsearch bulk indexing.

## File Paths

- `input_coco_file`: Path to the input COCO annotations JSON file (default: `"Months-Digits-5.v4i.coco/train/_annotations.coco.json"`).
- `output_bulk_file`: Path to the output JSON file for bulk Elasticsearch inserts (default: `"bulk_annotations.json"`).

## Usage


### Run the Script using Python

```bash
python script_name.py
```

Once executed, the script will generate a file named `bulk_annotations.json` (or any custom name specified in `output_bulk_file`), which contains the data formatted for Elasticsearch bulk indexing.

## Output Format

The script generates a JSON file where each entry consists of two parts:
1. The action metadata for Elasticsearch bulk API (`index` action).
2. The document containing image data and annotations in the following format:

```json
{
  "image_id": 123,
  "file_name": "image1.jpg",
  "image_width": 640,
  "image_height": 480,
  "category": "person",
  "bbox": [x, y, width, height],
  "area": 1234
}
```

## Notes

- Ensure the input COCO file has valid JSON format.
- The script assumes each image in the COCO annotations has a unique `id` and each annotation references an image by its `image_id`.
- The generated bulk file can be imported into Elasticsearch using the `_bulk` endpoint.

---
