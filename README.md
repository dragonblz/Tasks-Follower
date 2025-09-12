# 📝 Tasks Follower

A simple, interactive command-line To-Do manager built with Python and SQLite.  
Easily add, view, update, and delete your tasks—right from your terminal!

---

## Features

- **Add Tasks:** Add one or multiple tasks at once.
- **View Tasks:** See all your tasks in a clean, paginated format.
- **Update Tasks:** Change the status of any task (pending, completed, progress, overdue).
- **Delete Tasks:** Remove tasks by their ID.
- **Persistent Storage:** All tasks are saved in a local SQLite database (`tasks.db`).
- **Interactive CLI:** User-friendly prompts for all actions.

---

## Getting Started

### Prerequisites

- Python 3.x (comes with `sqlite3` module)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/dragonblz/Tasks-Follower.git
    cd Tasks-Follower
    ```

2. **Run the script:**
    ```bash
    python Tasks.py
    ```

---

## Usage

When you run the script, your current tasks will be displayed.  
You can then choose to add, view, update, or delete tasks interactively.

### Example Workflow

```
Your current tasks:
All tasks:
ID: 1
Title: Buy groceries
Status: pending
Due date: None
--------------------
ID: 2
Title: Finish homework
Status: completed
Due date: 2025-09-12
--------------------
What action do u want to perform? (add/view/delete/update): add
How many tasks do you want to add? 2
Enter task title: Call Alice
Task added!
Enter task title: Read a book
Task added!
```

---

## Task Status Options

- `pending`
- `completed`
- `progress`
- `overdue`

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE)

---

## Author

[dragonblz](https://github.com/dragonblz)
