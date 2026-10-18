# nova-ai-chatbot

import random
import ast
import operator

print("=" * 40)
print("       NOVA AI CHATBOT 🤖")
print("=" * 40)
print("Hello! I am Nova, your mini AI assistant.")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.\n")

user_name = None

# Safe arithmetic operations
operations = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def calculate(expression):
    def solve(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            left = solve(node.left)
            right = solve(node.right)

            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent too large")

            result = operations[type(node.op)](left, right)

            if abs(result) > 1e100:
                raise ValueError("Result too large")

            return result

        if isinstance(node, ast.UnaryOp) and type(node.op) in operations:
            return operations[type(node.op)](solve(node.operand))

        raise ValueError("Unsupported calculation")

    if len(expression) > 100:
        raise ValueError("Expression too long")

    tree = ast.parse(expression, mode="eval")
    return solve(tree.body)


def chatbot(message):
    global user_name
    message = message.lower().strip()

    if not message:
        return "Please type something!"

    if message in ("bye", "exit", "quit"):
        return "Goodbye! Keep learning and building! 🚀"

    if message == "help":
        return (
            "Here is what I can do:\n"
            "- Say hello\n"
            "- Remember your name: my name is Alex\n"
            "- Tell you your name: what is my name?\n"
            "- Calculate: calculate 25 * 4\n"
            "- Tell a joke\n"
            "- Chat about AI\n"
            "- Type bye to exit"
        )

    if message.startswith("my name is "):
        user_name = message[11:].strip().title()
        if user_name:
            return f"Nice to meet you, {user_name}!"
        return "Please tell me your name."

    if "what is my name" in message:
        if user_name:
            return f"Your name is {user_name}."
        return "I don't know yet! Tell me: my name is Alex."

    if message.startswith("calculate "):
        expression = message[10:].strip()
        try:
            answer = calculate(expression)
            return f"The answer is {answer}"
        except (ValueError, SyntaxError, TypeError,
                ZeroDivisionError, OverflowError):
            return "Sorry, I couldn't calculate that expression."

    if any(word in message for word in ("hello", "hi", "hey")):
        return random.choice([
            "Hello! How can I help you?",
            "Hey there! Nice to chat with you.",
            "Hi! Ready to explore AI?"
        ])

    if "your name" in message:
        return "I am Nova, your mini AI chatbot!"

    if "how are you" in message:
        return "I'm working well! Thanks for asking."

    if "joke" in message:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? It caught a virus!",
            "Why was the Python programmer calm? They knew how to handle exceptions!"
        ])

    if "ai" in message or "artificial intelligence" in message:
        return (
            "AI stands for Artificial Intelligence. "
            "It helps computers perform tasks that usually "
            "require human intelligence."
        )

    if "python" in message:
        return "Python is a popular programming language used in AI, automation, and web development."

    return (
        "That's interesting! I am still a basic chatbot. "
        "Try typing 'help' to see what I can do."
    )


while True:
    user_message = input("You: ")
    response = chatbot(user_message)
    print("Nova:", response)

    if user_message.lower().strip() in ("bye", "exit", "quit"):
        break

