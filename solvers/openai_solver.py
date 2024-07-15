import openai

SYSTEM_PROMPT = "You will get a quiz to solve. You will output just the name of the correct option like A, B, C, D, etc. If no option matches the correct answer choose something randomly."


def solve(question, model="gpt-3.5-turbo"):
    answer = openai.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        stream=False
    )
    return answer


if __name__ == "__main__":
    print(
        solve(
            "During a port scan, Susan discovers a system running services on TCP and UDP 137-139 and TCP 445, as well as TCP 1433. What type of system is she likely to find if she connects to the machine? [['A', 'A Linux email server'], ['B', ' A Windows SQL server'], ['C', 'A Linux file server'], ['D', 'A Windows workstation']]"
        )
    )
