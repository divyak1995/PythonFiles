from collections import defaultdict


def isNumeric(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def orderingBoxes(boxes):
    newer_boxes = []
    ties = []
    dictionary = defaultdict(list)
    for box in boxes:
        li = box.split()
        iden = li[0]
        ver = ' '.join(li[1:])
        dictionary[ver].append(iden)

        li_ver = ver.split()
        f = list()
        for k in li_ver:
            f.append(isNumeric(k))
        if all(f):
            newer_boxes.append(box)

    for k,v in dictionary.items():
        if len(v) > 1:
            for i in v:
                resu = i + " " + k
                ties.append(resu)

    older_boxes = list()

    for key, value in sorted(dictionary.items()):
        key_li = key.split()
        flag = []
        for k in key_li:
            flag.append(isNumeric(k))
        if all(flag):
            continue
        else:
            for i in value:
                older_boxes.append(i + " " + key)

    for box in ties:
        older_boxes.remove(box)

    ties = sorted(ties)

    output = older_boxes + ties + newer_boxes

    return output


arr = ["a8d cat mouse dog", "bdk cat ant rabbit", "ejd anl dsf", "q8f hello world", "s45 094 048", "a3d 878 345",
       "b54 hello world", "bls aps aps", "f43 aps aps"]

res = orderingBoxes(arr)

print(res)

