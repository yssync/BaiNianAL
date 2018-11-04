import yaml

with open("./login_data.yml", "r", encoding="utf-8") as f:
    data = yaml.load(f)
    print(data)