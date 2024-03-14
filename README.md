# flaskDBProject

# Description
The goal of this project was to implement a local mariaDB relational database using the Flask/Python framework that utilizes a website-based UI to allow for the management of restaurant-specific information through the application of CRUD operations.  

The locally-implemented mariaDB database stores information in terms of:
- Restaurant-specific information
- Each restaurant's menu item information (for all items listed in their respective menus)
- Sales invoices for each restaurant in terms of each item from their menu that was sold

This implementation was designed for use as a back-end UI that allows for database access/maintenance. This can be utilized as a working template for users who are relatively new to how the Flask framework can be utilized to pass SQL queries and retrieve/modify/display database records stored in a relational database, such as a mariaDB server. Additional features provided allow the user to:
 - Supplement the database with additional records by executing the "data_collection.py" file
 - Generate a CSV file of any specific restaurant's menu information or existing invoices that can be stored locally or within the cloned directory

# Environment Setup

The configuration files are omitted from the repository files as they are specific to VSCode's launch configuration. Instructions to ensure the git clone operates within a venv file can be found here: https://flask.palletsprojects.com/en/3.0.x/installation/

After creating a local virtual environment:
 - create a git clone within this environment
 - "app.py" is the executable file for initialization of Flask server(if not using CLI commands, ensure default run configuration is set to "app.py")

The following additional modules are required to be locally installed in order to fully utilize all files:
 - ```pandas``` - https://pandas.pydata.org/docs/getting_started/index.html
 - ```flask```  - https://flask.palletsprojects.com/en/2.3.x/
 - ```MySQLdb``` - https://mysqlclient.readthedocs.io/user_guide.html

BootStrap and jQuery are accessed through CDN deliverables placed directly within the jinja templates

# Locally Accessing the App using a Local Machine as Hosting Server

Download the MariaDB server from https://mariadb.org/download/ to local machine
 - NOTE: During installation process, make sure to set and record password to access local MariaDB and its location


In MariaDB folder:
 - Open Command Prompt
 - ```mariadb -u your_username -p``` then enter your password when prompted
 - ```CREATE DATABASE new_database_name;``` to create a new database
 - ```USE new_database_name;``` to select the new database

 - Determine the file path between the .ini file in "data" folder and your git clone's "DDL.sql" file on your local machine

 - ```source 'your_local_file_path';``` to fill the new database with the DDL's tables and data

This project was designed for locally hosting the database and UI instead of hosting on a remote server. Connection to either type of server will require adding a .env file that defines the user-specific values for authorized access to the database:

Example for .env format:

````
"database_nameHOST" = your_hostname
"database_nameUSER" = your_username
"database_namePW" = your_database_password
"database_name" = database_name
````

Ensure the .env definition names match those requested within the db_connector.py

In IDE terminal:
- Change to "flaskDBProject" directory:
```cd ./flaskDBProject"```
- Execute "app.py" to start Flask server
- You should now be able to access a locally-hosted version of the app at the address "http://localhost:PORT"
- PORT value should be defined in app.py


# Remotely Accessing the App using a Remote Host Server
While the local database can still be implemented following the instructions above, the hostname value in the .env file will need to be altered to reflect the remote server you wish to access.

This may also affect the website address that will display the UI
 - This most likely will be "http://'hostserver_IP_Address':PORT/" 


# Populating Database with Additional Sample Data
The repository files include the "sample_data.json" and "data_collection.py" files, which can be utilized for populating the database with addtional menu items to allow for increased flexibility in testing and modifying database values.

To populate the database with the additional information, execute the "data_collection.py" file which will organize and populate the database with the information stored in the "sample_data.json" file


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
