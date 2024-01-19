from flask import Flask, render_template, json, redirect, flash
from flask import request
from datetime import date
from io import StringIO
import database.db_connector as db
import pandas as pd
import os, openpyxl


today = date.today()


db_connection = db.connect_to_database()
app = Flask(__name__)

app.static_folder = 'static'
app.secret_key = "add_secret_key_here"
#TODO: Modularize redundent query code blocks
#TODO: Implement Pandas functionality to generate mock reports 
#TODO: Add comments for functions and parameters with type hinting
#TODO: Additional error-catching for queries and posts


#------------------------------------ROUTE FOR HOMEPAGE----------------------------------------------------------------------

@app.route('/')
def root():
    restaurant_query = "SELECT * FROM Restaurants ORDER BY name ASC;"
    restaurants = db.execute_query(db_connection=db_connection, query=restaurant_query)
    all_restaurants = restaurants.fetchall()
    return render_template("main.j2", restaurants=all_restaurants)


# -------------------------------------------RESTAURANTS TABLE OPERATIONS-------------------------------------------------------------

#-------------------------------ROUTE FOR CREATING/READING ALL RESTAURANTS IN RESTAURANTS TABLE----------------------------
@app.route('/restaurants', methods=['GET', 'POST'])
def restaurants():
    # if user wishes to add a new restaurant to the table of all restaurants stored in the database
    if request.method == "POST":
        if request.form.get("Add Restaurant"):
            name = request.form["restaurant-name"]
            address = request.form["restaurant-address"]
            category = request.form["restaurant-food-category"]
            query = "INSERT INTO Restaurants (name, address, food_categoryID) VALUES (%s, %s, %s);"
            db.execute_query(db_connection=db_connection, query=query, query_params=(name, address, category))
            return redirect("/restaurants")
    
    # if user wishes to view the information of the selected restaurant
    if request.method == "GET":
        query = """SELECT Restaurants.restaurantID AS Id, Restaurants.name AS Name, Restaurants.address AS Address, FoodCategories.name AS Category 
        FROM Restaurants INNER JOIN FoodCategories ON Restaurants.food_categoryID = FoodCategories.food_categoryID ORDER BY Restaurants.restaurantID ASC;"""
        cursor = db.execute_query(db_connection=db_connection, query=query)
        results = cursor.fetchall()
        query1 = "SELECT * FROM FoodCategories ORDER BY food_categoryID ASC;"
        categories = db.execute_query(db_connection=db_connection, query=query1)
        selected_categories = categories.fetchall()
        return render_template("restaurants.j2", restaurants=results, food_category=selected_categories)

#-------------------------------ROUTE FOR UPDATING SELECTED RESTAURANT INFORMATION IN RESTAURANTS TABLE--------------------
@app.route('/edit-restaurant/<int:restaurantID>', methods=["GET", "POST"])
def edit_restaurant(restaurantID):

    # if user wishes to edit an existing restaurant's information in database
    if request.method == "POST":
        if request.form.get("Edit Restaurant"):
            id = request.form['restaurant-id']
            name = request.form["restaurant-name"]
            address = request.form["restaurant-address"]
            category = request.form["restaurant-food-category"]
            query = "UPDATE Restaurants SET name = %s, address = %s, food_categoryID = %s WHERE restaurantID = %s;"
            db.execute_query(db_connection=db_connection, query=query, query_params=(name, address, category, id))
            return redirect("/restaurants")

    # if user wishes to access updated list of all restaurants in database
    if request.method == "GET":
        id_query = "SELECT * FROM Restaurants WHERE restaurantID = %s" % (restaurantID)
        cursor = db.execute_query(db_connection=db_connection, query=id_query)
        results = cursor.fetchall()
        category_query = "SELECT * FROM FoodCategories"
        categories = db.execute_query(db_connection=db_connection, query=category_query)
        selected_categories = categories.fetchall()
        return render_template("edit_restaurants.j2", restaurants=results, food_category=selected_categories)

#-------------------------------ROUTE FOR DELETING A RESTAURANT FROM RESTAURANTS TABLE-------------------------------------

@app.route('/delete-restaurant/<int:restaurantID>')
def delete_restaurant(restaurantID):
    delete_query = "DELETE FROM Restaurants WHERE restaurantID = %s" % (restaurantID)
    db.execute_query(db_connection=db_connection, query=delete_query)
    return redirect('/restaurants') 

#--------------------------------------------MENUITEMS TABLE OPERATIONS---------------------------------------------------------------

#-------------------------------ROUTE FOR VIEWING ALL MENU ITEMS IN MENUITEMS TABLE----------------------------------------

@app.route("/restaurant-menu")
#if user wishes to view master table of all items within MenuItems table stored in database
def display_all_items():
    all_items_query = "SELECT * FROM MenuItems ORDER BY menu_itemID ASC;"
    returned_items = db.execute_query(db_connection=db_connection, query=all_items_query)
    all_items = returned_items.fetchall()
    return render_template("menu_items.j2", item_list=all_items)


#-------------------------------ROUTE FOR READING/CREATING MENU ITEMS BY RESTAURANT----------------------------------------

@app.route("/restaurant-menu/<int:restaurantID>", methods=["GET", "POST"])
def display_menu_items(restaurantID):
    if request.method == "POST":
        
        # if user requests access to a specific restaurant's menu in database
        if request.form.get("View Restaurant Menu"):
            menu_query = """SELECT MenuItems.restaurantID, MenuItems.menu_itemID, MenuItems.name AS Item, MenuItems.calories AS Calories, MenuItems.unit_price AS Price, FoodCategories.name AS Category
            FROM MenuItems JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
            LEFT JOIN FoodCategories ON MenuItems.food_categoryID = FoodCategories.food_categoryID
            WHERE Restaurants.restaurantID = %s;""" % (restaurantID)
            matching_items = db.execute_query(db_connection=db_connection, query=menu_query)
            all_menu_items = matching_items.fetchall()
            
            name_query = "SELECT * FROM Restaurants WHERE restaurantID = %s;" % (restaurantID)
            matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
            restaurant_name = matching_restaurant.fetchall()

            category_query = "SELECT * FROM FoodCategories"
            categories = db.execute_query(db_connection=db_connection, query=category_query)
            selected_categories = categories.fetchall()
            
            # if there are no invoices associated with the selected restaurant
            if matching_items.rowcount == 0:
                return render_template("menu_not_found.j2", selected_restaurant=restaurant_name, food_category=selected_categories)

            else:
                return render_template("restaurant_menu.j2", menu_list=all_menu_items, restaurant_name=restaurant_name, food_category=selected_categories)
        
        # if a user wants to add a new item to the selected restaurant's menu in the databse
        elif request.form.get("Add Menu Item"):
            item_name = request.form["menu-item-name"]
            calories = request.form["menu-item-calories"]
            item_cost = request.form["menu-item-price"]
            category = request.form["menu-item-food-category"]
            query = "INSERT INTO MenuItems (name, calories, unit_price, food_categoryID, restaurantID) VALUES (%s, %s, %s, %s, %s);"
            db.execute_query(db_connection=db_connection, query=query, query_params=(item_name, calories, item_cost, category, restaurantID))
            
            menu_query = """SELECT MenuItems.restaurantID, MenuItems.menu_itemID, MenuItems.name AS Item, MenuItems.calories AS Calories, MenuItems.unit_price AS Price, FoodCategories.name AS Category
            FROM MenuItems JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
            LEFT JOIN FoodCategories ON MenuItems.food_categoryID = FoodCategories.food_categoryID
            WHERE Restaurants.restaurantID = %s;""" % (restaurantID)
            matching_items = db.execute_query(db_connection=db_connection, query=menu_query)
            all_menu_items = matching_items.fetchall()
            
            name_query = "SELECT * FROM Restaurants WHERE restaurantID = %s;" % (restaurantID)
            matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
            restaurant_name = matching_restaurant.fetchall()

            category_query = "SELECT * FROM FoodCategories"
            categories = db.execute_query(db_connection=db_connection, query=category_query)
            selected_categories = categories.fetchall()
            return render_template("restaurant_menu.j2", menu_list=all_menu_items, restaurant_name=restaurant_name, food_category=selected_categories)
        
        elif request.form.get("Generate Menu CSV"):
            menu_query = """SELECT MenuItems.restaurantID, MenuItems.menu_itemID, MenuItems.name AS Item, MenuItems.calories AS Calories, MenuItems.unit_price AS Price, FoodCategories.name AS Category
            FROM MenuItems JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
            LEFT JOIN FoodCategories ON MenuItems.food_categoryID = FoodCategories.food_categoryID
            WHERE Restaurants.restaurantID = %s;""" % (restaurantID)
            matching_items = db.execute_query(db_connection=db_connection, query=menu_query)
            all_menu_items = matching_items.fetchall()
            
            name_query = "SELECT * FROM Restaurants WHERE restaurantID = %s;" % (restaurantID)
            matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
            restaurant_name = matching_restaurant.fetchall()

            category_query = "SELECT * FROM FoodCategories"
            categories = db.execute_query(db_connection=db_connection, query=category_query)
            selected_categories = categories.fetchall()
            menu_information = json.dumps(all_menu_items)
            df = pd.read_json(StringIO(menu_information))
            
            try:
                df.to_csv(f"{os.environ.get('HOMEDRIVE')}{os.environ.get('HOMEPATH')}\Downloads\{restaurant_name[0]['name']}_menu.csv")
                flash("Menu Successfully Downloaded to local 'Downloads' Directory!", category="menu-path-success")
            except:
                df.to_csv(f"./flaskDBProject/static/restaurant_menus/{restaurant_name[0]['name']}_menu.csv")
                flash("Invalid Default Path: Menu Downloaded to Current 'static/restaurant_menus' Folder in Current Directory", category="menu-path-error")
            
            if matching_items.rowcount == 0:
                return render_template("menu_not_found.j2", selected_restaurant=restaurant_name, food_category=selected_categories)

            else:
                return render_template("restaurant_menu.j2", menu_list=all_menu_items, restaurant_name=restaurant_name, food_category=selected_categories)
        
        else:
            redirect("/")
    
    # if user wishes to revisit the table of current menu items specific to the restaurant
    else:
        menu_query = """SELECT MenuItems.restaurantID, MenuItems.menu_itemID, MenuItems.name AS Item, MenuItems.calories AS Calories, MenuItems.unit_price AS Price, FoodCategories.name AS Category
        FROM MenuItems JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
        LEFT JOIN FoodCategories ON MenuItems.food_categoryID = FoodCategories.food_categoryID
        WHERE Restaurants.restaurantID = %s;""" % (restaurantID)
        matching_items = db.execute_query(db_connection=db_connection, query=menu_query)
        all_menu_items = matching_items.fetchall()
        
        name_query = "SELECT * FROM Restaurants WHERE restaurantID = %s;" % (restaurantID)
        matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
        restaurant_name = matching_restaurant.fetchall()

        category_query = "SELECT * FROM FoodCategories"
        categories = db.execute_query(db_connection=db_connection, query=category_query)
        selected_categories = categories.fetchall()
        
        # if there are no invoices linked to selected restaurant
        if matching_items.rowcount == 0:
                return render_template("menu_not_found.j2", selected_restaurant=restaurant_name, food_category=selected_categories)
        else:
            return render_template("restaurant_menu.j2", menu_list=all_menu_items, restaurant_name=restaurant_name, food_category=selected_categories)

#-------------------------------ROUTE FOR UPDATING MENU ITEMS BY RESTAURANT------------------------------------------------

@app.route("/edit-menu-item/<int:menu_itemID>", methods=["GET", "POST"])
def edit_menu_items(menu_itemID):
    
    # if user wishes to edit an existing restaurant's information in database
    if request.method == "POST":
        if request.form.get("Edit Restaurant"):
            restaurant_id = request.form['restaurant']
            item_name = request.form["menu-item-name"]
            calories = request.form["menu-item-calories"]
            item_cost = request.form["menu-item-price"]
            category = request.form["menu-item-food-category"]
            query = "UPDATE MenuItems SET name = %s, calories = %s, unit_price = %s, food_categoryID = %s WHERE menu_itemID = %s;"
            db.execute_query(db_connection=db_connection, query=query, query_params=(item_name, calories, item_cost, category, menu_itemID))
            
            menu_query = """SELECT MenuItems.restaurantID, MenuItems.menu_itemID, MenuItems.name AS Item, MenuItems.calories AS Calories, MenuItems.unit_price AS Price, FoodCategories.name AS Category
            FROM MenuItems JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
            LEFT JOIN FoodCategories ON MenuItems.food_categoryID = FoodCategories.food_categoryID
            WHERE Restaurants.restaurantID = %s;""" % (restaurant_id)
            matching_items = db.execute_query(db_connection=db_connection, query=menu_query)
            all_menu_items = matching_items.fetchall()
            
            name_query = "SELECT * FROM Restaurants WHERE restaurantID = %s;" % (restaurant_id)
            matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
            restaurant_name = matching_restaurant.fetchall()

            category_query = "SELECT * FROM FoodCategories"
            categories = db.execute_query(db_connection=db_connection, query=category_query)
            selected_categories = categories.fetchall()
            return render_template("restaurant_menu.j2", menu_list=all_menu_items, restaurant_name=restaurant_name, food_category=selected_categories)

    # if user wishes to access updated list of all restaurants in database
    if request.method == "GET":
        menu_query = """SELECT MenuItems.restaurantID, MenuItems.menu_itemID, MenuItems.name AS Item, MenuItems.calories AS Calories, MenuItems.unit_price AS Price, FoodCategories.name AS Category
        FROM MenuItems JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
        LEFT JOIN FoodCategories ON MenuItems.food_categoryID = FoodCategories.food_categoryID
        WHERE MenuItems.menu_itemID = %s;""" % (menu_itemID)
        matching_items = db.execute_query(db_connection=db_connection, query=menu_query)
        all_menu_items = matching_items.fetchall()
        
        name_query = """SELECT Restaurants.name FROM MenuItems INNER JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
        WHERE MenuItems.menu_itemID = %s;""" % (menu_itemID)
        matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
        restaurant_name = matching_restaurant.fetchall()

        category_query = "SELECT * FROM FoodCategories"
        categories = db.execute_query(db_connection=db_connection, query=category_query)
        selected_categories = categories.fetchall()
        return render_template("edit_restaurant_menu.j2", menu_list=all_menu_items, restaurant_name=restaurant_name, food_category=selected_categories)

#-------------------------------ROUTE FOR DELETING SELECTED MENUITEMS BY RESTAURANT----------------------------------------    
    
@app.route('/delete-menu-item/<int:menu_itemID>')
def delete_menu_item(menu_itemID):
    # if user decides to delete a specific menu item from the selected restaurant's table of menu items 
    restaurant_query = "SELECT restaurantID FROM MenuItems WHERE menu_itemID = %s" % (menu_itemID)
    selected_restaurant = db.execute_query(db_connection=db_connection, query=restaurant_query)
    restaurant_identity = selected_restaurant.fetchall()
    for key in restaurant_identity[0].keys():
            if key == "restaurantID":
                restaurant_id = restaurant_identity[0][key]
     
    delete_query = "DELETE FROM MenuItems WHERE menu_itemID = %s" % (menu_itemID)
    db.execute_query(db_connection=db_connection, query=delete_query)

    menu_query = """SELECT MenuItems.restaurantID, MenuItems.menu_itemID, MenuItems.name AS Item, MenuItems.calories AS Calories, MenuItems.unit_price AS Price, FoodCategories.name AS Category
    FROM MenuItems JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID
    LEFT JOIN FoodCategories ON MenuItems.food_categoryID = FoodCategories.food_categoryID
    WHERE Restaurants.restaurantID = %s;""" % (restaurant_id)
    matching_items = db.execute_query(db_connection=db_connection, query=menu_query)
    all_menu_items = matching_items.fetchall()
    
    name_query = "SELECT * FROM Restaurants WHERE restaurantID = %s;" % (restaurant_id)
    matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
    restaurant_name = matching_restaurant.fetchall()

    category_query = "SELECT * FROM FoodCategories"
    categories = db.execute_query(db_connection=db_connection, query=category_query)
    selected_categories = categories.fetchall()
    
    # if user deletes only menu item in entire restaurant menu
    if matching_items.rowcount == 0:
            return render_template("menu_not_found.j2", selected_restaurant=restaurant_name, food_category=selected_categories)
    else:
        return render_template("restaurant_menu.j2", menu_list=all_menu_items, restaurant_name=restaurant_name, food_category=selected_categories)

#--------------------------------------------RESTAURANTSALESINVOICES TABLE OPERATIONS-------------------------------------------------    

#-------------------------------ROUTE FOR VIEWING ALL INVOICES WITHIN RESTAURANTSALESINVOICE TABLE-------------------------

@app.route("/invoices")
def display_all_invoices():
    # if user wishes to reference master table of all restaurant sales invoices
    universal_invoice_query = "SELECT * FROM RestaurantSalesInvoices ORDER BY invoiceID ASC;"
    universal_invoices = db.execute_query(db_connection=db_connection, query=universal_invoice_query)
    result_invoices = universal_invoices.fetchall()
    return render_template("invoices.j2", invoice_list=result_invoices)

#-------------------------------ROUTE FOR READING/CREATING INVOICES BY RESTAURANT------------------------------------------

@app.route("/invoices/<int:restaurantID>", methods=["GET", "POST"])
def display_invoices(restaurantID):
    # if user wishes to view the table containing the current invoices of the selected restaurant
    if request.method == "POST":
        if request.form.get("View Restaurant Invoices"):
            invoices_query = """SELECT RestaurantSalesInvoices.invoiceID, RestaurantSalesInvoices.restaurantID, Restaurants.name AS Restaurant,
            MenuItems.name AS Item, RestaurantSalesInvoices.quantity_sold AS Quantity, RestaurantSalesInvoices.date_sold AS DateSold,
            RestaurantSalesInvoices.quantity_sold * MenuItems.unit_price AS SaleTotal 
            FROM RestaurantSalesInvoices
            JOIN Restaurants ON RestaurantSalesInvoices.restaurantID = Restaurants.restaurantID
            JOIN MenuItems ON RestaurantSalesInvoices.menu_itemID = MenuItems.menu_itemID
            WHERE RestaurantSalesInvoices.restaurantID = %s;""" % (restaurantID)
            invoice_list = db.execute_query(db_connection=db_connection, query=invoices_query)
            invoices = invoice_list.fetchall()
            

            menu_item_query = "SELECT * FROM MenuItems WHERE MenuItems.restaurantID = %s;" % (restaurantID)
            menu_list = db.execute_query(db_connection=db_connection, query=menu_item_query)
            menu_items = menu_list.fetchall()

            if invoice_list.rowcount == 0:
                restaurant_query = "SELECT * FROM Restaurants WHERE restaurantID = %s" % (restaurantID)
                restaurant_result = db.execute_query(db_connection=db_connection, query=restaurant_query)
                selected_restaurant = restaurant_result.fetchall()
                return render_template("invoices_not_found.j2", selected_restaurant=selected_restaurant, menu=menu_items)
            
            else:
                return render_template("restaurant_invoices.j2", invoices=invoices, menu=menu_items)
        
        # if user decides to add a new invoice to the table of invoices for the selected restaurant
        elif request.form.get("Add Invoice"):
            menu_item_ID = request.form["menu-item-value"]
            quantity_sold = request.form["quantity-sold"]
            date_sold = request.form.get("sales-date")
            insert_query = "INSERT INTO RestaurantSalesInvoices (menu_itemID, quantity_sold, date_sold, restaurantID) VALUES (%s, %s, %s, %s);"
            db.execute_query(db_connection=db_connection, query=insert_query, query_params=(menu_item_ID, quantity_sold, date_sold, restaurantID))

            invoices_query = """SELECT RestaurantSalesInvoices.invoiceID, RestaurantSalesInvoices.restaurantID, Restaurants.name AS Restaurant,
            MenuItems.name AS Item, RestaurantSalesInvoices.quantity_sold AS Quantity, RestaurantSalesInvoices.date_sold AS DateSold,
            RestaurantSalesInvoices.quantity_sold * MenuItems.unit_price AS SaleTotal
            FROM RestaurantSalesInvoices 
            JOIN Restaurants ON RestaurantSalesInvoices.restaurantID = Restaurants.restaurantID
            JOIN MenuItems ON RestaurantSalesInvoices.menu_itemID = MenuItems.menu_itemID
            WHERE RestaurantSalesInvoices.restaurantID = %s;""" % (restaurantID)
            invoice_list = db.execute_query(db_connection=db_connection, query=invoices_query)
            invoices = invoice_list.fetchall()

            menu_item_query = "SELECT * FROM MenuItems WHERE MenuItems.restaurantID = %s" % (restaurantID)
            menu_list = db.execute_query(db_connection=db_connection, query=menu_item_query)
            menu_items = menu_list.fetchall()
            
            return render_template("restaurant_invoices.j2", invoices=invoices, menu=menu_items)

        elif request.form.get("Generate CSV Report"):
            invoices_query = """SELECT RestaurantSalesInvoices.invoiceID, RestaurantSalesInvoices.restaurantID, Restaurants.name AS Restaurant,
            MenuItems.name AS Item, RestaurantSalesInvoices.quantity_sold AS Quantity, RestaurantSalesInvoices.date_sold AS DateSold,
            RestaurantSalesInvoices.quantity_sold * MenuItems.unit_price AS SaleTotal 
            FROM RestaurantSalesInvoices
            JOIN Restaurants ON RestaurantSalesInvoices.restaurantID = Restaurants.restaurantID
            JOIN MenuItems ON RestaurantSalesInvoices.menu_itemID = MenuItems.menu_itemID
            WHERE RestaurantSalesInvoices.restaurantID = %s;""" % (restaurantID)
            invoice_list = db.execute_query(db_connection=db_connection, query=invoices_query)
            invoices = invoice_list.fetchall()
            report_information = json.dumps(invoices)
            df = pd.read_json(StringIO(report_information))

            try:
                df.to_csv(f"{os.environ.get('HOMEDRIVE')}{os.environ.get('HOMEPATH')}\Downloads\{invoices[0]['Restaurant']}_invoices.csv")
                flash("Successfully Downloaded to local 'Downloads' Directory!", category="path-success")
            except:
                df.to_csv(f"./flaskDBProject/static/invoice_reports/{invoices[0]['Restaurant']}_invoices.csv")
                flash("Invalid Default Path: Downloaded to Current 'static/invoice_reports' Folder in Current Directory", category="path-error")

            menu_item_query = "SELECT * FROM MenuItems WHERE MenuItems.restaurantID = %s;" % (restaurantID)
            menu_list = db.execute_query(db_connection=db_connection, query=menu_item_query)
            menu_items = menu_list.fetchall()

            if invoice_list.rowcount == 0:
                restaurant_query = "SELECT * FROM Restaurants WHERE restaurantID = %s" % (restaurantID)
                restaurant_result = db.execute_query(db_connection=db_connection, query=restaurant_query)
                selected_restaurant = restaurant_result.fetchall()
                return render_template("invoices_not_found.j2", selected_restaurant=selected_restaurant, menu=menu_items)
            
            else:
                return render_template("restaurant_invoices.j2", invoices=invoices, menu=menu_items)

        else:
            # use for error catching
            redirect("/")
    
    # if user wishes to revist the tables of currently existing invoices for the selected restaurant
    else:
        invoices_query = """SELECT RestaurantSalesInvoices.invoiceID, RestaurantSalesInvoices.restaurantID, Restaurants.name AS Restaurant,
        MenuItems.name AS Item, RestaurantSalesInvoices.quantity_sold AS Quantity, RestaurantSalesInvoices.date_sold AS DateSold,
        RestaurantSalesInvoices.quantity_sold * MenuItems.unit_price AS SaleTotal
        FROM RestaurantSalesInvoices 
        JOIN Restaurants ON RestaurantSalesInvoices.restaurantID = Restaurants.restaurantID
        JOIN MenuItems ON RestaurantSalesInvoices.menu_itemID = MenuItems.menu_itemID
        WHERE RestaurantSalesInvoices.restaurantID = %s;""" % (restaurantID)
        invoice_list = db.execute_query(db_connection=db_connection, query=invoices_query)
        invoices = invoice_list.fetchall()
        
        menu_item_query = "SELECT * FROM MenuItems WHERE MenuItems.restaurantID = %s;" % (restaurantID)
        menu_list = db.execute_query(db_connection=db_connection, query=menu_item_query)
        menu_items = menu_list.fetchall()
        
        return render_template("restaurant_invoices.j2", invoices=invoices, menu=menu_items)

#-------------------------------ROUTE FOR UPDATING INVOICES BY RESTAURANT--------------------------------------------------
    
@app.route("/edit-invoice/<int:invoiceID>", methods=["GET", "POST"])
def edit_invoice(invoiceID):
    
    # if user decides to submit changes to an existing restaurant's invoice information in database
    if request.method == "POST":
        if request.form.get("Edit Invoice"):
            restaurant_id = request.form['restaurant-id']
            item_id = request.form["menu-item-id"]
            quantity_sold = request.form["quantity-sold"]
            date_sold = request.form.get("sales-date")
            query = "UPDATE RestaurantSalesInvoices SET menu_itemID = %s, quantity_sold = %s, date_sold = %s, restaurantID = %s WHERE invoiceID = %s;"
            db.execute_query(db_connection=db_connection, query=query, query_params=(item_id, quantity_sold, date_sold, restaurant_id, invoiceID))
            
            invoice_query = """SELECT RestaurantSalesInvoices.invoiceID, RestaurantSalesInvoices.restaurantID, Restaurants.name AS Restaurant,
            MenuItems.name AS Item, RestaurantSalesInvoices.quantity_sold AS Quantity, RestaurantSalesInvoices.date_sold AS DateSold,
            RestaurantSalesInvoices.quantity_sold * MenuItems.unit_price AS SaleTotal
            FROM RestaurantSalesInvoices 
            JOIN Restaurants ON RestaurantSalesInvoices.restaurantID = Restaurants.restaurantID
            JOIN MenuItems ON RestaurantSalesInvoices.menu_itemID = MenuItems.menu_itemID
            WHERE RestaurantSalesInvoices.restaurantID = %s;""" % (restaurant_id)
            matching_invoices = db.execute_query(db_connection=db_connection, query=invoice_query)
            all_invoices = matching_invoices.fetchall()
            
            name_query = "SELECT * FROM Restaurants WHERE restaurantID = %s;" % (restaurant_id)
            matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
            restaurant_name = matching_restaurant.fetchall()

            menu_query = "SELECT * FROM MenuItems WHERE MenuItems.restaurantID = %s;" % (restaurant_id) 
            menu_items = db.execute_query(db_connection=db_connection, query=menu_query)
            selected_menus = menu_items.fetchall()
            return render_template("restaurant_invoices.j2", invoices=all_invoices, restaurant_name=restaurant_name, menu=selected_menus)

    # if user decides to edit the information of an invoice within selected restaurant's list of invoices    
    if request.method == "GET":
        invoice_query = """SELECT RestaurantSalesInvoices.invoiceID, RestaurantSalesInvoices.restaurantID, RestaurantSalesInvoices.menu_itemID,
        Restaurants.name AS Restaurant, MenuItems.name AS Item, RestaurantSalesInvoices.quantity_sold AS Quantity, RestaurantSalesInvoices.date_sold AS DateSold,
        RestaurantSalesInvoices.quantity_sold * MenuItems.unit_price AS SaleTotal
        FROM RestaurantSalesInvoices 
        JOIN Restaurants ON RestaurantSalesInvoices.restaurantID = Restaurants.restaurantID
        JOIN MenuItems ON RestaurantSalesInvoices.menu_itemID = MenuItems.menu_itemID
        WHERE RestaurantSalesInvoices.invoiceID = %s;""" % (invoiceID)
        matching_items = db.execute_query(db_connection=db_connection, query=invoice_query)
        all_invoices = matching_items.fetchall()
        
        name_query = """SELECT Restaurants.restaurantID, Restaurants.name FROM RestaurantSalesInvoices INNER JOIN Restaurants 
        ON RestaurantSalesInvoices.restaurantID = Restaurants.restaurantID
        WHERE RestaurantSalesInvoices.invoiceID = %s;""" % (invoiceID)
        matching_restaurant = db.execute_query(db_connection=db_connection, query=name_query)
        restaurant_name = matching_restaurant.fetchall()
        for key in restaurant_name[0].keys():
            if key == "restaurantID":
                target_restaurant = restaurant_name[0][key]
        
        get_menu_query = """SELECT MenuItems.menu_itemID, MenuItems.name FROM MenuItems
        JOIN Restaurants ON MenuItems.restaurantID = Restaurants.restaurantID WHERE Restaurants.restaurantID = %s;""" % (target_restaurant)
        selected_items = db.execute_query(db_connection=db_connection, query=get_menu_query)
        selected_menu = selected_items.fetchall()

        return render_template("edit_restaurant_invoice.j2", invoices=all_invoices, restaurant_name=restaurant_name, menu=selected_menu)

#--------------------------------------------END OF ROUTES----------------------------------------------------------------------------
# Listener
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8560))
    app.run(port=port, debug=True)

