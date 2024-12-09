class Task:
    def __init__(self, priority, deadline, goal):
        self.priority = priority
        self.deadline = deadline
        self.goal = goal

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the list."""
        self.tasks.append(task)

    def view_tasks(self):
        """Return a simple list of task goals."""
        result = []
        for task in self.tasks:
            result.append(task.goal)
        return result

    def view_sorted_by_deadline(self):
        """Return tasks sorted by deadline using bubble sort."""
        n = len(self.tasks)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.tasks[j].deadline > self.tasks[j + 1].deadline:
                    self.tasks[j], self.tasks[j + 1] = self.tasks[j + 1], self.tasks[j]

        # Return the sorted list
        sorted_tasks = []
        for task in self.tasks:
            sorted_tasks.append(task)
        return sorted_tasks

    def save_to_file(self, filename="tasks.txt"):
        """Save tasks to a text file."""
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.goal},{task.priority},{task.deadline}\n")

    def load_from_file(self, filename="tasks.txt"):
        """Load tasks from a text file."""
        self.tasks.clear()  # Clear existing tasks before loading new ones
        # Open the file directly without error handling
        with open(filename, "r") as file:
            for line in file:
                goal, priority, deadline = line.strip().split(",")
                self.tasks.append(Task(priority, int(deadline), goal))


# Main Program
task_list = TaskList()

# Load tasks from the file (will raise an error if the file doesn't exist)
task_list.load_from_file()

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. View tasks by deadlines")
    print("4. Save and close")

    function = input("Choose function(1, 2, 3, 4): ")

    if function == "1":
        goal = input("Enter goal: ")
        priority = input("Enter priority (High, Low, Medium): ")
        deadline = int(input("Enter deadline (YYYYMMDD): "))
        task_list.add_task(Task(priority, deadline, goal))
        print("Task were added")
    elif function == "2":
        print("Tasks:")
        tasks = task_list.view_tasks()
        for task in tasks:
            print(task)
    elif function == "3":
        print("Tasks were sorted by deadlines:")
        sorted_tasks = task_list.view_sorted_by_deadline()
        for task in sorted_tasks:
            print(f"{task.goal} (Priority: {task.priority}, Deadline: {task.deadline})")
    elif function == "4":
        task_list.save_to_file()
        print("Tasks were saved")
        break
    else:
        print("Error")

