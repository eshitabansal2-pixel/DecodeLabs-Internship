print(" College Assistant Bot ")
print("Type 'exit' to quit")
responses = {"hello": "Hi there",
"hi": "Hello!",
"fees": "Fee payment portal is open.",
"exam": "Exams start from 15 December.",
"library": "Library timing is 8 AM to 8 PM.",
"attendance": "Minimum attendance required is 75%.",
"internship": "Internship applications are open.",
"placement": "Placement training starts in 3rd semester."}

while True:
    user_input = input("You:").lower().strip()
    if user_input == "exit":
        print("Bot: Goodbye!")
        break

    reply = responses.get(user_input, "Bot: Sorry, I don't understand.")
    print(reply)