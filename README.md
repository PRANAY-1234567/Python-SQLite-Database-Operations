# Python SQLite Database Operations

## 📌 Project Overview

This project demonstrates basic database operations using Python's built-in `sqlite3` module. It creates a SQLite database, creates a table, inserts sample records, retrieves specific data using an SQL query, and displays the results.

## 🛠️ Technologies Used

* **Python** – Programming language
* **SQLite** – Lightweight database
* **sqlite3** – Python module for interacting with SQLite databases

## ✨ Features

* Connects to a SQLite database named `database.db`.
* Creates a table named `python` if it does not already exist.
* Deletes existing records from the table before inserting new data.
* Inserts sample records containing names, ages, and addresses.
* Retrieves a specific record using the SQL `WHERE` clause.
* Displays the retrieved record in the terminal.

## 📂 Database Structure

The project creates a table named `python` with the following columns:

| Column Name | Data Type   | Description                 |
| ----------- | ----------- | --------------------------- |
| `name`      | VARCHAR(20) | Stores the person's name    |
| `age`       | INTEGER     | Stores the person's age     |
| `address`   | VARCHAR(20) | Stores the person's address |

## 📋 Sample Data

The following records are inserted into the database:

| Name    | Age | Address |
| ------- | --: | ------- |
| Pranay  |  22 | Pune    |
| Jignesh |  24 | Nagar   |
| Raghu   |  25 | Mumbai  |

## ⚙️ How It Works

1. **Import SQLite:** Imports Python's built-in `sqlite3` module.
2. **Connect to the database:** Creates or opens `database.db`.
3. **Create a table:** Creates the `python` table if it does not already exist.
4. **Delete existing records:** Removes all existing records from the table.
5. **Insert records:** Adds three sample records to the table.
6. **Commit changes:** Saves the database changes.
7. **Retrieve data:** Executes a `SELECT` query to find the record where the name is `Pranay`.
8. **Display results:** Fetches and prints the matching record.
9. **Close the connection:** Closes the database connection.

## ▶️ How to Run the Project

### Prerequisites

* Python 3 installed on your system.
* No additional packages are required because `sqlite3` is included with standard Python installations.

### Steps

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Navigate to the project directory**

```bash
cd <your-project-folder>
```

**3. Run the Python script**

```bash
python main.py
```

Replace `main.py` with your actual Python filename if it is different.

## 💻 Expected Output

```text
('Pranay', 22, 'Pune')
```

## 📚 Concepts Covered

* Python database connectivity
* SQLite database creation
* SQL `CREATE TABLE` statement
* SQL `INSERT INTO` statement
* SQL `DELETE` statement
* SQL `SELECT` statement
* SQL `WHERE` clause
* Cursor execution and fetching results
* Database transactions and connection management

## 🎯 Learning Objective

The objective of this project is to understand how Python interacts with an SQLite database and how to perform basic CRUD-related database operations using SQL queries.

**Note:** This script demonstrates creating, inserting, deleting, and reading records. It does not demonstrate updating existing records.

## 👨‍💻 Author

**Pranay Vishwanath Jadhao**

<img width="1236" height="851" alt="image" src="https://github.com/user-attachments/assets/302cbda8-44cc-43ad-8dd5-7d31a90eaaf3" />

<img width="1307" height="878" alt="image" src="https://github.com/user-attachments/assets/458fc794-87c5-4b28-a1b7-0f39572b2824" />
