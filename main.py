tasks = [
    {"task": "Buy groceries", "priority": "High", "due_date": "2024-06-20"},
    {"task": "Finish homework", "priority": "Medium", "due_date": "2024-06-18"},
    {"task": "Clean room", "priority": "Low", "due_date": "2024-06-16"}
]

def add_task(tasks,task_name, priority, due_date):
    task = {"task": task_name, "priority": priority, "due_date": due_date}
    tasks.append(task)

def delete_task(tasks, task_name):
    for task in tasks:
        if task['task'] == task_name:
            tasks.remove(task)

def view_tasks(tasks):
    for i in range(len(tasks)):
        task = tasks[i]
        print(f"{i + 1}. {task['task']} - Priority: {task['priority']}, Due Date: {task['due_date']}")

def main():
    print("Hello Python!")
    # assign tasks to an empty array
    # task_list = []

    # create a cli that interacts with user
    while True:
        print("To - Do List Menu")
        print("1. ADD TASK")
        print("2. DELETE TASK")
        print("3. VIEW TASKS")
        print("4. EXIT")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            priority = input("Enter priority (HIGH/MEDIUM/LOW): ")
            due_date = input("Enter due date (YYY-MM-DD): ")
            add_task(tasks, task_name, priority, due_date)

        elif choice == "2":
            task_name = input("Enter task name to delete: ")
            delete_task(tasks, task_name)

        elif choice == "3":
            view_tasks (tasks)

        elif choice == '4':
            print("Exiting program...")
            break

        else:
            print("Invalid. Please choose either from 1-4: ")
if __name__ == "__main__":
    main()   