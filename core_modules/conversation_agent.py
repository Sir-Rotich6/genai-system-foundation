import re
from openai_api import make_openai_api_call

def cleanse_conversation_log(messages_obj):
    """
    Converts the conversation log into a single string and removes problematic punctuations.
    """
    conversation_str = " ".join(
        [f"{entry['role']}: {entry['content']}" for entry in messages_obj]
    )
    # Remove problematic punctuations
    return re.sub(r"[^\w\s,.?!:]", "", conversation_str)

def conversational_agent(initial_user_input, mrole, mcontent, user_role,user_name):
    # Initialize conversation log (messages object)
    messages_obj = [{"role": mrole, "content": mcontent}]  # Start with system message

    print("Welcome to the conversational agent! Type 'q' or 'quit' to end the conversation.")

    # Handle the initial user input
    if initial_user_input:
        print(f"{user_name}: {initial_user_input}")
        messages_obj.append({"role": user_role, "content": initial_user_input})

        # Cleansed string representation of conversation
        conversation_string = cleanse_conversation_log(messages_obj)

        # Make the API call with the cleansed conversation
        try:
            agent_response = make_openai_api_call(
                input=conversation_string,  # Use the cleansed string
                mrole=mrole,
                mcontent=mcontent,
                user_role=user_role
            )
        except Exception as e:
            print(f"Error during API call: {e}")
            agent_response = "Sorry, I encountered an error processing your input."

        # Save assistant's response to messages_obj
        messages_obj.append({"role": "assistant", "content": agent_response})

        # Display assistant's response
        print(f"Agent: {agent_response}")

    # Start the conversational loop
    while True:
        # User input
        user_input = input(f"{user_name}: ")
        
        # Check for quit condition
        if user_input.lower() in ["q", "quit"]:
            print("Exiting the conversation. Goodbye!")
            break

        # Append user input to conversation log
        messages_obj.append({"role": user_role, "content": user_input})

        # Cleansed string representation of conversation
        conversation_string = cleanse_conversation_log(messages_obj)

        # Make the API call with the cleansed conversation
        try:
            agent_response = make_openai_api_call(
                input=conversation_string,  # Use the cleansed string
                mrole=mrole,
                mcontent=mcontent,
                user_role=user_role
            )
        except Exception as e:
            print(f"Error during API call: {e}")
            agent_response = "Sorry, I encountered an error processing your input."

        # Append assistant's response to conversation log
        messages_obj.append({"role": "assistant", "content": agent_response})

        # Display assistant's response
        print(f"Agent: {agent_response}")

    # Save the conversation log to a file
    '''
    with open("conversation_log.txt", "w") as log_file:
        log_file.write("\n".join([f"{entry['role']}: {entry['content']}" for entry in messages_obj]))

    print("Conversation saved to 'conversation_log.txt'.")
    '''
    # Save the conversation log to a file
    with open("conversation_log.txt", "w") as log_file:
        log_file.write(
           "\n".join([
                f"{(user_name if entry['role'] == 'user' else entry['role'])}: {entry['content']}"
                for entry in messages_obj
            ])
        )
    print("Conversation saved to 'conversation_log.txt'.")
# Call the conversational agent
def run_conversational_agent(uinput, mrole, mcontent, user_role,user_name):
    conversational_agent(uinput, mrole, mcontent, user_role,user_name)
