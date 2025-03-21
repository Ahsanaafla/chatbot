import os
import requests


API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

API_TOKEN = os.getenv("HF_API_TOKEN")

if not API_TOKEN:
    raise ValueError("API token not found. Please set the 'HF_API_TOKEN' environment variable.")

def query_hugging_face(prompt):
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    payload = {"inputs": prompt}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        print("Error:", response.status_code, response.text)
        return None
    
#function to specify inappropriate words 

def is_content_inappropriate(text):
    inappropriate_keywords = ["bitch", "ugly", "idiot"]
    for keyword in inappropriate_keywords:
        if keyword.lower() in text.lower():
            return True
    return False

def main():
    print("Type your query. To exit, type 'stop', 'bye', or 'quit'.")
    
    while True:
        user_input = input("Enter your query: ").strip().lower()
        if user_input in ["stop", "bye", "quit"]:
            print("Goodbye!")
            break
        
        if is_content_inappropriate(user_input):
            print("Your input contains inappropriate content. Please try again.")
            continue
        
        prompt = f"Question: {user_input}\nAnswer concisely and clearly:"
        response = query_hugging_face(prompt)
        
        if response:
            response = response.split(".")[0] + "."
            if is_content_inappropriate(response):
                print("The generated response contains inappropriate content. Please try again.")
            else:
                print("Generated Response:", response)

if __name__ == "__main__":
    main()
