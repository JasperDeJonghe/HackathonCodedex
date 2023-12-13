def run_python_quiz():
    score = 0

    # Question 1
    print("Question 1: What is the output of the following code?")
    code1 = '''
    x = 5
    y = 2
    result = x ** y
    print(result)
    '''
    print(code1)
    answer1 = input("Your answer: ").strip()
    if answer1 == "25":
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is 25.\n")

    # Question 2
    print("Question 2: What is the output of the following code?")
    code2 = '''
    word = "Python"
    length = len(word)
    print(length)
    '''
    print(code2)
    answer2 = input("Your answer: ").strip()
    if answer2 == "6":
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is 6.\n")

    # Question 3
    print("Question 3: What is the output of the following code?")
    code3 = '''
    def main():
        print("Hello, World!")

    main()
    '''
    print(code3)
    answer3 = input("Your answer: ").strip()
    if answer3.lower() == "hello, world!":
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is 'Hello, World!'.\n")

    # Question 4
    print("Question 4: What is the output of the following code?")
    code4 = '''
    for i in range(3):
        print(i * 2, end=" ")
    '''
    print(code4)
    answer4 = input("Your answer: ").strip()
    if answer4 == "0 2 4":
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is 0 2 4.\n")

    # Question 5
    print("Question 5: What is the output of the following code?")
    code5 = '''
    for i in range(2, 5):
        print(i, end=" ")
    '''
    print(code5)
    answer5 = input("Your answer: ").strip()
    if answer5 == "2 3 4":
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is 2 3 4.\n")

    # Display final score
    print(f"Quiz completed! Your score: {score}/5")

run_python_quiz()
