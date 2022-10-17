import pandas as pd
import json

df = pd.read_csv("raw/flickr8k_captions.txt")
images = set(df.image.unique().tolist())

for target_split in ("train", "val", "test"):
    fd = open("raw/dataset_flickr8k.json")
    data = json.load(fd)
    rows = []
    nb = 0
    for dt in data["images"]:
        assert dt["filename"] in images
        if dt["split"] != target_split:
            continue
        #print(dt["sentences"])
        sents = [s["raw"] for s in dt["sentences"]]
        #print(sents)
        for sent in sents:
            rows.append({"image": dt["filename"], "caption": sent})
        nb += 1
    print(nb)
    out_df = pd.DataFrame(rows)
    out_df.to_csv(f"out/flickr8k_{target_split}_karpathy.txt", sep=",", index=False)
