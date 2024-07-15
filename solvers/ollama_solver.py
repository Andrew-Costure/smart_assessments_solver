import ollama

SYSTEM_PROMPT = "You will get a quiz to solve. You will output just the name of the correct option like A, B, C, D, etc. If no option matches the correct answer choose something randomly."


def solve(question, model="llama3"):
    answer = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        stream=False
    )
    return answer["message"]["content"].split()[0] # sometimes GenAI can give a detail as well so just ignore it since the first word must be our required output. (We hope it is A, B, C etc :P )
