import os
import json
from difflib import SequenceMatcher
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)


def read_and_clean_notebook(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            notebook_data = json.load(file)

        # Remove output cells
        for cell in notebook_data['cells']:
            if cell['cell_type'] == 'code':
                cell['outputs'] = []
                cell['execution_count'] = None

        return json.dumps(notebook_data)
    except Exception as e:
        logging.error(f"Error reading or cleaning notebook {file_path}: {e}")
        return None


def compare_similarity(content_a, content_b):
    try:
        return SequenceMatcher(None, content_a, content_b).ratio()
    except Exception as e:
        logging.error(f"Error comparing notebooks: {e}")
        return 0


def find_detailed_similarities(notebooks, threshold=0.9):
    detailed_similarities = []
    students = list(notebooks.keys())
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            student_a = students[i]
            student_b = students[j]
            content_a = notebooks[student_a]
            content_b = notebooks[student_b]

            if content_a is None or content_b is None:
                logging.warning(f"Skipping comparison between {student_a} and {student_b} due to missing content.")
                continue

            try:
                logging.info(f"Comparing {student_a} with {student_b}")
                similarity_ratio = compare_similarity(content_a, content_b)
                if similarity_ratio > threshold:  # Focus only on high similarities
                    similarity_level = "High Similarity" if similarity_ratio > 0.9 else "Moderate Similarity"
                    detailed_similarities.append((student_a, student_b, similarity_level, round(similarity_ratio, 2)))
            except Exception as e:
                logging.error(f"Error during similarity comparison between {student_a} and {student_b}: {e}")

    return detailed_similarities


def save_results_to_csv(results, output_csv_path):
    try:
        df = pd.DataFrame(results, columns=['Student A', 'Student B', 'Similarity Level', 'Similarity Ratio'])
        df.to_csv(output_csv_path, index=False)
        logging.info(f"Similarity results saved to {output_csv_path}")
    except Exception as e:
        logging.error(f"Error saving results to CSV {output_csv_path}: {e}")
