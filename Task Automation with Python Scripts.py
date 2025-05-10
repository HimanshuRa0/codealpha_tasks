import os
import shutil
from datetime import datetime

# Constants
LOG_FILE = "file_organizer_log.txt"
RECURSIVE = False  # Set to True to organize files inside subfolders too

# Define file type categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.csv', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.java', '.cpp', '.html', '.css'],
}

def log_action(message):
    with open(LOG_FILE, 'a') as log:
        log.write(f"{datetime.now()} - {message}\n")

def create_folder(folder_path):
    try:
        os.makedirs(folder_path, exist_ok=True)
        return True
    except Exception as e:
        log_action(f"Failed to create folder: {folder_path} - {str(e)}")
        return False

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def move_file(file_path, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            create_folder(destination_folder)
        shutil.move(file_path, destination_folder)
        return True
    except Exception as e:
        log_action(f"Failed to move {file_path} to {destination_folder}: {str(e)}")
        return False

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path. Exiting.")
        return

    total_files = 0
    moved_files = 0
    log_action(f"Started organizing folder: {folder_path}")

    # Traverse directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip log file itself
            if file == LOG_FILE:
                continue

            _, ext = os.path.splitext(file)
            if not ext:
                continue

            category = get_category(ext)
            dest_folder = os.path.join(folder_path, category)
            new_path = os.path.join(dest_folder, file)

            # Avoid moving files to themselves
            if file_path == new_path:
                continue

            total_files += 1
            if move_file(file_path, new_path):
                moved_files += 1
                print(f"Moved: {file} --> {category}")
                log_action(f"Moved {file} to {category}")

        if not RECURSIVE:
            break

    print(f"\n🎉 Organization complete!")
    print(f"Total files found: {total_files}")
    print(f"Files successfully moved: {moved_files}")
    log_action(f"Organized {moved_files} of {total_files} files.\n")

def clear_log():
    with open(LOG_FILE, 'w') as log:
        log.write("File Organizer Log\n")
        log.write("===================\n\n")

def main():
    print("=" * 50)
    print("📂 Welcome to Python File Organizer")
    print("=" * 50)

    folder_path = input("Enter the full path to the folder you want to organize:\n> ").strip()

    if not os.path.isdir(folder_path):
        print("❌ The folder path is invalid. Please check and try again.")
        return

    clear_log()
    organize_files(folder_path)

    print("\n📄 Log file saved as:", LOG_FILE)
    print("✔️ Done!")

if __name__ == "__main__":
    main()
