import requests
from utils import send_message

def handle_ai_command(group_id, user_id, command, text):
    # Placeholder for external AI API
    api_url = "https://api.example.com/generate"  # Replace with actual API
    payload = {"prompt": text, "model": "gpt-3.5-turbo"}  # Adjust based on API
    try:
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            result = response.json().get("response", "No response from AI.")
            send_message(group_id, f"🦉 AI Response: {result}")
        else:
            send_message(group_id, "Error: Unable to get AI response.")
    except Exception as e:
        send_message(group_id, f"Error: {str(e)}")