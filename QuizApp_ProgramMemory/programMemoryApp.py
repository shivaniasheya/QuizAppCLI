# In-memory storage for users and their scores
users = {}
quizzes = {
    "DSA": [
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n^2)", "O(1)"], "answer": 1},
        {"question": "Which data structure uses LIFO?", "options": ["Queue", "Stack", "Linked List", "Array"], "answer": 1},
        {"question": "What is a balanced binary tree?", "options": ["Tree with equal height", "Complete binary tree", "Tree with minimal height difference", "None"], "answer": 2},
        {"question": "What does BFS stand for?", "options": ["Binary First Search", "Breadth First Search", "Backward Forward Search", "Breadth Forward Sort"], "answer": 1},
        {"question": "Which sorting algorithm is the fastest on average?", "options": ["Bubble Sort", "Quick Sort", "Selection Sort", "Insertion Sort"], "answer": 1}
    ],
    "DBMS": [
        {"question": "What does SQL stand for?", "options": ["Structured Query Language", "Standard Query Language", "Sequential Query Language", "Simple Query Language"], "answer": 0},
        {"question": "Which of the following is a primary key?", "options": ["Unique value", "Duplicate value", "Null value", "None of the above"], "answer": 0},
        {"question": "What is a foreign key?", "options": ["Primary key in another table", "Unique identifier", "Attribute for indexing", "None"], "answer": 0},
        {"question": "What does ACID stand for?", "options": ["Atomicity, Consistency, Isolation, Durability", "Accuracy, Confidence, Integrity, Durability", "Atomicity, Control, Integrity, Duration", "None"], "answer": 0},
        {"question": "Which command is used to retrieve data?", "options": ["SELECT", "UPDATE", "DELETE", "INSERT"], "answer": 0}
    ],
    "OS": [
        {"question": "Which is not an OS?", "options": ["Linux", "Windows", "Oracle", "MacOS"], "answer": 2},
        {"question": "What is the primary purpose of an OS?", "options": ["Manage resources", "Perform tasks", "Control hardware", "All of the above"], "answer": 3},
        {"question": "Which is a process state?", "options": ["Running", "Paused", "Sleeping", "All of the above"], "answer": 3},
        {"question": "Which OS is open-source?", "options": ["Windows", "Linux", "MacOS", "All"], "answer": 1},
        {"question": "Which is a real-time OS?", "options": ["Linux", "FreeRTOS", "Windows", "MacOS"], "answer": 1}
    ]
}

# register function
def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try logging in.")
        return None
    password = input("Enter a password: ")
    users[username] = {"password": password, "scores": {}}
    print("Registration successful! Please login.")

#login function
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]["password"] == password:
        print("Login successful!")
        return username
    print("Invalid credentials. Please try again.")
    return None

#attempt quiz
def take_quiz(subject, username):
    score = 0
    print(f"\nStarting {subject} Quiz:")
    for idx, question in enumerate(quizzes[subject]):
        print(f"\nQuestion {idx + 1}: {question['question']}")
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        answer = int(input("Your answer (1-4): ")) - 1
        if answer == question["answer"]:
            score += 1
    users[username]["scores"][subject] = score
    print(f"\nYou scored {score}/{len(quizzes[subject])} in {subject}.")

def display_results(username):
    print("\nYour Results:")
    for subject, score in users[username]["scores"].items():
        print(f"{subject}: {score}/{len(quizzes[subject])}")
    print()

# Main application loop
def main():
    current_user = None
    while True:
        if current_user:
            print("\n1. Take Quiz\n2. View Results\n3. Logout\n4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                print("\nAvailable Subjects: DSA, DBMS, OS")
                subject = input("Choose a subject: ").strip().upper()
                if subject in quizzes:
                    take_quiz(subject, current_user)
                else:
                    print("Invalid subject!")
            elif choice == "2":
                display_results(current_user)
            elif choice == "3":
                current_user = None
                print("Logged out successfully.")
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        else:
            print("\n1. Register\n2. Login\n3. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                register()
            elif choice == "2":
                current_user = login()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
