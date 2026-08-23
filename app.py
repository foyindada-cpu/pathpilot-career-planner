import streamlit as st
from datetime import datetime
import pandas as pd

# ------------------------------
# PAGE SETUP
# ------------------------------
st.set_page_config(
    page_title="PathPilot — Career & Education Pathway Planner",
    page_icon="🎯",
    layout="wide"
)

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
# INITIALIZE SESSION STATE TO STORE ALL RESPONSES
# ------------------------------
if "all_responses" not in st.session_state:
    st.session_state.all_responses = []

# ------------------------------
# ADMIN SECTION — HIDDEN FROM USERS
# ------------------------------
def admin_panel():
    st.subheader("🔒 Admin — All Responses")
    st.info("Only you can see this!")
    
    if len(st.session_state.all_responses) == 0:
        st.write("No responses yet.")
    else:
        # Show all responses in a table
        df = pd.DataFrame(st.session_state.all_responses)
        st.dataframe(df, use_container_width=True)
        
        # Download ALL data as CSV
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 DOWNLOAD ALL RESPONSES",
            data=csv,
            file_name=f"PathPilot_All_Responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )

# ------------------------------
# MAIN APP — WHAT USERS SEE
# ------------------------------
st.title("🎯 PathPilot — Career & Education Pathway Planner")
st.subheader("Discover your perfect Degree Apprenticeship or University route!")
st.markdown("---")

# Check if admin mode
admin_mode = st.query_params.get("admin", "") == "pathpilot2026"

if admin_mode:
    admin_panel()
    st.markdown("---")

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
# SUBMIT & SAVE
# ------------------------------
if st.button("🚀 Get My Recommendations!", type="primary"):
    if not name:
        st.error("Please enter your name!")
    else:
        # Save this user's response
        user_data = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Subjects": ", ".join(subjects) if subjects else "Not entered",
            "Skills": ", ".join(skills) if skills else "Not entered",
            "Interests": ", ".join(interests) if interests else "Not entered",
            "Preferred Route": route
        }
        
        # Add to all responses
        st.session_state.all_responses.append(user_data)
        
        st.success("✅ Thank you! Your response has been recorded!")
        
        st.markdown("---")
        st.header(f"📊 Hi {name} — Your Recommendations")
        
        # Calculate matches
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

# ------------------------------
# YOUR SECRET LINK — ONLY YOU KNOW THIS!
# ------------------------------
if not admin_mode:
    st.markdown("---")
    st.caption(f"💡 **Your admin link:** {st.query_params.get('_', '')}?admin=pathpilot2026")
