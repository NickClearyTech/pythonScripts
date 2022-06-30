import os, argparse, csv, shutil

parser = argparse.ArgumentParser()

parser.add_argument(
    "SourceFolder", help="The folder from which to copy all the pictures"
)
parser.add_argument("DestFolder", help="The folder to copy all the files to")
parser.add_argument("FolderName", help="A reference to what folder the file came from")
parser.add_argument("CSV", help="CSV file to append information regarding pictures to")
args = parser.parse_args()

sourceFolder = args.SourceFolder
destFolder = args.DestFolder
folderPrefix = args.FolderName
csvFile = args.CSV

if os.path.isdir(sourceFolder) and os.path.isdir(destFolder):
    try:
        with open(csvFile, mode="w") as csvFile:
            csv_writer = csv.writer(csvFile, delimiter=",")
            for file in os.listdir(sourceFolder):
                filename = folderPrefix + "---" + file
                print("Copying {0}\n".format(filename))
                shutil.copy(
                    os.path.join(sourceFolder, (file)),
                    os.path.join(destFolder, filename),
                )
                print("Copied {0}\n".format(filename))
                csv_writer.writerow([filename, destFolder])
    except Exception as e:
        raise e
        print("Unable to open csv!")
        exit(1)
else:
    print("One or both of the provided folder paths are not valid!")
    exit(1)
