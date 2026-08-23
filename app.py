import streamlit as st
from urllib.parse import urlencode

# ============================================================
# PATHPILOT
# Career & Pathway Matching Platform
# ============================================================

st.set_page_config(
    page_title="PathPilot — Find Your Future",
    page_icon="🚀",
    layout="wide"
)

# ============================================================
# GOOGLE FORM SETTINGS
# ============================================================

# Paste your Google Form VIEWFORM link here.
# Example:
# https://docs.google.com/forms/d/e/XXXXXXXX/viewform

GOOGLE_FORM_LINK = "https://docs.google.com/spreadsheets/d/1XFLfhDqtm8whNvZsAppokGzLf0AAPrgv7fy_y0ENrJQ/edit?gid=0#gid=0/viewform"


# ============================================================
# GOOGLE FORM ENTRY IDs
# ============================================================
#
# IMPORTANT:
# These are NOT question names.
#
# They look something like:
#
# entry.123456789
# entry.987654321
#
# I have left placeholders here because your actual IDs
# depend on YOUR Google Form.
#
# Once you send me your Google Form link + questions,
# these can be filled in properly.
# ============================================================

FORM_ENTRIES = {
    "pathway": "entry.PATHWAY_ID",
    "subjects": "entry.SUBJECTS_ID",
    "skills": "entry.SKILLS_ID",
    "interests": "entry.INTERESTS_ID",
    "industries": "entry.INDUSTRIES_ID",
    "environment": "entry.ENVIRONMENT_ID",
    "values": "entry.VALUES_ID",
    "top_match": "entry.TOP_MATCH_ID",
    "second_match": "entry.SECOND_MATCH_ID",
    "third_match": "entry.THIRD_MATCH_ID",
    "feedback": "entry.FEEDBACK_ID"
}


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.hero {
    padding: 2.5rem;
    border-radius: 22px;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.hero p {
    font-size: 1.15rem;
}

.career-card {
    padding: 1.5rem;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    margin-bottom: 1.5rem;
    background: white;
    box-shadow: 0 4px 14px rgba(0,0,0,0.06);
}

.match-score {
    font-size: 2rem;
    font-weight: bold;
}

.small-text {
    color: #6b7280;
}

.route-box {
    padding: 1rem;
    border-radius: 12px;
    background: #f5f7ff;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<h1>🚀 PathPilot</h1>

<p>
Discover pathways and careers that fit YOU.
</p>

<p>
Explore careers based on your subjects, skills,
interests and goals.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# 1. PATHWAY
# ============================================================

st.subheader("1️⃣ What pathway are you thinking about?")

pathway = st.multiselect(
    "Select all that apply:",
    [
        "A Levels",
        "T Level",
        "BTEC (Level 3 / Extended Diploma)",
        "CTEC",
        "OCR Cambridge Technical",
        "International Baccalaureate (IB)",
        "Degree Apprenticeship",
        "University",
        "Higher Apprenticeship (Level 4/5)",
        "Advanced Apprenticeship (Level 3)",
        "Intermediate Apprenticeship (Level 2)",
        "School Leaver Programme",
        "Access to HE",
        "Not sure yet"
    ]
)


# ============================================================
# 2. SUBJECTS
# ============================================================

st.subheader("2️⃣ What subjects are you studying right now?")

subjects = st.multiselect(
    "Tick all that apply:",
    [
        "Maths",
        "English Language",
        "English Literature",
        "Biology",
        "Chemistry",
        "Physics",
        "Computer Science",
        "IT / Digital Technology",
        "Economics",
        "Business Studies",
        "Psychology",
        "Sociology",
        "History",
        "Geography",
        "French / Spanish / Other Language",
        "Art & Design",
        "Graphic Design",
        "Engineering",
        "Health & Social Care",
        "Law",
        "Media Studies",
        "PE / Sports Science",
        "Music / Music Technology",
        "Drama / Theatre",
        "Philosophy & Ethics",
        "Other"
    ]
)


# ============================================================
# 3. SKILLS
# ============================================================

st.subheader("3️⃣ What are your best skills?")

st.caption(
    "Examples: problem-solving, coding, teamwork, public speaking, "
    "leadership, creativity, data analysis, writing, planning, "
    "research, empathy, negotiation or time management."
)

skills = st.text_area(
    "Type your best skills:",
    placeholder="e.g. coding, problem-solving, teamwork..."
)


# ============================================================
# 4. INTERESTS
# ============================================================

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


# ============================================================
# 5. INDUSTRIES
# ============================================================

st.subheader("5️⃣ Which industries interest you the most?")

industries = st.multiselect(
    "Pick multiple:",
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


# ============================================================
# 6. WORK ENVIRONMENT
# ============================================================

st.subheader("6️⃣ What kind of work environment do you prefer?")

environment = st.multiselect(
    "Select all that fit:",
    [
        "Professional office setting",
        "Fast-paced & busy",
        "Creative / relaxed vibe",
        "Working outdoors / on-site",
        "Lab / research facility",
        "Remote / from home",
        "Team-focused",
        "Independent working",
        "Customer-facing",
        "Not sure yet"
    ]
)


# ============================================================
# 7. VALUES
# ============================================================

st.subheader("7️⃣ What matters most to you?")

values = st.multiselect(
    "Pick your top priorities:",
    [
        "High earning potential",
        "Job security",
        "Creative freedom",
        "Helping people",
        "Fast career progression",
        "Good work-life balance",
        "Learning new skills",
        "Making an impact",
        "Working with people",
        "Not sure yet"
    ]
)


# ============================================================
# CAREER DATABASE
# ============================================================

CAREERS = [

    {
        "name": "Software Engineer",

        "levels": ["level3", "degree"],

        "industries": [
            "Technology, Software Development & IT"
        ],

        "subjects": [
            "Computer Science",
            "Maths",
            "Physics",
            "IT / Digital Technology"
        ],

        "interests": [
            "Coding, programming & software development",
            "Gaming, esports & streaming",
            "Building, making, fixing & hands-on creating",
            "Working with numbers, data, maths & analysing facts"
        ],

        "keywords": [
            "coding",
            "programming",
            "problem-solving",
            "logical",
            "python",
            "software",
            "technology",
            "data",
            "algorithms",
            "building"
        ],

        "environments": [
            "Professional office setting",
            "Fast-paced & busy",
            "Remote / from home",
            "Team-focused",
            "Independent working"
        ],

        "values": [
            "High earning potential",
            "Fast career progression",
            "Learning new skills",
            "Creative freedom",
            "Good work-life balance"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "Python",
            "Git & GitHub",
            "Algorithms",
            "Data structures",
            "Software development"
        ]
    },

    {
        "name": "Data Scientist",

        "levels": ["level3", "degree"],

        "industries": [
            "Technology, Software Development & IT",
            "Science, Research, Biotech & Pharmaceuticals",
            "Business, Finance, Accounting & Banking"
        ],

        "subjects": [
            "Maths",
            "Computer Science",
            "Economics",
            "Physics"
        ],

        "interests": [
            "Working with numbers, data, maths & analysing facts",
            "Science experiments, research & discovering new things",
            "Coding, programming & software development",
            "Reading, learning & discovering new things"
        ],

        "keywords": [
            "data",
            "maths",
            "statistics",
            "analysis",
            "research",
            "coding",
            "python",
            "problem-solving",
            "numbers"
        ],

        "environments": [
            "Professional office setting",
            "Lab / research facility",
            "Remote / from home",
            "Independent working",
            "Team-focused"
        ],

        "values": [
            "High earning potential",
            "Learning new skills",
            "Making an impact",
            "Fast career progression"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship"
        ],

        "develop": [
            "Python",
            "Statistics",
            "SQL",
            "Data visualisation",
            "Machine learning"
        ]
    },

    {
        "name": "Cyber Security Analyst",

        "levels": ["level3", "degree"],

        "industries": [
            "Technology, Software Development & IT",
            "Law Enforcement, Security & Intelligence"
        ],

        "subjects": [
            "Computer Science",
            "Maths",
            "IT / Digital Technology",
            "Physics"
        ],

        "interests": [
            "Coding, programming & software development",
            "Gaming, esports & streaming",
            "Debating, politics, current affairs & discussing ideas",
            "Reading, learning & discovering new things"
        ],

        "keywords": [
            "coding",
            "security",
            "technology",
            "problem-solving",
            "investigation",
            "research",
            "logical",
            "computers"
        ],

        "environments": [
            "Professional office setting",
            "Fast-paced & busy",
            "Remote / from home",
            "Team-focused",
            "Independent working"
        ],

        "values": [
            "High earning potential",
            "Job security",
            "Learning new skills",
            "Making an impact",
            "Fast career progression"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "Networking",
            "Python",
            "Cybersecurity fundamentals",
            "Linux",
            "Threat analysis"
        ]
    },

    {
        "name": "Accountant",

        "levels": ["level3", "degree"],

        "industries": [
            "Business, Finance, Accounting & Banking"
        ],

        "subjects": [
            "Maths",
            "Economics",
            "Business Studies"
        ],

        "interests": [
            "Working with numbers, data, maths & analysing facts",
            "Business ideas, entrepreneurship & starting projects",
            "Reading, learning & discovering new things"
        ],

        "keywords": [
            "numbers",
            "maths",
            "finance",
            "analysis",
            "organisation",
            "detail",
            "business",
            "economics"
        ],

        "environments": [
            "Professional office setting",
            "Fast-paced & busy",
            "Team-focused",
            "Independent working"
        ],

        "values": [
            "High earning potential",
            "Job security",
            "Fast career progression",
            "Learning new skills",
            "Good work-life balance"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "School Leaver Programme",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "Financial analysis",
            "Excel",
            "Accounting principles",
            "Communication",
            "Attention to detail"
        ]
    },

    {
        "name": "Business Analyst",

        "levels": ["level3", "degree"],

        "industries": [
            "Business, Finance, Accounting & Banking",
            "Technology, Software Development & IT"
        ],

        "subjects": [
            "Maths",
            "Economics",
            "Business Studies",
            "Computer Science"
        ],

        "interests": [
            "Business ideas, entrepreneurship & starting projects",
            "Working with numbers, data, maths & analysing facts",
            "Planning events, organising & bringing people together",
            "Coding, programming & software development"
        ],

        "keywords": [
            "analysis",
            "business",
            "problem-solving",
            "data",
            "organisation",
            "communication",
            "research",
            "planning"
        ],

        "environments": [
            "Professional office setting",
            "Team-focused",
            "Fast-paced & busy",
            "Independent working"
        ],

        "values": [
            "High earning potential",
            "Fast career progression",
            "Learning new skills",
            "Working with people",
            "Good work-life balance"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "Excel",
            "Data analysis",
            "Presentation skills",
            "Business strategy",
            "Stakeholder communication"
        ]
    },

    {
        "name": "Civil Engineer",

        "levels": ["level3", "degree"],

        "industries": [
            "Engineering — Mechanical, Electrical, Civil & Aerospace",
            "Construction, Architecture, Surveying & Property"
        ],

        "subjects": [
            "Maths",
            "Physics",
            "Engineering",
            "Geography"
        ],

        "interests": [
            "Building, making, fixing & hands-on creating",
            "Working with numbers, data, maths & analysing facts",
            "Science experiments, research & discovering new things"
        ],

        "keywords": [
            "maths",
            "engineering",
            "building",
            "design",
            "problem-solving",
            "physics",
            "construction"
        ],

        "environments": [
            "Working outdoors / on-site",
            "Professional office setting",
            "Team-focused",
            "Fast-paced & busy"
        ],

        "values": [
            "High earning potential",
            "Job security",
            "Making an impact",
            "Learning new skills"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "CAD",
            "Engineering mathematics",
            "Project management",
            "Structural principles",
            "Technical drawing"
        ]
    },

    {
        "name": "Doctor / Medical Practitioner",

        "levels": ["degree"],

        "industries": [
            "Healthcare, Medicine, Nursing & Mental Health"
        ],

        "subjects": [
            "Biology",
            "Chemistry",
            "Maths",
            "Physics"
        ],

        "interests": [
            "Science experiments, research & discovering new things",
            "Helping people, mentoring, charity & community work",
            "Reading, learning & discovering new things"
        ],

        "keywords": [
            "biology",
            "science",
            "research",
            "helping",
            "people",
            "communication",
            "problem-solving"
        ],

        "environments": [
            "Lab / research facility",
            "Fast-paced & busy",
            "Customer-facing",
            "Team-focused"
        ],

        "values": [
            "Helping people",
            "Making an impact",
            "Job security",
            "Learning new skills",
            "Working with people"
        ],

        "routes": [
            "University"
        ],

        "develop": [
            "Biology",
            "Chemistry",
            "Communication",
            "Critical thinking",
            "Research"
        ]
    },

    {
        "name": "Nurse / Midwife",

        "levels": ["level3", "degree"],

        "industries": [
            "Healthcare, Medicine, Nursing & Mental Health"
        ],

        "subjects": [
            "Biology",
            "Health & Social Care",
            "Psychology",
            "Chemistry"
        ],

        "interests": [
            "Helping people, mentoring, charity & community work",
            "Teaching, explaining, tutoring & supporting others",
            "Science experiments, research & discovering new things"
        ],

        "keywords": [
            "helping",
            "people",
            "biology",
            "science",
            "communication",
            "empathy",
            "care"
        ],

        "environments": [
            "Fast-paced & busy",
            "Customer-facing",
            "Team-focused"
        ],

        "values": [
            "Helping people",
            "Making an impact",
            "Job security",
            "Working with people"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship"
        ],

        "develop": [
            "Communication",
            "Biology",
            "Teamwork",
            "Empathy",
            "Decision-making"
        ]
    },

    {
        "name": "Graphic Designer",

        "levels": ["level2", "level3", "degree"],

        "industries": [
            "Creative, Media, Design, Film & Journalism",
            "Marketing, Advertising, PR & Communications"
        ],

        "subjects": [
            "Art & Design",
            "Graphic Design",
            "Media Studies",
            "Computer Science"
        ],

        "interests": [
            "Art, design, drawing & creative work",
            "Photography, videography & visual storytelling",
            "Social media, content creation, marketing & trends",
            "Fashion, beauty, styling & lifestyle"
        ],

        "keywords": [
            "design",
            "creative",
            "art",
            "visual",
            "photoshop",
            "branding",
            "content"
        ],

        "environments": [
            "Creative / relaxed vibe",
            "Remote / from home",
            "Team-focused",
            "Independent working"
        ],

        "values": [
            "Creative freedom",
            "Learning new skills",
            "Good work-life balance",
            "Making an impact"
        ],

        "routes": [
            "University",
            "College / Level 3 qualification",
            "Apprenticeship"
        ],

        "develop": [
            "Adobe Creative Suite",
            "Typography",
            "Branding",
            "UI design",
            "Visual communication"
        ]
    },

    {
        "name": "UX / UI Designer",

        "levels": ["level3", "degree"],

        "industries": [
            "Technology, Software Development & IT",
            "Creative, Media, Design, Film & Journalism"
        ],

        "subjects": [
            "Art & Design",
            "Graphic Design",
            "Computer Science",
            "Media Studies"
        ],

        "interests": [
            "Art, design, drawing & creative work",
            "Coding, programming & software development",
            "Photography, videography & visual storytelling",
            "Building, making, fixing & hands-on creating"
        ],

        "keywords": [
            "design",
            "creative",
            "technology",
            "user",
            "problem-solving",
            "visual",
            "research"
        ],

        "environments": [
            "Creative / relaxed vibe",
            "Professional office setting",
            "Remote / from home",
            "Team-focused"
        ],

        "values": [
            "Creative freedom",
            "Learning new skills",
            "Good work-life balance",
            "Making an impact"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "Figma",
            "User research",
            "Wireframing",
            "Prototyping",
            "Design thinking"
        ]
    },

    {
        "name": "Marketing Executive",

        "levels": ["level3", "degree"],

        "industries": [
            "Marketing, Advertising, PR & Communications",
            "Creative, Media, Design, Film & Journalism"
        ],

        "subjects": [
            "Business Studies",
            "Media Studies",
            "English Language",
            "Art & Design"
        ],

        "interests": [
            "Social media, content creation, marketing & trends",
            "Writing, journalism, blogging & content creation",
            "Business ideas, entrepreneurship & starting projects",
            "Photography, videography & visual storytelling"
        ],

        "keywords": [
            "creative",
            "marketing",
            "social",
            "media",
            "writing",
            "business",
            "communication"
        ],

        "environments": [
            "Creative / relaxed vibe",
            "Professional office setting",
            "Fast-paced & busy",
            "Team-focused",
            "Customer-facing"
        ],

        "values": [
            "Creative freedom",
            "Fast career progression",
            "Working with people",
            "Making an impact",
            "Learning new skills"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "Social media",
            "Copywriting",
            "Analytics",
            "Campaign planning",
            "Communication"
        ]
    },

    {
        "name": "Lawyer / Solicitor",

        "levels": ["degree"],

        "industries": [
            "Law, Legal Services, Politics & Government"
        ],

        "subjects": [
            "English Language",
            "English Literature",
            "History",
            "Law",
            "Philosophy & Ethics"
        ],

        "interests": [
            "Debating, politics, current affairs & discussing ideas",
            "Writing, journalism, blogging & content creation",
            "Reading, learning & discovering new things"
        ],

        "keywords": [
            "debating",
            "research",
            "writing",
            "argument",
            "communication",
            "analysis",
            "law"
        ],

        "environments": [
            "Professional office setting",
            "Fast-paced & busy",
            "Team-focused",
            "Independent working",
            "Customer-facing"
        ],

        "values": [
            "High earning potential",
            "Fast career progression",
            "Making an impact",
            "Working with people",
            "Learning new skills"
        ],

        "routes": [
            "University",
            "Solicitor Apprenticeship"
        ],

        "develop": [
            "Legal research",
            "Writing",
            "Public speaking",
            "Critical thinking",
            "Negotiation"
        ]
    },

    {
        "name": "Teacher / Lecturer",

        "levels": ["level3", "degree"],

        "industries": [
            "Education, Teaching & Training"
        ],

        "subjects": [
            "Maths",
            "English Language",
            "English Literature",
            "Biology",
            "Chemistry",
            "Physics",
            "Computer Science",
            "History",
            "Geography",
            "French / Spanish / Other Language"
        ],

        "interests": [
            "Teaching, explaining, tutoring & supporting others",
            "Helping people, mentoring, charity & community work",
            "Reading, learning & discovering new things"
        ],

        "keywords": [
            "teaching",
            "communication",
            "helping",
            "leadership",
            "patience",
            "explaining",
            "people"
        ],

        "environments": [
            "Customer-facing",
            "Team-focused",
            "Professional office setting",
            "Fast-paced & busy"
        ],

        "values": [
            "Helping people",
            "Making an impact",
            "Job security",
            "Working with people",
            "Learning new skills"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Teacher Training"
        ],

        "develop": [
            "Public speaking",
            "Lesson planning",
            "Communication",
            "Leadership",
            "Subject knowledge"
        ]
    },

    {
        "name": "Project Manager",

        "levels": ["level3", "degree"],

        "industries": [
            "Business, Finance, Accounting & Banking",
            "Construction, Architecture, Surveying & Property",
            "Technology, Software Development & IT"
        ],

        "subjects": [
            "Business Studies",
            "Economics",
            "Maths",
            "Computer Science"
        ],

        "interests": [
            "Planning events, organising & bringing people together",
            "Business ideas, entrepreneurship & starting projects",
            "Building, making, fixing & hands-on creating"
        ],

        "keywords": [
            "planning",
            "organisation",
            "leadership",
            "teamwork",
            "communication",
            "project",
            "problem-solving"
        ],

        "environments": [
            "Professional office setting",
            "Fast-paced & busy",
            "Team-focused",
            "Customer-facing"
        ],

        "values": [
            "Fast career progression",
            "Working with people",
            "High earning potential",
            "Making an impact",
            "Learning new skills"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "develop": [
            "Leadership",
            "Planning",
            "Communication",
            "Risk management",
            "Organisation"
        ]
    },

    {
        "name": "Psychologist",

        "levels": ["degree"],

        "industries": [
            "Healthcare, Medicine, Nursing & Mental Health",
            "Education, Teaching & Training"
        ],

        "subjects": [
            "Psychology",
            "Biology",
            "Maths",
            "English Language"
        ],

        "interests": [
            "Helping people, mentoring, charity & community work",
            "Science experiments, research & discovering new things",
            "Teaching, explaining, tutoring & supporting others"
        ],

        "keywords": [
            "psychology",
            "research",
            "people",
            "helping",
            "communication",
            "empathy",
            "analysis"
        ],

        "environments": [
            "Customer-facing",
            "Professional office setting",
            "Lab / research facility",
            "Team-focused"
        ],

        "values": [
            "Helping people",
            "Making an impact",
            "Learning new skills",
            "Working with people"
        ],

        "routes": [
            "University"
        ],

        "develop": [
            "Research",
            "Statistics",
            "Communication",
            "Critical thinking",
            "Psychology"
        ]
    },

    {
        "name": "Digital Marketer / Social Media Manager",

        "levels": ["level2", "level3", "degree"],

        "industries": [
            "Marketing, Advertising, PR & Communications",
            "Creative, Media, Design, Film & Journalism"
        ],

        "subjects": [
            "Media Studies",
            "Business Studies",
            "English Language",
            "Art & Design"
        ],

        "interests": [
            "Social media, content creation, marketing & trends",
            "Writing, journalism, blogging & content creation",
            "Photography, videography & visual storytelling",
            "Business ideas, entrepreneurship & starting projects"
        ],

        "keywords": [
            "social",
            "media",
            "content",
            "marketing",
            "creative",
            "writing",
            "communication"
        ],

        "environments": [
            "Creative / relaxed vibe",
            "Remote / from home",
            "Team-focused",
            "Fast-paced & busy"
        ],

        "values": [
            "Creative freedom",
            "Good work-life balance",
            "Fast career progression",
            "Learning new skills"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship",
            "Advanced Apprenticeship (Level 3)"
        ],

        "develop": [
            "Social media strategy",
            "Content creation",
            "Analytics",
            "Copywriting",
            "Marketing"
        ]
    },

    {
        "name": "Architect",

        "levels": ["degree"],

        "industries": [
            "Construction, Architecture, Surveying & Property",
            "Creative, Media, Design, Film & Journalism"
        ],

        "subjects": [
            "Maths",
            "Art & Design",
            "Graphic Design",
            "Physics",
            "Engineering"
        ],

        "interests": [
            "Art, design, drawing & creative work",
            "Building, making, fixing & hands-on creating",
            "Photography, videography & visual storytelling"
        ],

        "keywords": [
            "design",
            "art",
            "building",
            "maths",
            "creative",
            "architecture",
            "drawing"
        ],

        "environments": [
            "Creative / relaxed vibe",
            "Professional office setting",
            "Working outdoors / on-site",
            "Team-focused"
        ],

        "values": [
            "Creative freedom",
            "Making an impact",
            "Learning new skills",
            "Working with people"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship"
        ],

        "develop": [
            "CAD",
            "Technical drawing",
            "Design",
            "Mathematics",
            "Project management"
        ]
    },

    {
        "name": "Environmental Scientist",

        "levels": ["level3", "degree"],

        "industries": [
            "Environment, Sustainability, Green Energy & Conservation",
            "Science, Research, Biotech & Pharmaceuticals"
        ],

        "subjects": [
            "Biology",
            "Chemistry",
            "Geography",
            "Physics"
        ],

        "interests": [
            "Nature, animals, wildlife & the environment",
            "Science experiments, research & discovering new things",
            "Reading, learning & discovering new things"
        ],

        "keywords": [
            "science",
            "environment",
            "nature",
            "research",
            "biology",
            "analysis",
            "sustainability"
        ],

        "environments": [
            "Lab / research facility",
            "Working outdoors / on-site",
            "Independent working",
            "Team-focused"
        ],

        "values": [
            "Making an impact",
            "Learning new skills",
            "Job security"
        ],

        "routes": [
            "University",
            "Degree Apprenticeship"
        ],

        "develop": [
            "Research",
            "Data analysis",
            "Environmental science",
            "Fieldwork",
            "Scientific writing"
        ]
    },

    {
        "name": "Sports Coach",

        "levels": ["level2", "level3"],

        "industries": [
            "Sports, Fitness, Leisure & Nutrition"
        ],

        "subjects": [
            "PE / Sports Science",
            "Biology",
            "Psychology"
        ],

        "interests": [
            "Sports, fitness, training & outdoor activities",
            "Teaching, explaining, tutoring & supporting others",
            "Helping people, mentoring, charity & community work"
        ],

        "keywords": [
            "sports",
            "fitness",
            "leadership",
            "teamwork",
            "motivation",
            "helping",
            "communication"
        ],

        "environments": [
            "Working outdoors / on-site",
            "Customer-facing",
            "Team-focused",
            "Fast-paced & busy"
        ],

        "values": [
            "Helping people",
            "Making an impact",
            "Working with people",
            "Job security"
        ],

        "routes": [
            "College / Level 3 qualification",
            "Advanced Apprenticeship (Level 3)",
            "University"
        ],

        "develop": [
            "Leadership",
            "Coaching",
            "Communication",
            "Sports science",
            "Motivation"
        ]
    }
]


# ============================================================
# PATHWAY LEVEL
# ============================================================

DEGREE_LEVELS = {
    "University",
    "Degree Apprenticeship"
}

LEVEL3_PATHWAYS = {
    "A Levels",
    "T Level",
    "BTEC (Level 3 / Extended Diploma)",
    "CTEC",
    "OCR Cambridge Technical",
    "International Baccalaureate (IB)",
    "Advanced Apprenticeship (Level 3)",
    "School Leaver Programme",
    "Access to HE",
    "Higher Apprenticeship (Level 4/5)"
}

LEVEL2_PATHWAYS = {
    "Intermediate Apprenticeship (Level 2)"
}


def determine_user_level(selected_pathways):

    if not selected_pathways:
        return "unknown"

    if "Not sure yet" in selected_pathways:
        return "unknown"

    if any(x in DEGREE_LEVELS for x in selected_pathways):
        return "degree"

    if any(x in LEVEL3_PATHWAYS for x in selected_pathways):
        return "level3"

    if any(x in LEVEL2_PATHWAYS for x in selected_pathways):
        return "level2"

    return "unknown"


# ============================================================
# MATCHING ALGORITHM
# ============================================================

def calculate_match(role, user):

    score = 0
    max_score = 0
    reasons = []

    # --------------------------------------------------------
    # PATHWAY
    # --------------------------------------------------------

    max_score += 15

    if user["level"] == "unknown":
        score += 15

    elif user["level"] in role["levels"]:
        score += 15
        reasons.append(
            "your chosen pathway is compatible with this career"
        )

    # --------------------------------------------------------
    # INDUSTRY
    # --------------------------------------------------------

    if user["industries"]:

        max_score += 20

        matches = set(user["industries"]).intersection(
            role["industries"]
        )

        if matches:

            score += min(
                20,
                len(matches) * 10
            )

            reasons.append(
                "your industry interests align with this role"
            )

    # --------------------------------------------------------
    # SUBJECTS
    # --------------------------------------------------------

    if user["subjects"]:

        max_score += 20

        matches = set(user["subjects"]).intersection(
            role["subjects"]
        )

        if matches:

            score += min(
                20,
                len(matches) * 6
            )

            reasons.append(
                "your subjects are relevant to this career"
            )

    # --------------------------------------------------------
    # INTERESTS
    # --------------------------------------------------------

    if user["interests"]:

        max_score += 20

        matches = set(user["interests"]).intersection(
            role["interests"]
        )

        if matches:

            score += min(
                20,
                len(matches) * 7
            )

            reasons.append(
                "your interests strongly overlap with this career"
            )

    # --------------------------------------------------------
    # SKILLS
    # --------------------------------------------------------

    if user["skills"].strip():

        max_score += 15

        skill_text = user["skills"].lower()

        matches = []

        for keyword in role["keywords"]:

            if keyword.lower() in skill_text:
                matches.append(keyword)

        if matches:

            score += min(
                15,
                len(matches) * 4
            )

            reasons.append(
                "some of your stated skills are relevant to this career"
            )

    # --------------------------------------------------------
    # ENVIRONMENT
    # --------------------------------------------------------

    if user["environment"]:

        max_score += 5

        matches = set(user["environment"]).intersection(
            role["environments"]
        )

        if matches:
            score += 5

    # --------------------------------------------------------
    # VALUES
    # --------------------------------------------------------

    if user["values"]:

        max_score += 5

        matches = set(user["values"]).intersection(
            role["values"]
        )

        if matches:
            score += 5

    # --------------------------------------------------------
    # PERCENTAGE
    # --------------------------------------------------------

    if max_score == 0:
        percentage = 0
    else:
        percentage = round(
            (score / max_score) * 100
        )

    percentage = min(100, percentage)

    return percentage, reasons


# ============================================================
# BUILD GOOGLE FORM URL
# ============================================================

def create_google_form_url(
    pathway,
    subjects,
    skills,
    interests,
    industries,
    environment,
    values,
    results
):

    if (
        not GOOGLE_FORM_LINK
        or GOOGLE_FORM_LINK == "PASTE_YOUR_GOOGLE_FORM_LINK_HERE"
    ):
        return None

    top_match = results[0]["role"]["name"] if len(results) > 0 else ""
    second_match = results[1]["role"]["name"] if len(results) > 1 else ""
    third_match = results[2]["role"]["name"] if len(results) > 2 else ""

    params = {}

    data = {
        FORM_ENTRIES["pathway"]: ", ".join(pathway),
        FORM_ENTRIES["subjects"]: ", ".join(subjects),
        FORM_ENTRIES["skills"]: skills,
        FORM_ENTRIES["interests"]: ", ".join(interests),
        FORM_ENTRIES["industries"]: ", ".join(industries),
        FORM_ENTRIES["environment"]: ", ".join(environment),
        FORM_ENTRIES["values"]: ", ".join(values),
        FORM_ENTRIES["top_match"]: top_match,
        FORM_ENTRIES["second_match"]: second_match,
        FORM_ENTRIES["third_match"]: third_match
    }

    for key, value in data.items():

        if key.startswith("entry.") and not key.endswith("_ID"):
            params[key] = value

    return GOOGLE_FORM_LINK + "?" + urlencode(params)


# ============================================================
# FIND MATCHES
# ============================================================

if st.button(
    "🔍 Find My Career Matches",
    type="primary",
    use_container_width=True
):

    if (
        not pathway
        and not subjects
        and not interests
        and not industries
    ):

        st.warning(
            "Please select at least one pathway, subject, "
            "interest or industry."
        )

    else:

        st.markdown("---")

        st.header("✨ Your PathPilot Results")

        st.caption(
            "Your results are based on the answers you provided. "
            "They are designed to help you explore options, "
            "not tell you what career you must choose."
        )

        user = {
            "level": determine_user_level(pathway),
            "subjects": subjects,
            "skills": skills,
            "interests": interests,
            "industries": industries,
            "environment": environment,
            "values": values
        }

        results = []

        for career in CAREERS:

            percentage, reasons = calculate_match(
                career,
                user
            )

            results.append({
                "role": career,
                "percentage": percentage,
                "reasons": reasons
            })

        results.sort(
            key=lambda x: x["percentage"],
            reverse=True
        )

        top_results = results[:5]

        # ====================================================
        # RESULTS
        # ====================================================

        st.subheader("🏆 Your Top Career Matches")

        for index, result in enumerate(
            top_results,
            start=1
        ):

            career = result["role"]
            percentage = result["percentage"]
            reasons = result["reasons"]

            st.markdown(
                '<div class="career-card">',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns([4, 1])

            with col1:

                if index == 1:
                    st.markdown(
                        f"## 🥇 {career['name']}"
                    )

                elif index == 2:
                    st.markdown(
                        f"## 🥈 {career['name']}"
                    )

                elif index == 3:
                    st.markdown(
                        f"## 🥉 {career['name']}"
                    )

                else:
                    st.markdown(
                        f"## {index}. {career['name']}"
                    )

            with col2:

                st.markdown(
                    f"""
                    <div class="match-score">
                    {percentage}%
                    </div>
                    <div class="small-text">
                    PathPilot Match
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.progress(
                percentage / 100
            )

            # ------------------------------------------------
            # WHY
            # ------------------------------------------------

            st.markdown("### 💡 Why this could suit you")

            unique_reasons = list(
                dict.fromkeys(reasons)
            )

            if unique_reasons:

                for reason in unique_reasons[:4]:

                    st.write(
                        f"✓ {reason.capitalize()}."
                    )

            else:

                st.write(
                    "Your answers show some potential alignment "
                    "with this career."
                )

            # ------------------------------------------------
            # ROUTES
            # ------------------------------------------------

            st.markdown("### 🎓 Possible routes")

            st.write(
                " • ".join(
                    career["routes"]
                )
            )

            # ------------------------------------------------
            # SKILLS
            # ------------------------------------------------

            st.markdown("### 🛠️ Useful skills to develop")

            st.write(
                " • ".join(
                    career["develop"]
                )
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


        # ====================================================
        # FEEDBACK / DATA COLLECTION
        # ====================================================

        st.markdown("---")

        st.subheader(
            "📊 Want to help improve PathPilot?"
        )

        st.write(
            "You can optionally submit your results anonymously. "
            "Your responses help us understand which careers "
            "young people are exploring and improve PathPilot."
        )

        st.caption(
            "No name, email address or other unnecessary personal "
            "information is requested."
        )

        # ====================================================
        # GOOGLE FORM
        # ====================================================

        form_url = create_google_form_url(
            pathway,
            subjects,
            skills,
            interests,
            industries,
            environment,
            values,
            top_results
        )

        if form_url:

            st.link_button(
                "📋 Submit My Results",
                form_url,
                use_container_width=True
            )

        else:

            st.warning(
                "Your Google Form hasn't been connected yet. "
                "Add your Form link and entry IDs at the top of the code."
            )


        # ====================================================
        # EXPLANATION
        # ====================================================

        st.markdown("---")

        st.subheader(
            "🧭 Your results are a starting point"
        )

        st.write(
            "A PathPilot match isn't a prediction of your future. "
            "It's simply a way of connecting your current interests, "
            "skills and preferences with careers you may want to explore."
        )

        st.write(
            "Your interests can change, your skills can develop, "
            "and there are often multiple routes into the same career."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "💛 PathPilot — Your path, your playbook. "
    "No wrong moves — just what works for YOU."
)
