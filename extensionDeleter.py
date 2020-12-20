import os, argparse
parser = argparse.ArgumentParser()

parser.add_argument("FolderPath", help="The path to the folder to scan the files in")
parser.add_argument("FileExtension", help="The extension of the files you want to delete")
parser.add_argument("-s", "--silent", help="Do not require confirmation to delete files", action="store_true")
args = parser.parse_args()
location = args.FolderPath
extension = args.FileExtension
filenames = []
response = None


if os.path.isdir(location):
    for file in os.listdir(location):
        try:
            if file.endswith(extension):
                filenames.append(file)
        except Exception as e:
            raise e
            print("No files found!")
    if not args.silent:
        print("Here's all the files to be deleted:\n")
        for file in filenames:
            print("\t"+file+"\n")
        print("Are you sure you want to delete them all? Y for yes, N for no.")
        response = input()
    if response == "y" or response == "Y" or args.silent:
        for file in filenames:
            os.remove(os.path.join(location, file))
        print("All files deleted")
    else:
        print("No files deleted. Exiting now")
        exit(0)
else:
    print("Invalid directory!")
    exit(1)
