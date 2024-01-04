import json
from datetime import datetime
import database.db_connector as db

db_connection = db.connect_to_database()

# function can be called in tandem with json file to add increased sample data to database
def collect_data():
    with open("add_menus.json", "r") as in_file:
        restaurants_data = json.load(in_file)

    restaurant_menus = {}
    entry_size = len(restaurants_data["4food"]["menu_item"]) # number of randomly generated items to add to each restaurant menu

    # list comprehension to generate a list of menu items for each restaurant during iteration over JSON file 
    for restaurant in restaurants_data.keys():
        # each restaurant now has a "menu" key with a list of arrays as its value, where each array contains individual item information  
        restaurant_menus[restaurant] = {"menu":[[restaurants_data[restaurant]["menu_item"][i], restaurants_data[restaurant]["calories"][i],
                                                restaurants_data[restaurant]["food_category"][i]] for i in range(entry_size)],
                                                "address": restaurants_data[restaurant]["address"],
                                                "restaurant_category": restaurants_data[restaurant]["restaurant_category"]}
    
        
    # initial query made to identify new restaurants that do not exist within the database
    names_query = "SELECT restaurantID, name FROM Restaurants;"
    restaurant_names = db.execute_query(db_connection=db_connection, query=names_query)
    existing_names = restaurant_names.fetchall() # all restaurants already in database
    
    # creates list of all existing restaurants in current database
    current_restaurants = []
    for value in existing_names:
        current_restaurants.append(value["name"])
    
    # restaurants that do not currently exist in database are added to Restaurants table first
    for key in restaurant_menus.keys():
        if key not in current_restaurants:
            name = key
            print(name)
            address = restaurant_menus[key]["address"]
            category_name = restaurant_menus[key]['restaurant_category']

            restaurant_category_query = 'SELECT food_categoryID FROM FoodCategories WHERE FoodCategories.name = "%s";' % category_name
            category_results = db.execute_query(db_connection=db_connection, query=restaurant_category_query)
            result_category = category_results.fetchall()
            restaurant_categoryID = result_category[0]["food_categoryID"]

            
            add_new_query = 'INSERT INTO Restaurants (name, address, food_categoryID) VALUES (%s, %s, %s);'
            db.execute_query(db_connection=db_connection, query=add_new_query, query_params=(name, address, restaurant_categoryID))
    
    # after adding new restaurants and their information to database, a new query is made to include these in selection
    updated_names_query = "SELECT restaurantID, name FROM Restaurants;"
    updated_restaurant_names = db.execute_query(db_connection=db_connection, query=updated_names_query)
    updated_existing_names = updated_restaurant_names.fetchall() # updated list of restaurants, including new additions

    # using updated selection from Restuarants, all menu items for each restaurant in JSON file are added to MenuItems table
    for restaurant in updated_existing_names:
        id_value = restaurant["restaurantID"]
        name = restaurant["name"]
        
        # adds each menu item associated with a specific restaurant in add_items.json to MenuItems table
        for i in range(len(restaurant_menus[name]["menu"])):
            item_name = restaurant_menus[name]["menu"][i][0]
            calorie_amt = restaurant_menus[name]["menu"][i][1]
            item_category = restaurant_menus[name]["menu"][i][2]
            
            categories_query = 'SELECT food_categoryID FROM FoodCategories WHERE name="%s";' % (item_category)
            category_name = db.execute_query(db_connection=db_connection, query=categories_query)
            selected_category = category_name.fetchall()

            category_id = selected_category[0]["food_categoryID"]
            insert_data_query = "INSERT INTO MenuItems(name, calories, food_categoryID, restaurantID) VALUES (%s,%s, %s, %s);"
            db.execute_query(db_connection=db_connection, query=insert_data_query, query_params=(item_name,calorie_amt, category_id, id_value))

if __name__ == "__main__":
    # testing and timing
    now_time = datetime.now()
    start_time = datetime(now_time.year, now_time.month , now_time.day)
    
    try:
        collect_data()
    except:
        print("there was an error in the input data format\n")
        print("Format as {'<restaurant_name>': {'menu_item':[<name1>,..], 'calories': [<number1>,..]}, 'food_category':[<category1>,..]},{..")

    finish_time = datetime.now()
    duration = finish_time - now_time
    seconds, microseconds = divmod(duration.microseconds, 1000000)
    print(f'The function took {seconds} seconds and {microseconds} ms to run.')