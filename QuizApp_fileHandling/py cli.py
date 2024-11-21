#user registeration 
def reg():
    name = input("Enter your name: ").strip()
    branch = input("Enter your branch: ").capitalize().strip()
    year = input("Enter your year: ").strip()

    username =  input("Create username: ").strip()
    with open("registration.txt", "a+") as regFile:
        if username in regFile:
            print("Username already exists. Enter another username.")
            username =  input("Create username: ").strip()
        else:
            password = input("Create password: ").strip()
            if(username == password):
                print("Password cannot be same as username. Create another password.")
                password =  input("Create password: ").strip()
            else:
                regFile.write(f'{name}, {year}, {branch}, {username}, {password}\n')
                with open("login.txt", "a") as loginFile:
                    loginFile.write(f'{username},{password}\n')
    print("Registration Finshed!")

#user login
def login():
    username = input("Enter username: ").strip()
    pwd = input("Enter password: ").strip()
    with open("login.txt", "r") as file:
        users = file.readlines()
    for log in users:
        userData = log.strip().replace('/n',' ').split(',')
        if userData[0] == username and userData[1] == pwd:
            print("Login Successfull!")
            return username
    else:
        print("Invalid credentials. Enter username and password again")
    
  
#code for attempting quiz
def quiz(username):
    subject = ['DSA', 'DBMS', 'OS']
    for s in range(len(subject)):
        print(f"{s + 1}. {subject[s]}")
    choice = int(input("Enter your choice: "))

    sub = subject[choice - 1]
    ques = []
    score = 0
    with open("quiz.txt","r") as file:
        quizData = file.readlines()
 
    for li in quizData:
        quizQuestions = li.strip().split(';')
        if quizQuestions[0] == sub:
            ques.append(quizQuestions)      
    
    for opt in ques:
        question = opt[1]
        options = opt[2:6]
        correctAnswer = opt[6]

        print(f"Q: {question}")
        for i in range(len(options)):
            print(f"{i + 1}. {options[i]}")
        answer = input("Choose the correct answer (1-4): ")

        if options[int(answer) - 1] == correctAnswer:
            score += 1
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer was: {correctAnswer}\n")

    with open("results.txt", "a") as file:
        file.write(f"{username},{sub},{score}\n")

    print(f"Your score for {sub}: {score}/{len(ques)}")

#code to display result of the user
def showResult(username):
    with open('results.txt', 'r') as resultFile:
        result = resultFile.readlines()
    for user in result:
        userData = user.strip().split(',')
        if userData[0] == username:
            print(f"{userData[1]}: {userData[2]} points")


def main():

    while True:
        print("Welcome to Quiz App")
        print("1. Register")
        print("2. Login")
        print("3. Attempt Quiz")
        print("4. View Results")
        print("5. Exit")
        
        option = input("Enter your choice: ")

        if option == '1':
            reg()
        elif option == '2':
            username = login()
            if username:
                while True:
                    print("\nLogged in as", username)
                    print("1. Attempt Quiz")
                    print("2. View Results")
                    print("3. Logout")
                    
                    logopt = input("Enter your choice: ")
                    if logopt == '1':
                        quiz(username)
                    elif logopt == '2':
                        showResult(username)
                    elif logopt == '3':
                        break
                    else:
                        print("Invalid choice, try again.")
        elif option == '3':
            print("Please login first.")
        elif option == '4':
            print("Please login first.")
        elif option == '5':
            print("Exiting app.")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()