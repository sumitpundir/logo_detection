# logo_detection




SETUP 

1. Setup Faster RCNN from the github repositery (https://github.com/rbgirshick/py-faster-rcnn).

2. Convert the dataset. Create three separate folders named Annotations, ImageSets and JPEGImages. The script( convert_flickr.py ) converts the dataset into .xml annotation files  (Annotation folder) and  train.txt file (ImageSets folder). Copy all the images in the JPEGImages folder. The converted dataset suitable for training is in the folder training_dataset.

3. Update the factory.py file in py-faster-rcnn/lib/datasets/ or replace it with our factory.py. The purpose of factory.py file is to get all sets of whole dataset. 

4. Add the dataset python file . Add the new logo.py file in py-faster-rcnn/lib/datasets/ folder.  The purpose of logo.py is to read a part of whole dataset , such as train set. Add logo_eval.py  file inside the  py-faster-rcnn/lib/datasets/ folder.

5. Trained the model from fine tuning a pre-trained Faster R-CNN model because a pre-trained model contains a lot of good low level features. Used the ZF-net network.

6. Update the number of output in final layer. We have 28 classes ( 27 class + 1 background class) and 112 (28*4) output for bounding box regressor.  Rename the last fully connected layer.



Training

1. Rename the last fuly connected layer.

2. 1st fine tune. (./tools/train_net.py --gpu 0 --weights data/faster_rcnn_models/ZF_faster_rcnn_final.caffemodel --imdb logo_train --cfg experiments/cfgs/config.yml --solver models/logo/solver.prototxt --iter 0 )

3. Rename the layers back to their original names. Set the parameters in solver.prototxt. Due to low computation resources we trained our model on lowest minimum parameters.

4. 2nd fine tune. Set the paths to 1st fine tuned model to get it's weight.  (./tools/train_net.py --gpu 0 --weights output/logo/train/zf_faster_rcnn_iter_0.caffemodel --imdb logo_train --cfg experiments/cfgs/config.yml --solver models/logo/solver.prototxt --iter 10000 )
