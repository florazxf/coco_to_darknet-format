import os
import json
from os import listdir,getcwd
from os.path import join
import pdb
import argparse as args

classes = ["person","bicycle","car","motorcycle","airplane","bus","train",
	   "truck","boat","traffic light","fire hydrant","stop sign","parking meter",
	   "bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra",
	   "giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis",
	   "snowboard","sports ball","kite","baseball bat","baseball glove","skateboard",
	   "surfboard","tennis racket","bottle","wine glass","cup","fork","knife","spoon",
	   "bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza",
	   "donut","cake","chair","couch","potted plant","bed","dining table","toilet","tv",
	   "laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink",
	   "refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]


#box form[x,y,w,h]
def convert(size,box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = round((box[0]+box[2]/2)*dw,6) #(x+bbox_width/2)/img_width
    y = round((box[1]+box[3]/2)*dh,6) #(y+bbox_height/2)/img_height
    w = round(box[2]*dw,6) #bbox_width/img_width
    h = round(box[3]*dh,6) #bbox_height
    return (x,y,w,h)


def convert_annotation(input_path,output_path):
    with open(input_path,'r') as f:
    #with open('/hdd2/wh/six/annotations/instances_val.json','r') as f:
    #with open('/hdd2/wh/coco2017/annotations/instances_val2017.json','r') as f:
        data = json.load(f)
    #pdb.set_trace()
    for item in data['images']:
        image_id = item['id']
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
        #outfile = open('/home/flora/coco/labels/sixval/%s.txt'%(file_name[:-4]), 'a+')
        outfile = open(output_path+'/'+'%s.txt'%(file_name[:-4]), 'a+')
        for item2 in value:
            category_id=item2['category_id']
            value1 = filter(lambda item3: item3['id'] == category_id,data['categories'])
            name = value1[0]['name']
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width,height),box)
            outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        #pdb.set_trace()
        outfile.close()



if __name__=='__main__':
    parser = args.ArgumentParser()
    parser.add_argument('--input-path',type=str,help='file path to COCO or custom COCO formatted annotations')
    parser.add_argument('--output-path',type=str,help='file path to txt')
    opt = parser.parse_args()
    convert_annotation(opt.input_path,opt.output_path)
