import json
INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    list_dict = []
    with open("input.csv", "r") as f:
        headers_data = f.readline().rstrip().split(sep=",")
        for row in f:
            list_dict.append(dict(zip(headers_data, row.rstrip().split(sep=","))))

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
