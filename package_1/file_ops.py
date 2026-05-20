# Write ops in file

# file = open("media/file.txt", "w")
# content_length = file.write("This is a file created using Python.")
# print(content_length)
# file.close()

# # Read ops in file
# file = open("media/file.txt", "r")
# content = file.read()   
# print(content)
# file.close()



# Using context manger to read file
with open("media/file.txt", "r") as file:
    content = file.read()
    print(content)


# CSV
import csv

data = [
     
        ["Name", "Age", "City"], 
        ["Sagar", 30, "Kathmandu"], 
        ["John", 25, "New York"]
    
    ]

with open("media/data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("media/data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# CSV


# JSON
import json

json_data = {
    "name": "Sagar",
    "age": 30,
    "city": "Kathmandu",
    "address":{
        "street": "New Road",
        "number": 123,
        "extra": {
            "landmark": "Near City Hall",
            "postal_code": "44600",
            "extra_info": {
                "country": "Nepal",
                "continent": "Asia",
                "extra_info_2": {
                    "timezone": "NPT",
                    "currency": "NPR"
                }
            }
        }
    }
}


with open("media/data.json", "w") as file:
    json.dump(json_data, file, indent=4)

with open("media/data.json", "r") as file:
    data = json.load(file)
    print(data)
# JSON