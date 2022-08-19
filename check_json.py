import json

f = open("new_oo.json",'r')
f1 = json.load(f)
'''
print f1["ArrayName"][0]   # to print first review object
print f1["ArrayName"][0]["reviewerID"] # to print reveiwer id of first review object
print f1["ArrayName"][0]["asin"]
print f1["ArrayName"][0]["overall"]
'''
d = {}
#pid = {}
for i in range(0,10000):
    d[str(f1["ArrayName"][i]["asin"])] = {}
for i in range(0,10000):
    asin = str(f1["ArrayName"][i]["asin"])
    reviewerID = str(f1["ArrayName"][i]["reviewerID"])
    overall = float(f1["ArrayName"][i]["overall"])
    #print asin, reviewerID, overall
    d[asin][reviewerID] = overall

#print d
