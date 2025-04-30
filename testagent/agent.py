from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import pandas as pd
import os
from typing import str, Optional, List, Dict, Any

class FoodDataHandler:
    """
    A class to handle food-related data operations from CSV file.
    
    This class manages the loading and processing of food menu data,
    including details like food names, prices, offers, and restaurants.
    """
    
    def __init__(self) -> None:
        self.csv_path: str = os.path.join(os.path.dirname(__file__), 'data', 'food_data.csv')
        self.food_data: pd.DataFrame = pd.read_csv(self.csv_path)

    def get_food_info(self) -> str:
        """
        Retrieves formatted food menu information.
        
        Returns:
            str: A formatted string containing food names, types, prices,
                 offers, and restaurant information.
        """
        menu_info: str = self.food_data[['food_name', 'type', 'price', 'offer', 'restaurant']].to_string()
        return menu_info

def create_agent() -> Agent:
    """
    Creates and configures a Swiggy delivery agent.
    
    This function initializes an AI agent that can handle food orders,
    provide recommendations, and assist with delivery tracking.
    
    Returns:
        Agent: Configured Swiggy delivery agent instance.
    """
    AGENT_MODEL: str = "ollama/llama3:8b"
    food_handler: FoodDataHandler = FoodDataHandler()
    food_info: str = food_handler.get_food_info()

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
root_agent: Agent = create_agent()