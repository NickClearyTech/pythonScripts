'''Takes in a CSV file which lists filenames and a directory. Scans both, and finds which file names are present in one but not the other'''


import csv, argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("FolderPath", help="Path of the folder to scan for files")
parser.add_argument("CSVFile", help="CSV file containg filenames to look for")
args = parser.parse_args()
Folder = args.FolderPath
CSVFile = args.CSVFile

csvFiles = []
filesPresent = []

if os.path.isdir(Folder):
    with open(CSVFile, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            csvFiles.append(row["Name"].lower())
    for file in os.listdir(Folder):
        filesPresent.append(file[:-4].lower())
    print("Files in csv but not in folder:\n")
    for name in csvFiles:
        if name not in filesPresent:
            print('\t' + name + '\n')
    print("Files in folder, but not in csv:\n")
    for file in filesPresent:
        if file not in csvFiles:
            print('\t' + file + '\n')
else:
    print("That is not a valid path!\n")
    exit(1)