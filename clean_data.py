import json

with open("./backlog_agg.json") as cve_file:
    backlog = json.load(
        cve_file
    )

for index, object in enumerate(backlog):
    backlog[index] = {"cves": object["cves"], "vulnerable": object["vulnerable"]}

with open("backlog_clean.json", "w") as outfile:
    outfile.write(json.dumps(backlog))

