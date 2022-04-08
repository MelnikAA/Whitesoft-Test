import json as js
import requests

response = requests.get("https://raw.githubusercontent.com/thewhitesoft/student-2022-assignment/main/data.json")
data = response.json()

with open("replacement.json") as file:
    replacements = js.load(file)
rep_d = {}
for item in replacements:
    rep_d[item["replacement"]] = item["source"]

ans = []
for line in data:
    ans_line = line
    for replacement in rep_d.keys():
        value = rep_d[replacement]
        if replacement in ans_line and value is None:
            ans_line = None
            break
        if replacement in ans_line:
            ans_line = str(ans_line).replace(replacement, value)
    if ans_line is not None:
        ans.append(ans_line)

with open(r".\answer.json", "w") as file:
    js.dump(ans, file, sort_keys=False, indent=4)
