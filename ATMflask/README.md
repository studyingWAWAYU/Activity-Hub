Activity Hub
====

### Table of Contents
* Background
* Introduction
* Directory
* Install
* Usage
* Maintainers
* Contributing
* License


### Background
This project is an assignment for five university students in China.


### Introduction
Activity Hub is a comprehensive platform designed to manage campus club activities efficiently. 
It offers robust user management features, including user registration and login, role-based access for different user types, and personal profile management. 
The platform enables club managers to create and edit club information, complete with dedicated pages showcasing activities, member lists, and announcements. 
Activity Hub also streamlines event management, allowing managers to create, edit, or cancel events while providing users with a chronological list of upcoming activities and a personalized section to track their participation. 
Additionally, the system supports online registration for events and includes participant management features for club leaders, along with a digital check-in process for efficient attendance tracking. 
Overall, Activity Hub fosters engagement and collaboration within campus clubs, making it easier for users to connect and participate in various activities.

### Directory
In the project main folder, there are three subfolders:
1. The "static" folder stores static files.
2. The "templates" folder stores all the .html files.
3. The "views" folder stores all the .py files. (Each .py file corresponds to a .html file.)

### Install
1. Install Dependencies  
Flask==2.3.2  
Flask-Migrate==4.0.4  
Flask-SQLAlchemy==3.0.3

2. Database
Create a local MySQL database first.  
In the "sql.py" file and "setting.py" file, there are related settings for connecting to the database. You can modify them according to your own local database name and account password.  
Before using the system, you need to run the code for creating tables and writing initial data in "sql.py" (currently commented out). You need to delete the triple quotes and run it once, and then comment it out again.  
The login module in the system does not have the registration function.  
Users can only log in with existing data in the database. You can modify the content of creating tables in "sql.py" to add users.  

3. Run the Main File
Start the MySQL service and run the "manager.py" file to get the website URL

4. Open the Website to Use
Click the URL to enter and use the system. 
If you have installed successfully, you will see a login page.


### Usage
You can check out the small project we have created using Flask framework, and we are open to any advice you have.


### Maintainers
@studyingWAWAYU  
@ZIE  
@mm-ss-dd  


### Contributing
Feel free to dive in Open an issue or submit PRs.  
Activity Hub follows the Contributor Covenant Code of Conduct.


### License
MIT License