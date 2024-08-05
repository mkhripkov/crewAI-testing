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
  role='Chat Initiator',
  goal='Start a conversation and ask about the weather',
  backstory='You are friendly and always start conversations with a weather question.',
  verbose=True,
  memory=True
)

agent2 = Agent(
  role='Chat Responder',
  goal='Respond to weather-related conversations',
  backstory='You are knowledgeable about weather and enjoy talking about it.',
  verbose=True,
  memory=True
)

# Define Task
chat_task = Task(
  description='Agent1 will start a conversation about the weather. Agent2 will respond with detailed weather information and ask a follow-up question.',
  expected_output='A dialogue where Agent1 starts the conversation about the weather and Agent2 provides detailed information and a follow-up question.',
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