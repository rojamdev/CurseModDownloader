import os.path
import json
import wget

manifest = open("manifest.json")
data = json.load(manifest)

os.mkdir("mods")

blacklist = []

with open("blacklist.txt") as bl_file:
    for line in bl_file:
        blacklist.append(line)

print(blacklist)

for i in data["files"]:
    projectID = str(i["projectID"])
    fileID = str(i["fileID"])

    url = "https://www.curseforge.com/api/v1/mods/" + projectID + "/files/" + fileID + "/download"
    filename = projectID + "_" + fileID + ".jar"
    output = os.path.join("mods", filename)

    wget.download(url, out=output)