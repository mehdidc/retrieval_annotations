import json

splits = (("train", "raw/captions_train2014.json"), ("val", "raw/captions_val2014.json"), ("test", "raw/captions_val2014.json"))
out_splits = []
for target_split, source_name in splits:
    data = json.load(open(source_name))
    fd = open("raw/dataset_coco.json")
    data_split = json.load(fd)

    # Get filenames for the karpathy split
    split = []
    for img in data_split['images']:
        if img['split'] == target_split:
            split.append(img["filename"])
    split  = set(split)
    out_splits.append(split)
    nb = 0
    data_new = {}
    data_new.update(data)
    data_new['images'] = []
    data_new['annotations'] = []
    ids = []
    for img in data['images']:
        if img['file_name'] in split:
            nb += 1
            data_new['images'].append(img)
            ids.append(img['id'])
    ids = set(ids)
    for ann in data['annotations']:
        if ann['image_id'] in ids:
            data_new['annotations'].append(ann)
    print(len(data_new['images']), len(split))
    with open(f"out/coco_{target_split}_karpathy.json", "w") as fd:
        json.dump(data_new, fd)

print(out_splits[0] & out_splits[1])
print(out_splits[0] & out_splits[2])
print(out_splits[1] & out_splits[2])
