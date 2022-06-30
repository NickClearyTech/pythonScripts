import os
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("Path1", help="Path of the first folder")
parser.add_argument("Path2", help="Path of second folder")
parser.add_argument("DestinationPath", help="Path of directory to copy files to")

args = parser.parse_args()

for root, dirs, files in os.walk(args.Path1):
    for name in dirs:
        if not os.path.isdir(
            os.path.join(args.DestinationPath, root.replace(args.Path1, "")[1:], name)
        ):
            os.mkdir(
                os.path.join(
                    args.DestinationPath, root.replace(args.Path1, "")[1:], name
                )
            )
    for name in files:
        if not os.path.isfile(
            os.path.join(args.DestinationPath, root.replace(args.Path1, "")[1:], name)
        ):
            print(f"Coyping {os.path.join(root, name)}")
            shutil.copy(
                os.path.join(root, name),
                os.path.join(
                    args.DestinationPath, root.replace(args.Path1, "")[1:], name
                ),
            )


for root, dirs, files in os.walk(args.Path2):
    for name in dirs:
        if not os.path.isdir(
            os.path.join(args.DestinationPath, root.replace(args.Path2, "")[1:], name)
        ):
            os.mkdir(
                os.path.join(
                    args.DestinationPath, root.replace(args.Path2, "")[1:], name
                )
            )
    for name in files:
        if not os.path.isfile(
            os.path.join(args.DestinationPath, root.replace(args.Path2, "")[1:], name)
        ):
            print(f"Coyping {os.path.join(root, name)}")
            shutil.copy(
                os.path.join(root, name),
                os.path.join(
                    args.DestinationPath, root.replace(args.Path2, "")[1:], name
                ),
            )
