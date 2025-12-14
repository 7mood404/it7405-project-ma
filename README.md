# it7405-project-ma

# QuickBite

## Project Description and Technologies

QuickBite is a restaurant website that allows users to browse the menu, add items to a cart, place orders, book table reservations, and write customer reviews. The project demonstrates a complete web application with authentication, multiple core functionalities, and admin management.

**Technologies used:**
- **Backend language:** Python  
- **Framework:** Django  
- **Database:** MongoDB  
  - Connection string: `mongodb://localhost:27017`
- **Frontend:** HTML, CSS, Bootstrap, JavaScript  

---

## Project Environment and Demo Data

This project runs using a **pre-configured Anaconda environment** and includes **demo database data**.  
By importing the provided Conda environment and loading the fixture file, the project can be run on another device without manual dependency installation or data recreation.

---

## Requirements

Before starting, make sure you have:
- Anaconda Navigator installed
- Git installed (optional, for cloning)
- A modern web browser (Chrome, Edge, Firefox)
- MongoDB running locally on `localhost:27017`

---

## Setup Instructions

### 1. Get the Project

You can obtain the project in one of two ways:

**Option A: Download as ZIP**
- Download the repository as a ZIP file from GitHub
- Extract it to a local folder

**Option B: Clone from GitHub**
```bash
git clone <REPO_URL>
````

After downloading or cloning, open the project root folder.

**Project root folder contains:**

* `manage.py`
* `AnacondaEnv.yaml`
* `db_backup.json`
* `README.md`
* Django project folder: `it7405_project_ma`
* Django app folders:

  * `accounts`
  * `frontend`
  * `menu`
  * `orders`
  * `reservations`
  * `reviews`

---

### 2. Import the Conda Environment

1. Open **Anaconda Navigator**
2. Go to **Environments**
3. Click **Import**
4. Select the file: `AnacondaEnv.yaml`
5. Choose a name for the environment (for example: `quickbite-env`)
6. Click **Import**

This environment includes:

* Python
* Django
* MongoDB drivers
* All required dependencies to run the project

---

### 3. Open the Project in VS Code Inside Anaconda

1. In **Anaconda Navigator**, activate the imported environment
2. Click **Launch VS Code**
3. In VS Code, open the project root folder
4. Open the integrated terminal
5. Navigate to the project root (where `manage.py` is located)
6. Run:

```bash
dir
```

**Expected output (example):**

```
accounts
frontend
it7405_project_ma
menu
orders
reservations
reviews
AnacondaEnv.yaml
db_backup.json
manage.py
README.md
```

---

### 4. (Optional but Recommended) Drop Existing Database

This step ensures there are no conflicts with old or incorrect data.

1. Open the MongoDB shell
2. Run:

```bash
use restaurant_db
db.dropDatabase()
exit
```

This clears the database so demo data can be loaded cleanly.

---

### 5. Apply Migrations

This step creates the database structure.

Run:

```bash
python manage.py migrate
```

Django will create all required collections and tables.

---

### 6. Load Demo Data

Load the provided fixture file to restore all demo data.

Run:

```bash
python manage.py loaddata db_backup.json --exclude contenttypes
```

**Expected result:**
A success message indicating that objects were loaded.

---

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Open the following URLs in your browser:

* **Home page:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Menu page:** [http://127.0.0.1:8000/menu/](http://127.0.0.1:8000/menu/)
* **Admin panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

If demo data was loaded correctly, menu items, orders, reservations, and reviews will be visible.

---

## Sign Up Note

* The first signup attempt may fail due to Django validation rules
* Passwords must follow Django’s security requirements (minimum length, complexity)

---

## Admin Login (SuperUser)

Use the following credentials for testing:

* **Username:** admin
* **Password:** 10dmin999

After logging in:

* You can log out at any time using the Logout button
* If changes do not appear immediately, perform a hard refresh in the browser

---

## What You Can Do in Admin

From the Django admin panel, the administrator can:

* Add, edit, and delete menu items
* View and update order statuses (Pending, Successful, Failed)
* Approve or reject table reservations
* View and manage user reviews
* Manage user accounts

All changes made in the admin panel are immediately reflected on the website.

---

```
```
