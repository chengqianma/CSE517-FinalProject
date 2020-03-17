import json
import tqdm

x1 = list()
x2 = list()
xx2 = list()
y = list()
yy = list()

with open("test_data.json", "r") as f:
    for line in tqdm.tqdm(f):
        temp = json.loads(line.strip())
        x1.append(temp["premise"])
        x2.append(temp["initial"])
        xx2.append(temp["counterfactual"])
        y.append(temp["original_ending"])
        yy.append(temp["edited_endings"])

name = "test_"

with open(name + "x1.txt", "w") as f:
    for x in x1:
        f.write(x + "\n")

with open(name + "x2.txt", "w") as f:
    for x in x2:
        f.write(x + "\n")

with open(name + "xx2.txt", "w") as f:
    for x in xx2:
        f.write(x + "\n")

with open(name + "y.txt", "w") as f:
    for x in y:
        f.write(x + "\n")

with open(name + "yy.txt", "w") as f:
    for x in yy:
        # print(x)
        f.write(x[0][0] + " " + x[0][1] + " " + x[0][2] + "\n")