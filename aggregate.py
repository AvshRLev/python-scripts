import json


with open("./backlog.json") as cve_file:
    backlog = json.load(
        cve_file
    )

with open("./backlog_old.json") as cve_file:
    backlog_old = json.load(
        cve_file
    )

with open("./backlog_backlogv1.json") as cve_file:
    backlog_backlogv1 = json.load(
        cve_file
    )

with open("./backlog2.json") as cve_file:
    backlog2 = json.load(
        cve_file
    )

# with open("./backlog_backlogv02.json", 'r') as j:
#     contents = json.loads(j.read())

aggregated = json.dumps(backlog + backlog_old + backlog_backlogv1 + backlog2)


with open("backlog_agg.json", "w") as outfile:
    outfile.write(aggregated)