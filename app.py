import streamlit as st
from datetime import datetime

# ==============================================
# 👇👇👇 PASTE YOUR GOOGLE FORM LINK HERE! 👇👇👇
# ==============================================
GOOGLE_FORM_LINK == "PASTE_YOUR_GOOGLE_FORM_LINK_HERE"
# ==============================================

# ------------------------------
# PAGE SETUP
# ------------------------------
st.set_page_config(
    page_title="PathPilot — Find YOUR Perfect Path",
    page_icon="🎯",
    layout="wide"
)

# ------------------------------
# 🌍 ALL-INCLUSIVE CAREERS — FOR EVERY STUDENT!
# GCSE • BTEC • T Level • A-Level • Apprenticeship • Uni
# ------------------------------
CAREERS = [
    # === TECHNOLOGY ===
    {
        "career": "Software Engineer",
        "category": "Technology",
        "subjects": ["Computer Science", "Maths", "IT"],
        "skills": ["Programming", "Problem Solving", "Logical Thinking", "Attention to Detail"],
        "interests": ["coding", "software", "apps", "technology", "building", "systems"],
        "description": "Design, build, test and maintain software applications and systems.",
        "skills_to_develop": ["Python", "JavaScript", "Git", "Data Structures", "SQL"],
        "routes": ["GCSE Pathway", "BTEC IT", "T Level Digital", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Cybersecurity Analyst",
        "category": "Technology",
        "subjects": ["Computer Science", "Maths", "IT"],
        "skills": ["Problem Solving", "Logical Thinking", "Attention to Detail", "Integrity"],
        "interests": ["security", "protection", "networks", "hacking", "safety", "defence"],
        "description": "Protect computer systems and data from cyber threats and attacks.",
        "skills_to_develop": ["Network Security", "Python", "Cryptography", "Risk Assessment"],
        "routes": ["GCSE Pathway", "BTEC IT", "T Level Digital", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Data Scientist",
        "category": "Technology",
        "subjects": ["Maths", "Computer Science", "Statistics"],
        "skills": ["Analytical Skills", "Critical Thinking", "Problem Solving", "Curiosity"],
        "interests": ["data", "numbers", "analysis", "patterns", "ai", "machine learning"],
        "description": "Analyse complex data to find insights and solve real-world problems.",
        "skills_to_develop": ["Python", "SQL", "Statistics", "Machine Learning"],
        "routes": ["BTEC", "T Level", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Web Developer",
        "category": "Technology",
        "subjects": ["Computer Science", "Art", "Design", "IT"],
        "skills": ["Creativity", "Attention to Detail", "Problem Solving", "Design"],
        "interests": ["websites", "design", "ui", "user experience", "visuals", "frontend"],
        "description": "Build, design and maintain websites and web applications.",
        "skills_to_develop": ["HTML/CSS", "JavaScript", "React", "UI Design"],
        "routes": ["GCSE Pathway", "BTEC IT", "T Level Digital", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "IT Support Technician",
        "category": "Technology",
        "subjects": ["Computer Science", "IT"],
        "skills": ["Communication", "Problem Solving", "Patience", "Empathy"],
        "interests": ["helping people", "fixing", "hardware", "tech", "troubleshooting"],
        "description": "Help people and organisations with computer systems and technical issues.",
        "skills_to_develop": ["Troubleshooting", "Networking", "Customer Service"],
        "routes": ["GCSE Pathway", "BTEC IT", "T Level Digital", "Apprenticeship", "A-Level", "University"]
    },
    {
        "career": "Video Game Developer",
        "category": "Technology",
        "subjects": ["Computer Science", "Art", "Design", "IT"],
        "skills": ["Creativity", "Problem Solving", "Storytelling", "Programming"],
        "interests": ["gaming", "games", "creativity", "worldbuilding", "interactive"],
        "description": "Design and code video games — bring worlds and stories to life!",
        "skills_to_develop": ["C#", "Unity", "Game Design", "3D Modelling"],
        "routes": ["GCSE Pathway", "BTEC IT", "T Level Digital", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "UX / UI Designer",
        "category": "Technology",
        "subjects": ["Design", "Art", "IT"],
        "skills": ["Empathy", "Creativity", "User Focus", "Visual Design"],
        "interests": ["people", "design", "experience", "how things feel", "usability"],
        "description": "Design digital products that feel natural, beautiful and easy to use for everyone.",
        "skills_to_develop": ["Figma", "User Research", "Prototyping"],
        "routes": ["GCSE Pathway", "BTEC Art/Design", "T Level Digital", "A-Level", "Degree Apprenticeship", "University"]
    },

    # === LAW & LEGAL ===
    {
        "career": "Solicitor / Lawyer",
        "category": "Law",
        "subjects": ["Law", "English", "History", "Politics"],
        "skills": ["Communication", "Critical Thinking", "Research", "Debate", "Writing"],
        "interests": ["justice", "rules", "rights", "argument", "helping people", "society"],
        "description": "Advise and represent clients in legal matters — interpret and apply the law.",
        "skills_to_develop": ["Legal Research", "Public Speaking", "Negotiation", "Writing"],
        "routes": ["BTEC Law", "T Level Legal", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Paralegal / Legal Assistant",
        "category": "Law",
        "subjects": ["Law", "English", "Business"],
        "skills": ["Organisation", "Attention to Detail", "Research", "Communication"],
        "interests": ["documents", "cases", "law", "organisation", "support"],
        "description": "Support lawyers with research, documents and case preparation — great starting point!",
        "skills_to_develop": ["Legal Research", "Document Management", "Case Prep"],
        "routes": ["GCSE Pathway", "BTEC Law", "T Level Legal", "Apprenticeship", "A-Level", "University"]
    },
    {
        "career": "Human Rights Lawyer",
        "category": "Law",
        "subjects": ["Law", "Politics", "Sociology", "English"],
        "skills": ["Empathy", "Courage", "Research", "Persuasion", "Advocacy"],
        "interests": ["equality", "fairness", "people", "change", "justice", "rights"],
        "description": "Fight for equality and protect people's rights — make a real difference to society.",
        "skills_to_develop": ["International Law", "Advocacy", "Policy"],
        "routes": ["BTEC", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Mediator / Conflict Resolver",
        "category": "Law",
        "subjects": ["Psychology", "Law", "English", "Health & Social Care"],
        "skills": ["Listening", "Neutrality", "Empathy", "Communication", "Patience"],
        "interests": ["resolution", "people", "fairness", "agreement", "peace", "understanding"],
        "description": "Help people resolve disputes without court — find fair solutions together.",
        "skills_to_develop": ["Conflict Resolution", "Active Listening", "Negotiation"],
        "routes": ["GCSE Pathway", "BTEC", "T Level", "A-Level", "Degree Apprenticeship", "University"]
    },

    # === FINANCE & BUSINESS ===
    {
        "career": "Accountant",
        "category": "Finance",
        "subjects": ["Maths", "Business", "Economics"],
        "skills": ["Attention to Detail", "Organisation", "Trustworthiness", "Analytical"],
        "interests": ["numbers", "money", "business", "tax", "reports", "accuracy"],
        "description": "Manage financial records, taxes and budgets for individuals and companies.",
        "skills_to_develop": ["Financial Reporting", "Tax", "Spreadsheets", "Auditing"],
        "routes": ["GCSE Pathway", "BTEC Business", "T Level Management", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Business Manager / Entrepreneur",
        "category": "Business",
        "subjects": ["Business", "Economics", "English"],
        "skills": ["Leadership", "Communication", "Organisation", "Decision Making", "Resilience"],
        "interests": ["business", "leading", "ideas", "growth", "teamwork", "innovation"],
        "description": "Lead teams, run operations or build your own business from scratch.",
        "skills_to_develop": ["Leadership", "Strategy", "Marketing", "Finance"],
        "routes": ["GCSE Pathway", "BTEC Business", "T Level Management", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Human Resources (HR) Manager",
        "category": "Business",
        "subjects": ["Psychology", "Business", "English"],
        "skills": ["Communication", "Empathy", "Organisation", "Conflict Resolution"],
        "interests": ["people", "hiring", "culture", "teams", "development", "support"],
        "description": "Manage hiring, training and wellbeing — make companies great places to work.",
        "skills_to_develop": ["People Management", "Employment Law", "Recruitment"],
        "routes": ["BTEC Business", "T Level Management", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Marketing Manager",
        "category": "Business",
        "subjects": ["Business", "Art", "English", "Psychology"],
        "skills": ["Creativity", "Communication", "Social Skills", "Analytical"],
        "interests": ["creativity", "social media", "branding", "people", "advertising", "trends"],
        "description": "Promote products and brands — connect businesses with their audiences.",
        "skills_to_develop": ["Social Media", "Branding", "Content Creation", "Analytics"],
        "routes": ["GCSE Pathway", "BTEC Business", "T Level Digital", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Supply Chain / Logistics Manager",
        "category": "Business",
        "subjects": ["Business", "Maths", "Geography"],
        "skills": ["Organisation", "Problem Solving", "Planning", "Communication"],
        "interests": ["moving things", "organisation", "global", "delivery", "systems", "planning"],
        "description": "Manage how goods get made, moved and delivered — keep the world running!",
        "skills_to_develop": ["Logistics", "Project Management", "Global Trade"],
        "routes": ["GCSE Pathway", "BTEC Business", "T Level", "A-Level", "Degree Apprenticeship", "University"]
    },

    # === HEALTHCARE & COMMUNITY CARE ===
    {
        "career": "Nurse",
        "category": "Healthcare",
        "subjects": ["Biology", "Chemistry", "Psychology", "Health & Social Care"],
        "skills": ["Empathy", "Patience", "Communication", "Stamina", "Compassion"],
        "interests": ["helping people", "caring", "health", "patients", "support", "wellbeing"],
        "description": "Care for patients, give treatment and support people through illness and recovery.",
        "skills_to_develop": ["Patient Care", "Medical Knowledge", "First Aid"],
        "routes": ["BTEC Health & Social", "T Level Health", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Psychologist / Therapist",
        "category": "Healthcare",
        "subjects": ["Psychology", "Biology", "English"],
        "skills": ["Empathy", "Listening", "Communication", "Patience", "Trust"],
        "interests": ["mind", "behaviour", "helping people", "feelings", "mental health", "understanding"],
        "description": "Understand human behaviour — help people with mental health and wellbeing.",
        "skills_to_develop": ["Psychology", "Active Listening", "Counselling", "Research"],
        "routes": ["BTEC Health & Social", "A-Level", "University"]
    },
    {
        "career": "Midwife",
        "category": "Healthcare",
        "subjects": ["Biology", "Psychology", "Health & Social Care"],
        "skills": ["Empathy", "Calmness", "Communication", "Strength", "Trust"],
        "interests": ["birth", "families", "new life", "support", "care", "people"],
        "description": "Support people through pregnancy and birth — bring new life into the world safely.",
        "skills_to_develop": ["Antenatal Care", "Labour Support", "Postnatal Care"],
        "routes": ["BTEC Health & Social", "T Level Health", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Occupational Therapist",
        "category": "Healthcare",
        "subjects": ["Psychology", "Biology", "Health & Social Care"],
        "skills": ["Creativity", "Empathy", "Problem Solving", "Patience"],
        "interests": ["independence", "everyday life", "ability", "helping people", "adaptation"],
        "description": "Help people live their best lives — overcome barriers to do everyday things.",
        "skills_to_develop": ["Rehabilitation", "Adaptation", "Person-Centred Care"],
        "routes": ["BTEC Health & Social", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Social Worker",
        "category": "Community",
        "subjects": ["Sociology", "Psychology", "English", "Health & Social Care"],
        "skills": ["Empathy", "Resilience", "Advocacy", "Communication", "Bravery"],
        "interests": ["people", "families", "support", "change", "justice", "community"],
        "description": "Stand up for vulnerable people — support families and protect those in need.",
        "skills_to_develop": ["Safeguarding", "Legislation", "Person-Centred Support"],
        "routes": ["BTEC Health & Social", "T Level Health", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Dietitian / Nutritionist",
        "category": "Healthcare",
        "subjects": ["Biology", "Chemistry", "Health"],
        "skills": ["Communication", "Empathy", "Organisation", "Science"],
        "interests": ["food", "health", "wellbeing", "nutrition", "science", "lifestyle"],
        "description": "Help people understand food and health — eat well and feel their best.",
        "skills_to_develop": ["Nutritional Science", "Public Health", "Diet Planning"],
        "routes": ["BTEC Health & Social", "A-Level", "Degree Apprenticeship", "University"]
    },

    # === ENGINEERING, BUILDING & PRACTICAL ===
    {
        "career": "Civil Engineer",
        "category": "Engineering",
        "subjects": ["Maths", "Physics", "Design"],
        "skills": ["Problem Solving", "Design", "Organisation", "Teamwork"],
        "interests": ["building", "construction", "design", "infrastructure", "cities", "structures"],
        "description": "Design and build bridges, roads, buildings and infrastructure that shapes our world.",
        "skills_to_develop": ["Design", "Structural Analysis", "Project Planning"],
        "routes": ["BTEC Engineering", "T Level Construction", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Mechanical Engineer",
        "category": "Engineering",
        "subjects": ["Maths", "Physics", "Design"],
        "skills": ["Problem Solving", "Creativity", "Hands-on", "Design"],
        "interests": ["machines", "engines", "mechanics", "invention", "how things work"],
        "description": "Design and build machines — from cars to robots to spacecraft!",
        "skills_to_develop": ["Mechanics", "Design", "CAD Software"],
        "routes": ["BTEC Engineering", "T Level", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Architect",
        "category": "Engineering",
        "subjects": ["Art", "Maths", "Design", "Physics"],
        "skills": ["Creativity", "Design", "Visual Thinking", "Organisation"],
        "interests": ["design", "buildings", "art", "spaces", "cities", "creativity"],
        "description": "Design beautiful, functional buildings — combine art with engineering!",
        "skills_to_develop": ["Design", "CAD", "Architecture History", "Creativity"],
        "routes": ["BTEC Construction/Art", "A-Level", "University"]
    },
    {
        "career": "Environmental Scientist",
        "category": "Science",
        "subjects": ["Biology", "Chemistry", "Geography"],
        "skills": ["Curiosity", "Research", "Analytical", "Passion"],
        "interests": ["nature", "planet", "climate", "environment", "sustainability", "wildlife"],
        "description": "Study and protect our planet — solve climate change and environmental issues.",
        "skills_to_develop": ["Environmental Science", "Research", "Sustainability"],
        "routes": ["BTEC Applied Science", "T Level Science", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Quantity Surveyor",
        "category": "Construction",
        "subjects": ["Maths", "Business", "Design"],
        "skills": ["Organisation", "Attention to Detail", "Communication", "Problem Solving"],
        "interests": ["building", "costs", "projects", "measurement", "planning", "construction"],
        "description": "Manage the money and contracts for building projects — keep them on budget!",
        "skills_to_develop": ["Cost Management", "Contracts", "Construction Knowledge"],
        "routes": ["BTEC Construction", "T Level Construction", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Town Planner",
        "category": "Construction",
        "subjects": ["Geography", "Art", "Design", "Sociology"],
        "skills": ["Vision", "Organisation", "Communication", "Creativity"],
        "interests": ["cities", "communities", "spaces", "future", "design", "people"],
        "description": "Design how our towns and cities grow — create better places for people to live.",
        "skills_to_develop": ["Urban Design", "Community Engagement", "Policy"],
        "routes": ["BTEC", "A-Level", "Degree Apprenticeship", "University"]
    },

    # === CREATIVE, MEDIA & PERFORMING ===
    {
        "career": "Graphic Designer",
        "category": "Creative",
        "subjects": ["Art", "Design", "IT"],
        "skills": ["Creativity", "Visual Thinking", "Attention to Detail", "Imagination"],
        "interests": ["art", "design", "creativity", "visuals", "branding", "images"],
        "description": "Create visual concepts — design logos, branding, websites and more.",
        "skills_to_develop": ["Photoshop", "Illustrator", "Design Principles"],
        "routes": ["GCSE Pathway", "BTEC Art/Design", "T Level Creative", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Journalist / Reporter",
        "category": "Media",
        "subjects": ["English", "History", "Politics", "Media"],
        "skills": ["Curiosity", "Writing", "Communication", "Confidence", "Research"],
        "interests": ["news", "stories", "people", "current affairs", "writing", "truth"],
        "description": "Research and report news — tell the stories that matter.",
        "skills_to_develop": ["Writing", "Research", "Interviewing", "Reporting"],
        "routes": ["BTEC Media", "T Level Digital", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Teacher / Lecturer",
        "category": "Education",
        "subjects": ["Any Subject", "English"],
        "skills": ["Communication", "Patience", "Empathy", "Organisation", "Passion"],
        "interests": ["helping people", "teaching", "learning", "knowledge", "inspiration", "children"],
        "description": "Inspire the next generation — share your passion and help others grow.",
        "skills_to_develop": ["Subject Knowledge", "Public Speaking", "Lesson Planning"],
        "routes": ["BTEC Education", "T Level Education", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Video Editor",
        "category": "Creative",
        "subjects": ["Media", "Art", "IT"],
        "skills": ["Creativity", "Attention to Detail", "Storytelling", "Patience"],
        "interests": ["video", "film", "editing", "stories", "visuals", "production"],
        "description": "Edit footage into films, videos and shows — shape the story!",
        "skills_to_develop": ["Premiere Pro", "DaVinci Resolve", "Storytelling"],
        "routes": ["GCSE Pathway", "BTEC Media", "T Level Creative", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Copywriter / Content Creator",
        "category": "Creative",
        "subjects": ["English", "Media", "Business"],
        "skills": ["Creativity", "Writing", "Voice", "Adaptability"],
        "interests": ["writing", "words", "stories", "brands", "social media", "communication"],
        "description": "Write words that connect — from ads to articles to social media.",
        "skills_to_develop": ["Writing", "SEO", "Brand Voice"],
        "routes": ["GCSE Pathway", "BTEC Media", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Interpreter / Translator",
        "category": "Language",
        "subjects": ["Modern Languages", "English"],
        "skills": ["Fluency", "Cultural Awareness", "Listening", "Communication"],
        "interests": ["languages", "cultures", "connection", "communication", "people", "world"],
        "description": "Bridge the gap between people — speak and understand the world.",
        "skills_to_develop": ["Fluency", "Cultural Knowledge", "Simultaneous Speaking"],
        "routes": ["GCSE Pathway", "A-Level", "Degree Apprenticeship", "University"]
    },

    # === PUBLIC SERVICE, COMMUNITY & PROTECTIVE ===
    {
        "career": "Police Officer",
        "category": "Public Service",
        "subjects": ["Law", "English", "PE"],
        "skills": ["Responsibility", "Communication", "Confidence", "Calmness"],
        "interests": ["helping people", "community", "safety", "justice", "protection", "law"],
        "description": "Protect the public, uphold the law and keep communities safe.",
        "skills_to_develop": ["Conflict Resolution", "Law Knowledge", "Communication"],
        "routes": ["GCSE Pathway", "BTEC Public Services", "T Level", "Apprenticeship", "A-Level", "Degree Apprenticeship"]
    },
    {
        "career": "Firefighter",
        "category": "Public Service",
        "subjects": ["PE", "Science", "English"],
        "skills": ["Courage", "Teamwork", "Physical Strength", "Calmness", "Empathy"],
        "interests": ["helping people", "emergency", "safety", "protection", "community", "action"],
        "description": "Save lives and protect communities from fire and other emergencies.",
        "skills_to_develop": ["Fire Safety", "Rescue", "First Aid", "Teamwork"],
        "routes": ["GCSE Pathway", "BTEC Public Services", "Apprenticeship", "A-Level", "Degree Apprenticeship"]
    },
    {
        "career": "Civil Servant / Government Official",
        "category": "Public Service",
        "subjects": ["Politics", "English", "History"],
        "skills": ["Organisation", "Responsibility", "Communication", "Integrity"],
        "interests": ["society", "policy", "government", "public", "rules", "community"],
        "description": "Work for the government — help make policies and run public services.",
        "skills_to_develop": ["Policy Making", "Research", "Public Service"],
        "routes": ["BTEC", "T Level", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Charity Fundraiser / Manager",
        "category": "Community",
        "subjects": ["Business", "English", "Sociology"],
        "skills": ["Empathy", "Communication", "Organisation", "Passion", "Resilience"],
        "interests": ["helping people", "causes", "community", "change", "giving", "impact"],
        "description": "Raise money and awareness for good causes — make a real difference.",
        "skills_to_develop": ["Campaigning", "Community Engagement", "Project Management"],
        "routes": ["GCSE Pathway", "BTEC", "T Level", "A-Level", "Degree Apprenticeship", "University"]
    },
    {
        "career": "Project Manager",
        "category": "Business",
        "subjects": ["Business", "Any Subject"],
        "skills": ["Leadership", "Organisation", "Communication", "Problem Solving", "Planning"],
        "interests": ["planning", "leading", "teams", "goals", "organisation", "delivery"],
        "description": "Lead teams and deliver big projects — make things happen on time and on budget.",
        "skills_to_develop": ["Planning", "Leadership", "Agile", "Organisation"],
        "routes": ["BTEC", "T Level", "A-Level", "Degree Apprenticeship", "University"]
    }
]

# ------------------------------
# MAIN APP — FOR EVERY STUDENT!
# ------------------------------
st.title("🎯 PathPilot — Find YOUR Perfect Path")
st.subheader("For EVERYONE — GCSE • BTEC • T Level • A-Level • Apprenticeship • University — there's a path for YOU! 💛🌍")
st.markdown("---")

st.header("👤 Tell us about yourself")
name = st.text_input("What's your name?")

st.subheader("🎓 What qualification path are you doing / considering?")
qual_path = st.selectbox(
    "Pick the one that fits you!",
    [
        "GCSE Pathway",
        "BTEC (any level)",
        "T Level",
        "A-Level",
        "Degree Apprenticeship",
        "University",
        "Exploring all options — not sure yet!"
    ]
)

st.subheader("📚 What subjects do you enjoy / best at?")
subjects_input = st.text_area("Type your subjects — one per line:", 
                              placeholder="Computer Science\nMaths\nEnglish\nHealth & Social Care\nArt\nBusiness\nIT\nPsychology")
user_subjects = [s.strip().lower() for s in subjects_input.split("\n") if s.strip()]

st.subheader("💪 What are your best skills?")
skills_input = st.text_area("What are you good at? — one per line:", 
                           placeholder="Problem Solving\nCreativity\nCommunication\nHelping people\nOrganisation")
user_skills = [s.strip().lower() for s in skills_input.split("\n") if s.strip()]

st.subheader("💡 What interests you most?")
interests_input = st.text_area("What do you love doing? — one per line:", 
                              placeholder="Technology\nHelping people\nBusiness\nArt & Design\nScience\nLaw")
user_interests = [s.strip().lower() for s in interests_input.split("\n") if s.strip()]

# ------------------------------
# CALCULATE MATCHES
# ------------------------------
if st.button("🚀 Find My Perfect Career!", type="primary"):
    if not name:
        st.error("Please enter your name!")
    else:
        st.markdown("---")
        st.header(f"📊 Hi {name} — Your Top Career Matches!")
        st.info(f"🎓 Path selected: **{qual_path}** — showing careers that fit YOUR route! 💛")
        
        user_path = qual_path
        if "Exploring" in qual_path:
            user_path = None
        
        matches = []
        for career in CAREERS:
            score = 0
            max_score = 0
            
            # Path filter
            if user_path:
                path_matched = False
                if user_path in career["routes"]:
                    path_matched = True
                elif user_path == "BTEC (any level)" and any("BTEC" in r for r in career["routes"]):
                    path_matched = True
                elif user_path == "T Level" and any("T Level" in r for r in career["routes"]):
                    path_matched = True
                if not path_matched:
                    continue
            
            # Subject match
            career_subjects = [s.lower() for s in career["subjects"]]
            subject_matches = len(set(user_subjects) & set(career_subjects))
            if career_subjects:
                score += (subject_matches / len(career_subjects)) * 30
            max_score += 30
            
            # Skill match
            career_skills = [s.lower() for s in career["skills"]]
            skill_matches = len(set(user_skills) & set(career_skills))
            if career_skills:
                score += (skill_matches / len(career_skills)) * 35
            max_score += 35
            
            # Interest match
            career_interests = [s.lower() for s in career.get("interests", [])]
            interest_matches = len(set(user_interests) & set(career_interests))
            if career_interests:
                score += (interest_matches / len(career_interests)) * 35
            max_score += 35
            
            percentage = round(score) if max_score > 0 else 0
            matches.append({"career": career, "score": percentage})
        
        matches = sorted(matches, key=lambda x: x["score"], reverse=True)
        
        if not matches:
            st.warning("No matches found — try broadening your options! 💛")
        else:
            for i, match in enumerate(matches[:5], 1):
                career = match["career"]
                score = match["score"]
                color = "🟢" if score >= 70 else "🟡" if score >= 40 else "🔴"
                
                with st.expander(f"{color} #{i} — {career['career']} — {score}% Match", expanded=True):
                    st.write(f"**Category:** {career['category']}")
                    st.write(f"**Match Score:** {score}%")
                    st.write(f"**Description:** {career['description']}")
                    st.write(f"✅ **Available Paths:** {', '.join(career['routes'])}")
                    st.write(f"**Key Subjects:** {', '.join(career['subjects'])}")
                    st.write(f"**Key Skills:** {', '.join(career['skills'])}")
                    st.write(f"**Skills to Develop:** {', '.join(career['skills_to_develop'])}")
        
        # === SUBMIT BUTTON ===
        st.markdown("---")
        st.subheader("📬 Help us improve — submit your results!")
        st.info("Click below to send your answers — it takes 10 seconds!")
        
        if GOOGLE_FORM_LINK != "PASTE_YOUR_GOOGLE_FORM_LINK_HERE":
 ":
            st.markdown(f'<a href="{GOOGLE_FORM_LINK}" target="_blank"><button style="background-color:#4CAF50;color:white;padding:12px 24px;border:none;border-radius:8px;font-size:18px;cursor:pointer;width:100%;">📋 Submit My Results</button></a>', unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please add your Google Form link in the code!")
        
        st.markdown("---")
        st.success(f"Thank you for using PathPilot, {name}! 🎉")
        st.info("💛 Remember: NO path is 'better' — what matters is what fits YOU. Every student belongs here! 🌍✨")
