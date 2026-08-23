import streamlit as st
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="PathPilot — Find Your Future",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================
if "results" not in st.session_state:
    st.session_state.results = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ============================================================
# STYLING
# ============================================================
st.markdown(
    """
    <style>
    .main { padding-top: 1.5rem; }
    .hero {
        padding: 2.5rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .hero h1 { font-size: 3rem; margin-bottom: 0.5rem; }
    .hero p { font-size: 1.15rem; }
    .career-card {
        padding: 1.5rem;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
        background: white;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    }
    .match-score { font-size: 2rem; font-weight: 700; }
    .small-text { color: #6b7280; }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================
st.markdown(
    """
    <div class="hero">
        <h1>🚀 PathPilot</h1>
        <p>Discover pathways and careers that fit YOU.</p>
        <p>Explore your options based on your subjects, skills, interests and goals.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# QUESTIONS — IB SL & HL ADDED
# ============================================================
st.subheader("1️⃣ What pathway are you thinking about?")
pathway = st.multiselect(
    "Select all that apply:",
    [
        "A Levels",
        "International Baccalaureate — Standard Level (IB SL)",
        "International Baccalaureate — Higher Level (IB HL)",
        "T Level",
        "BTEC (Level 3 / Extended Diploma)",
        "CTEC",
        "OCR Cambridge Technical",
        "Intermediate Apprenticeship (Level 2)",
        "Advanced Apprenticeship (Level 3)",
        "Higher Apprenticeship (Level 4)",
        "Higher Apprenticeship (Level 5)",
        "Degree Apprenticeship (Level 6)",
        "Degree Apprenticeship (Level 7)",
        "University",
        "School Leaver Programme",
        "Access to HE",
        "Not sure yet"
    ]
)

st.subheader("2️⃣ What subjects are you studying right now?")
subjects = st.multiselect(
    "Tick all that apply:",
    [
        "Maths", "Further Maths", "English Language", "English Literature",
        "Biology", "Chemistry", "Physics", "Computer Science",
        "IT / Digital Technology", "Economics", "Business Studies",
        "Psychology", "Sociology", "History", "Geography",
        "French / Spanish / Other Language", "Art & Design", "Graphic Design",
        "Engineering", "Health & Social Care", "Law", "Media Studies",
        "PE / Sports Science", "Music / Music Technology", "Drama / Theatre",
        "Philosophy & Ethics", "Other"
    ]
)

st.subheader("3️⃣ What are your best skills?")
st.caption(
    "Tell us what you're good at. For example: "
    "coding, problem-solving, leadership, teamwork, "
    "public speaking, creativity, organisation, "
    "writing, research, data analysis or planning."
)
skills = st.text_area("Your skills:", placeholder="e.g. coding, problem-solving, teamwork...")

st.subheader("4️⃣ What do you enjoy doing most?")
interests = st.multiselect(
    "Pick all that match:",
    [
        "Coding, programming & software development",
        "Art, design, drawing & creative work",
        "Sports, fitness, training & outdoor activities",
        "Gaming, esports & streaming",
        "Writing, journalism, blogging & content creation",
        "Science experiments, research & discovering new things",
        "Business ideas, entrepreneurship & starting projects",
        "Helping people, mentoring, charity & community work",
        "Teaching, explaining, tutoring & supporting others",
        "Building, making, fixing & hands-on creating",
        "Travelling, exploring & learning about different cultures",
        "Music, performing, singing, instruments & entertainment",
        "Social media, content creation, marketing & trends",
        "Working with numbers, data, maths & analysing facts",
        "Nature, animals, wildlife & the environment",
        "Debating, politics, current affairs & discussing ideas",
        "Cooking, baking, food & hospitality",
        "Fashion, beauty, styling & lifestyle",
        "Photography, videography & visual storytelling",
        "Planning events, organising & bringing people together",
        "Languages, learning about other countries & translating",
        "Reading, learning & discovering new things",
        "Not sure yet"
    ]
)

st.subheader("5️⃣ Which industries interest you most?")
industries = st.multiselect(
    "Pick as many as you like:",
    [
        "Technology, Software Development & IT",
        "Engineering — Mechanical, Electrical, Civil & Aerospace",
        "Healthcare, Medicine, Nursing & Mental Health",
        "Business, Finance, Accounting & Banking",
        "Creative, Media, Design, Film & Journalism",
        "Education, Teaching & Training",
        "Law, Legal Services, Politics & Government",
        "Science, Research, Biotech & Pharmaceuticals",
        "Sports, Fitness, Leisure & Nutrition",
        "Public Services, Police, Fire, Military & Civil Service",
        "Environment, Sustainability, Green Energy & Conservation",
        "Hospitality, Events, Tourism & Travel",
        "Marketing, Advertising, PR & Communications",
        "Construction, Architecture, Surveying & Property",
        "Transport, Logistics, Aviation & Supply Chain",
        "Fashion, Retail, Merchandising & Consumer Brands",
        "Digital Media, Gaming, Animation & VFX",
        "Charity, Non-Profit & Social Impact",
        "Manufacturing, Production & Industrial Design",
        "Human Resources, Recruitment & People Management",
        "Publishing, Literature & Libraries",
        "Performing Arts, Music Production & Entertainment",
        "Agriculture, Food Science & Veterinary",
        "Energy, Oil & Gas / Renewables",
        "Law Enforcement, Security & Intelligence",
        "Not sure yet"
    ]
)

st.subheader("6️⃣ What kind of work environment do you prefer?")
environment = st.multiselect(
    "Select all that fit:",
    [
        "Professional office setting", "Fast-paced & busy",
        "Creative / relaxed vibe", "Working outdoors / on-site",
        "Lab / research facility", "Remote / from home",
        "Team-focused", "Independent working",
        "Customer-facing", "Not sure yet"
    ]
)

st.subheader("7️⃣ What matters most to you?")
values = st.multiselect(
    "Pick your top priorities:",
    [
        "High earning potential", "Job security", "Creative freedom",
        "Helping people", "Fast career progression", "Good work-life balance",
        "Learning new skills", "Making an impact", "Working with people",
        "Not sure yet"
    ]
)

# ============================================================
# CAREER DATABASE
# ============================================================
CAREERS = [
    {
        "name": "Software Engineer",
        "industries": ["Technology, Software Development & IT"],
        "subjects": ["Maths", "Further Maths", "Computer Science", "Physics", "IT / Digital Technology"],
        "interests": ["Coding, programming & software development", "Gaming, esports & streaming", "Building, making, fixing & hands-on creating", "Working with numbers, data, maths & analysing facts"],
        "keywords": ["coding", "programming", "software", "python", "technology", "problem-solving", "data", "algorithms"],
        "environment": ["Professional office setting", "Fast-paced & busy", "Remote / from home", "Team-focused", "Independent working"],
        "values": ["High earning potential", "Fast career progression", "Learning new skills", "Creative freedom", "Good work-life balance"],
        "levels": [3, 4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)", "Advanced Apprenticeship (Level 3)"],
        "skills_to_build": ["Python", "Git & GitHub", "Algorithms", "Data structures", "Software development"]
    },
    {
        "name": "Data Scientist",
        "industries": ["Technology, Software Development & IT", "Science, Research, Biotech & Pharmaceuticals", "Business, Finance, Accounting & Banking"],
        "subjects": ["Maths", "Further Maths", "Computer Science", "Economics", "Physics"],
        "interests": ["Working with numbers, data, maths & analysing facts", "Science experiments, research & discovering new things", "Coding, programming & software development", "Reading, learning & discovering new things"],
        "keywords": ["data", "maths", "statistics", "analysis", "research", "coding", "python", "numbers"],
        "environment": ["Professional office setting", "Lab / research facility", "Remote / from home", "Independent working", "Team-focused"],
        "values": ["High earning potential", "Learning new skills", "Making an impact", "Fast career progression"],
        "levels": [4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)"],
        "skills_to_build": ["Python", "Statistics", "SQL", "Data visualisation", "Machine learning"]
    },
    {
        "name": "Cyber Security Analyst",
        "industries": ["Technology, Software Development & IT", "Law Enforcement, Security & Intelligence"],
        "subjects": ["Computer Science", "Maths", "Further Maths", "IT / Digital Technology", "Physics"],
        "interests": ["Coding, programming & software development", "Gaming, esports & streaming", "Debating, politics, current affairs & discussing ideas", "Reading, learning & discovering new things"],
        "keywords": ["coding", "security", "technology", "problem-solving", "investigation", "research", "computers", "networking"],
        "environment": ["Professional office setting", "Fast-paced & busy", "Remote / from home", "Team-focused", "Independent working"],
        "values": ["High earning potential", "Job security", "Learning new skills", "Making an impact", "Fast career progression"],
        "levels": [3, 4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)", "Advanced Apprenticeship (Level 3)"],
        "skills_to_build": ["Networking", "Python", "Linux", "Cybersecurity fundamentals", "Threat analysis"]
    },
    {
        "name": "Accountant",
        "industries": ["Business, Finance, Accounting & Banking"],
        "subjects": ["Maths", "Further Maths", "Economics", "Business Studies"],
        "interests": ["Working with numbers, data, maths & analysing facts", "Business ideas, entrepreneurship & starting projects", "Reading, learning & discovering new things"],
        "keywords": ["numbers", "maths", "finance", "analysis", "organisation", "business", "economics"],
        "environment": ["Professional office setting", "Fast-paced & busy", "Team-focused", "Independent working"],
        "values": ["High earning potential", "Job security", "Fast career progression", "Learning new skills", "Good work-life balance"],
        "levels": [3, 4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)", "School Leaver Programme"],
        "skills_to_build": ["Financial analysis", "Excel", "Accounting principles", "Communication", "Attention to detail"]
    },
    {
        "name": "Business Analyst",
        "industries": ["Business, Finance, Accounting & Banking", "Technology, Software Development & IT"],
        "subjects": ["Maths", "Economics", "Business Studies", "Computer Science"],
        "interests": ["Business ideas, entrepreneurship & starting projects", "Working with numbers, data, maths & analysing facts", "Planning events, organising & bringing people together", "Coding, programming & software development"],
        "keywords": ["analysis", "business", "problem-solving", "data", "organisation", "communication", "research", "planning"],
        "environment": ["Professional office setting", "Team-focused", "Fast-paced & busy", "Independent working"],
        "values": ["High earning potential", "Fast career progression", "Learning new skills", "Working with people", "Good work-life balance"],
        "levels": [4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)"],
        "skills_to_build": ["Excel", "Data analysis", "Presentation skills", "Business strategy", "Stakeholder communication"]
    },
    {
        "name": "Civil Engineer",
        "industries": ["Engineering — Mechanical, Electrical, Civil & Aerospace", "Construction, Architecture, Surveying & Property"],
        "subjects": ["Maths", "Further Maths", "Physics", "Engineering", "Geography"],
        "interests": ["Building, making, fixing & hands-on creating", "Working with numbers, data, maths & analysing facts", "Science experiments, research & discovering new things"],
        "keywords": ["maths", "engineering", "building", "design", "problem-solving", "physics", "construction"],
        "environment": ["Working outdoors / on-site", "Professional office setting", "Team-focused", "Fast-paced & busy"],
        "values": ["High earning potential", "Job security", "Making an impact", "Learning new skills"],
        "levels": [4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)"],
        "skills_to_build": ["CAD", "Engineering mathematics", "Project management", "Structural principles", "Technical drawing"]
    },
    {
        "name": "Doctor / Medical Practitioner",
        "industries": ["Healthcare, Medicine, Nursing & Mental Health"],
        "subjects": ["Biology", "Chemistry", "Maths", "Physics"],
        "interests": ["Science experiments, research & discovering new things", "Helping people, mentoring, charity & community work", "Reading, learning & discovering new things"],
        "keywords": ["biology", "science", "research", "helping", "people", "communication", "problem-solving"],
        "environment": ["Lab / research facility", "Fast-paced & busy", "Customer-facing", "Team-focused"],
        "values": ["Helping people", "Making an impact", "Job security", "Learning new skills", "Working with people"],
        "levels": [6, 7],
        "routes": ["University"],
        "skills_to_build": ["Biology", "Chemistry", "Communication", "Critical thinking", "Research"]
    },
    {
        "name": "Graphic Designer",
        "industries": ["Creative, Media, Design, Film & Journalism", "Marketing, Advertising, PR & Communications"],
        "subjects": ["Art & Design", "Graphic Design", "Media Studies", "Computer Science"],
        "interests": ["Art, design, drawing & creative work", "Photography, videography & visual storytelling", "Social media, content creation, marketing & trends", "Fashion, beauty, styling & lifestyle"],
        "keywords": ["design", "creative", "art", "visual", "branding", "content"],
        "environment": ["Creative / relaxed vibe", "Remote / from home", "Team-focused", "Independent working"],
        "values": ["Creative freedom", "Learning new skills", "Good work-life balance", "Making an impact"],
        "levels": [3, 4, 5, 6],
        "routes": ["University", "Advanced Apprenticeship (Level 3)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)"],
        "skills_to_build": ["Adobe Creative Suite", "Typography", "Branding", "UI design", "Visual communication"]
    },
    {
        "name": "Marketing Executive",
        "industries": ["Marketing, Advertising, PR & Communications", "Creative, Media, Design, Film & Journalism"],
        "subjects": ["Business Studies", "Media Studies", "English Language", "Art & Design"],
        "interests": ["Social media, content creation, marketing & trends", "Writing, journalism, blogging & content creation", "Business ideas, entrepreneurship & starting projects", "Photography, videography & visual storytelling"],
        "keywords": ["creative", "marketing", "social", "media", "writing", "business", "communication"],
        "environment": ["Creative / relaxed vibe", "Professional office setting", "Fast-paced & busy", "Team-focused", "Customer-facing"],
        "values": ["Creative freedom", "Fast career progression", "Working with people", "Making an impact", "Learning new skills"],
        "levels": [3, 4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)", "Advanced Apprenticeship (Level 3)"],
        "skills_to_build": ["Social media", "Copywriting", "Analytics", "Campaign planning", "Communication"]
    },
    {
        "name": "Lawyer / Solicitor",
        "industries": ["Law, Legal Services, Politics & Government"],
        "subjects": ["English Language", "English Literature", "History", "Law", "Philosophy & Ethics"],
        "interests": ["Debating, politics, current affairs & discussing ideas", "Writing, journalism, blogging & content creation", "Reading, learning & discovering new things"],
        "keywords": ["debating", "research", "writing", "argument", "communication", "analysis", "law"],
        "environment": ["Professional office setting", "Fast-paced & busy", "Team-focused", "Independent working", "Customer-facing"],
        "values": ["High earning potential", "Fast career progression", "Making an impact", "Working with people", "Learning new skills"],
        "levels": [6, 7],
        "routes": ["University"],
        "skills_to_build": ["Legal research", "Writing", "Public speaking", "Critical thinking", "Negotiation"]
    },
    {
        "name": "Teacher",
        "industries": ["Education, Teaching & Training"],
        "subjects": ["Maths", "English Language", "English Literature", "Biology", "Chemistry", "Physics", "Computer Science", "History", "Geography"],
        "interests": ["Teaching, explaining, tutoring & supporting others", "Helping people, mentoring, charity & community work", "Reading, learning & discovering new things"],
        "keywords": ["teaching", "communication", "helping", "leadership", "patience", "explaining", "people"],
        "environment": ["Customer-facing", "Team-focused", "Professional office setting", "Fast-paced & busy"],
        "values": ["Helping people", "Making an impact", "Job security", "Working with people", "Learning new skills"],
        "levels": [3, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)"],
        "skills_to_build": ["Public speaking", "Lesson planning", "Communication", "Leadership", "Subject knowledge"]
    },
    {
        "name": "Project Manager",
        "industries": ["Business, Finance, Accounting & Banking", "Construction, Architecture, Surveying & Property", "Technology, Software Development & IT"],
        "subjects": ["Business Studies", "Economics", "Maths", "Computer Science"],
        "interests": ["Planning events, organising & bringing people together", "Business ideas, entrepreneurship & starting projects", "Building, making, fixing & hands-on creating"],
        "keywords": ["planning", "organisation", "leadership", "teamwork", "communication", "project", "problem-solving"],
        "environment": ["Professional office setting", "Fast-paced & busy", "Team-focused", "Customer-facing"],
        "values": ["Fast career progression", "Working with people", "High earning potential", "Making an impact", "Learning new skills"],
        "levels": [4, 5, 6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)"],
        "skills_to_build": ["Leadership", "Planning", "Communication", "Risk management", "Organisation"]
    },
    {
        "name": "Psychologist",
        "industries": ["Healthcare, Medicine, Nursing & Mental Health", "Education, Teaching & Training"],
        "subjects": ["Psychology", "Biology", "Maths", "English Language"],
        "interests": ["Helping people, mentoring, charity & community work", "Science experiments, research & discovering new things", "Teaching, explaining, tutoring & supporting others"],
        "keywords": ["psychology", "research", "people", "helping", "communication", "empathy", "analysis"],
        "environment": ["Customer-facing", "Professional office setting", "Lab / research facility", "Team-focused"],
        "values": ["Helping people", "Making an impact", "Learning new skills", "Working with people"],
        "levels": [6, 7],
        "routes": ["University"],
        "skills_to_build": ["Research", "Statistics", "Communication", "Critical thinking", "Psychology"]
    },
    {
        "name": "Digital Marketer / Social Media Manager",
        "industries": ["Marketing, Advertising, PR & Communications", "Creative, Media, Design, Film & Journalism"],
        "subjects": ["Media Studies", "Business Studies", "English Language", "Art & Design"],
        "interests": ["Social media, content creation, marketing & trends", "Writing, journalism, blogging & content creation", "Photography, videography & visual storytelling", "Business ideas, entrepreneurship & starting projects"],
        "keywords": ["social", "media", "content", "marketing", "creative", "writing", "communication"],
        "environment": ["Creative / relaxed vibe", "Remote / from home", "Team-focused", "Fast-paced & busy"],
        "values": ["Creative freedom", "Good work-life balance", "Fast career progression", "Learning new skills"],
        "levels": [3, 4, 5, 6],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)", "Advanced Apprenticeship (Level 3)"],
        "skills_to_build": ["Social media strategy", "Content creation", "Analytics", "Copywriting", "Marketing"]
    },
    {
        "name": "Architect",
        "industries": ["Construction, Architecture, Surveying & Property", "Creative, Media, Design, Film & Journalism"],
        "subjects": ["Maths", "Art & Design", "Graphic Design", "Physics", "Engineering"],
        "interests": ["Art, design, drawing & creative work", "Building, making, fixing & hands-on creating", "Photography, videography & visual storytelling"],
        "keywords": ["design", "art", "building", "maths", "creative", "architecture", "drawing"],
        "environment": ["Creative / relaxed vibe", "Professional office setting", "Working outdoors / on-site", "Team-focused"],
        "values": ["Creative freedom", "Making an impact", "Learning new skills", "Working with people"],
        "levels": [6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)"],
        "skills_to_build": ["CAD", "Technical drawing", "Design", "Mathematics", "Project management"]
    },
    {
        "name": "Environmental Scientist",
        "industries": ["Environment, Sustainability, Green Energy & Conservation", "Science, Research, Biotech & Pharmaceuticals"],
        "subjects": ["Biology", "Chemistry", "Geography", "Physics"],
        "interests": ["Nature, animals, wildlife & the environment", "Science experiments, research & discovering new things", "Reading, learning & discovering new things"],
        "keywords": ["science", "environment", "nature", "research", "biology", "analysis", "sustainability"],
        "environment": ["Lab / research facility", "Working outdoors / on-site", "Independent working", "Team-focused"],
        "values": ["Making an impact", "Learning new skills", "Job security"],
        "levels": [6, 7],
        "routes": ["University", "Degree Apprenticeship (Level 6)", "Degree Apprenticeship (Level 7)"],
        "skills_to_build": ["Research", "Data analysis", "Environmental science", "Fieldwork", "Scientific writing"]
    },
    {
        "name": "Sports Coach",
        "industries": ["Sports, Fitness, Leisure & Nutrition"],
        "subjects": ["PE / Sports Science", "Biology", "Psychology"],
        "interests": ["Sports, fitness, training & outdoor activities", "Teaching, explaining, tutoring & supporting others", "Helping people, mentoring, charity & community work"],
        "keywords": ["sports", "fitness", "leadership", "teamwork", "motivation", "helping", "communication"],
        "environment": ["Working outdoors / on-site", "Customer-facing", "Team-focused", "Fast-paced & busy"],
        "values": ["Helping people", "Making an impact", "Working with people", "Job security"],
        "levels": [3, 4, 5, 6],
        "routes": ["Advanced Apprenticeship (Level 3)", "Higher Apprenticeship (Level 4)", "Higher Apprenticeship (Level 5)", "University"],
        "skills_to_build": ["Leadership", "Coaching", "Communication", "Sports science", "Motivation"]
    }
]

# ============================================================
# MATCHING FUNCTION — IB SL & HL FAIR MATCHING ✅
# ============================================================
def calculate_match(career):
    score = 0
    reasons = []
    selected_levels = set()

    for item in pathway:
        if "Level 2" in item:
            selected_levels.add(2)
        elif "Level 3" in item or "Standard Level (IB SL)" in item:
            selected_levels.add(3)
        elif "Level 4" in item:
            selected_levels.add(4)
        elif "Level 5" in item:
            selected_levels.add(5)
        elif "Level 6" in item or "University" in item or "Higher Level (IB HL)" in item:
            selected_levels.update([3, 4, 5, 6, 7])
        elif "Level 7" in item:
            selected_levels.add(7)
        elif item in ["A Levels", "T Level", "BTEC (Level 3 / Extended Diploma)", "CTEC", "OCR Cambridge Technical", "School Leaver Programme"]:
            selected_levels.add(3)
        elif item == "Access to HE":
            selected_levels.update([3, 4, 5])

    if not pathway or "Not sure yet" in pathway:
        score += 15
    else:
        if selected_levels.intersection(set(career["levels"])):
            score += 15
            reasons.append("your chosen pathway can lead towards this career")

    if industries and "Not sure yet" not in industries:
        industry_matches = set(industries).intersection(set(career["industries"]))
        if industry_matches:
            score += 20
            reasons.append("your industry interests align strongly with this role")
    else:
        score += 10

    if subjects:
        subject_matches = set(subjects).intersection(set(career["subjects"]))
        if subject_matches:
            subject_score = min(len(subject_matches) * 7, 20)
            score += subject_score
            reasons.append("your subjects are relevant to this career")
    else:
        score += 10

    if interests and "Not sure yet" not in interests:
        interest_matches = set(interests).intersection(set(career["interests"]))
        if interest_matches:
            interest_score = min(len(interest_matches) * 7, 20)
            score += interest_score
            reasons.append("your interests match this career")
    else:
        score += 10

    if skills.strip():
        skill_text = skills.lower()
        keyword_matches = sum(1 for kw in career["keywords"] if kw.lower() in skill_text)
        skill_score = min(keyword_matches * 4, 15)
        score += skill_score
        if keyword_matches:
            reasons.append("some of your skills could transfer well")
    else:
        score += 7

    if environment and "Not sure yet" not in environment:
        env_matches = set(environment).intersection(set(career["environment"]))
        score += min(len(env_matches) * 2, 5)
    else:
        score += 3

    if values and "Not sure yet" not in values:
        val_matches = set(values).intersection(set(career["values"]))
        score += min(len(val_matches) * 2, 5)
    else:
        score += 3

    return min(round(score), 100), reasons

# ============================================================
# GOOGLE SHEETS CONNECTION
# ============================================================
def connect_to_google_sheet():
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
        credentials = Credentials.from_service_account_info(dict(st.secrets["gcp_service_account"]), scopes=scopes)
        client = gspread.authorize(credentials)
        spreadsheet = client.open_by_url(st.secrets["google_sheet_url"])
        return spreadsheet.sheet1
    except Exception as error:
        st.error("There was a problem connecting to the PathPilot response sheet.")
        st.caption("Check that your Streamlit Secrets are configured correctly and that the service account has access to the Google Sheet.")
        return None

# ============================================================
# SAVE RESPONSE
# ============================================================
def save_response(results):
    worksheet = connect_to_google_sheet()
    if worksheet is None:
        return False
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        top_matches = [r["career"]["name"] for r in results[:5]]
        scores = [r["score"] for r in results[:5]]
        row = [
            timestamp, ", ".join(pathway), ", ".join(subjects), skills.strip(),
            ", ".join(interests), ", ".join(industries), ", ".join(environment), ", ".join(values),
            top_matches[0] if len(top_matches) > 0 else "",
            top_matches[1] if len(top_matches) > 1 else "",
            top_matches[2] if len(top_matches) > 2 else "",
            top_matches[3] if len(top_matches) > 3 else "",
            top_matches[4] if len(top_matches) > 4 else "",
            scores[0] if len(scores) > 0 else "",
            scores[1] if len(scores) > 1 else "",
            scores[2] if len(scores) > 2 else "",
            scores[3] if len(scores) > 3 else "",
            scores[4] if len(scores) > 4 else ""
        ]
        worksheet.append_row(row, value_input_option="USER_ENTERED")
        return True
    except Exception:
        st.error("Your results could not be saved right now.")
        return False

# ============================================================
# FIND MY MATCHES
# ============================================================
if st.button("🔍 Find My Career Matches", type="primary", use_container_width=True):
    if not any([pathway, subjects, skills.strip(), interests, industries, environment, values]):
        st.warning("Please answer at least a few questions before finding your matches.")
    else:
        results = []
        for career in CAREERS:
            score, reasons = calculate_match(career)
            results.append({"career": career, "score": score, "reasons": reasons})
        results.sort(key=lambda x: x["score"], reverse=True)
        st.session_state.results = results
        st.session_state.submitted = False

# ============================================================
# DISPLAY RESULTS
# ============================================================
if st.session_state.results:
    top_results = st.session_state.results[:5]
    st.markdown("---")
    st.header("✨ Your PathPilot Results")
    st.write("These matches are based on the information you provided. They are designed to help you explore options — not decide your future for you.")

    for idx, result in enumerate(top_results, start=1):
        medal = ["🥇", "🥈", "🥉"][idx-1] if idx <= 3 else f"{idx}."
        career = result["career"]
        score = result["score"]
        reasons = result["reasons"]

        st.markdown('<div class="career-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([4, 1])
        with col1:
            st.subheader(f"{medal} {career['name']}")
        with col2:
            st.markdown(f'<div class="match-score">{score}%</div><div class="small-text">Match</div>', unsafe_allow_html=True)
        st.progress(score / 100)
        st.markdown("### 💡 Why this could suit you")
        unique_reasons = list(dict.fromkeys(reasons))
        if unique_reasons:
            for reason in unique_reasons[:4]:
                st.write(f"✓ {reason.capitalize()}.")
        else:
            st.write("Your answers show some potential alignment with this career.")
        st.markdown("### 🎓 Possible routes")
        for route in career["routes"]:
            st.write(f"• {route}")
        st.markdown("### 🛠️ Skills worth developing")
        st.write(" • ".join(career["skills_to_build"]))
        st.markdown("</div>", unsafe_allow_html=True)

    # ========================================================
    # SUBMIT RESULTS
    # ========================================================
    st.markdown("---")
    st.subheader("📊 Help us improve PathPilot")
    st.write("Want to help us understand which pathways and careers young people are exploring?")
    st.caption("We don't ask for your name or email address. Your responses are used to understand trends.")

    if not st.session_state.submitted:
        if st.button("📋 Submit My Results", use_container_width=True):
            with st.spinner("Saving your results..."):
                success = save_response(st.session_state.results)
            if success:
                st.session_state.submitted = True
                st.success("✅ Your results have been submitted!")
                st.info("Thank you for helping us improve PathPilot 💛")
            else:
                st.warning("We couldn't save your results right now. You can still use PathPilot normally.")
    else:
        st.success("✅ Your results have already been submitted. Thank you for helping PathPilot! 💛")

# ============================================================
# FOOTER — YOUR SLOGAN
# ============================================================
st.markdown("---")
st.caption("💛 PathPilot — Your path, your playbook. No wrong moves — just what works for YOU.")
