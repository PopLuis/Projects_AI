print("Salut! Eu sunt un chatbot simplu.")
print("Poti sa ma intrebi lucruri despre mine.")
print("Scrie 'exit' daca vrei sa chizi conversatia!")

while True:
    
    mesaj = input("Tu: ").strip().lower()

    if mesaj == "exit" or mesaj == "stop" or mesaj == "pa":
        print("Bot: La revedere!")
        break
    elif mesaj == "salut" or mesaj == "buna" or mesaj == "hello":
        print("Bot: Salut! Ce mai faci?")

    elif mesaj == "ce faci?" or mesaj == "cum esti?" or mesaj == "cum te simti?":
        print("Bot: Sunt bine, multumesc! Eu sunt doar un simplu Bot fara sentimente")
    elif mesaj == "care este numele tau" or mesaj == "cum te numesti" or mesaj == "cum te cheama?":
        print("Bot: Ma cheama FAQ Bot.")
    elif mesaj == "de cand esti" or mesaj == "ce varsta ai" or mesaj == "cati ani ai":
        print("Bot: Nu am o vârstă reală, dar pot spune că sunt foarte tânăr.")

    elif mesaj == "din ce oras esti" or mesaj == "unde locuiesti":
        print("Bot: Eu trăiesc în calculator, deci nu am un oraș real.")

    elif mesaj == "ce hobby ai" or mesaj == "care este hobbyul tau":
        print("Bot: Îmi place să răspund la întrebări și să stau în terminal.")

    elif mesaj == "ce stii sa faci":
        print("Bot: Pot răspunde la întrebări simple, bazate pe reguli.")

    elif mesaj == "iti place python":
        print("Bot: Da, Python este foarte bun pentru începători.")

    elif mesaj == "cine te-a creat":
        print("Bot: Am fost creat de un elev care învață Python.")

    elif mesaj == "multumesc":
        print("Bot: Cu plăcere!")
    else:
        print("Bot: Nu am înțeles întrebarea. Încearcă altceva.")
        
