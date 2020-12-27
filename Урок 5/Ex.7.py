import json
inc = 0
total_average = 0
firm_number = 0
firm_dict = {}
firm_list = []

with open ("Ex.7.txt", "r", encoding="UTF-8") as new_file:
    for line in new_file:
        firm_number += 1
        new_line = line.split(" ")
        inc = int(new_line[2]) - int(new_line[3])
        if inc > 0:
            total_average += inc
        firm_dict[new_line[0]] = inc
    total_average = total_average / firm_number
    firm_dict["average profit"] = total_average
firm_list.append(firm_dict)
print(firm_list)

with open("Ex.7.json", "w", encoding="UTF-8") as write_f:
    json.dump(firm_list, write_f)