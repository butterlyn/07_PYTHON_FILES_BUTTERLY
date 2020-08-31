# 
# Example file for parsing and processing JSON
#
import json

 
def main():
  with open("./samplejson.json") as json_obj:
    json_content = json.load(json_obj)
    print(json_content.keys())
    print(len(json_content["channels"]))
    print(json_content["name"])

    print("\n+++++++++++++++++++++++++\n")

    print(json_content["channels"][0].keys())
    print(json_content["channels"][0]["name"])

    


if __name__ == "__main__":
  main()

  # json files are read as dictionaries, use .keys() method for dictionaries to list the top-level dictionary categories