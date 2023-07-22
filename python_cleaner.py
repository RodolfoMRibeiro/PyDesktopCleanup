import os
import shutil

def get_extension(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower()

def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)

def move_file(source_file, destination_folder):
    shutil.move(source_file, destination_folder)

def organize_folder_by_extension(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            extension = get_extension(filename)
            folder_name = extension[1:] if extension else "other"
            destination_folder = os.path.join(folder_path, folder_name)
            create_folder(destination_folder)
            destination_file_path = os.path.join(destination_folder, filename)
            move_file(file_path, destination_file_path)

def get_standard_folder_paths_windows():
    desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    images_folder = os.path.join(os.path.expanduser("~"), "Pictures")
    videos_folder = os.path.join(os.path.expanduser("~"), "Videos")
    music_folder = os.path.join(os.path.expanduser("~"), "Music")
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    return desktop_folder, documents_folder, images_folder, videos_folder, music_folder, downloads_folder

def get_standard_folder_paths_mac():
    desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
    images_folder = os.path.join(os.path.expanduser("~"), "Pictures")
    videos_folder = os.path.join(os.path.expanduser("~"), "Movies")
    music_folder = os.path.join(os.path.expanduser("~"), "Music")
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    
    return desktop_folder, documents_folder, images_folder, videos_folder, music_folder, downloads_folder

if __name__ == "__main__":
    operating_system = input("Enter your operating system (Windows or macOS): ").lower()

    if operating_system == "windows":
        desktop_folder, documents_folder, images_folder, videos_folder, music_folder, downloads_folder = get_standard_folder_paths_windows()
    elif operating_system == "macos":
        desktop_folder, documents_folder, images_folder, videos_folder, music_folder, downloads_folder = get_standard_folder_paths_mac()
    else:
        print("Unsupported operating system. Please provide the paths manually.")
        exit()

    organize_folder_by_extension(desktop_folder)
    print("Desktop folder organized successfully!")

    organize_folder_by_extension(documents_folder)
    print("Documents folder organized successfully!")

    organize_folder_by_extension(images_folder)
    print("Images folder organized successfully!")

    organize_folder_by_extension(videos_folder)
    print("Videos folder organized successfully!")

    organize_folder_by_extension(music_folder)
    print("Music folder organized successfully!")

    organize_folder_by_extension(downloads_folder)
    print("Downloads folder organized successfully!")
