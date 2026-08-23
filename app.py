import streamlit as st
from datetime import datetime
import json
import os

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
# 🛡️ FORCE-INITIALISE EVERYTHING — NO MORE CRASH! ✅
# ============================================================
if "results" not in st.session_state:
    st.session_state.results = []  # ← EMPTY LIST, NOT NONE
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "path_preference" not in st.session_state:
    st.session_state.path_preference = None
if "all_submissions" not in st.session_state:
    st.session_state.all_submissions = []

# ============================================================
# PERMANENT STORAGE
# ============================================================
SUBMISSIONS_FILE = "submissions_data.json"
def load_submissions():
    if os.path.exists(SUBMISSIONS_FILE):
        with open(SUBMISSIONS_FILE, "r") as f:
            return json.load(f)
    return []
def save_submissions(data):
    with open(SUBMISSIONS_FILE, "w") as f:
        json.dump(data, f)
if not st.session_state.all_submissions:
    st.session_state.all_submissions = load_submissions()

# ============================================================
# STYLING
# ============================================================
st.markdown("""
    <style>
    .main { padding-top: 1.5rem; }
    .hero {
        padding: 2.5rem; border-radius: 24px; margin-bottom: 2rem;
        background: linear-gradient(135deg, #5B21B6 0%, #7C3AED 100%); color: white;
    }
    .career-card {
        padding: 1.5rem; border-radius: 18px; border: 1px solid #e5e7eb;
        margin-bottom: 1.5rem; background: white;
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    }
    .match-score { font-size: 2rem; font-weight: 700; }
    .uni-option {
        background: #F0F4FF; padding: 1.25rem; border-radius: 14px; margin: 0.75rem 0;
        border-left: 5px solid #7C3AED;
    }
    .app-option {
        background: #FFF7ED; padding: 1.25rem; border-radius: 14px; margin: 0.75rem 0;
        border-left: 5px solid #F97316;
    }
    .reason-box {
        background: #F0FFF4; padding: 1rem; border-radius: 12px; margin: 0.5rem 0;
        border-left: 4px solid #22C55E;
    }
    .level-tag {
        display: inline-block; padding: 0.25rem 0.75rem; border-radius: 20px;
        font-size: 0.85rem; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.25rem;
    }
    .level-2 { background: #E0E7FF; color: #4338CA; }
    .level-3 { background: #C7D2FE; color: #3730A3; }
    .level-4 { background: #A5B4FC; color: #312E81; }
    .level-6 { background: #F97316; color: white; }
    .level-7 { background: #EA580C; color: white; }
    .option-header { font-size: 1.1rem; font-weight: 700; margin-bottom: 0.5rem; }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# 🔒 ADMIN DASHBOARD
# ============================================================
if st.query_params.get("admin") == "yes":
    st.markdown("## 🔐 ADMIN DASHBOARD")
    total = len(st.session_state.all_submissions)
    st.metric("📊 Total Submissions", total)
    if total > 0:
        avg = round(sum(s["top_score"] for s in st.session_state.all_submissions)/total)
        st.metric("📈 Avg Match", f"{avg}%")
        for i, sub in enumerate(reversed(st.session_state.all_submissions), 1):
            st.markdown(f"**#{i}** {sub['time']} | {sub['stage']} | {sub['path_preference']} | {sub['top_match']} ({sub['top_score']}%)")
    st.stop()

# ============================================================
# 🎒 HERO
# ============================================================
st.markdown("""
    <div class="hero">
        <h1>🚀 PathPilot</h1>
        <p>GCSE • A Level • IB • University OR Degree Apprenticeship • Career Changers</p>
        <p>Your path, your playbook. No wrong moves — just what works for YOU.</p>
    </div>
""", unsafe_allow_html=True)

# ============================================================
# 👤 STAGE
# ============================================================
st.subheader("👤 Where are you at right now?")
stage = st.multiselect("Select all that apply:", [
    "🏫 GCSE / Year 9–11 — deciding next steps",
    "📚 A Levels",
    "📘 IB — Standard Level (SL)",
    "📕 IB — Higher Level (HL)",
    "🔧 T Level / BTEC / College",
    "🛠️ Apprenticeship (Level 2–5) — already started",
    "🎓 Degree Apprenticeship (Level 6–7) — already started",
    "🏛️ UNDERGRADUATE — First Year",
    "🏛️ UNDERGRADUATE — Second Year",
    "🏛️ UNDERGRADUATE — Final Year",
    "🎓 POSTGRADUATE — Master's / MA / MSc",
    "🔄 Graduated — exploring options",
    "💼 Working — career change",
    "❓ Not sure yet"
])

# ============================================================
# 🎯 THE KEY QUESTION
# ============================================================
st.subheader("🎓 What route are you interested in?")
st.caption("💛 We'll show you exactly what YOU want to see!")
path_preference = st.radio("Choose one:", [
    "🎓 I want to go to UNIVERSITY first",
    "🛠️ I want to do an APPRENTICESHIP (earn while I learn)",
    "🔄 Show me BOTH options — I want to compare them",
    "❓ I'm NOT SURE yet — show me everything!"
])

# ============================================================
# 1️⃣ SUBJECTS
# ============================================================
st.subheader("1️⃣ What subjects / courses are you studying?")
st.caption("Include your degree modules if you're at university!")
subjects = st.multiselect("Tick all that apply:", [
    "Maths", "Further Maths", "English Language", "English Literature",
    "Biology", "Chemistry", "Physics", "Combined Science",
    "Computer Science", "Data Science", "AI / Machine Learning", "Cybersecurity",
    "Engineering — General", "Mechanical Engineering", "Electrical Engineering", "Civil Engineering",
    "Economics", "Business Studies", "Accounting / Finance", "Marketing",
    "Psychology", "Sociology", "Politics / International Relations", "Law",
    "Medicine / Biomedical Science", "Nursing", "Pharmacy", "Health & Social Care",
    "History", "Geography", "Philosophy & Ethics", "Religious Studies",
    "French", "Spanish", "German", "Other Language",
    "Art & Design", "Media / Film / Journalism", "Photography", "Digital Media",
    "Education", "Drama / Theatre Studies",
    "Other — not listed"
])

# ============================================================
# 2️⃣ SKILLS
# ============================================================
st.subheader("2️⃣ What are your BEST skills?")
st.caption("💛 Skills like problem-solving, communication & creativity are valuable in EVERY sector!")
skills = st.text_area("List your skills 💪:", placeholder="e.g. problem-solving, communication, research, writing, creativity...")

# ============================================================
# 3️⃣ INTERESTS
# ============================================================
st.subheader("3️⃣ What do you ENJOY?")
interests = st.multiselect("Pick all that match:", [
    "⚖️ Law, justice & debating", "📖 Reading, writing & research",
    "💻 Coding & software development", "🤖 AI & technology", "📊 Data & problem-solving",
    "🔬 Science, experiments & research", "🏥 Helping people & healthcare",
    "💰 Finance, business & economics", "🎨 Design, creativity & visual arts",
    "🎬 Content creation, video & media", "📱 Social media & digital trends",
    "🏗️ Building, engineering & design", "🌍 Environment & sustainability",
    "🎓 Teaching, mentoring & explaining", "📈 Politics, policy & current affairs",
    "🍀 Hospitality, events & customer service", "🚀 Entrepreneurship & starting businesses",
    "❓ Not sure yet"
])

# ============================================================
# 4️⃣ INDUSTRIES
# ============================================================
st.subheader("4️⃣ Which industries interest you MOST?")
st.caption("⚠️ We will ONLY show roles from the industries you pick. Be specific!")
industries = st.multiselect("Select industries 🎯:", [
    "⚖️ LAW — Solicitor, Barrister, Legal Executive, Compliance, Paralegal",
    "💻 TECHNOLOGY — Software Dev, Data Science, Cybersecurity, AI, Web Dev",
    "🏥 HEALTHCARE — Doctor, Nurse, Paramedic, Pharmacist, Researcher",
    "💰 FINANCE — Banking, Investment, Accounting, Financial Analyst, Tax",
    "🏗️ ENGINEERING — Civil, Mechanical, Electrical, Aerospace, Structural",
    "🎬 CREATIVE & MEDIA — Content Creator, Social Media, UX, Design, Film, Journalism",
    "📚 EDUCATION — Teacher, Lecturer, Researcher, Academic, Tutor",
    "🌍 ENVIRONMENT — Sustainability, Conservation, Climate Science, Ecology",
    "🏛️ PUBLIC SERVICES — Civil Service, Police, Government, Policy",
    "🏨 HOSPITALITY & EVENTS — Management, Events, Tourism, Food & Beverage",
    "🚗 TRANSPORT & LOGISTICS — Aviation, Logistics, Supply Chain, Transport Planning",
    "🏠 PROPERTY — Surveyor, Architect, Estate Agent, Construction Management",
    "❓ Not sure yet — show me everything"
])

# ============================================================
# 5️⃣ WORK ENVIRONMENT
# ============================================================
st.subheader("5️⃣ What work style fits you best?")
environment = st.multiselect("Select all:", [
    "🏢 Professional office", "🏠 Remote / Hybrid", "🔬 Lab / Courtroom / Studio",
    "🤝 Meeting people & client-facing", "🧑‍💻 Independent work & focus",
    "⚡ Fast-paced & dynamic", "📚 Quiet & research-focused",
    "🎨 Creative & visual", "💰 Earning while I learn",
    "❓ Not sure yet"
])

# ============================================================
# 📚 CAREER DATABASE
# ============================================================
CAREERS = [
    {
        "industry": "🎬 CREATIVE & MEDIA — Content Creator, Social Media, UX, Design, Film, Journalism",
        "name": "Content Creator / Digital Creator",
        "desc": "Build an audience, create video, social media, podcasts — shape culture & build brands online",
        "required_subjects": ["Media / Film / Journalism", "Art & Design", "English Language", "Digital Media", "Marketing"],
        "required_interests": ["🎬 Content creation, video & media", "📱 Social media & digital trends", "🎨 Design, creativity & visual arts"],
        "key_skills": ["creativity", "video editing", "storytelling", "social media", "communication", "self-management", "problem-solving"],
        "uni_undergrad": ["Digital Media & Production", "Media & Communications", "Journalism", "Film Production", "Digital Marketing"],
        "uni_postgrad": ["MA Digital Media", "MA Creative Media Practice", "MA Social Media & Communications"],
        "uni_route": "A Levels → Media/Creative Degree (3 yrs) → Build Portfolio → Freelance/Agency/Own Channel",
        "app_levels": ["Level 3 (Creative Media)", "Level 4 (Digital Marketer)", "Level 6 (Digital Media Degree Apprenticeship)"],
        "app_route": "A Levels → Digital Media/Content Creator Apprenticeship → Build Portfolio → Full-Time/Own Business — PAID • NO FEES",
        "app_extra": "Level 6 = full degree equivalent — earn while you build your brand!",
        "skills_build": ["Video Editing", "Social Media Strategy", "Copywriting", "Content Planning", "Visual Design"]
    },
    {
        "industry": "💻 TECHNOLOGY — Software Dev, Data Science, Cybersecurity, AI, Web Dev",
        "name": "Software Engineer",
        "desc": "Build apps, websites, systems — the backbone of the digital world",
        "required_subjects": ["Computer Science", "Maths", "Further Maths", "Physics"],
        "required_interests": ["💻 Coding & software development", "🤖 AI & technology"],
        "key_skills": ["coding", "python", "problem-solving", "logic", "debugging", "teamwork"],
        "uni_undergrad": ["Computer Science", "Software Engineering", "Computer Science with AI"],
        "uni_postgrad": ["MSc Advanced Computer Science", "MSc Software Engineering"],
        "uni_route": "A Levels → Computer Science Degree → Graduate Scheme → Junior Dev",
        "app_levels": ["Level 4 (Software Dev)", "Level 6 (Degree Apprenticeship)", "Level 7 (Master's Level)"],
        "app_route": "A Levels → Software Developer Degree Apprenticeship → Junior Dev — PAID • DEBT-FREE",
        "app_extra": "Level 7 = Master's equivalent — earn while you specialise in AI/Cloud!",
        "skills_build": ["Python", "JavaScript", "Git", "SQL", "Problem Solving"]
    },
    {
        "industry": "⚖️ LAW — Solicitor, Barrister, Legal Executive, Compliance, Paralegal",
        "name": "Solicitor",
        "desc": "Advise clients, prepare legal documents, manage cases — work in all areas of law",
        "required_subjects": ["Law", "Politics / International Relations", "History", "English Language", "Philosophy & Ethics"],
        "required_interests": ["⚖️ Law, justice & debating", "📖 Reading, writing & research", "📈 Politics, policy & current affairs"],
        "key_skills": ["legal research", "written communication", "attention to detail", "client care", "negotiation", "problem-solving"],
        "uni_undergrad": ["Law (LLB)", "Law with Politics", "Law with Business", "Law with International Relations"],
        "uni_postgrad": ["LPC — Legal Practice Course", "LLM Master of Laws", "MSc Law & Governance"],
        "uni_route": "A Levels → Law Degree (3 yrs) → LPC (1 yr) → Training Contract (2 yrs) → Qualified Solicitor",
        "app_levels": ["Level 3 (Legal Services)", "Level 6 (Solicitor Degree Apprenticeship)", "Level 7 (Solicitor — Master's Level)"],
        "app_route": "A Levels → Solicitor Degree Apprenticeship (Level 6, 4–5 yrs) → Qualified — PAID • NO TUITION FEES",
        "app_extra": "Level 6 = full Bachelor's equivalent — fully funded by employer!",
        "skills_build": ["Legal Research", "Contract Law", "Written Advocacy", "Client Management", "Time Management"]
    },
    {
        "industry": "🏥 HEALTHCARE — Doctor, Nurse, Paramedic, Pharmacist, Researcher",
        "name": "Registered Nurse",
        "desc": "Care for patients, support families — make a real difference every single shift",
        "required_subjects": ["Biology", "Health & Social Care", "Psychology"],
        "required_interests": ["🏥 Helping people & healthcare"],
        "key_skills": ["compassion", "communication", "patience", "teamwork", "problem-solving", "resilience"],
        "uni_undergrad": ["Nursing (Adult/Child/Mental Health)", "Nursing with Foundation Year"],
        "uni_postgrad": ["MSc Advanced Nursing", "Specialist Practitioner Courses"],
        "uni_route": "A Levels → Nursing Degree → NMC Registration → Band 5 Nurse",
        "app_levels": ["Level 5 (Nursing Associate)", "Level 6 (Nursing Degree Apprenticeship)"],
        "app_route": "A Levels → Nursing Degree Apprenticeship (Level 6) → NMC Registered Nurse — PAID • NO TUITION FEES",
        "app_extra": "Start as Level 5 Nursing Associate, progress to Level 6 Registered Nurse — fully funded!",
        "skills_build": ["Empathy", "Patient Care", "Communication", "Clinical Skills", "Time Management"]
    },
    {
        "industry": "💰 FINANCE — Banking, Investment, Accounting, Financial Analyst, Tax",
        "name": "Chartered Accountant",
        "desc": "Manage finances, audit accounts, advise on tax — essential to every organisation",
        "required_subjects": ["Maths", "Accounting / Finance", "Business Studies", "Economics"],
        "required_interests": ["💰 Finance, business & economics"],
        "key_skills": ["attention to detail", "numeracy", "organisation", "integrity", "problem-solving", "analysis"],
        "uni_undergrad": ["Accounting & Finance", "Business & Accounting", "Economics"],
        "uni_postgrad": ["ACA", "ACCA", "CIMA"],
        "uni_route": "A Levels → Degree → ACA/ACCA Training → Qualified Chartered Accountant",
        "app_levels": ["Level 4 (Accounting Technician)", "Level 6 (Degree Apprenticeship)", "Level 7 (ACA/ACCA Integrated)"],
        "app_route": "A Levels → Accountancy Degree Apprenticeship → Qualified — PAID • NO FEES • DEBT-FREE",
        "app_extra": "Level 7 apprenticeships include ACA/ACCA exams — qualify fully while earning!",
        "skills_build": ["Excel", "Financial Reporting", "Tax Knowledge", "Audit Procedures"]
    },
    {
        "industry": "🏗️ ENGINEERING — Civil, Mechanical, Electrical, Aerospace, Structural",
        "name": "Civil Engineer",
        "desc": "Design & build the world we live in — bridges, roads, railways, buildings",
        "required_subjects": ["Maths", "Further Maths", "Physics"],
        "required_interests": ["🏗️ Building, engineering & design", "🌍 Environment & sustainability"],
        "key_skills": ["design", "problem-solving", "maths", "project management", "teamwork"],
        "uni_undergrad": ["Civil Engineering", "Civil & Structural Engineering"],
        "uni_postgrad": ["MSc Civil Engineering", "MSc Sustainable Infrastructure"],
        "uni_route": "A Levels → Civil Engineering Degree → ICE Graduate Scheme → Chartered Engineer",
        "app_levels": ["Level 4 (Technician)", "Level 6 (Degree Apprenticeship)", "Level 7 (Chartered Engineer)"],
        "app_route": "A Levels → Civil Engineering Degree Apprenticeship → Chartered — PAID • NO FEES",
        "app_extra": "Level 7 leads straight to CEng (Chartered Engineer) status!",
        "skills_build": ["CAD", "Maths", "Project Management", "Sustainability Knowledge"]
    }
]

# ============================================================
# 🎯 MATCHING ENGINE
# ============================================================
def calculate_match(career):
    score = 0
    reasons = []
    
    if "❓ Not sure yet — show me everything" not in industries:
        if career["industry"] not in industries:
            return 0, ["❌ Not in your selected industry"]
    
    skill_text = skills.lower()
    transferable_skills = {
        "problem-solving": 5, "problem solving": 5, "communication": 5, "people skills": 5,
        "research": 5, "writing": 5, "creativity": 5, "teamwork": 4, "analysis": 5
    }
    transferable_match = sum(pts for kw, pts in transferable_skills.items() if kw in skill_text)
    if transferable_match > 0:
        score += min(transferable_match, 20)
        reasons.append("✅ Your skills are highly valued here!")
    
    spec_match = sum(1 for kw in career["key_skills"] if kw in skill_text)
    if spec_match > 0:
        score += min(spec_match * 8, 30)
        reasons.append(f"✅ {spec_match}+ key skills match perfectly!")
    
    subject_match = set(subjects).intersection(set(career["required_subjects"]))
    if subject_match:
        score += min(len(subject_match) * 6, 20)
        reasons.append(f"✅ Subjects match: {', '.join(list(subject_match)[:3])}")
    
    interest_match = set(interests).intersection(set(career["required_interests"]))
    if interest_match:
        score += min(len(interest_match) * 6, 20)
        reasons.append(f"✅ Interests match: {', '.join(list(interest_match)[:3])}")
    
    return min(score, 100), reasons

# ============================================================
# 🔍 FIND MATCHES
# ============================================================
if st.button("🔍 Find My Personalised Matches", type="primary", use_container_width=True):
    if not any([subjects, skills.strip(), interests, industries]):
        st.warning("Please answer at least a few questions — this is YOUR future! 💛")
    else:
        results = []
        for c in CAREERS:
            score, reasons = calculate_match(c)
            if score > 0:
                results.append({"career": c, "score": score, "reasons": reasons})
        results.sort(key=lambda x: x["score"], reverse=True)
        st.session_state.results = results
        st.session_state.path_preference = path_preference
        st.rerun()

# ============================================================
# 📊 SHOW RESULTS — ✅ FIXED LINE 518 AREA!
# ============================================================
if len(st.session_state.results) > 0:  # ← THIS IS THE FIXED LINE!
    st.markdown("---")
    st.header("✨ Your Personalised PathPilot Results")
    st.subheader(f"Based on: **{st.session_state.path_preference}**")
    
    for idx, r in enumerate(st.session_state.results[:5], 1):
        medal = ["🥇", "🥈", "🥉"][idx-1] if idx <= 3 else f"{idx}."
        c = r["career"]
        score = r["score"]
        
        st.markdown(f"""
        <div class="career-card">
            <h2>{medal} {c['name']}</h2>
            <div class="match-score">{score}% Match</div>
            <p><em>{c['desc']}</em></p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(score / 100)
        
        st.markdown("### ✅ Why THIS fits YOU:")
        st.markdown('<div class="reason-box">', unsafe_allow_html=True)
        for reason in r["reasons"]:
            st.write(f"• {reason}")
        st.markdown("</div>", unsafe_allow_html=True)
        
        pref = st.session_state.path_preference
        
        if pref == "🎓 I want to go to UNIVERSITY first":
            st.markdown("---")
            st.markdown('<p class="option-header">🎓 YOUR UNIVERSITY OPTION:</p>', unsafe_allow_html=True)
            st.markdown('<div class="uni-option">', unsafe_allow_html=True)
            st.markdown("**📘 Undergraduate Degree:**")
            st.write(" • ".join(c["uni_undergrad"]))
            st.markdown("**🎓 Postgraduate / Master's options:**")
            st.write(" • ".join(c["uni_postgrad"]))
            st.markdown("**🗺️ Full Route:**")
            st.write(c["uni_route"])
            st.markdown("</div>", unsafe_allow_html=True)
        
        elif pref == "🛠️ I want to do an APPRENTICESHIP (earn while I learn)":
            st.markdown("---")
            st.markdown('<p class="option-header">🛠️ YOUR APPRENTICESHIP OPTION:</p>', unsafe_allow_html=True)
            st.markdown('<div class="app-option">', unsafe_allow_html=True)
            if c["app_levels"]:
                st.markdown("**📋 Available Levels:**")
                levels_html = ""
                for lvl in c["app_levels"]:
                    lvl_class = "level-2" if "Level 2" in lvl else "level-3" if "Level 3" in lvl else "level-4" if "Level 4" in lvl else "level-6" if "Level 6" in lvl else "level-7"
                    levels_html += f'<span class="level-tag {lvl_class}">{lvl}</span>'
                st.markdown(levels_html, unsafe_allow_html=True)
            st.markdown("**🗺️ Full Apprenticeship Route:**")
            st.write(c["app_route"])
            if c.get("app_extra"):
                st.markdown(f"💡 *{c['app_extra']}*")
            st.markdown("</div>", unsafe_allow_html=True)
        
        else:
            st.markdown("---")
            st.markdown('<p class="option-header">🔄 BOTH OPTIONS — Compare below!</p>', unsafe_allow_html=True)
            col_uni, col_app = st.columns(2)
            with col_uni:
                st.markdown("#### 🎓 UNIVERSITY OPTION")
                st.markdown('<div class="uni-option">', unsafe_allow_html=True)
                st.markdown("**📘 Undergraduate:**")
                st.write(" • ".join(c["uni_undergrad"]))
                st.markdown("**🎓 Postgraduate:**")
                st.write(" • ".join(c["uni_postgrad"]))
                st.markdown("**🗺️ Route:**")
                st.write(c["uni_route"])
                st.markdown("</div>", unsafe_allow_html=True)
            with col_app:
                st.markdown("#### 🛠️ APPRENTICESHIP OPTION")
                st.markdown('<div class="app-option">', unsafe_allow_html=True)
                if c["app_levels"]:
                    st.markdown("**📋 Levels Available:**")
                    levels_html = ""
                    for lvl in c["app_levels"]:
                        lvl_class = "level-2" if "Level 2" in lvl else "level-3" if "Level 3" in lvl else "level-4" if "Level 4" in lvl else "level-6" if "Level 6" in lvl else "level-7"
                        levels_html += f'<span class="level-tag {lvl_class}">{lvl}</span>'
                    st.markdown(levels_html, unsafe_allow_html=True)
                st.markdown("**🗺️ Route:**")
                st.write(c["app_route"])
                if c.get("app_extra"):
                    st.markdown(f"💡 *{c['app_extra']}*")
                st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("### 🛠️ Skills to Start Building")
        st.write(" • ".join(c["skills_build"]))
        st.markdown("---")
    
    if not st.session_state.submitted:
        st.subheader("📋 Submit your results")
        if st.button("✅ Submit My Results", type="primary", use_container_width=True):
            top = st.session_state.results[0]
            st.session_state.all_submissions.append({
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "stage": ", ".join(stage[:2]),
                "path_preference": st.session_state.path_preference,
                "top_match": top["career"]["name"],
                "top_score": top["score"]
            })
            save_submissions(st.session_state.all_submissions)
            st.session_state.submitted = True
            st.success("✅ Saved anonymously — thank you! 💛")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption("💛 PathPilot — Your path, your playbook. No wrong moves — just what works for YOU.")
