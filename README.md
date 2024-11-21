# Python CLI Quiz App

## Version-1: In-Memory Data Storage

This is a CLI-based Python quiz application that allows users to register, log in, take quizzes in three subjects (DSA, DBMS, OS), and view their results. User data and scores are stored in program memory during runtime, and all data is reset when the program exits.

### Usage Instructions
#### 1.Starting the Application:
Run the script using Python:

```programMemoryApp.py```

### 2.Registering a User:
Select the Register option and enter a unique username and password.Once registered, log in to access the quizzes.

```
1. Register
2. Login
3. Exit
Enter your choice: 1

Enter a username: ram 
Enter a password: raman  
Registration successful! Please login.
```

### 3.Logging In:
Choose the Login option. Enter your registered username and password. Successful login grants access to the main menu.

```
Enter your username: ram
Enter your password: raman

Login successful!
```

### 4.Taking a Quiz:
From the main menu, select the Take Quiz option. The score is displayed at the end of the quiz and saved in the results.

```
Available Subjects: DSA, DBMS, OS
Choose a subject: DSA

Starting DSA Quiz:

Question 1: What is the time complexity of binary search?
1. O(n)
2. O(log n)
3. O(n^2)
4. O(1)
Your answer (1-4): 2

Question 2: Which data structure uses LIFO?
1. Queue
2. Stack
3. Linked List
4. Array
Your answer (1-4): 2
....
```

### 5.Viewing Results:

From the main menu, select View Results.

```
Your Results:
DSA: 5/5
```

### 6.Logging Out or Exiting:
Select Logout to return to the login screen or Exit to close the application.

```
1. Take Quiz
2. View Results
3. Logout
4. Exit
Enter your choice: 4
Goodbye!
```

## Version-2: Python CLI Quiz App with File Storage

This CLI-based Python quiz app allows users to register, log in, take quizzes in three subjects (DSA, DBMS, OS), and view their results. All data, including user credentials, quiz questions, and results, is stored in separate .txt files, enabling persistence across multiple sessions.

### Usage Instructions

#### 1.Running the Application
Save the Python script to a file. Ensure the required .txt files (registration.txt, results.txt, quiz.txt,etc) are in the same directory.
Run the program using:
```
py cli.py
```

#### 2. Register
Users must register before accessing the quizzes. Registration details are stored in registration.txt.
```
Welcome to Quiz App
1. Register
2. Login
3. Attempt Quiz
4. View Results
5. Exit

Enter your choice: 1
Enter your name: ram  
Enter your branch: cse
Enter your year: 4
Create username: ram
Create password: rman
Registration Finshed!
Welcome to Quiz App
```

#### 4. Login
Existing users can log in with their credentials.
```
Enter your choice: 2
Enter username: ram
Enter password: rman
Login Successfull!
```

#### 5. Take Quiz
Users can take a quiz in a subject of their choice. Questions are loaded from the quiz.txt file.

```
Logged in as shi
1. Attempt Quiz
2. View Results
3. Logout

Enter your choice: 1
1. DSA
2. DBMS
3. OS
Enter your choice: 1

Q: What is the time complexity of binary search in a sorted array?
1. O(n)
2. O(log n)
3. O(n log n)
4. O(1)
Choose the correct answer (1-4): 2

```

#### 6. View Results
User scores are retrieved from results.txt.

```
DBMS: 3 points
DSA: 3 points
```

#### 7. Logout/Exit
Users can log out to switch accounts or exit the app.
```
Exiting app.
```
### Features
1. User Registration and Login
2. Quiz Management
3. Results Tracking

## Requirements
The application is written in Python and requires **Python 3.x** to run.
