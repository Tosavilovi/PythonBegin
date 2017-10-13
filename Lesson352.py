import json

js = json.loads(input())

dtree = {}
res = {}
for row in js:
    if row['name'] not in dtree:
        dtree[row['name']] = row['parents']
    else:
        for parent in row['parents']:
            if not dtree[row['name']].count(parent):
                dtree[row['name']].append(parent)
    print(dtree)

for key in dtree:
    res[key] = 1
    for key2 in dtree:
        if dtree[key2].count(key):
            res[key] = res[key] + 1
for k in sorted(res.keys()):
    print(k, ':', res[k])
