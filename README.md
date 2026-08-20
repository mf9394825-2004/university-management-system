# 🎓 University Management System

A desktop-based **University Management System** built with **Python, Object-Oriented Programming (OOP), and Tkinter**.

The application provides a graphical interface for managing **students, doctors, and courses**, while demonstrating practical OOP concepts such as abstraction, inheritance, encapsulation, polymorphism, and object relationships.

## ✨ Key Features

* 👨‍🎓 Add and manage students
* 👨‍🏫 Add and manage doctors
* 📚 Add and manage courses
* 🔗 Assign doctors to courses
* 📝 Enroll students in courses
* 📋 Display stored records
* 🖥️ Interactive Tkinter GUI
* 🌙 Professional dark-themed interface
* 🧩 Modular OOP project structure

## 🧠 OOP Concepts Demonstrated

### Abstraction

The `Person` class is implemented as an abstract base class using `ABC` and `abstractmethod`.

### Inheritance

`Student` and `Doctor` inherit common functionality from the `Person` class.

### Encapsulation

Each class manages its own attributes and behaviors through constructors and methods.

### Polymorphism

The `display_info()` method is implemented differently in the `Student` and `Doctor` classes.

### Object Relationships

Students, doctors, and courses interact with each other through object references and collections.

## 🛠️ Technologies

| Technology | Usage                     |
| ---------- | ------------------------- |
| Python     | Core programming language |
| Tkinter    | Graphical User Interface  |
| OOP        | Application architecture  |
| Git        | Version control           |
| GitHub     | Project hosting           |

## 📁 Project Structure

```text
university-management-system/
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── student.py
│   ├── doctor.py
│   └── course.py
│
├── screenshots/
│   ├── main-dashboard.png
│   ├── add-student.png
│   ├── add-doctor.png
│   ├── add-course.png
│   └── all-records-added.png
│
├── .gitignore
├── README.md
├── class-diagram-for-university-management.webp
└── university_system.py
```

## 📊 Class Diagram

![Class Diagram](class-diagram-for-university-management.webp)

## 🖥️ Application Screenshots

### Main Dashboard

![Main Dashboard](screenshots/main-dashboard.png)

### Add Student

![Add Student](screenshots/add-student.png)

### Add Doctor

![Add Doctor](screenshots/add-doctor.png)

### Add Course

![Add Course](screenshots/add-course.png)

### All Records

![All Records](screenshots/all-records-added.png)

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/mf9394825-2004/university-management-system.git
```

### 2. Open the project directory

```bash
cd university-management-system
```

### 3. Run the application

```bash
python university_system.py
```

> Make sure Python 3.x is installed on your system.

## 🎯 Learning Outcomes

This project was developed to practice and demonstrate:

* Designing applications using OOP principles
* Creating reusable and modular Python classes
* Working with abstract classes and inheritance
* Managing relationships between multiple objects
* Building desktop interfaces with Tkinter
* Organizing a Python project into separate modules
* Using Git and GitHub for version control

## 🔮 Future Improvements

Possible future improvements include:

* 💾 Database integration
* 🔐 User authentication
* ✏️ Edit and delete operations
* 🔎 Search and filtering
* 📊 More advanced dashboards and statistics
* 🗄️ Persistent data storage

## 👨‍💻 Author

**Mohamed Fathy**

---

⭐ If you find this project useful, feel free to explore the code and class structure.
