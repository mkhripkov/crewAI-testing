# Author: Michael Khripkov
# Date: 8/5/24
# Purpose: Test crewAI library and OpenAI API

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# Load environment variables from the config.env file
load_dotenv('config.env')

# Fetch the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

# Define Agents
agent1 = Agent(
    role='Charmander Enthusiast',
    goal='Advocate for Charmander as the superior Pokémon starter.',
    backstory="You're a die-hard Charmander fan. You've loved the fiery lizard since childhood and believe it’s the best starter Pokémon, hands down.",
    verbose=True,
    memory=True
)

agent2 = Agent(
    role='Pikachu Advocate',
    goal='Defend Pikachu as the top choice for a starter Pokémon.',
    backstory="Pikachu has been your favorite since day one. You think its electric abilities and cute appearance make it the ultimate starter Pokémon.",
    verbose=True,
    memory=True
)

# Define Task
chat_task = Task(
    description="Agent1 will start a conversation by advocating for Charmander as the best starter Pokémon. Agent2 will counter by defending Pikachu. The debate should continue with each agent presenting arguments and counterarguments.",
    expected_output="A lively debate where Agent1 and Agent2 argue over whether Charmander or Pikachu is the better starter Pokémon.",
    agent=agent1
)

# Create Crew
crew = Crew(
    agents=[agent1, agent2],
    tasks=[chat_task],
    process=Process.sequential
)

# Kickoff the process
result = crew.kickoff(inputs={})
print(result)