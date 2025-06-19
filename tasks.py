from crewai import Task
from agents import College_researcher, college_info_collector, presentation_specialist


research_task = Task(
    description=(
        "engineering colleges other than IIT's in Maharashtra."
        "For each institution, gather: official name, year of establishment, "
        "institutional type (Government/Private/Autonomous), official website, and governing body. "
        "Focus on colleges with strong academic reputations and good infrastructure."
    ),
    expected_output=(
        "colleges with basic identifying information presented in clear paragraphs. "
        "Each entry should begin with the college name as a heading, "
        "covering location, institutional background, and admission pathways."
    ),
    agent=College_researcher,
    async_execution=False,

  
)

detail_collection_task = Task(
    description=(
        "For each college, gather comprehensive information and organize it into narrative paragraphs covering: "
        "1. Academic Profile: Describe the NIRF rankings, accreditations, notable programs, and faculty strength "
        "in flowing paragraphs. "
        "2. Campus Life: Write descriptive paragraphs about the infrastructure, hostels, mess facilities, and campus "
        "amenities. Include student perspectives from forums when available. Use provided tools "
        "3. Admissions Process: Explain the admission criteria, cutoff trends, and fee structure in clear, "
        "connected sentences. for cutoffs of different college use source https://fe2024.mahacet.org/ViewPublicDocument?MenuId=2449 "
        "4. Career Outcomes: Present placement statistics, salary packages, and recruiter information as "
        "a cohesive story rather than bullet points. Use official websites of colleges for placement information. Get exact numbers and top recruiters"
        "Maintain a factual yet engaging writing style throughout."
    ),
    expected_output=(
        "Detailed narrative profiles for each college with: "
        "1. Flowing academic overview (3-4 paragraphs) "
        "2. Vibrant campus description (2-3 paragraphs) "
        "3. Clear admission guidelines (2 paragraphs) "
        "4. Mention cutoffs for all categories"
        "5. Professional placement report (2-3 paragraphs) "
        "All information should connect naturally without bullet points or tables."
    ),
    agent=college_info_collector,
    async_execution=False,
    context=[research_task],
  
    
)

presentation_task = Task(
    description=(
        "Compose detailed profiles for all colleges with enhanced focus on Hostel, Mess, Placements and Cutoffs using this structure:\n\n"
        
        "## [College Full Name] ([Common Abbreviation])\n"
        "[4-5 sentence introduction highlighting:\n"
        "- Year established and institution type\n"
        "- Quick reputation summary\n"
        "- Notable alumni if relevant]\n\n"
        
        "### 🏠 Hostel & Campus Life\n"
        "[3 detailed paragraphs with verified numbers and descriptions:\n"
        "1. Hostel Infrastructure:\n"
        "   - Exact number of hostels (gender-wise breakdown)\n"
        "   - Room types (single/double/triple) with current fees\n"
        "   - First-year allocation policy with percentages\n"
        "   - Example: 'VJTI Mumbai's 6 hostels (4 male/2 female) accommodate 1,200 students. First-years get triple rooms (₹85,000/yr)'\n\n"
        "2. Mess & Food:\n"
        "   - Number of mess halls and meal plans\n"
        "   - Monthly food costs and quality indicators\n"
        "   - Special dietary provisions\n"
        "3. Campus Facilities:\n"
        "   - Key amenities (labs, libraries, medical)\n"
        "   - Security measures\n"
        "   - Student testimonials about daily life]\n\n"
        
        "### 📊 Placements & Internships\n"
        "[3 data-rich paragraphs covering:\n"
        "1. Placement Statistics:\n"
        "   - 2024 placement percentage (department-wise if available)\n"
        "   - Average, median, highest packages\n"
        "   - Example: '2024 saw 92% placements with median ₹12.5 LPA'\n\n"
        "2. Top Recruiters:\n"
        "   - List Top Recruiters  \n"
        "   - Notable department-wise recruiters if available\n"
        "3. Internship Pipeline if available:\n"
        "   - Summer internship conversion rates\n"
        "   - Stipend ranges\n"
        "   - Pre-placement offer percentages]\n\n"
        
        "### 🎚️ Cutoffs & Admissions\n"
        "[2 analytical paragraphs with exact figures:\n"
        "1. Entrance Exam Cutoffs:\n"
        "   - 2024 opening/closing ranks for all categories\n"
        "   - Mention MHCET cutoff \n"
        "   - Example: 'MHCET 2024 cutoff: General-98.3%, OBC-96.1%'\n\n"
        "2. Fee Structure :\n"
        "   - Annual tuition + hostel breakdown\n"
        "   - Payment plans\n"
        "   - Scholarship impact on effective costs]\n\n"
        
        "Research Requirements:\n"
        "1. For missing data:\n"
        "   - Contact college administration via official channels\n"
        "   - Reference latest NIRF reports\n"
        "   - Extract from placement brochures\n"
        "Even if some data is unavailable provide the data that is available "
        
    ),
    expected_output=(
        "10 complete college profiles featuring:\n"
        "1. 300-word Hostel/Mess section with verified numbers\n"
        "2. 250-word Placement analysis with exact statistics\n"
        "3. 200-word Cutoff details with historical trends\n"
        "4. All data properly sourced and timestamped\n"
        
        "Format: GitHub Markdown with ### headings for each section"
    ),
    agent=presentation_specialist,
    async_execution=False,
    context=[detail_collection_task],
    output_file = "clg10.md" 
    
)