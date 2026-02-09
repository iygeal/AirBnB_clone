This repo contains the implementation of a clone of the AirBnB website.
# 🏠 AirBnB Clone — Backend (Console + File Storage)

## 📌 Project Overview
This project is the **first stage of the AirBnB Clone** built as part of the ALX / Holberton curriculum.
It focuses on building the backend logic and command interpreter that manages application data before adding web interfaces.

The project implements:
- Object models for AirBnB entities
- A command-line interpreter (console)
- JSON file storage engine
- Object creation, retrieval, update, and deletion (CRUD)

The goal is to simulate how a real backend application manages data and objects before building a full web application.

---

## ✨ Features

### 🧠 Object-Oriented Models
The project includes models representing core AirBnB entities such as:
- BaseModel (parent class)
- User
- State
- City
- Amenity
- Place
- Review

All models inherit shared attributes and behaviors from `BaseModel`.

---

### 💾 File Storage Engine
- Uses JSON serialization
- Saves objects to file
- Reloads objects automatically on startup

---

### 💻 Command Interpreter (Console)
The console allows you to:

- Create objects
- View objects
- Update objects
- Delete objects
- Count instances
- Persist data to storage

#### Supported Commands

| Command | Description |
|---|---|
| create | Creates new instance and saves it |
| show | Displays instance details |
| destroy | Deletes an instance |
| all | Displays all instances |
| update | Updates attributes |
| count | Counts instances |

---

## 🧱 Project Structure

```
AirBnB_clone/
│
├── console.py
├── models/
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   └── engine/
│       └── file_storage.py
│
├── tests/
├── README.md
└── AUTHORS
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/iygeal/AirBnB_clone.git
cd AirBnB_clone
```

---

### 2️⃣ Run Console (Interactive Mode)
```bash
./console.py
```

You will see:
```
(hbnb)
```

---

### 3️⃣ Run Console (Non-Interactive Mode)
```bash
echo "help" | ./console.py
```

---

## 🖥️ Console Usage Examples

### Create Object
```bash
(hbnb) create BaseModel
```

---

### Show Object
```bash
(hbnb) show BaseModel <id>
```

---

### Update Object
```bash
(hbnb) update BaseModel <id> name "New Name"
```

---

### Delete Object
```bash
(hbnb) destroy BaseModel <id>
```

---

### Show All Objects
```bash
(hbnb) all
```

---

## 🧪 Testing
If test files exist:
```bash
python3 -m unittest discover tests
```

---

## 🛠 Technologies Used
- Python 3
- Object-Oriented Programming (OOP)
- JSON Serialization
- Command Line Interface (cmd module)
- Unit Testing

---

## 🎯 Learning Objectives
This project demonstrates:
- Building command interpreters
- Data persistence with serialization
- OOP design patterns
- Modular project structure
- Backend architecture foundations

---

## 👨‍💻 Authors
**Iygeal Anozie** and **Charis Adu**

GitHub Repository:
https://github.com/iygeal/AirBnB_clone
