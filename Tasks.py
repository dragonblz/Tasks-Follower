import sqlite3
from datetime import datetime

con = sqlite3.connect('tasks.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, title TEXT, status TEXT, due_date INTEGER)')
con.commit()
res = cur.execute('SELECT * FROM tasks')


def add_task(description, due_date=None):
    cur.execute('INSERT INTO tasks(title, status, due_date) VALUES(?, ?, ?)', (description, 'pending', due_date))
    con.commit()

def add_multiple_tasks():
    count_input = input("How many tasks do you want to add? ")
    if not count_input.isdigit() or int(count_input) <= 0:
        print("Please enter a positive number.")
        return
    count = int(count_input)
    for i in range(count):
        description = input("Enter task title: ")
        due_date_input = input("Enter due date (YYYY-MM-DD) or leave blank: ")
        if due_date_input:
            try:
                due_date = int(datetime.strptime(due_date_input, "%Y-%m-%d").strftime("%Y%m%d"))
            except ValueError:
                print("Invalid date format. Saving without due date.")
                due_date = None
        else:
            due_date = None
        add_task(description, due_date)
        print("Task added!")

def get_all_tasks():
    cur.execute('SELECT * FROM tasks')
    return cur.fetchall()

def print_all_tasks_paginated(page_size=10):
    tasks = get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("All tasks:")
    for i, task in enumerate(tasks, 1):
        due_date_str = (
            datetime.strptime(str(task[3]), "%Y%m%d").strftime("%Y-%m-%d")
            if task[3] else "None"
        )
        print(f"ID: {task[0]}\nTitle: {task[1]}\nStatus: {task[2]}\nDue Date: {due_date_str}\n" + "-"*20)
        if i % page_size == 0 and i != len(tasks):
            input("Press Enter to see more tasks...")

def Delete_task(task_id):
    cur.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    con.commit()

def update_task_status(task_id, new_status):
    cur.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
    con.commit()



print("Your current tasks:")
print_all_tasks_paginated()

user = input("What action do u want to perform? (add/view/delete/update): ")

if user == "add":
    add_multiple_tasks()

elif user == "view":
    print_all_tasks_paginated()

elif user == "delete":
    task_id = int(input("Enter the ID of the task to delete: "))
    Delete_task(task_id)
    print("Task deleted!")

elif user == "update":
    task_id = int(input("enter the ID of the task to update: "))
    new_status = input("enter the new status (pending/completed/progress/overdue): ")
    update_task_status(task_id, new_status)
    print("Task updated!")


user1 = input("do u want to perform another action? (yes/no): ")

if user1.lower() == "yes":
    count = int(input("How many actions do you want to perform? "))
    for i in range(count):
        user = input("What action do u want to perform? (add/view/delete/update): ")
        if user == "add":
            add_multiple_tasks()
        elif user == "view":
            print_all_tasks_paginated()
        elif user == "delete":
            task_id = int(input("Enter the ID of the task to delete: "))
            Delete_task(task_id)
            print("Task deleted!")
        elif user == "update":
            task_id = int(input("enter the ID of the task to update: "))
            new_status = input("enter the new status (pending/completed/progress/overdue): ")
            update_task_status(task_id, new_status)
            print("Task updated!")
        else:
            print("Invalid action.")

con.close()