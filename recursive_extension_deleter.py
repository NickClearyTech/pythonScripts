import os, argparse
parser = argparse.ArgumentParser()

def parse_folder(folder_path: str, extension: str):
    current_folder_path = folder_path
    items = os.listdir(current_folder_path)
    # print(items)
    for item in items:
        new_path = os.path.join(current_folder_path, item)
        if item.endswith(extension):
            print("Deleting file {0}/{1}".format(current_folder_path, item))
            os.remove(new_path)
        if os.path.isdir(new_path):
            print("Entering {0}".format(new_path))
            parse_folder(new_path, extension)


parser.add_argument("FolderPath", help="The path to the folder to scan the files in")
parser.add_argument("FileExtension", help="The extension of the files you want to delete")
args = parser.parse_args()
location = args.FolderPath
extension = args.FileExtension

if not os.path.isdir(location):
    print("Invalid directory provided!")
    exit(1)

parse_folder(location, extension)

