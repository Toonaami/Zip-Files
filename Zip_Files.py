import os
import zipfile

def zip_files(folder_path, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w') as zip_file:
        for foldername, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

if __name__ == "__main__":
    folder_to_zip = input("Enter the path of the folder to zip: ")
    zip_name = input("Enter the desired zip file name (e.g., output.zip): ")
    zip_files(folder_to_zip, zip_name)
    print(f"Successfully created {zip_name} from {folder_to_zip}")