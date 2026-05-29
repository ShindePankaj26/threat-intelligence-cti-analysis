import re
import json


def preprocess_text(text):
    """
    Basic text preprocessing for CTI reports.
    """

    if not text:
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Remove special characters except dots and dashes
    text = re.sub(r'[^a-zA-Z0-9\s\.-]', '', text)

    return text.strip()


def load_json_file(file_path):
    """
    Load JSON file safely.
    """

    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
