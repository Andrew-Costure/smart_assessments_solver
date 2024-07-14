import ollama

SYSTEM_PROMPT = "You will get a quiz to solve. You will output just the name of the correct option like A, B, C. If no option matches the correct answer choose something randomly."


def solve_quiz(question):
    answer = ollama.chat(
        model="llama3",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        stream=False
    )
    return answer["message"]["content"]
