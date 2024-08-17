import os
import glob
import argparse
import logging
from similarity_checker import read_and_clean_notebook, find_detailed_similarities, save_results_to_csv

logging.basicConfig(level=logging.INFO)


def main(folder_path, output_csv_path, similarity_threshold):
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder path {folder_path} does not exist.")

        # Find all Jupyter Notebook files (.ipynb) in the extracted folders
        notebook_files = glob.glob(os.path.join(folder_path, '**/*.ipynb'), recursive=True)

        if not notebook_files:
            raise FileNotFoundError("No Jupyter Notebook files found in the specified folder.")

        # Dictionary to store the cleaned content of each notebook file
        notebooks_content = {}

        # Reading and cleaning all notebook contents
        for file in notebook_files:
            student_name = os.path.basename(os.path.dirname(file))
            cleaned_content = read_and_clean_notebook(file)
            if cleaned_content:
                notebooks_content[student_name] = cleaned_content

        # Perform the similarity check
        high_similarities = find_detailed_similarities(notebooks_content, threshold=similarity_threshold)

        # Save the results to a CSV file
        save_results_to_csv(high_similarities, output_csv_path)

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notebook Similarity Checker")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing the notebook files")
    parser.add_argument("--output", type=str, default="similarity_results.csv", help="Output CSV file path")
    parser.add_argument("--threshold", type=float, default=0.9, help="Similarity threshold (0 to 1)")

    args = parser.parse_args()

    main(args.folder_path, args.output, args.threshold)
