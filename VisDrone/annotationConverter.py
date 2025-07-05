
import os
from pathlib import Path

from ultralytics.utils.downloads import download


def visdrone2yolo(dir):
    """Convert VisDrone annotations to YOLO format, creating label files with normalized bounding box coordinates."""
    from PIL import Image
    from tqdm import tqdm

    def convert_box(size, box):
        # Convert VisDrone box to YOLO xywh box
        dw = 1.0 / size[0]
        dh = 1.0 / size[1]
        return (box[0] + box[2] / 2) * dw, (box[1] + box[3] / 2) * dh, box[2] * dw, box[3] * dh

    (dir / "labels").mkdir(parents=True, exist_ok=True)  # make labels directory
    pbar = tqdm((dir / "annotations").glob("*.txt"), desc=f"Converting {dir}")
    for f in pbar:
        img_size = Image.open((dir / "images" / f.name).with_suffix(".jpg")).size
        lines = []
        with open(f, encoding="utf-8") as file:  # read annotation.txt
            for row in [x.split(",") for x in file.read().strip().splitlines()]:
                if row[4] == "0":  # VisDrone 'ignored regions' class 0
                    continue
                cls = int(row[5]) - 1
                box = convert_box(img_size, tuple(map(int, row[:4])))
                lines.append(f"{cls} {' '.join(f'{x:.6f}' for x in box)}\n")
                with open(str(f).replace(f"{os.sep}annotations{os.sep}", f"{os.sep}labels{os.sep}"), "w", encoding="utf-8") as fl:
                    fl.writelines(lines)  # write label.txt



def filterClassAnnotations(dir, vehicle_classes):
    """
    By default, YOLO adapted VisDrone has these classes:
        0: pedestrian
        1: people
        2: bicycle
        3: car
        4: van
        5: truck
        6: tricycle
        7: awning-tricycle
        8: bus
        9: motor

    Since we need vehicle detection only, reduce it to binary classification:
        
        0: non-vehicle
        1: vehicle (car, van, truck, bus, motor)

    This method loads the files in the built labels folder dir and adjusts class names accordingly. It then writes them to disk
    
    Parameters
    ----------

    dir: a path object, directory where images and labels are stored

    vehicle_classes: a list of classes which will be considered a vehicle class in the output

    """
    from tqdm import tqdm
    pbar = tqdm((dir / "labels").glob("*.txt"), desc=f"Adjusting class names in {dir}")
    for f in pbar:
        lines = []
        with open(f, encoding="utf-8") as file:
            for row in [x.split(" ") for x in file.read().strip().splitlines()]:
                if int(row[0]) in vehicle_classes:
                    row[0]="0"
                else:
                    continue
                
                lines.append(f'{" ".join(row)}\n')
        with open(f, "w", encoding="utf-8") as fl:
            fl.writelines(lines)  # write label.txt





# Download
dir = Path("./VisDrone")  # dataset root dir


# Convert
for d in ["train"]:# add other directories here (ex. train, test, valid) 
    visdrone2yolo(dir / d)  # convert VisDrone annotations to YOLO labels

# Adjust class vals
for d in ["train"]:# add other directories here (ex. train, test, valid) 
    filterClassAnnotations(dir / d , [3,4,5,8,9])  # convert VisDrone annotations to YOLO labels

for d in ["test"]:# add other directories here (ex. train, test, valid) 
    filterClassAnnotations(dir / d , [1])  # convert VisDrone annotations to YOLO labels

for d in ["valid"]:# add other directories here (ex. train, test, valid) 
    filterClassAnnotations(dir / d , [1])  # convert VisDrone annotations to YOLO labels