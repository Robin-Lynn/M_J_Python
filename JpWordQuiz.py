

#Save the words
ques={
    "Ohayo": "good morning",
    "Arigatou": "thanks",
    "Tsukki": "moon",
    "Hana":"flower",
    "Nomimono":"drinks",
    "Tabemono":"food",
    "Hi":"sun"
    }

print("----Japan Words Quiz----")

for jp_word in ques:
    user_answer=input(f"What's the meaning of {jp_word} ")

    if user_answer.lower()==ques[jp_word]:
        print("You're absolutely correct!")
    else:
        print("Game Over! Try Again!")
