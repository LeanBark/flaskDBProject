# flaskDBProject

# Description
The goal of this project was to implement a local mariaDB relational database using the Flask/Python framework that utilizes a website-based UI to allow for the management of restaurant-specific information through the application of CRUD operations.  

The locally-implemented mariaDB database stores information in terms of:
- Restaurant-specific information
- Each restaurant's menu item information (for all items listed in their respective menus)
- Sales invoices for each restaurant in terms of each item from their menu that was sold

This implementation was designed for use as a back-end UI that allows for database access/maintenance. This can be utilized as a working template for users who are relatively new to how the Flask framework can be utilized to pass SQL queries and retrieve/modify/display database records stored in a relational database, such as a mariaDB server. Additional features provided allow the user to:
 - Automatically install all required modules not provided in the Python standard library by executing the ```setup.py``` file
 - Supplement the database with additional records by executing the ```data_collection.py``` file
 - Generate a CSV file of any specific restaurant's menu information or existing invoices that can be stored locally or within the cloned directory

# Environment Setup

## 1. Creating a local virtual environment: ##

It is strongly advised to create a virtual environment within which to import the repository.

For Windows systems, enter the following commands:
````
py -m venv .venv
source .venv/Scripts/activate
```` 

For Linux/macOS systems, enter the following commands:
````
python3 -m venv .venv
source .venv/bin/activate
````

NOTE: If the set of commands listed do not work, instructions to ensure the clone operates within a venv file can be found here: https://flask.palletsprojects.com/en/3.0.x/installation/

## 2. Create a git clone within your activated virtual environment: ##
 
 ```git clone <copied https/ssh url>```


## 3. Establish a launch/run configuration for Flask application ##

The launch.json configuration files are located within the .vscode folder. While specific to VS Code, the information within in the launch.json file can be adapted to run within other editors. 
 - ```app.py``` is the executable file for initialization of Flask server (ensure FLASK_APP is configured to run "app.py")


## 4. Install dependencies within virtual environment ##
Ensure that python3 is installed for use in local environment

The following additional modules are required to initialize the flask application in its intended state:
 - ```pandas``` - https://pandas.pydata.org/docs/getting_started/index.html
 - ```flask-mysqldb```  - https://pypi.org/project/Flask-MySQLdb/
 - ```python-dotenv``` - https://pypi.org/project/python-dotenv/
 - ```click``` - https://pypi.org/project/python-dotenv/

To quickly install/update all required versions of the necessary modules, run ```setup.py```:

Windows:
````
cd ./flaskDBProject
py setup.py
````

macOS/Linux:
````
cd ./flaskDBProject
python3 setup.py
````


# Locally Accessing the App using a Local Machine as Hosting Server

NOTE: It is advised that the flask server instance is executed within a directory existing on your local machine and NOT from within a Codespace environment. The default socket connection settings for the locally-installed database may result in the local database being inaccessible to a flask server instance running within a Codespace environment.

## 1. Install and configure a local MariaDB server on your local machine ## 

Download the MariaDB server from https://mariadb.org/download/ to local machine
 - NOTE: During installation process, make sure to set and record password to access local MariaDB and its location


In MariaDB folder:
 - Open Command Prompt
 - ```mariadb -u your_username -p``` then enter your password when prompted
 - ```CREATE DATABASE new_database_name;``` to create a new database
 - ```USE new_database_name;``` to select the new database

 - Determine the file path between the .ini file in "data" folder and your git clone's "DDL.sql" file on your local machine

 - ```source 'your_local_file_path';``` to fill the new database with the DDL's tables and data

## 2. Create a .env file to store database access credentials ##

This project was designed for locally hosting the database and UI instead of hosting on a remote server. However, connection to either type of server will require adding a .env file that defines the user-specific values for authorized access to the database:

Example for .env file format:

````
"database_nameHOST" = your_hostname
"database_nameUSER" = your_username
"database_namePW" = your_database_password
"database_name" = database_name
````

Ensure the ```.env``` definition names match those requested within ```db_connector.py```

## 3. Start the Flask Application Server ##

Change to the flaskDBProject directory by entering:
```cd ./flaskDBProject```

Launch Flask instance using ```app.py``` to start Flask server (using the configuration settings enclosed in the launch.json file) 
- You should now be able to access a locally-hosted version of the app at the address "http://localhost:PORT"
- PORT value should be defined in app.py


# Remotely Accessing the App using a Remote Host Server
While the local database can still be implemented following the instructions above, the hostname value in the .env file will need to be altered to reflect the remote server you wish to access.

This may also affect the website address that will display the UI
 - This most likely will be "http://'hostserver_IP_Address':PORT/" 


# Populating Database with Additional Sample Data

The repository files also include: 
````
sample_data.json
data_collection.py
````

Executing the ```data_collection.py``` file will populate the local database with additional menu items stored within ```sample_data.json``` to allow for increased flexibility in testing/modification.


# Demonstration Video

Click the link below to view a demonstration video of the current version of the project

"https://cdnapisec.kaltura.com/p/391241/sp/39124100/embedIframeJs/uiconf_id/22119142/partner_id/391241?iframeembed=true&playerId=kaltura_player&entry_id=1_5q7ukdl4&flashvars[localizationCode]=en&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_ct58u147"

# Citations

Citation for the UI templating design, app.py routing structure, and MariaDB database connection procedures:
- Date: 12/20/2023
- Adapted from the OSU CS340 Flask Starter App
- Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app/tree/master?tab=readme-ov-file

Citation for Icons:
- Date: 1/3/2024
- Icons for Delete, and Edit buttons were provided from svgrepo.com
- Source URL for Edit Icons: https://www.svgrepo.com/svg/521620/edit
- Source Url for Delete Icons: https://www.svgrepo.com/svg/502614/delete

Citation for Bootstrap and its implementation based on the provided documentation:
- Date: 1/4/2024
- Bootstrap utility for layout design/styling obtained from https://getbootstrap.com
- Source URL: https://getbootstrap.com/docs/5.3/getting-started/introduction/

Citation for jQuery and CDN deliverables (implementation for datepicker):
- Date: 1/7/2024
- Jquery format and CDN deliverables obtained from https://api.jquery.com/
- Source URL: https://jquery.com/download/

Citation for Pandas Module Implementation and Documentation (used for generating CSV files from queries)
- Date: 1/20/2024
- Pandas documentation and implementation obtained from https://pandas.pydata.org/docs/user_guide/index.html
- Source URL: https://pandas.pydata.org/docs/user_guide/index.html

Citation for Flask Implementation:
- Date: 1/3/2024
- Flask documentation and implemetation obtained from https://flask.palletsprojects.com/en/2.3.x/
- Source URL: https://flask.palletsprojects.com/en/2.3.x/quickstart/
