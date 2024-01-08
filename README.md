# flaskDBProject

# Description
The goal of this project was to implement a local mariaDB relational database using the Flask/Python framework that utilizes a website-based UI to allow for the management of restaurant-specific information through the application of CRUD operations.

The locally-implemented mariaDB database stores information in terms of:
- Restaurant-specific information
- Each restaurant's menu item information (for all items listed in their respective menus)
- Sales invoices for each restaurant in terms of the item from their menu that was sold

This implementation was designed for use as an accessible back-end user interface for database access/maintenance. This allows views table to be made for basic cost and sales analysis. Future plans to include date values to invoice records.

# Environment Setup

The configuration files are omitted from the repository files as they are specific to VSCode's launch configuration. Instructions to ensure the git clone operates within a venv file can be found here: https://flask.palletsprojects.com/en/3.0.x/installation/

After creating a local virtual environment:
 - create a git clone within this environment
 - establish editor launch configuration to ensure "app.py" is executed by default


# Locally Accessing the app using a local machine as hosting server

Download the MariaDB server from https://mariadb.org/download/ to local machine
 - NOTE: During installation process, make sure to set and record password to access local MariaDB and its location


In MariaDB folder:
 - Open Command Prompt
 - Enter "mariadb -u your_username -p" then enter your password when prompted
 - Enter "CREATE DATABASE new_database_name;" to create a new database
 - Enter "USE new_database_name;" to select the new database
 - Determine the file path between the .ini file in "data" folder and your git clone's "DDL.sql" file on your local machine
 - Enter "source 'your_local_file_path';" to fill the new database with the DDL's tables and data

This project was designed for locally hosting the database and UI instead of hosting on a remote server. Connection to either type of server will require adding a .env file that defines the user-specific values for authorized access to the database:

Example for .env format:
 - "database_nameHOST" = your_hostname
 - "database_nameUSER" = your_username
 - "database_namePW" = your_database_password
 - "database_name" = database_name

Ensure the .env definition names match those requested within the db_connector.py

In IDE terminal:
- Change to "flaskDBProject" directory (Usually "cd ./flaskDBProject" in CLI)
- Execute "app.py" to start Flask server
- You should now be able to access a locally-hosted version of the app at the address "http://localhost:PORT"
- PORT value should be defined in app.py


# Remotely Accessing the App using a Remote Host Server
While the a local database can still be implemented following the instructions above, the hostname value in the .env file will need to be altered to reflect the remote server you wish to access.

This may also affect the website address that will display the UI
 - This most likely will be "http://{hostserver's IP address}:{PORT value defined in app.py}/" 


# Populating Database with Additional Sample Data
The repository files include the "sample_data.json" and "data_collection.py" files, which can be utilized for populating the database with addtional menu items to allow for increased flexibility in testing and modifying database values.

To populate the database with the additional information, execute the "data_collection.py" file which will organize and populate the database with the information stored in the "add_menus.json" file

# Citations

Citation for the UI templating design, app.py routing structure, and MariaDB database connection procedures:
- Date: 12/20/2023
- Adapted form the OSU CS340 Flask Starter App
- Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app/tree/master?tab=readme-ov-file

Citation for Icons:
- Date: 1/3/2024
- Icons for Submit, Delete, and Edit buttons were provided from svgrepo.com
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