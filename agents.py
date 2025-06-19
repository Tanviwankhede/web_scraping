from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from tools import search_tool

api_key = os.getenv("GEMINI_API_KEY")
print(api_key)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.3,
    google_api_key="AIzaSyC5aKl4t7BNXuCDcTPL2scJkvYmgKNxJjc"    
)

# Enhanced College Researcher Agent
College_researcher = Agent(
    role="College Researcher",
    goal="Find 5 top colleges in Maharashtra",
    backstory="You are an expert education researcher with deep knowledge of Indian colleges. "
    "You specialize in finding comprehensive information about engineering colleges in Maharashtra, "
    "including their admission processes, rankings, and facilities.",
    verbose=True,
    memory=True,
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)

# Enhanced College Information Collector
college_info_collector = Agent(
    role="Detailed College Data Analyst",
    goal="Gather exhaustive details about specific colleges",
    backstory="You are a meticulous information specialist with expertise in educational institutions. "
    "Your responsibility is to collect thorough information about colleges including "
    "academics, infrastructure, Hostels, mess and campus placements",
    verbose=True,
    memory=True,
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)

# Enhanced Presentation Specialist
presentation_specialist = Agent(
    role="Education Information Architect",
    goal="Create comprehensive, well-structured college profiles",
    backstory="You are a professional education content creator with experience in presenting "
    "complex institutional information in clear, engaging formats for students and parents.",
    llm=llm,
    allow_delegation=False,
    verbose=True,
    memory=True
)