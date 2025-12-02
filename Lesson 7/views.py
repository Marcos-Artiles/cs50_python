import numpy as np
from PIL import Image
import CSV

def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)

        #reading and writing a specific fieldname called "brightness"
        writer = csv.DictReader(analysis, fieldnames = reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)
            writer.writerow(row)

main()