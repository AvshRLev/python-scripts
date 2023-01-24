import json

with open("/Users/avshi/Downloads/nvd-prod.json") as fp:
    prod = json.load(fp)
prod_table = {
    f"{item['external_id']}-{item['assigner']}": item
    for item in prod
}

with open("/Users/avshi/Downloads/nvd-pre-prod.json") as fp:
    prod = json.load(fp)
pre_prod_table = {
    f"{item['external_id']}-{item['assigner']}": item
    for item in prod
}

common_keys = set(prod_table.keys()) & set(pre_prod_table.keys())

diff = []
for key in common_keys:
    if prod_table[key] != pre_prod_table[key]:
        diff.append(key)
print(diff)
