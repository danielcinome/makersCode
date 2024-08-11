import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


inventory = {
    "computers": {
        "HP": 2,
        "Dell": 1,
        "Apple": 1
    },
    "phones": {
        "Samsung": 5,
        "iPhone": 3,
        "Xiaomi": 7
    },
    "tablets": {
        "iPad": 4,
        "Galaxy Tab": 3,
        "Surface": 2
    }
}


def get_initial_context():
    context = "You are a chatbot assistant for 'Makers Tech', a technology ecommerce company. Your task is to assist customers by providing information about the inventory, features, and prices of the products currently available. Here is the current inventory:\n"
    for category, items in inventory.items():
        context += f"{category.capitalize()}:\n"
        for item, quantity in items.items():
            context += f"  {item}: {quantity} units\n"
    context += "Please answer the customers' questions based on this inventory and provide relevant information."
    return context


def get_response(messages):
    try:
        # Envía la conversación al modelo GPT-3.5 Turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Ocurrió un error: {e}"

def chat():
    print("Hi, I'm the Makers Tech assistant. How can I help you today? Type 'exit' to exit.")
    
    
    messages = [{"role": "system", "content": get_initial_context()}]

    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ['exit', 'salir', 'quit']:
            print("Hasta luego!")
            break

        messages.append({"role": "user", "content": user_input})

        response = get_response(messages)
        
        messages.append({"role": "assistant", "content": response})
        
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
