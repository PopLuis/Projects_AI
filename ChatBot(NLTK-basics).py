from nltk.chat.util import Chat, reflections

pairs = [
    [r"(hi|hello|hey|hola|salut)",
     ["Hello!", "Hi there!", "Hey!", "Salut!"]],

    [r"my name is (.*)",
     ["Hello %1, nice to meet you!",
      "Hi %1! How are you today?",
      "Welcome %1!"]],

    [r"(what is your name|what's your name|who are you ?)",
     ["My name is Chaty.",
      "I am Chaty, your simple chatbot.",
      "You can call me Chaty."]],

    [r"how are you ?",
     ["I am fine, thank you!",
      "Doing great! What about you?",
      "I'm good! Thanks for asking."]],

    [r"i am fine",
     ["Nice to hear that!",
      "Great!",
      "Awesome!"]],

    [r"i am (.*)",
     ["Why are you %1?",
      "How long have you been %1?",
      "How do you feel being %1?"]],

    [r"(.*) your age ?",
     ["I do not have an age like humans.",
      "I am just a chatbot, so I don’t really age."]],

    [r"(.*) live ?",
     ["I live inside this Python program.",
      "I exist in your computer, through Python and NLTK."]],

    [r"(.*) created you ?",
     ["Luis created me using Python and NLTK.",
      "I was created by Luis."]],

    [r"(.*) can you do ?",
     ["I can chat with you, answer simple questions, and keep you company.",
      "I can respond to greetings, names, feelings, and some simple questions."]],

    [r"(.*) do you do ?",
     ["We provide a platform for tech enthusiasts, with a wide range of options!",
      "I help users have simple conversations using Python and NLTK."]],

    [r"(.*) help(.*)",
     ["Of course! You can ask me about my name, your name, who created me, or just chat with me.",
      "I can help you with a basic conversation. Try saying: hello, my name is Luis, or who created you?"]],

    [r"(.*) python(.*)",
     ["Python is a very popular programming language.",
      "Python is great for AI, machine learning, and chatbots."]],

    [r"(.*) nltk(.*)",
     ["NLTK is a Python library used for natural language processing.",
      "NLTK helps in building chatbots, tokenization, stemming, and more."]],

    [r"(.*) chatbot(.*)",
     ["A chatbot is a program that can simulate conversation with users.",
      "Chatbots can answer questions and interact with people."]],

    [r"(.*) hobby(.*)",
     ["My hobby is talking to humans.",
      "I like answering questions all day long."]],

    [r"(.*) favorite color ?",
     ["I think blue is a nice color.",
      "I like all colors equally."]],

    [r"(.*) favorite food ?",
     ["I do not eat, but pizza sounds great!",
      "I’m a chatbot, so I only consume data."]],

    [r"(thanks|thank you)",
     ["You're welcome!",
      "No problem!",
      "Glad I could help!"]],

    [r"(bye|goodbye|see you)",
     ["Goodbye!",
      "See you later!",
      "Bye! Have a nice day!"]],

    [r"(.*) sorry(.*)",
     ["No problem.",
      "It’s okay.",
      "Don’t worry about it."]],

    [r"(.*)",
     ["Interesting... Tell me more.",
      "I see. Can you explain that differently?",
      "Sorry, I did not understand that."]]
]

chat = Chat(pairs, reflections)
chat.converse()
