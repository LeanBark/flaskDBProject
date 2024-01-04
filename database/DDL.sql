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
    food_categoryID,
    restaurantID
)

VALUES 
    -- ("Dynamo-Twister", 600, (SELECT food_categoryID FROM FoodCategories WHERE name="American"),
    -- (SELECT restaurantID FROM Restaurants WHERE restaurantID = 1)),

    ("melgalllll Sandwich", 319, (SELECT food_categoryID FROM FoodCategories WHERE name="Sandwiches"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 1)),

    ("Caesar Dressing", 120, (SELECT food_categoryID FROM FoodCategories WHERE name="Italian"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 2)),

    ("Trick OREO Treat Ice Cream", 300, (SELECT food_categoryID FROM FoodCategories WHERE name="American"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 3)),

    ("Sweet Fries Snack", 1150, (SELECT food_categoryID FROM FoodCategories WHERE name="Hamburger"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 4)),

    ("Egg-on Steak", 860, (SELECT food_categoryID FROM FoodCategories WHERE name="Barbeque"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 5)),

    ("Spinach Salad", 360, (SELECT food_categoryID FROM FoodCategories WHERE name="Steak"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 6)),

    ("Shrimp Ramen", 250, (SELECT food_categoryID FROM FoodCategories WHERE name="Japanese"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 7)),

    ("Passion Fruit Tart", 400, (SELECT food_categoryID FROM FoodCategories WHERE name="Indian"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 8)),

    ("Hand battered Fish Dinner", 750, (SELECT food_categoryID FROM FoodCategories WHERE name="Thai"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 9)),

    ("Salmon Sashimi", 300, (SELECT food_categoryID FROM FoodCategories WHERE name="Sushi"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 10)),

    ("Shirmp Salad", 500, (SELECT food_categoryID FROM FoodCategories WHERE name="Seafood"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 11)),

    ("Chili Burrito", 450, (SELECT food_categoryID FROM FoodCategories WHERE name="Mexican"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 12)),

    ("Supreme Veggie Pizza", 900, (SELECT food_categoryID FROM FoodCategories WHERE name="Pizza"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 13)),

    ("Wanton Soup", 650, (SELECT food_categoryID FROM FoodCategories WHERE name="Chinese"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 14)),

    ("Clam Chowder Soup", 600, (SELECT food_categoryID FROM FoodCategories WHERE name="French"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 15)),

    ("Mediterranean Ratatouille", 246, (SELECT food_categoryID FROM FoodCategories WHERE name="Italian"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 8)),

    ("Swordfish Soba Noodle", 420, (SELECT food_categoryID FROM FoodCategories WHERE name="Seafood"),
    (SELECT restaurantID FROM Restaurants WHERE restaurantID = 8));


-------------------------POPULATING RESTAURANTSALESINVOICES TABLE----------------------
INSERT INTO RestaurantSalesInvoices (
    menu_itemID,
    restaurantID
)

VALUES 
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10),
    (11, 11),
    (12, 12),
    (13, 13),
    (14, 14),
    (15, 15),
    (16, 8),
    (17,8);

SET FOREIGN_KEY_CHECKS = 1;
COMMIT;