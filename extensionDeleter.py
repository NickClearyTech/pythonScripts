import sys, os, argparse
parser = argparse.ArgumentParser()

parser.add_argument("FolderPath", help="The path to the folder to scan the files in")
parser.add_argument("FileExtension", help="The extension of the files you want to delete")
args = parser.parse_args()
location = args.FolderPath
extension = args.FileExtension

for file in os.listdir(location):
    try:
        if file.endswith(extension):
            print("mkv file found:\t", file, "\n")
            os.remove(file)
    except Exception as e:
        raise e
        print("No files foun!d")
