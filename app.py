import streamlit as st
import json

# ------------------------------
# CAREER DATA
# ------------------------------
PATHWAYS = [
    {
        "career": "Software Engineer",
        "routes": ["Degree Apprenticeship", "University"],
        "subjects": ["Computer Science", "Maths"],
        "skills": ["Programming", "Problem Solving", "Logical Thinking"],
        "description": "Design, develop, test, and maintain software applications and systems.",
        "skills_to_develop": ["Python", "Git and GitHub", "Data Structures and Algorithms", "SQL"]
    },
    {
        "career": "Cybersecurity Analyst",
        "routes": ["Degree Apprenticeship", "University"],
        "subjects": ["Computer Science", "Maths"],
        "skills": ["Problem Solving", "Logical Thinking"],
        "description": "Protect systems and data from cyber threats and breaches.",
        "skills_to_develop": ["Network Security", "Python", "Cryptography", "Risk Assessment"]
    }
]

# ------------------------------
# PAGE SETUP
# ------------------------------
st.set_page_config(
    page_title="PathPilot — Career & Education Pathway Planner",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 PathPilot — Career & Education Pathway Planner")
st.subheader("Discover your perfect Degree Apprenticeship or University route!")
st.markdown("---")

# ------------------------------
# USER INPUTS
# ------------------------------
st.header("👤 Tell us about yourself")

name = st.text_input("What's your name?")

st.subheader("📚 Your Subjects")
subjects_input = st.text_area("Enter your subjects (one per line):", 
                              placeholder="Computer Science\nMaths\nPhysics")
subjects = [s.strip() for s in subjects_input.split("\n") if s.strip()]

st.subheader("💪 Your Skills")
skills_input = st.text_area("Enter your skills (one per line):", 
                           placeholder="Programming\nProblem Solving\nTeamwork")
skills = [s.strip() for s in skills_input.split("\n") if s.strip()]

st.subheader("💡 Your Interests")
interests_input = st.text_area("Enter your career interests (one per line):", 
                              placeholder="Software\nCybersecurity\nAI")
interests = [s.strip() for s in interests_input.split("\n") if s.strip()]

st.subheader("🎓 Preferred Route")
route = st.radio("Which route are you interested in?", 
                 ["Degree Apprenticeship", "University", "Either"])

# ------------------------------
# CALCULATE & SHOW RESULTS
# ------------------------------
if st.button("🚀 Get My Recommendations!", type="primary"):
    if not name:
        st.error("Please enter your name!")
    else:
        st.markdown("---")
        st.header(f"📊 Hi {name} — Your Recommendations")
        
        matches = []
        user_subjects = set(s.lower() for s in subjects)
        user_skills = set(s.lower() for s in skills)
        user_interests = set(i.lower() for i in interests)
        
        for p in PATHWAYS:
            score = max_score = 0
            if route != "Either" and route not in p["routes"]:
                continue
            
            p_subjects = set(s.lower() for s in p["subjects"])
            score += len(user_subjects & p_subjects) * 2
            max_score += len(p["subjects"]) * 2
            
            p_skills = set(s.lower() for s in p["skills"])
            score += len(user_skills & p_skills) * 1.5
            max_score += len(p["skills"]) * 1.5
            
            if any(i in p["career"].lower() for i in user_interests):
                score += 3
            max_score += 3
            
            percent = round((score / max_score) * 100) if max_score > 0 else 50
            matches.append({"pathway": p, "percentage": percent})
        
        matches.sort(key=lambda x: x["percentage"], reverse=True)
        
        for i, m in enumerate(matches, 1):
            p = m["pathway"]
            with st.expander(f"🎯 {i}. {p['career']} — {m['percentage']}% Match", expanded=True):
                st.write(f"**Routes:** {', '.join(p['routes'])}")
                st.write(f"**Description:** {p['description']}")
                st.write(f"**Skills to develop:** {', '.join(p['skills_to_develop'])}")
        
        st.markdown("---")
        st.success(f"Thank you for using PathPilot, {name}! 🎉")
