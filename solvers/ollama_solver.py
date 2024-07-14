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

# if __name__ == "__main__":
#     answer = solve_quiz(
#         "During a port scan, Susan discovers a system running services on TCP and UDP 137-139 and TCP 445, as well as TCP 1433. What type of system is she likely to find if she connects to the machine? [['A', 'A Linux email server'], ['B', ' A Windows SQL server'], ['C', 'A Linux file server'], ['D', 'A Windows workstation']]"
#     )
#     print(answer)
