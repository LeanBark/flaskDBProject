import json
import random
menu_items = []
with open("menu_items.txt", "r") as in_file:
    for line in in_file:
        menu_items.append(in_file.readline().strip("\n"))
seen = set()
unique_list = []
for item in menu_items:
    if item not in seen:
        seen.add(item)
        unique_list.append(item)
        

# print(menu_items)
with open("add_menus.json", "r") as next_in:
    restaurants = json.load(next_in)

for restaurant in restaurants:
    # print([restaurants[restaurant]["menu_item"][i] for i in range(10)])
    for item in restaurants[restaurant]["menu_item"]:
        unique_list.append(item)

final_list = unique_list[:961]
# print(final_list)
# print(len(final_list))
# unique_list = list(dict.fromkeys(menu_items))

restaurants_list = list(restaurants.keys())
random.seed(4)
# test_list = [round(random.uniform(3.25, 18.65),2) for i in range(10)]
# print(test_list)
i = 10
for j in range(len(restaurants_list)):
    
    if i % 10 == 0 and i!=0:
        restaurants[restaurants_list[j]]["menu_item"] = final_list[i-10: i]
        restaurants[restaurants_list[j]]["unit_price"] = [round(random.uniform(3.25, 18.65),2) for i in range(10)]
    i+=10

for restaurant in restaurants:
    print(restaurants[restaurant])

with open("sample_data.json", "w") as out_file:
    json.dump(restaurants, out_file)


    # for i in range(0, len(final_list), 10):
    #     if i % 10 == 0 and i!=0:
            # print(i)
            # print(i-10)
            # print(final_list[i-10:i])
            # print(restaurants[restaurants_list[i-10]])
            # restaurants[restaurant]["menu_item"] = final_list[i-10:i]
            
        # elif i == len(final_list) - 1:
        #     print(i)
        #     print(i-9)
        #     print(final_list[i-9:i+1])
            # restaurants[restaurant]["menu_item"] = final_list[i-9:i+1]

