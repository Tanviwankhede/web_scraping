# main.py
from dotenv import load_dotenv
load_dotenv()
import os
from agents import college_info_collector,College_researcher,presentation_specialist
from crewai import Crew, Process
from tasks import research_task, detail_collection_task, presentation_task

# Form the crew
college_crew = Crew(
    agents=[College_researcher, college_info_collector, presentation_specialist],
    tasks=[research_task, detail_collection_task, presentation_task],
    process=Process.sequential,
    verbose=2
)

# Execute the crew
result = college_crew.kickoff()
print(result)