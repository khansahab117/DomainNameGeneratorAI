import openai
import json
import time
from checkDomain import check_domain_availability
from dotenv import load_dotenv
import os

load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def chat_with_ai():
    initial_message = {"role": "system", "content": "You are a helpful assistant, whose job is to only recommend domain names."}

    print("Start chatting with the AI (type 'quit' to stop):")
    while True:
        user_input = input("Describe your domain name: ")

        if user_input.lower() in ["quit", "exit"]:
            print("Ending the chat. Goodbye!")
            break

        counter = 10
        unavailable = []
        messages = [initial_message]

        while counter > 0:
            prompt = f"""
            You are to recommend {counter} domain names.

            This is the user's description of the domain name: {user_input}

            These domains are unavailable: {unavailable[-5:]}

            Only reply back in the following JSON format for processing:  

            {{
                "domains": ["list", "of", "domain", "names"]
            }}
            """
            
            messages.append({"role": "user", "content": prompt})

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
            except openai.error.RateLimitError as e:
                wait_time = 60
                print(e)
                print(f"Rate limit reached, waiting {wait_time} seconds")
                time.sleep(wait_time)

                # Reset messages and unavailable list
                messages = [initial_message]
                unavailable = []
                continue

            ai_response = response.choices[0].message['content']
            messages.append({"role": "assistant", "content": ai_response})

            try:
                domain_suggestions = json.loads(ai_response)["domains"]
                parseErrorBool = False
            except (json.JSONDecodeError, KeyError):
                parseErrorBool = True
                print("Failed to parse the AI response. Please try again.")
                continue

            for domain in domain_suggestions:
                if check_domain_availability(domain):
                    print(f"Available domain: {domain}")
                    with open("domainNames.txt", "a") as file:
                        file.write(f"{domain}\n")
                    counter -= 1
                    if counter == 0:
                        break
                else:
                    unavailable.append(domain)

            # Limit the messages to the last 1 system message and 3 user/assistant interactions
            messages = [initial_message] + messages[-6:]

        # Reset messages and unavailable list after each user input
        messages = [initial_message]
        unavailable = []

if __name__ == "__main__":
    chat_with_ai()