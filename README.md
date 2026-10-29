# 🎓 Student Management System

### Python · Flask · MySQL · HTML · CSS

**Developed for:** Sayan Sir's Tutorials (CoE Kolkata)

A beginner-friendly, web-based **Student Management System** built using Python Flask and MySQL. This project demonstrates CRUD operations (Create, Read, Update, Delete), database connectivity, form validation, and dynamic HTML rendering using Jinja2 templates.

---

## 📌 Project Overview

The Student Management System allows users to manage student records through a simple web interface. Users can add new students, view and search existing records, update student information, and delete records.

### ✨ Key Features

- **Add Students:** Register students with roll number, name, section, stream, and marks.
- **View Students:** Display all student records in a structured table.
- **Search Students:** Search records by student name or roll number.
- **Edit Records:** Update existing student information.
- **Delete Records:** Remove student records with confirmation.
- **Form Validation:** Validate required fields, numeric inputs, marks, sections, and streams.
- **Duplicate Prevention:** Enforce unique roll numbers through MySQL constraints.
- **SQL Injection Protection:** Use parameterized SQL queries.
- **Responsive Interface:** Simple HTML and CSS interface for easy navigation.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Relational database |
| mysql-connector-python | Python–MySQL connectivity |
| HTML5 | Web page structure |
| CSS3 | Styling and layout |
| Jinja2 | Dynamic HTML templates |
| Git & GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
student_crud/
│
├── app.py                  # Flask application and CRUD routes
├── schema.sql              # Database, table and sample data
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── templates/
│   ├── base.html            # Common page layout
│   ├── index.html           # Student list and search
│   └── form.html            # Add and edit student forms
│
└── static/
    └── style.css            # Application styles
```

---

## ⚙️ Prerequisites

Before running the project, install the following:

- Python 3.8 or newer
- MySQL Server
- MySQL Workbench (optional, for database management)
- Git
- A code editor such as Visual Studio Code
- A modern web browser

Verify the installations:

```bash
python --version
git --version
mysql --version
```

*Note: The `mysql` command may not be available until the MySQL client is added to your system PATH.*

---

## 🚀 Installation and Setup

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username and `YOUR_REPOSITORY` with your repository name.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate to the project directory:

```bash
cd student_crud
```

### Step 2: Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The required packages are Flask and MySQL Connector/Python.

### Step 4: Configure the MySQL Database

Start your MySQL server and log in using MySQL Workbench or the MySQL command-line client.

Execute the SQL script provided in `schema.sql`.

**Using the command line:**

```bash
mysql -u root -p < schema.sql
```

Enter your MySQL password when prompted.

Verify the database and table:

```sql
USE school_db;
SHOW TABLES;
SELECT * FROM students;
```

The database should contain the `students` table and the sample records defined in `schema.sql`.

### Step 5: Configure Database Credentials

Configure the MySQL connection in `app.py` to match your local environment.

For example:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "school_db"
}
```

Replace the placeholder with your actual MySQL password.

**Security recommendation:** Do not commit real database passwords or other secrets to GitHub. For a public repository, use environment variables or a local `.env` file that is excluded from version control.

### Step 6: Run the Application

```bash
python app.py
```

Open your browser and visit:

**http://127.0.0.1:5000**

To stop the application, press `Ctrl + C` in the terminal.

---

## 🗄️ Database Design

**Database:** `school_db`

**Table:** `students`

| Column | Data Type | Description |
|---|---|---|
| `id` | INT | Auto-incremented primary key |
| `roll_no` | INT | Unique student roll number |
| `name` | VARCHAR(50) | Student name |
| `section` | CHAR(1) | Student section |
| `stream` | VARCHAR(20) | Academic stream |
| `marks` | INT | Student marks |

### Database Constraints

- `PRIMARY KEY`: Uniquely identifies each student record.
- `AUTO_INCREMENT`: Automatically generates the record ID.
- `UNIQUE`: Prevents duplicate roll numbers.
- `NOT NULL`: Ensures required fields contain values.

---

## 🔄 CRUD Operations

CRUD stands for **Create, Read, Update, and Delete**.

| Operation | SQL Command | Flask Function | Description |
|---|---|---|---|
| Create | `INSERT` | `add_student()` | Adds a new student |
| Read | `SELECT` | `index()` | Displays and searches records |
| Update | `UPDATE` | `edit_student()` | Modifies student information |
| Delete | `DELETE` | `delete_student()` | Removes a student record |

### Application Routes

| Route | HTTP Method | Purpose |
|---|---|---|
| `/` | GET | Display and search student records |
| `/add` | GET, POST | Display the add form and save a student |
| `/edit/<id>` | GET, POST | Display and update a student record |
| `/delete/<id>` | POST | Delete a student record |

---

## 🔐 Security and Validation

The project demonstrates several important development practices:

- **Parameterized SQL queries:** Use `%s` placeholders to separate SQL commands from user-supplied values.
- **Server-side validation:** Validate form inputs before inserting or updating records.
- **Database constraints:** Enforce unique roll numbers and required fields.
- **POST for deletion:** Prevent deletion through a simple GET request.
- **Development configuration:** Keep Flask debug mode disabled in production.
- **Credential protection:** Store passwords outside source code and exclude secret files from Git.

*Note: This project is intended for learning and local development. Authentication, CSRF protection, production deployment settings, and other safeguards should be added before using it with real student data.*

---

## 🧪 How to Use the Application

1. Open the home page to view the student list.
2. Click **Add Student** to register a new student.
3. Enter the required information and save the record.
4. Use the search field to find a student by name or roll number.
5. Click **Edit** to update an existing record.
6. Click **Delete** and confirm to remove a record.

---

## 🐛 Troubleshooting

| Error | Possible Cause | Solution |
|---|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Dependencies are missing | Activate the virtual environment and install `requirements.txt` |
| `Access denied for user 'root'` | Incorrect MySQL credentials | Verify the username and password |
| `Unknown database 'school_db'` | Database has not been created | Execute `schema.sql` |
| `Table 'school_db.students' doesn't exist` | Table was not created | Check and execute the database script |
| `Can't connect to MySQL server` | MySQL server is stopped or unreachable | Start MySQL and verify the connection settings |
| Duplicate roll number error | The roll number already exists | Enter a different roll number |
| `Address already in use` | Port 5000 is occupied | Stop the other process or configure another port |

---

## 📚 Learning Outcomes

By completing this project, students can learn:

- Python functions and exception handling.
- Flask routes and HTTP request methods.
- MySQL database and table creation.
- CRUD operations using SQL.
- Connecting a Python application to MySQL.
- HTML forms and CSS styling.
- Jinja2 template inheritance and loops.
- Input validation and SQL injection prevention.
- Git version control and GitHub repository management.

---

## 💡 Future Enhancements

The following features can be added as further practice:

- Student login and teacher authentication.
- Grade calculation based on marks.
- Stream-based filtering and sorting.
- Dashboard displaying average marks and the class topper.
- Pagination for large student lists.
- Export student records to CSV or Excel.
- Improved responsive design.
- Role-based access control and secure deployment.

---

## 🎤 Viva Questions

1. What is CRUD, and why is it used?
2. What is Flask?
3. What is the purpose of `mysql-connector-python`?
4. What is the difference between a primary key and a unique key?
5. Why is `commit()` required after an INSERT, UPDATE, or DELETE?
6. What is the difference between GET and POST?
7. What is SQL injection, and how do parameterized queries help prevent it?
8. What is the purpose of Flask's `templates` directory?
9. What does `fetchall()` return?
10. Why should database credentials not be uploaded to GitHub?

---

## 👨‍💻 Author

**sayansau496**

Educational project developed for learning Python Flask, MySQL database integration, and web application development.

---

## 📄 License

This project is intended for educational purposes. Add a `LICENSE` file to the repository if you want to specify formal reuse and distribution permissions.
