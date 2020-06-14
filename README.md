# coco_to_darknet-format
Convert COCO annotations to darknet format. If you want to train COCO or your custom dataset, this program can help you convert annotation json file to txt file that darknet need.
# Requirements
python 2.7
argparse

# How to run
</$ cd coco_to_darknet-format>
if you want to convert your custom dataset, please modify the classes on the 7th line of the convert.py.
</$ python convert.py --input-path your coco annotation path --output-path txt path>
eg:
</$ python convert.py --input-path /home/flora/coco/annotations/instances_train2017.json --output-path /home/flora/label/tarin>
