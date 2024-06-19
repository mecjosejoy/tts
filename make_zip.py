import shutil


def zip_folder(folder_path, output_zip):
    shutil.make_archive(output_zip, "zip", folder_path)


folder_path = "output"  # Replace with your folder path
output_zip = "output"  # Replace with your desired output zip file path without extension

zip_folder(folder_path, output_zip)
