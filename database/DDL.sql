SET FOREIGN_KEY_CHECKS = 0;
SET AUTOCOMMIT = 0;


-----------------------------CREATE TABLES-----------------------------------------

--------------------CREATE FOODCATEGORIES TABLE----------------------
CREATE OR REPLACE TABLE FoodCategories (
    food_categoryID int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY (food_categoryID),
    UNIQUE (name)
);


--------------------CREATE RESTAURANTS TABLE----------------------
CREATE OR REPLACE TABLE Restaurants (
    restaurantID int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    address varchar(255) NOT NULL,
    food_categoryID int,
    PRIMARY KEY (restaurantID),
    FOREIGN KEY (food_categoryID) REFERENCES FoodCategories(food_categoryID)
    ON DELETE RESTRICT,
    UNIQUE (name)
);

---------------------CREATE MENUITEMS TABLE-----------------------------
CREATE OR REPLACE TABLE MenuItems (
    menu_itemID int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    calories int NOT NULL,
    unit_price decimal(4,2) NOT NULL,
    food_categoryID int,
    restaurantID int,
    PRIMARY KEY (menu_itemID),
    FOREIGN KEY (food_categoryID) REFERENCES FoodCategories(food_categoryID)
    ON DELETE RESTRICT,
    FOREIGN KEY (restaurantID) REFERENCES Restaurants(restaurantID)
    ON DELETE CASCADE
);

---------------------CREATE RESTAURANTSALESINVOICES TABLE------------------
CREATE OR REPLACE TABLE RestaurantSalesInvoices (
    invoiceID int NOT NULL AUTO_INCREMENT,
    menu_itemID int,
    quantity_sold int NOT NULL,
    restaurantID int,
    PRIMARY KEY (invoiceID),
    FOREIGN KEY (menu_itemID) REFERENCES MenuItems(menu_itemID)
    ON DELETE CASCADE,
    FOREIGN KEY (restaurantID) REFERENCES Restaurants(restaurantID)
    ON DELETE CASCADE
);

---------------------------------INSERT SAMPLE DATA--------------------------------------

--------------POPULATING FOODCATEGORIES TABLE--------------------------------
INSERT INTO FoodCategories (
    name
)
VALUES
    ("American"),
    ("Barbeque"),
    ("Chinese"),
    ("French"),
    ("Hamburger"),
    ("Italian"),
    ("Indian"),
    ("Japanese"),
    ("Mexican"),
    ("Pizza"),
    ("Sandwiches"),
    ("Seafood"),
    ("Steak"),
    ("Sushi"),
    ("Thai");

---------------POPULATING RESTAURANTS TABLE-------------------------
INSERT INTO Restaurants (
    name,
    address,
    food_categoryID
)

VALUES 
    ("4food", "35 Sage Circle", (SELECT food_categoryID FROM FoodCategories WHERE name="Sandwiches")),
    ("Bertuccis", "94 Continental Drive", (SELECT food_categoryID FROM FoodCategories WHERE name="Italian")),
    ("Baskin Robbins", "67284 Schlimgen Plaza", (SELECT food_categoryID FROM FoodCategories WHERE name="American")),
    ("Bareburger", "90460 Loomis Trail", (SELECT food_categoryID FROM FoodCategories WHERE name="Hamburger")),
    ("Bds Mongolian Grill", "201 Commercial Road", (SELECT food_categoryID FROM FoodCategories WHERE name="Barbeque")),
    ("Ponsa Steakhouse", "8 Jennifer Pass", (SELECT food_categoryID FROM FoodCategories WHERE name="Steak")),
    ("Aki Lounge", "389 Bunker Hill Lane", (SELECT food_categoryID FROM FoodCategories WHERE name="Japanese")),
    ("16 Handles", "4483 Roxbury Junction", (SELECT food_categoryID FROM FoodCategories WHERE name="Indian")),
    ("Nand Peri-Peri", "32 Center Street", (SELECT food_categoryID FROM FoodCategories WHERE name="Thai")),
    ("Ralls", "40 Derek Plaza", (SELECT food_categoryID FROM FoodCategories WHERE name="Sushi")),
    ("Golden Krust Caribbean Bakery & Grill", "12449 Truax Place", (SELECT food_categoryID FROM FoodCategories WHERE name="Seafood")),
    ("Mimis Cafe", "34 Pennsylvania Lane", (SELECT food_categoryID FROM FoodCategories WHERE name="Mexican")),
    ("Brixx Wood Fired Pizza", "79666 Gateway Court", (SELECT food_categoryID FROM FoodCategories WHERE name="Pizza")),
    ("K Cafeterias", "32430 Burning Wood Point", (SELECT food_categoryID FROM FoodCategories WHERE name="Chinese")),
    ("Buona Restaurants", "6476 Bashford Plaza", (SELECT food_categoryID FROM FoodCategories WHERE name="French"));

-----------------------POPULATING MENUITEMS TABLE-----------------------------------
INSERT INTO MenuItems (
    name,
    calories,
    unit_price,
    food_categoryID,
    restaurantID
)

VALUES 

    ("Melgal Sandwich", 319, 5.29, (SELECT food_categoryID FROM FoodCategories WHERE name="Sandwiches"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 1)),

    (" Ultimate Caesar Salad", 120, 6.25, (SELECT food_categoryID FROM FoodCategories WHERE name="Italian"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 2)),

    ("Trick OREO Treat Ice Cream", 300, 4.50, (SELECT food_categoryID FROM FoodCategories WHERE name="American"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 3)),

    ("Sweet Fries Snack", 1150, 7.65, (SELECT food_categoryID FROM FoodCategories WHERE name="Hamburger"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 4)),

    ("Egg-on Steak", 860, 9.45, (SELECT food_categoryID FROM FoodCategories WHERE name="Barbeque"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 5)),

    ("Spinach Salad", 360, 5.34, (SELECT food_categoryID FROM FoodCategories WHERE name="Steak"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 6)),

    ("Shrimp Ramen", 250, 8.67, (SELECT food_categoryID FROM FoodCategories WHERE name="Japanese"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 7)),

    ("Passion Fruit Tart", 400, 4.23, (SELECT food_categoryID FROM FoodCategories WHERE name="Indian"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 8)),

    ("Hand battered Fish Dinner", 750, 9.23, (SELECT food_categoryID FROM FoodCategories WHERE name="Thai"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 9)),

    ("Salmon Sashimi", 300, 12.43, (SELECT food_categoryID FROM FoodCategories WHERE name="Sushi"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 10)),

    ("Shirmp Salad", 500, 10.25, (SELECT food_categoryID FROM FoodCategories WHERE name="Seafood"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 11)),

    ("Chili Burrito", 450, 7.66, (SELECT food_categoryID FROM FoodCategories WHERE name="Mexican"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 12)),

    ("Supreme Veggie Pizza", 900, 8.65, (SELECT food_categoryID FROM FoodCategories WHERE name="Pizza"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 13)),

    ("Wanton Soup", 650, 6.28, (SELECT food_categoryID FROM FoodCategories WHERE name="Chinese"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 14)),

    ("Clam Chowder Soup", 600, 12.23, (SELECT food_categoryID FROM FoodCategories WHERE name="French"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 15)),

    ("Mediterranean Ratatouille", 246, 14.36, (SELECT food_categoryID FROM FoodCategories WHERE name="Italian"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 8)),

    ("Swordfish Soba Noodle", 420, 17.56, (SELECT food_categoryID FROM FoodCategories WHERE name="Seafood"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 8));


-------------------------POPULATING RESTAURANTSALESINVOICES TABLE----------------------
INSERT INTO RestaurantSalesInvoices (
    menu_itemID,
    quantity_sold,
    restaurantID
)

VALUES 
    (1, 3, 1),
    (2, 2, 2),
    (3, 1, 3),
    (4, 2, 4),
    (5, 3, 5),
    (6, 4, 6),
    (7, 2, 7),
    (8, 1, 8),
    (9, 2, 9),
    (10, 3, 10),
    (11, 1, 11),
    (12, 2, 12),
    (13, 3, 13),
    (14, 2, 14),
    (15, 3, 15),
    (16, 4, 8),
    (17, 2, 8);

SET FOREIGN_KEY_CHECKS = 1;
COMMIT;