import os, argparse, csv, shutil

parser = argparse.ArgumentParser()

parser.add_argument(
    "SourceFolder", help="The folder containing the files you wish to copy from"
)
parser.add_argument(
    "DestinationFolder", help="The folder where you wish to put the file"
)
parser.add_argument("CSV", help="Path to CSV file containing video names and tags")
parser.add_argument(
    "Tag",
    help="Tag from second column of CSV. When this tag appears in the second column, the video file tagged with it will copy to the destination folder",
)
args = parser.parse_args()
sourceFolder = args.SourceFolder
destFolder = args.DestinationFolder
csvFile = args.CSV
tag = args.Tag
videoFiles = []


if os.path.isdir(sourceFolder) and os.path.isdir(destFolder):
    try:
        with open(csvFile, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if tag.lower() in row["People"].lower():
                    videoFiles.append(row["Name"])
    except Exception as e:
        raise e
        print("Unable to open csv!")
        exit(1)
    for file in videoFiles:
        filename = file + ".mp4"
        print("Copying " + filename + "\n")
        os.system(
            'copy "'
            + os.path.join(sourceFolder, filename)
            + '" "'
            + os.path.join(destFolder, filename)
            + '"'
        )
        print("Copied " + filename + "\n")
else:
    print("One or both of folders specified are not valid!")
    exit(1)
