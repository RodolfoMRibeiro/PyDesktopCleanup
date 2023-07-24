import os
import shutil


class FileOrganizer:
    def __init__(self, base_folder):
        self.base_folder = base_folder
        self.standard_folders = [
            "Pictures", "Videos", "Music"]

    def get_extension(self, file_name):
        _, extension = os.path.splitext(file_name)
        return extension.lower()

    def create_folder(self, folder_path):
        os.makedirs(folder_path, exist_ok=True)

    def move_file(self, source_file, destination_folder):
        shutil.move(source_file, destination_folder)

    def organize_folder_by_extension(self, folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                extension = self.get_extension(filename)
                folder_name = extension[1:] if extension else "other"

                destination_folder = os.path.join(folder_path, folder_name)
                self.create_folder(destination_folder)

                destination_file_path = os.path.join(
                    destination_folder, filename)
                self.move_file(file_path, destination_file_path)

    def organize_standard_folders(self):
        for folder_name in self.standard_folders:
            folder_path = os.path.join(self.base_folder, folder_name)
            if not os.path.exists(folder_path):
                print(
                    f"Folder '{folder_name}' does not exist in the specified location.")
                continue

            self.organize_folder_by_extension(folder_path)


if __name__ == "__main__":
    x = input("Enter the base folder name: ")
    base_folder = os.path.join("C:\\Users\\QUERO2\\Desktop\\", x)

    print(base_folder)

    if not os.path.exists(base_folder):
        print("Specified base folder does not exist.")
        exit()

    organizer = FileOrganizer(base_folder)
    organizer.organize_standard_folders()

    print("Standard folders organized successfully in the specified location!")
