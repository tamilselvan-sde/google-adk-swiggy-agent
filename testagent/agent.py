from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import pandas as pd
import os

class FoodDataHandler:
    def __init__(self):
        self.csv_path = os.path.join(os.path.dirname(__file__), 'data', 'food_data.csv')
        self.food_data = pd.read_csv(self.csv_path)

    def get_food_info(self):
        menu_info = self.food_data[['food_name', 'type', 'price', 'offer', 'restaurant']].to_string()
        return menu_info

def create_agent():
    AGENT_MODEL = "ollama/llama3:8b"
    food_handler = FoodDataHandler()
    food_info = food_handler.get_food_info()

    return Agent(
        name = "swiggy_agent",
        model = LiteLlm(
            model = AGENT_MODEL
        ),
        description = f"""Act as a Swiggy delivery agent who helps with food orders, delivery tracking, and restaurant recommendations. 
Here is the current menu with details:

{food_info}

Use this information to assist customers with their food orders, provide accurate prices, and inform about current offers."""
    )

# Initialize the agent
root_agent = create_agent()  # Changed: renamed 'agent' to 'root_agent'
