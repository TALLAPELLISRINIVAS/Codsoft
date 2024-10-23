def display_todos(todos):
    print("\nTo-Do List:")
    for index, task in enumerate(todos, start=1):
        print(f"{index}. {task}")
    print("\n")

def main():
    todos = []

    while True:
        print("Select an option:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            todos.append(task)
            print(f'Task "{task}" added.')

        elif choice == '2':
            display_todos(todos)

        elif choice == '3':
            display_todos(todos)
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(todos):
                    removed_task = todos.pop(task_num - 1)
                    print(f'Task "{removed_task}" deleted.')
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
