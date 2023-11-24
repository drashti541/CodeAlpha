import os
import shutil

def organize_files(source_dir):
    # Your extension mapping here
    extensions = {
        '.jpeg': 'Images', '.jpg': 'Images', '.png': 'Images', '.gif': 'Images', '.bmp': 'Images',
        '.avi': 'Videos', '.flv': 'Videos', '.wmv': 'Videos', '.mov': 'Videos', '.mp4': 'Videos',
        '.doc': 'Documents', '.docx': 'Documents', '.pdf': 'Documents', '.txt': 'Documents',
        '.xls': 'Documents', '.xlsx': 'Documents', '.ppt': 'Documents', '.pptx': 'Documents',
        '.mp3': 'Music', '.wav': 'Music', '.flac': 'Music', '.m4a': 'Music'
    }

    # Path to the directory containing the files
    source_directory_path = os.path.join(source_dir, 'files')

    # Directory to store organized files
    organized_directory_path = os.path.join(source_dir, 'organized_files')

    # Create organized directory if it doesn't exist
    if not os.path.exists(organized_directory_path):
        os.makedirs(organized_directory_path)

    # Create folders for different file types
    for folder in set(extensions.values()):
        if not os.path.exists(os.path.join(organized_directory_path, folder)):
            os.makedirs(os.path.join(organized_directory_path, folder))

    # Move files to their respective folders based on extensions
    files = [f for f in os.listdir(source_directory_path) if os.path.isfile(os.path.join(source_directory_path, f))]

    # Copy files to their respective folders based on extensions in the organized directory
    for file in files:
        extension = os.path.splitext(file)[1].lower()
        if extension in extensions:
            folder = extensions[extension]
            source_file_path = os.path.join(source_directory_path, file)
            destination_file_path = os.path.join(organized_directory_path, folder, file)
            shutil.copy(source_file_path, destination_file_path)

    print("Files organized successfully in 'organized_files' directory!")

# Get the directory where the script is located
script_directory = os.getcwd()

organize_files(script_directory)
