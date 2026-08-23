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
# STYLING
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1.5rem;
    }

    .hero {
        padding: 2.5rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        background: linear-gradient(
            135deg,
            #667eea 0%,
            #764ba2 100%
        );
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
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.06);
    }

    .match-score {
        font-size: 2rem;
        font-weight: 700;
    }

    .small-text {
        color: #6b7280;
    }

    .section-box {
        padding: 1.2rem;
        border-radius: 15px;
        background: #f7f8ff;
        margin-bottom: 1rem;
    }

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

        <p>
        Discover pathways and careers that fit YOU.
        </p>

        <p>
        Explore your options based on your subjects,
        skills, interests and goals.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# PATHWAYS
# ============================================================

st.subheader("1️⃣ What pathway are you thinking about?")

pathway = st.multiselect(
    "Select all that apply:",
    [
        # Academic
        "A Levels",
        "International Baccalaureate (IB)",

        # Technical
        "T Level",
        "BTEC (Level 3 / Extended Diploma)",
        "CTEC",
        "OCR Cambridge Technical",

        # Apprenticeships
        "Intermediate Apprenticeship (Level 2)",
        "Advanced Apprenticeship (Level 3)",
        "Higher Apprenticeship (Level 4)",
        "Higher Apprenticeship (Level 5)",
        "Degree Apprenticeship (Level 6)",
        "Degree Apprenticeship (Level 7)",

        # Other routes
        "University",
        "School Leaver Programme",
        "Access to HE",

        "Not sure yet"
    ]
)


# ============================================================
# SUBJECTS
# ============================================================

st.subheader("2️⃣ What subjects are you studying right now?")

subjects = st.multiselect(
    "Tick all that apply:",
    [
        "Maths",
        "Further Maths",
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
# SKILLS
# ============================================================

st.subheader("3️⃣ What are your best skills?")

st.caption(
    "Tell us what you're good at. For example: "
    "coding, problem-solving, leadership, teamwork, "
    "public speaking, creativity, organisation, "
    "writing, research, data analysis or planning."
)

skills = st.text_area(
    "Your skills:",
    placeholder="e.g. coding, problem-solving, teamwork..."
)


# ============================================================
# INTERESTS
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
# INDUSTRIES
# ============================================================

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


# ============================================================
# WORK ENVIRONMENT
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
# PRIORITIES
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

        "industries": [
            "Technology, Software Development & IT"
        ],

        "subjects": [
            "Maths",
            "Further Maths",
            "Computer Science",
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
            "software",
            "python",
            "technology",
            "problem-solving",
            "data",
            "algorithms",
            "programming"
        ],

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)",
            "Advanced Apprenticeship (Level 3)"
        ],

        "skills_to_build": [
            "Python",
            "Git & GitHub",
            "Algorithms",
            "Data structures",
            "Software development"
        ]
    },

    {
        "name": "Data Scientist",

        "industries": [
            "Technology, Software Development & IT",
            "Science, Research, Biotech & Pharmaceuticals",
            "Business, Finance, Accounting & Banking"
        ],

        "subjects": [
            "Maths",
            "Further Maths",
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
            "numbers"
        ],

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "skills_to_build": [
            "Python",
            "Statistics",
            "SQL",
            "Data visualisation",
            "Machine learning"
        ]
    },

    {
        "name": "Cyber Security Analyst",

        "industries": [
            "Technology, Software Development & IT",
            "Law Enforcement, Security & Intelligence"
        ],

        "subjects": [
            "Computer Science",
            "Maths",
            "Further Maths",
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
            "computers",
            "networking"
        ],

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)",
            "Advanced Apprenticeship (Level 3)"
        ],

        "skills_to_build": [
            "Networking",
            "Python",
            "Linux",
            "Cybersecurity fundamentals",
            "Threat analysis"
        ]
    },

    {
        "name": "Accountant",

        "industries": [
            "Business, Finance, Accounting & Banking"
        ],

        "subjects": [
            "Maths",
            "Further Maths",
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
            "business",
            "economics"
        ],

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)",
            "School Leaver Programme"
        ],

        "skills_to_build": [
            "Financial analysis",
            "Excel",
            "Accounting principles",
            "Communication",
            "Attention to detail"
        ]
    },

    {
        "name": "Business Analyst",

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

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "skills_to_build": [
            "Excel",
            "Data analysis",
            "Presentation skills",
            "Business strategy",
            "Stakeholder communication"
        ]
    },

    {
        "name": "Civil Engineer",

        "industries": [
            "Engineering — Mechanical, Electrical, Civil & Aerospace",
            "Construction, Architecture, Surveying & Property"
        ],

        "subjects": [
            "Maths",
            "Further Maths",
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

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "skills_to_build": [
            "CAD",
            "Engineering mathematics",
            "Project management",
            "Structural principles",
            "Technical drawing"
        ]
    },

    {
        "name": "Doctor / Medical Practitioner",

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

        "environment": [
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

        "skills_to_build": [
            "Biology",
            "Chemistry",
            "Communication",
            "Critical thinking",
            "Research"
        ]
    },

    {
        "name": "Graphic Designer",

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
            "branding",
            "content"
        ],

        "environment": [
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
            "Advanced Apprenticeship (Level 3)",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "skills_to_build": [
            "Adobe Creative Suite",
            "Typography",
            "Branding",
            "UI design",
            "Visual communication"
        ]
    },

    {
        "name": "Marketing Executive",

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

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)",
            "Advanced Apprenticeship (Level 3)"
        ],

        "skills_to_build": [
            "Social media",
            "Copywriting",
            "Analytics",
            "Campaign planning",
            "Communication"
        ]
    },

    {
        "name": "Lawyer / Solicitor",

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

        "environment": [
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
            "Solicitor Apprenticeship (Level 7)"
        ],

        "skills_to_build": [
            "Legal research",
            "Writing",
            "Public speaking",
            "Critical thinking",
            "Negotiation"
        ]
    },

    {
        "name": "Teacher",

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
            "Geography"
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

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Teacher Training"
        ],

        "skills_to_build": [
            "Public speaking",
            "Lesson planning",
            "Communication",
            "Leadership",
            "Subject knowledge"
        ]
    },

    {
        "name": "Project Manager",

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

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)"
        ],

        "skills_to_build": [
            "Leadership",
            "Planning",
            "Communication",
            "Risk management",
            "Organisation"
        ]
    },

    {
        "name": "Psychologist",

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

        "environment": [
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

        "skills_to_build": [
            "Research",
            "Statistics",
            "Communication",
            "Critical thinking",
            "Psychology"
        ]
    },

    {
        "name": "Digital Marketer / Social Media Manager",

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

        "environment": [
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
            "Degree Apprenticeship (Level 6)",
            "Higher Apprenticeship (Level 4/5)",
            "Advanced Apprenticeship (Level 3)"
        ],

        "skills_to_build": [
            "Social media strategy",
            "Content creation",
            "Analytics",
            "Copywriting",
            "Marketing"
        ]
    },

    {
        "name": "Architect",

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

        "environment": [
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
            "Degree Apprenticeship (Level 6)"
        ],

        "skills_to_build": [
            "CAD",
            "Technical drawing",
            "Design",
            "Mathematics",
            "Project management"
        ]
    },

    {
        "name": "Environmental Scientist",

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

        "environment": [
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
            "Degree Apprenticeship (Level 6)"
        ],

        "skills_to_build": [
            "Research",
            "Data analysis",
            "Environmental science",
            "Fieldwork",
            "Scientific writing"
        ]
    },

    {
        "name": "Sports Coach",

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

        "environment": [
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
            "Advanced Apprenticeship (Level 3)",
            "Higher Apprenticeship (Level 4/5)",
            "University"
        ],

        "skills_to_build": [
            "Leadership",
            "Coaching",
            "Communication",
            "Sports science",
            "Motivation"
        ]
    }
]


# ============================================================
# MATCHING FUNCTION
# ============================================================

def calculate_match(career):

    score = 0
    reasons = []

    # Maximum possible weighting:
    # Pathway = 15
    # Industry = 20
    # Subjects = 20
    # Interests = 20
    # Skills = 15
    # Environment = 5
    # Values = 5
    #
    # Total = 100

    max_score = 100

    # --------------------------------------------------------
    # PATHWAY
    # --------------------------------------------------------

    selected_levels = []

    for item in pathway:

        if "Level 2" in item:
            selected_levels.append(2)

        elif "Level 3" in item:
            selected_levels.append(3)

        elif "Level 4" in item:
            selected_levels.append(4)

        elif "Level 5" in item:
            selected_levels.append(5)

        elif "Level 6" in item:
            selected_levels.append(6)

        elif "Level 7" in item:
            selected_levels.append(7)

        elif item == "University":
            selected_levels.extend([6, 7])

        elif item in [
            "A Levels",
            "T Level",
            "BTEC (Level 3 / Extended Diploma)",
            "CTEC",
            "OCR Cambridge Technical",
            "International Baccalaureate (IB)"
        ]:
            selected_levels.append(3)

    if not pathway or "Not sure yet" in pathway:

        score += 15

    else:

        # If they selected a pathway, we give partial
        # credit rather than assuming a specific career
        # is impossible.

        route_text = " ".join(
            career["routes"]
        ).lower()

        route_match = False

        for level in selected_levels:

            if f"level {level}" in route_text:

                route_match = True
                break

        if "university" in pathway and "university" in route_text:
            route_match = True

        if route_match:

            score += 15

            reasons.append(
                "your chosen pathway can lead towards this career"
            )

    # --------------------------------------------------------
    # INDUSTRIES
    # --------------------------------------------------------

    if industries:

        industry_matches = set(
            industries
        ).intersection(
            career["industries"]
        )

        if industry_matches:

            score += 20

            reasons.append(
                "your industry interests align strongly with this role"
            )

    # --------------------------------------------------------
    # SUBJECTS
    # --------------------------------------------------------

    if subjects:

        subject_matches = set(
            subjects
        ).intersection(
            career["subjects"]
        )

        if subject_matches:

            percentage = min(
                len(subject_matches) * 7,
                20
            )

            score += percentage

            reasons.append(
                "your subjects are relevant to this career"
            )

    # --------------------------------------------------------
    # INTERESTS
    # --------------------------------------------------------

    if interests:

        interest_matches = set(
            interests
        ).intersection(
            career["interests"]
        )

        if interest_matches:

            percentage = min(
                len(interest_matches) * 7,
                20
            )

            score += percentage

            reasons.append(
                "your interests match this career"
            )

    # --------------------------------------------------------
    # SKILLS
    # --------------------------------------------------------

    if skills:

        skill_text = skills.lower()

        keyword_matches = 0

        for keyword in career["keywords"]:

            if keyword.lower() in skill_text:

                keyword_matches += 1

        if keyword_matches:

            score += min(
                keyword_matches * 4,
                15
            )

            reasons.append(
                "some of your skills could transfer well"
            )

    # --------------------------------------------------------
    # ENVIRONMENT
    # --------------------------------------------------------

    if environment:

        environment_matches = set(
            environment
        ).intersection(
            career["environment"]
        )

        if environment_matches:

            score += min(
                len(environment_matches) * 2,
                5
            )

    # --------------------------------------------------------
    # VALUES
    # --------------------------------------------------------

    if values:

        value_matches = set(
            values
        ).intersection(
            career["values"]
        )

        if value_matches:

            score += min(
                len(value_matches) * 2,
                5
            )

    return min(score, 100), reasons


# ============================================================
# GOOGLE SHEETS CONNECTION
# ============================================================

def connect_to_google_sheet():

    try:

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        credentials = Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=scopes
        )

        client = gspread.authorize(credentials)

        spreadsheet = client.open_by_url(
            st.secrets["google_sheet_url"]
        )

        worksheet = spreadsheet.sheet1

        return worksheet

    except Exception as error:

        st.error(
            "There was a problem connecting to the "
            "PathPilot response sheet."
        )

        st.caption(
            "Check your Google Sheet connection and "
            "Streamlit secrets."
        )

        return None


# ============================================================
# SAVE RESPONSE
# ============================================================

def save_response(results):

    worksheet = connect_to_google_sheet()

    if worksheet is None:

        return False

    try:

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        top_matches = [
            result["career"]["name"]
            for result in results[:5]
        ]

        row = [
            timestamp,

            ", ".join(pathway),

            ", ".join(subjects),

            skills,

            ", ".join(interests),

            ", ".join(industries),

            ", ".join(environment),

            ", ".join(values),

            top_matches[0] if len(top_matches) > 0 else "",

            top_matches[1] if len(top_matches) > 1 else "",

            top_matches[2] if len(top_matches) > 2 else "",

            top_matches[3] if len(top_matches) > 3 else "",

            top_matches[4] if len(top_matches) > 4 else "",

            results[0]["score"] if len(results) > 0 else "",
            results[1]["score"] if len(results) > 1 else "",
            results[2]["score"] if len(results) > 2 else ""
        ]

        worksheet.append_row(
            row,
            value_input_option="USER_ENTERED"
        )

        return True

    except Exception:

        st.error(
            "Your results could not be saved."
        )

        return False


# ============================================================
# FIND MY MATCHES
# ============================================================

if st.button(
    "🔍 Find My Career Matches",
    type="primary",
    use_container_width=True
):

    if not any([
        pathway,
        subjects,
        skills,
        interests,
        industries,
        environment,
        values
    ]):

        st.warning(
            "Please answer at least a few questions "
            "before finding your matches."
        )

    else:

        # ----------------------------------------------------
        # CALCULATE RESULTS
        # ----------------------------------------------------

        results = []

        for career in CAREERS:

            score, reasons = calculate_match(
                career
            )

            results.append(
                {
                    "career": career,
                    "score": score,
                    "reasons": reasons
                }
            )

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        top_results = results[:5]

        # ----------------------------------------------------
        # RESULTS HEADER
        # ----------------------------------------------------

        st.markdown("---")

        st.header(
            "✨ Your PathPilot Results"
        )

        st.write(
            "These matches are based on the information "
            "you provided. They are designed to help you "
            "explore options — not decide your future for you."
        )

        # ----------------------------------------------------
        # CAREER CARDS
        # ----------------------------------------------------

        for index, result in enumerate(
            top_results,
            start=1
        ):

            career = result["career"]

            score = result["score"]

            reasons = result["reasons"]

            if index == 1:

                medal = "🥇"

            elif index == 2:

                medal = "🥈"

            elif index == 3:

                medal = "🥉"

            else:

                medal = f"{index}."

            st.markdown(
                '<div class="career-card">',
                unsafe_allow_html=True
            )

            col1, col2 = st.columns(
                [4, 1]
            )

            with col1:

                st.subheader(
                    f"{medal} {career['name']}"
                )

            with col2:

                st.markdown(
                    f"""
                    <div class="match-score">
                    {score}%
                    </div>

                    <div class="small-text">
                    Match
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.progress(
                score / 100
            )

            # ------------------------------------------------
            # WHY THIS MATCH
            # ------------------------------------------------

            st.markdown(
                "### 💡 Why this could suit you"
            )

            if reasons:

                for reason in list(
                    dict.fromkeys(reasons)
                )[:4]:

                    st.write(
                        f"✓ {reason.capitalize()}."
                    )

            else:

                st.write(
                    "Your answers show some potential "
                    "alignment with this career."
                )

            # ------------------------------------------------
            # ROUTES
            # ------------------------------------------------

            st.markdown(
                "### 🎓 Possible routes"
            )

            for route in career["routes"]:

                st.write(
                    f"• {route}"
                )

            # ------------------------------------------------
            # SKILLS
            # ------------------------------------------------

            st.markdown(
                "### 🛠️ Skills worth developing"
            )

            st.write(
                " • ".join(
                    career["skills_to_build"]
                )
            )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

        # ----------------------------------------------------
        # SAVE TO GOOGLE SHEETS
        # ----------------------------------------------------

        st.markdown("---")

        st.subheader(
            "📊 Help us improve PathPilot"
        )

        st.write(
            "Want to help us understand which pathways "
            "and careers young people are exploring?"
        )

        st.caption(
            "Your results are submitted without your "
            "name or email address."
        )

        if st.button(
            "📋 Submit My Anonymous Results",
            use_container_width=True
        ):

            with st.spinner(
                "Saving your results..."
            ):

                success = save_response(
                    results
                )

            if success:

                st.success(
                    "✅ Your results have been submitted!"
                )

                st.info(
                    "Thank you for helping us improve PathPilot 💛"
                )

            else:

                st.warning(
                    "We couldn't save your results right now. "
                    "You can still use PathPilot normally."
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "💛 PathPilot — Your path, your playbook. "
    "No wrong moves — just what works for YOU."
)
