mkdir -p raw out
# download all https://www.kaggle.com/datasets/shtvkumar/karpathy-splits and put them in raw
# thanks to @shtvkumar
wget http://images.cocodataset.org/annotations/annotations_trainval2014.zip
unzip annotations_trainval2014.zip -d raw
python build_coco_splits.py
python build_flickr30k_splits.py
python build_flickr8k_splits.py

