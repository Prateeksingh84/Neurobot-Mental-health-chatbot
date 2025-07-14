# from groq import Groq

# groq_api = Groq(api_key="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")
# def respond(question):
#     chat_completion = groq_api.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": f"This is the question asked by user {question} answer this question in one or two lines",
#             }
#                 ],
#                 model="llama-3.3-70b-versatile",
#             )
    
#     return chat_completion.choices[0].message.content

# question=input("Enter Query:")
# answer=respond(question)
# from groq import Groq

# # Replace 'your_groq_api_key_here' with your actual key
# client = Groq(api_key="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")

# # Sample message; replace with your conversation history as needed
# messages = [
#     {"role": "user", "content": "Hello, can you give me a mental wellness tip?"}
# ]

# completion = client.chat.completions.create(
#     model="llama-guard-3-8b",
#     messages=messages,
#     temperature=1,
#     max_tokens=1024,  # Note: `max_completion_tokens` should be `max_tokens`
#     top_p=1,
#     stream=True,
#     stop=None,
# )

# for chunk in completion:
#     print(chunk.choices[0].delta.content or "", end="")
from groq import Groq

# Initialize client with your GROQ API key
groq_api = Groq(api_key="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")

# Function to get concise response
def respond(question: str) -> str:
    chat_completion = groq_api.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"This is the question asked by user: {question}. Answer this question in one or two lines.",
            }
        ],
        model="llama3-70b-8192",  # Use exact model name supported
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        stop=None
    )
    return chat_completion.choices[0].message.content.strip()

# Loop for chatting
if __name__ == "__main__":
    print("🧠 Mental Health Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Take care! 💚")
            break
        reply = respond(user_input)
        print(f"Bot: {reply}")


