import subprocess

def run_code_analysis(file_path):
    subprocess.run(['pylint', file_path])  # Run pylint
    subprocess.run(['flake8', file_path])  # Run flake8

if __name__ == "__main__":
    file_to_review = 'problem3.py'  # Replace with your file path
    run_code_analysis(file_to_review)
