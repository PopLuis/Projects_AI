import os
from langchain.agents import create_agent

os.environ['GROQ_API_KEY'] = 'gsk_r4Zylq3mU571FAxd6ZXwWGdyb3FY6Yzei5tqKrZGTVokqNvLMz'

agent = create_agent(
    model="groq:llama-3.1-8b-instant",
    tools=[],
    system_prompt='you are an ai assistant, pls be very concise and precise'
)

history = []

print("Type 'exit' to quit.\n")

while True:
    user_prompt = input("You: ")
    if user_prompt.lower() == "exit":
        print("Exiting chat...")
        break

    # adaugă mesajul utilizatorului în istoric
    user_msg = {'role': 'user', 'content': user_prompt}
    history.append(user_msg)

    # apelează agentul
    response = agent.invoke({'messages': history})
    reply = response['messages'][-1].content

    # afișează răspunsul
    print(f"Assistant: {reply}\n")
    print("-" * 60)

    # adaugă răspunsul asistentului în istoric
    ass_msg = {'role': 'assistant', 'content': reply}
    history.append(ass_msg)
