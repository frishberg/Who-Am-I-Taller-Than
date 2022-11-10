import json
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

f = open("Webpage/data.json", "r")
data = json.load(f)

for x in range(len(data)) :
    entry1 = data[x]
    networth1 = entry1["networth"]
    height1 = entry1["height"]
    for y in range(x+1, len(data)) :
        entry2 = data[y]
        networth2 = entry2["networth"]
        height2 = entry2["height"]
        if (networth2==networth1 and height2==height1 and similar(entry1["name"], entry2["name"])>0.5) :
            print(entry1["name"] + ", " + entry2["name"])
