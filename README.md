# To-Do-List-CLI-App

# 📝 To-Do List CLI App

A simple **command-line To-Do List app** built with Python.

## 🚀 Features
- Add tasks
- View all tasks
- Remove tasks
- Saves tasks in a text file (`tasks.txt`)

## 🛠️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/todo-app.git
   cd todo-app

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


pip install -r requirements.txt


python todo.py add "Buy groceries"
python todo.py list
python todo.py remove 1

$ python todo.py add "Finish Python project"
✅ Task added: Finish Python project

$ python todo.py list
📌 To-Do List:
1. Finish Python project

$ python todo.py remove 1
🗑️ Removed: Finish Python project
