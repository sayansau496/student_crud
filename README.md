# Student Management System
### Python + Flask + MySQL CRUD Project for Class 12 Students
**Sayan Sir's Tutorials (CoE Kolkata)**

---

## 1. What is this project?

A small web application that manages a list of students. From a web page (HTML) the user can:

| Operation | Meaning | SQL used | Flask function |
|-----------|---------|----------|----------------|
| **C**reate | Add a new student | `INSERT` | `add_student()` |
| **R**ead   | View / search students | `SELECT` | `index()` |
| **U**pdate | Edit a student | `UPDATE` | `edit_student()` |
| **D**elete | Remove a student | `DELETE` | `delete_student()` |

**How the pieces talk to each other**

```
Browser (HTML page)  <-->  Flask (app.py)  <-->  MySQL (school_db.students)
```

1. You click a button on the web page.
2. The browser sends a request to Flask.
3. Flask runs a SQL query on MySQL using `mysql-connector-python`.
4. Flask sends back an HTML page with the result.

---

## 2. Project structure

```
student_crud/
|-- app.py                 <- Flask code (all 4 CRUD operations)
|-- schema.sql             <- creates the database + table + sample data
|-- requirements.txt       <- Python packages to install
|-- README.md              <- this file
|-- templates/             <- HTML pages (Flask looks for this folder name)
|   |-- base.html          <- common layout (header, footer, messages)
|   |-- index.html         <- list of students + search  (READ)
|   `-- form.html          <- Add / Edit form  (CREATE + UPDATE)
`-- static/
    `-- style.css          <- colours, table and button design
```

> The folder names `templates` and `static` are fixed by Flask. Do not rename them.

---

## 3. Requirements

- Python 3.8 or newer
- MySQL Server (with MySQL Workbench or the command-line client)
- Any text editor (VS Code or PyCharm is fine)
- A web browser

---

## 4. Step-by-step setup

### Step 1: Install the software
1. Install **Python** from python.org. Tick **"Add Python to PATH"** during installation.
2. Install **MySQL Server**. Remember the **root password** you set.
3. Check both work. Open a terminal / command prompt:
   ```
   python --version
   mysql --version
   ```

### Step 2: Unzip the project
Unzip `student_crud.zip` to a folder, for example `D:\student_crud`. Open a terminal inside this folder.

### Step 3: Create a virtual environment (recommended)
A virtual environment keeps this project's packages separate from other projects.

Windows:
```
python -m venv venv
venv\Scripts\activate
```
Linux / macOS:
```
python3 -m venv venv
source venv/bin/activate
```
You will see `(venv)` at the start of the prompt.

### Step 4: Install the packages
```
pip install -r requirements.txt
```
This installs **Flask** (web framework) and **mysql-connector-python** (lets Python talk to MySQL).

### Step 5: Create the database and table
**Option A: MySQL Workbench**
1. Open MySQL Workbench and connect to your server.
2. Choose *File > Open SQL Script* and select `schema.sql`.
3. Click the lightning (Execute) button.

**Option B: Command line**
```
mysql -u root -p < schema.sql
```
Enter your root password when asked.

Check that it worked:
```sql
USE school_db;
SELECT * FROM students;
```
You should see 4 sample students.

> Run `schema.sql` only **once**. Running it again will give a "Duplicate entry" error for the sample rows, because roll numbers must be unique. That is harmless.

### Step 6: Put your MySQL password in app.py
Open `app.py` and find:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",   # <-- change this
    "database": "school_db",
}
```
Replace `your_password` with your real MySQL root password.

### Step 7: Run the application
```
python app.py
```
You will see a message like `Running on http://127.0.0.1:5000`.

### Step 8: Open it in the browser
Go to **http://127.0.0.1:5000**. You should see the student list.

To stop the server press **Ctrl + C** in the terminal.

---

## 5. How to use the web page

| What you want | What to do |
|---------------|-----------|
| See all students | Open the home page |
| Search | Type a name or roll number in the search box, click **Search** |
| Add a student | Click **+ Add Student**, fill the form, click **Save** |
| Edit a student | Click **Edit** in that row, change the values, click **Save** |
| Delete a student | Click **Delete**, then confirm in the pop-up |

---

## 6. Understanding the code

### 6.1 Database table (schema.sql)
```sql
CREATE TABLE students (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    roll_no INT NOT NULL UNIQUE,
    name    VARCHAR(50) NOT NULL,
    section CHAR(1) NOT NULL,
    stream  VARCHAR(20) NOT NULL,
    marks   INT NOT NULL
);
```
- `id` is the **primary key**. MySQL fills it automatically (`AUTO_INCREMENT`).
- `roll_no` is `UNIQUE`, so two students cannot share a roll number.
- `NOT NULL` means the field cannot be left empty.

### 6.2 Connecting Python to MySQL
```python
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root",
                               password="...", database="school_db")
cur = conn.cursor()
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
cur.close()
conn.close()
```
- **connection** = the link to the database.
- **cursor** = the object that runs SQL queries.
- `commit()` is needed after INSERT / UPDATE / DELETE to save the change permanently.

### 6.3 The four CRUD operations in app.py

**Create**
```python
cur.execute(
    "INSERT INTO students (roll_no, name, section, stream, marks) "
    "VALUES (%s, %s, %s, %s, %s)", data)
conn.commit()
```
**Read**
```python
cur.execute("SELECT * FROM students ORDER BY roll_no")
students = cur.fetchall()
```
**Update**
```python
cur.execute("UPDATE students SET roll_no=%s, name=%s, section=%s, "
            "stream=%s, marks=%s WHERE id=%s", data + (student_id,))
conn.commit()
```
**Delete**
```python
cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
conn.commit()
```

### 6.4 Why `%s` and not f-strings?
Never build SQL like `"... WHERE name = '" + name + "'"`. A user could type SQL code into the form and damage the database (this attack is called **SQL injection**). Using `%s` placeholders lets the connector treat the typed text only as data. Always use placeholders.

### 6.5 Flask routes
| URL | Methods | Purpose |
|-----|---------|---------|
| `/` | GET | show list / search |
| `/add` | GET, POST | GET shows the empty form, POST saves it |
| `/edit/<id>` | GET, POST | GET shows the filled form, POST updates it |
| `/delete/<id>` | POST | deletes the record |

- **GET** = "give me a page". **POST** = "here is form data, please save it".
- Delete uses POST so that a record cannot be deleted just by opening a link.

### 6.6 HTML templates (Jinja2)
Flask uses the **Jinja2** template language inside HTML:
- `{{ s.name }}` prints a value.
- `{% for s in students %} ... {% endfor %}` repeats a block (one table row per student).
- `{% extends "base.html" %}` reuses the common header and footer.
- `url_for('edit_student', student_id=s.id)` builds the correct link.

### 6.7 Validation
`read_form()` checks the data before it reaches the database: no empty fields, numbers only for roll number and marks, marks not above 100, section is one letter, and stream is from the list. Errors are shown on the page using `flash()`.

---

## 7. Common errors and fixes

| Error message | Reason | Fix |
|---------------|--------|-----|
| `Access denied for user 'root'` | Wrong password in `app.py` | Correct `DB_CONFIG["password"]` |
| `Unknown database 'school_db'` | `schema.sql` not run | Run Step 5 |
| `Can't connect to MySQL server` | MySQL service is not running | Start the MySQL service |
| `ModuleNotFoundError: No module named 'flask'` | Packages not installed, or venv not active | Activate venv, run `pip install -r requirements.txt` |
| `Table 'school_db.students' doesn't exist` | Table not created | Run `schema.sql` again |
| "This roll number already exists." | Duplicate roll number | Use a different roll number |
| `Address already in use` | Port 5000 busy | Change to `app.run(debug=True, port=5001)` |
| `Authentication plugin 'caching_sha2_password'...` | Old connector with new MySQL | `pip install --upgrade mysql-connector-python` |

---

## 8. Practice exercises (extensions)

1. Add a new column `phone` (change the table, the form and the table display).
2. Add a **Grade** column on the list page: 90+ = A, 75 to 89 = B, 60 to 74 = C, below 60 = D.
3. Show the **average marks** and the **topper's name** at the top of the list page (`AVG()` and `MAX()`).
4. Add a filter by **stream** using a drop-down.
5. Sort the list by marks (highest first) when a button is clicked.
6. Add a login page so that only a teacher can delete records.

---

## 9. Viva questions

1. What does CRUD stand for? Give the SQL command for each.
2. What is the use of `commit()`?
3. What is a primary key? Which column is the primary key here?
4. What is the difference between a connection and a cursor?
5. What is the difference between GET and POST?
6. What is SQL injection and how does `%s` prevent it?
7. Why are HTML files kept in the `templates` folder?
8. What is `debug=True` used for?
9. What does `fetchall()` return?
10. What is the use of `UNIQUE` on `roll_no`?

---

*Sayan Sir's Tutorials (CoE Kolkata)*
