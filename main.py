
import random
import ast
import operator

print("=== NOVA AI CHATBOT ===")
print("Type 'help' for commands or 'bye' to exit.")

name = None

def calculate(expression):
    operations = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv
    }

    def solve(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](
                solve(node.left), solve(node.right)
            )

        raise ValueError("Unsupported calculation")

    return solve(ast.parse(expression, mode="eval").body)


def reply(message):
    global name
    message = message.lower().strip()

    if message in ("bye", "exit", "quit"):
        return "Goodbye! Keep building!"

    if message == "help":
        return "Try: hello, my name is Alex, what is my name, calculate 5 * 6, joke"

    if message.startswith("my name is "):
        name = message[11:].strip().title()
        return f"Nice to meet you, {name}!"

    if "what is my name" in message:
        return f"Your name is {name}!" if name else "Tell me your name first."

    if message.startswith("calculate "):
        try:
            return f"Answer: {calculate(message[10:])}"
        except (ValueError, SyntaxError, TypeError,
                ZeroDivisionError):
            return "Sorry, I cannot calculate that."

    if any(word in message for word in ("hello", "hi", "hey")):
        return random.choice([
            "Hello! How can I help?",
            "Hey! Welcome to Nova.",
            "Hi there! What shall we learn?"
        ])

    if "joke" in message:
        return "Why do programmers like Python? Because it is easy to read!"

    if "your name" in message:
        return "I am Nova, your Python chatbot."

    if "ai" in message:
        return "AI stands for Artificial Intelligence."

    return "I am a beginner chatbot. Type 'help' to see my commands."


while True:
    message = input("\nYou: ")
    answer = reply(message)
    print("Nova:", answer)

    if message.lower().strip() in ("bye", "exit", "quit"):
        break
