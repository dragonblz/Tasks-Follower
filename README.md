# 📝 Tasks Follower

A simple, interactive command-line To-Do manager built with Python and SQLite.  
Easily add, view, update, and delete your tasks—right from your terminal!

---

## Features

- **Add Tasks:** Add one or multiple tasks at once, with optional due dates.
- **View Tasks:** See all your tasks in a clean, paginated format.
- **Update Tasks:** Change the status of any task (pending, completed, progress, overdue).
- **Delete Tasks:** Remove tasks by their ID.
- **Persistent Storage:** All tasks are saved in a local SQLite database (`tasks.db`).
- **Interactive CLI:** User-friendly prompts for all actions.

---

## Installation

### With pipx (Recommended)

1. **Clone the repository:**
    ```sh
    git clone https://github.com/dragonblz/Tasks-Follower.git
    cd Tasks-Follower
    ```

2. **Install with pipx:**
    ```sh
    pipx install .
    ```

3. **(Optional) If you see a PATH warning, run:**
    ```sh
    pipx ensurepath
    ```
    Then restart your terminal.

---

## Usage

After installation, run the tool from any terminal:

```sh
tasks-follower
```

You’ll see your current tasks and be prompted to add, view, update, or delete tasks interactively.

---

## Example Workflow

```
Your current tasks:
All tasks:
ID: 1
Title: Buy groceries
Status: pending
Due Date: 2025-09-15
--------------------
What action do u want to perform? (add/view/delete/update): add
How many tasks do you want to add? 2
Enter task title: Call Alice
Enter due date (YYYY-MM-DD) or leave blank: 2025-09-20
Task added!
Enter task title: Read a book
Enter due date (YYYY-MM-DD) or leave blank:
Task added!
```

---

## Task Status Options

- `pending`
- `completed`
- `progress`
- `overdue`

---

## Credits

- Project by [dragonblz](https://github.com/dragonblz)
- **README generated with the help of AI (GitHub Copilot)**

---

## License

[MIT](LICENSE)