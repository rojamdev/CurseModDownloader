import os.path
import json
import wget

manifest = open("manifest.json")
data = json.load(manifest)

if not os.path.isdir("mods"):
    os.mkdir("mods")

blacklist = []
skip_count = 0

with open("blacklist.txt") as bl_file:
    for line in bl_file:
        line = line.strip()
        blacklist.append(line)

for i in data["files"]:
    projectID = str(i["projectID"])
    fileID = str(i["fileID"])

    if projectID in blacklist:
        print("Skipping mod with project ID " + projectID)
        skip_count += 1
        continue

    url = "https://www.curseforge.com/api/v1/mods/" + projectID + "/files/" + fileID + "/download"
    filename = projectID + "_" + fileID + ".jar"
    output = os.path.join("mods", filename)

    wget.download(url, out=output)

print("Download complete, " + str(skip_count) + " mods skipped.")
