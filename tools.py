from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the search tool
search_tool = SerperDevTool()