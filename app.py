import streamlit as st
from datetime import datetime

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
# SESSION STATE — PERMANENT ANONYMOUS SUBMISSIONS
# ============================================================
if "results" not in st.session_state:
    st.session_state.results = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "submissions" not in st.session_state:
    st.session_state.submissions = []  # Only YOU see these

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
        box-shadow: 0 4px 14px rgba(0,0,0,0.06);
    }
    .match-score { font-size: 2rem; font-weight: 700; }
    .small-text { color: #6b7280; }
    .admin-box {
        background: #f0f4ff;
        padding: 1rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# 🔒 SECRET ADMIN DASHBOARD — ONLY YOU SEE THIS
# ============================================================
query_params = st.query_params
if query_params.get("admin") == "yes":
    st.markdown("## 🔐 ADMIN DASHBOARD — YOUR DATA ONLY")
    st.info("✅ No one else sees this — only you!")
    
    total = len(st.session_state.submissions)
    st.metric("📊 Total Submissions", total)
    
    if total > 0:
        avg_score = round(sum(s["top_score"] for s in st.session_state.submissions) / total)
        st.metric("📈 Average Match Score", f"{avg_score}%")
        
        st.markdown("### 📋 All Submissions (Anonymous)")
        for i, sub in enumerate(reversed(st.session_state.submissions), 1):
            st.markdown(f"""
            <div class="admin-box">
            <strong>#{i}</strong> — 🕒 {sub['time']}<br>
            🎓 Stage: {sub['stage']}<br>
            🥇 Top Match: <strong>{sub['top_match']}</strong> ({sub['top_score']}%)<br>
            🏭 Interests: {sub['industries']}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No submissions yet!")
    
    st.markdown("---")
    st.caption("← Remove ?admin=yes from the URL to go back to the main app")
    st.stop()

# ============================================================
# 🎒 MAIN APP — FOR EVERYONE
# ============================================================
st.markdown(
    """
    <div class="hero">
        <h1>🚀 PathPilot</h1>
        <p><strong>For GCSE • A Level • IB • Apprenticeships • University • Degree Apprenticeships • Career Changers</strong></p>
        <p>No matter where you are in life — if you're figuring out your next move, this is for YOU.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# QUESTIONS
# ============================================================
st.subheader("👤 Where are you at right now?")

st.subheader("1️⃣ What stage & pathway are you on?")
pathway = st.multiselect(
    "Select ALL that apply — no matter where you are:",
    [
        "🏫 GCSE / Year 9–11 — deciding next steps",
        "📚 A Levels",
        "📘 IB — Standard Level (SL)",
        "📕 IB — Higher Level (HL)",
        "🔧 T Level",
        "📖 BTEC / CTEC / Cambridge Technical",
        "🛠️ Apprenticeship — Level 2 / Intermediate",
        "🛠️ Apprenticeship — Level 3 / Advanced",
        "🛠️ Apprenticeship — Level 4/5 / Higher",
        "🎓 Degree Apprenticeship — Level 6",
        "🎓 Degree Apprenticeship — Level 7",
        "🏛️ University — Undergraduate",
        "🏛️ University — Postgraduate / Master's",
        "🔄 Graduate / Finished Uni — exploring options",
        "💼 Working — looking for a career change",
        "❓ Not sure yet — still figuring it all out!"
    ]
)

st.subheader("2️⃣ What subjects or qualifications are you studying / have you done?")
st.caption("GCSE, A Level, IB, Degree, College — everything counts!")
subjects = st.multiselect(
    "Tick all that apply:",
    [
        "Maths", "Further Maths", "English Language", "English Literature",
        "Combined Science (GCSE)", "Biology", "Chemistry", "Physics",
        "Computer Science", "IT / Digital Technology", "Data Science",
        "Geography", "History", "Politics", "Citizenship / PSHE",
        "French", "Spanish", "German", "Other Language",
        "Art & Design", "Graphic Design", "Photography", "Textiles", "Fine Art",
        "Music", "Music Technology", "Drama / Theatre", "Dance", "Film / Media",
        "Business Studies", "Economics", "Accounting", "Finance", "Enterprise",
        "Health & Social Care", "Child Development", "Psychology", "Sociology",
        "Food Preparation & Nutrition", "Hospitality & Catering", "Travel & Tourism",
        "Design & Technology", "Engineering", "Electronics", "Construction",
        "PE / Sports Science", "Sports Management", "Nutrition",
        "Law", "Philosophy & Ethics", "Religious Studies",
        "Creative Writing", "Journalism", "Marketing", "Digital Media",
        "Education / Teaching", "Social Work", "Criminology",
        "Other — not listed"
    ]
)

st.subheader("3️⃣ What are your BEST skills?")
st.caption(
    "Everything you're good at — school, work, life, hobbies! "
    "Examples: problem-solving, teamwork, leadership, coding, communication, "
    "organisation, creativity, research, data analysis, public speaking, writing..."
)
skills = st.text_area("Your skills — be proud, list them! 💪:", 
                      placeholder="e.g. good at problem solving, work well in teams, great at communicating, organised, good with numbers...")

st.subheader("4️⃣ What do you ENJOY doing?")
st.caption("Hobbies, passions, things you lose track of time doing — ALL of it matters!")
interests = st.multiselect(
    "Pick ALL that match:",
    [
        "💻 Coding, programming, tech & software development",
        "🎨 Art, design, creativity & making things look good",
        "⚽ Sports, fitness, keeping active & outdoor adventures",
        "🎮 Gaming, esports, streaming & digital content",
        "✍️ Writing, storytelling, blogging & journalism",
        "🔬 Science — experiments, research & discovering how things work",
        "💡 Business ideas, entrepreneurship & starting projects",
        "🤝 Helping people, mentoring, charity & making a difference",
        "👩‍🏫 Teaching, explaining & helping others learn",
        "🔨 Building, making, fixing & hands-on creating",
        "✈️ Travel, cultures, languages & exploring the world",
        "🎵 Music, performing, singing & entertainment",
        "📱 Social media, content creation, marketing & trends",
        "📊 Numbers, data, maths & analysing information",
        "🌿 Nature, animals, wildlife & the environment",
        "🗣️ Debating, politics, current affairs & discussing ideas",
        "🍳 Cooking, baking & food",
        "👗 Fashion, styling & design",
        "📸 Photography, videography & visual storytelling",
        "📋 Planning, organising & bringing people together",
        "📚 Reading, researching & learning new things",
        "❓ Not sure yet — still exploring!"
    ]
)

st.subheader("5️⃣ Which industries or fields interest you MOST?")
industries = st.multiselect(
    "Pick as many as you like — dream big! ✨:",
    [
        "💻 Technology, Software Development, IT & Digital",
        "🏗️ Engineering — Mechanical, Electrical, Civil, Aerospace",
        "🏥 Healthcare, Medicine, Nursing & Mental Health",
        "💰 Business, Finance, Accounting, Banking & Economics",
        "🎬 Creative, Media, Design, Film, Gaming & Journalism",
        "📚 Education, Teaching & Training",
        "⚖️ Law, Legal Services, Politics & Government",
        "🔬 Science, Research, Biotech & Pharmaceuticals",
        "🏃 Sports, Fitness, Leisure & Nutrition",
        "🚔 Public Services — Police, Fire, Ambulance, Military",
        "🌱 Environment, Sustainability, Green Energy & Conservation",
        "🏨 Hospitality, Events, Tourism & Travel",
        "📣 Marketing, Advertising, PR & Communications",
        "🏢 Construction, Architecture, Surveying & Property",
        "✈️ Transport, Logistics, Aviation & Supply Chain",
        "🛍️ Retail, Fashion, Merchandising & Customer Service",
        "📱 Digital Media, Gaming, Animation & VFX",
        "❤️ Charity, Non-Profit & Social Impact",
        "🏭 Manufacturing, Production & Industrial Design",
        "👥 Human Resources, Recruitment & People Management",
        "🎭 Performing Arts, Music Production & Entertainment",
        "🐾 Agriculture, Food Science & Veterinary",
        "⚡ Energy, Renewables & Utilities",
        "❓ Not sure yet — still exploring!"
    ]
)

st.subheader("6️⃣ What kind of work environment do you thrive in?")
environment = st.multiselect(
    "Select ALL that fit you — there's no right or wrong!:",
    [
        "🏢 Professional office setting", "⚡ Fast-paced & busy",
        "🎨 Creative, relaxed & informal vibe", "🏕️ Outdoors / on-site",
        "🔬 Lab, studio or specialist facility", "🏠 Remote / work from home",
        "🤝 Team-focused & collaborative", "🧑‍💻 Independent working",
        "🗣️ Customer-facing / meeting people", "❓ Not sure yet!"
    ]
)

st.subheader("7️⃣ What matters MOST to you in a career?")
values = st.multiselect(
    "Pick your top priorities — what do you actually want? 💛:",
    [
        "💷 Good earning potential", "🛡️ Job security & stability", 
        "🎨 Creative freedom & expression", "🤝 Helping people / making impact", 
        "🚀 Fast career progression", "⚖️ Good work-life balance",
        "📖 Continuous learning & growth", "👥 Working with people", 
        "🏆 Job satisfaction & purpose", "❓ Not sure yet!"
    ]
)

# ============================================================
# CAREER DATABASE
# ============================================================
CAREERS = [
    {
        "name": "Software Engineer / Developer",
        "short_desc": "Build apps, websites, systems — the backbone of the digital world",
        "industries": ["💻 Technology, Software Development, IT & Digital"],
        "subjects": ["Maths", "Further Maths", "Computer Science", "IT / Digital Technology", "Data Science"],
        "interests": ["💻 Coding, programming, tech & software development", "🎮 Gaming, esports, streaming & digital content", "📊 Numbers, data, maths & analysing information"],
        "keywords": ["coding", "programming", "software", "tech", "problem solving", "logic", "development", "algorithms"],
        "environment": ["🏢 Professional office setting", "🤝 Team-focused & collaborative", "🏠 Remote / work from home"],
        "values": ["💷 Good earning potential", "🚀 Fast career progression", "📖 Continuous learning & growth"],
        "levels": [2, 3, 4, 5, 6, 7],
        "routes": [
            "GCSE → BTEC/College → Apprenticeship → Junior Dev",
            "A Level/IB → Degree Apprenticeship → Full-Time Role",
            "University → Graduate Role → Senior Roles",
            "Self-taught → Portfolio → Junior Position"
        ],
        "skills_to_build": ["Python", "HTML/CSS/JS", "Git & GitHub", "Problem Solving", "Communication"]
    },
    {
        "name": "Data Scientist / Analyst",
        "short_desc": "Turn numbers into stories — help businesses make smart decisions",
        "industries": ["💻 Technology, Software Development, IT & Digital", "💰 Business, Finance, Accounting, Banking & Economics"],
        "subjects": ["Maths", "Computer Science", "Data Science", "Economics"],
        "interests": ["📊 Numbers, data, maths & analysing information", "🔬 Science — experiments, research & discovering how things work"],
        "keywords": ["data", "maths", "analysis", "patterns", "insights", "research"],
        "environment": ["🏢 Professional office setting", "🧑‍💻 Independent working", "🏠 Remote / work from home"],
        "values": ["💷 Good earning potential", "📖 Continuous learning & growth"],
        "levels": [3, 4, 5, 6, 7],
        "routes": [
            "A Level/IB → Higher/Degree Apprenticeship → Data Analyst",
            "University → Graduate Scheme → Junior → Senior"
        ],
        "skills_to_build": ["Excel", "Python", "SQL", "Statistics", "Critical Thinking"]
    },
    {
        "name": "Marketing / Social Media Strategist",
        "short_desc": "Tell stories, build brands & connect people with ideas",
        "industries": ["📣 Marketing, Advertising, PR & Communications", "🎬 Creative, Media, Design, Film, Gaming & Journalism"],
        "subjects": ["English Language", "Business Studies", "Media", "Psychology", "Art & Design"],
        "interests": ["📱 Social media, content creation, marketing & trends", "✍️ Writing, storytelling, blogging & journalism", "🎨 Art, design, creativity & making things look good"],
        "keywords": ["creative", "communication", "content", "strategy", "people", "trends", "writing"],
        "environment": ["🎨 Creative, relaxed & informal vibe", "⚡ Fast-paced & busy", "🤝 Team-focused & collaborative"],
        "values": ["🎨 Creative freedom & expression", "🚀 Fast career progression", "👥 Working with people"],
        "levels": [2, 3, 4, 5, 6, 7],
        "routes": [
            "GCSE → Apprenticeship → Junior → Executive",
            "College/Uni → Degree Apprenticeship → Specialist",
            "Portfolio → Freelance → Agency → Senior"
        ],
        "skills_to_build": ["Social Media", "Copywriting", "Analytics", "Creativity", "Communication"]
    },
    {
        "name": "Civil Engineer",
        "short_desc": "Design & build the world we live in — bridges, roads, buildings",
        "industries": ["🏗️ Engineering — Mechanical, Electrical, Civil, Aerospace", "🏢 Construction, Architecture, Surveying & Property"],
        "subjects": ["Maths", "Further Maths", "Physics", "Design & Technology"],
        "interests": ["🔨 Building, making, fixing & hands-on creating", "🔬 Science — experiments, research & discovering how things work"],
        "keywords": ["design", "construction", "maths", "physics", "planning", "practical"],
        "environment": ["🏕️ Outdoors / on-site", "🏢 Professional office setting", "🤝 Team-focused & collaborative"],
        "values": ["🛡️ Job security & stability", "🤝 Helping people / making impact", "💷 Good earning potential"],
        "levels": [3, 4, 5, 6, 7],
        "routes": [
            "GCSE → BTEC → Apprenticeship → Technician → Engineer",
            "A Level/IB → Degree Apprenticeship → Chartered Status",
            "Uni → Master's → Senior / Project Lead"
        ],
        "skills_to_build": ["CAD Design", "Maths & Physics", "Project Management", "Teamwork", "Practical Skills"]
    },
    {
        "name": "Healthcare Professional / Nurse",
        "short_desc": "Care for people, save lives, make a real difference every day",
        "industries": ["🏥 Healthcare, Medicine, Nursing & Mental Health"],
        "subjects": ["Biology", "Chemistry", "Combined Science (GCSE)", "Psychology"],
        "interests": ["🤝 Helping people, mentoring, charity & making a difference", "🔬 Science — experiments, research & discovering how things work"],
        "keywords": ["caring", "people", "health", "empathy", "communication", "patience"],
        "environment": ["⚡ Fast-paced & busy", "🗣️ Customer-facing / meeting people", "🤝 Team-focused & collaborative"],
        "values": ["🤝 Helping people / making impact", "🛡️ Job security & stability", "🏆 Job satisfaction & purpose"],
        "levels": [2, 3, 4, 5, 6, 7],
        "routes": [
            "GCSE → Care Certificate → Apprenticeship → Assistant",
            "A Level/IB → Nursing Degree / Degree Apprenticeship → Registered Nurse",
            "Uni → Master's → Specialist / Advanced Practitioner"
        ],
        "skills_to_build": ["Empathy", "Communication", "Teamwork", "Resilience", "Organisation"]
    },
    {
        "name": "Teacher / Educator",
        "short_desc": "Shape the future — inspire, teach & make a lifelong impact",
        "industries": ["📚 Education, Teaching & Training"],
        "subjects": ["English Language", "Maths", "Biology", "Chemistry", "Physics", "History", "Geography"],
        "interests": ["👩‍🏫 Teaching, explaining & helping others learn", "🤝 Helping people, mentoring, charity & making a difference"],
        "keywords": ["teaching", "people", "communication", "patience", "leadership"],
        "environment": ["🗣️ Customer-facing / meeting people", "🤝 Team-focused & collaborative"],
        "values": ["🤝 Helping people / making impact", "🛡️ Job security & stability", "🏆 Job satisfaction & purpose"],
        "levels": [3, 6, 7],
        "routes": [
            "A Level/IB → Uni + QTS → NQT → Teacher",
            "Degree Apprenticeship → Qualified Teacher",
            "Subject Specialism → Further Education / Lecturing"
        ],
        "skills_to_build": ["Communication", "Public Speaking", "Empathy", "Organisation", "Leadership"]
    },
    {
        "name": "Cyber Security Analyst",
        "short_desc": "Protect people, companies & governments from digital threats",
        "industries": ["💻 Technology, Software Development, IT & Digital", "⚖️ Law, Legal Services, Politics & Government"],
        "subjects": ["Computer Science", "Maths", "IT / Digital Technology"],
        "interests": ["💻 Coding, programming, tech & software development", "🗣️ Debating, politics, current affairs & discussing ideas"],
        "keywords": ["security", "networks", "protection", "investigation", "problem solving"],
        "environment": ["🏢 Professional office setting", "⚡ Fast-paced & busy", "🤝 Team-focused & collaborative"],
        "values": ["🛡️ Job security & stability", "💷 Good earning potential", "🤝 Helping people / making impact"],
        "levels": [3, 4, 5, 6, 7],
        "routes": [
            "GCSE → Advanced Apprenticeship → Junior Role",
            "A Level/IB → Degree Apprenticeship or Uni → Certified Professional",
            "Uni → Master's → Government / Senior Roles"
        ],
        "skills_to_build": ["Networking", "Linux", "Python", "Risk Analysis", "Attention to Detail"]
    },
    {
        "name": "Financial Analyst / Accountant",
        "short_desc": "Manage money, guide decisions — the heartbeat of every organisation",
        "industries": ["💰 Business, Finance, Accounting, Banking & Economics"],
        "subjects": ["Maths", "Further Maths", "Business Studies", "Economics"],
        "interests": ["📊 Numbers, data, maths & analysing information", "💡 Business ideas, entrepreneurship & starting projects"],
        "keywords": ["numbers", "finance", "analysis", "accuracy", "organisation", "business"],
        "environment": ["🏢 Professional office setting", "🤝 Team-focused & collaborative", "🧑‍💻 Independent working"],
        "values": ["💷 Good earning potential", "🛡️ Job security & stability", "🚀 Fast career progression"],
        "levels": [2, 3, 4, 5, 6, 7],
        "routes": [
            "GCSE → Apprenticeship → AAT → Qualified",
            "A Level/IB → Degree Apprenticeship / Uni → ACCA/CIMA",
            "Graduate → Chartered → Senior / Partner"
        ],
        "skills_to_build": ["Excel", "Attention to Detail", "Analysis", "Organisation", "Communication"]
    }
]

# ============================================================
# MATCHING FUNCTION
# ============================================================
def calculate_match(career):
    score = 0
    reasons = []
    selected_levels = set()

    for item in pathway:
        if "GCSE" in item or "Level 2" in item:
            selected_levels.add(2)
        elif "Level 3" in item or "Standard Level (IB SL)" in item:
            selected_levels.add(3)
        elif "Level 4" in item or "Higher" in item and "Degree" not in item:
            selected_levels.add(4)
        elif "Level 5" in item:
            selected_levels.add(5)
        elif "Level 6" in item or "University" in item or "Higher Level (IB HL)" in item or "Graduate" in item:
            selected_levels.update([3, 4, 5, 6, 7])
        elif "Level 7" in item or "Postgraduate" in item:
            selected_levels.update([4, 5, 6, 7])
        elif "Working" in item or "Career Change" in item:
            selected_levels.update([2, 3, 4, 5, 6, 7])
        elif item in ["📚 A Levels", "🔧 T Level", "📖 BTEC / CTEC / Cambridge Technical"]:
            selected_levels.add(3)
        elif item == "❓ Not sure yet — still figuring it all out!":
            pass

    if not pathway or "❓ Not sure yet — still figuring it all out!" in pathway:
        score += 15
    else:
        if selected_levels.intersection(set(career["levels"])):
            score += 15
            reasons.append("your current stage can lead directly towards this career")
        else:
            score += 10
            reasons.append("this career is still reachable with further steps")

    if industries and "❓ Not sure yet — still exploring!" not in industries:
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
            reasons.append("your subjects are directly relevant")
    else:
        score += 10

    if interests and "❓ Not sure yet — still exploring!" not in interests:
        interest_matches = set(interests).intersection(set(career["interests"]))
        if interest_matches:
            interest_score = min(len(interest_matches) * 7, 20)
            score += interest_score
            reasons.append("your personal interests match this career")
    else:
        score += 10

    if skills.strip():
        skill_text = skills.lower()
        keyword_matches = sum(1 for kw in career["keywords"] if kw.lower() in skill_text)
        skill_score = min(keyword_matches * 4, 15)
        score += skill_score
        if keyword_matches:
            reasons.append("your existing skills are a great foundation")
    else:
        score += 7

    if environment and "❓ Not sure yet!" not in environment:
        env_matches = set(environment).intersection(set(career["environment"]))
        score += min(len(env_matches) * 2, 5)
    else:
        score += 3

    if values and "❓ Not sure yet!" not in values:
        val_matches = set(values).intersection(set(career["values"]))
        score += min(len(val_matches) * 2, 5)
    else:
        score += 3

    return min(round(score), 100), reasons

# ============================================================
# FIND MY MATCHES
# ============================================================
if st.button("🔍 Find My Career Matches", type="primary", use_container_width=True):
    if not any([pathway, subjects, skills.strip(), interests, industries, environment, values]):
        st.warning("Please answer at least a few questions before finding your matches — you've got this! 💛")
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
    st.subheader("Here's what fits YOU — your skills, your interests, YOUR future.")
    st.write("These are suggestions to help you explore — NOT final answers. You can do ANYTHING you set your mind to! 💛")

    for idx, result in enumerate(top_results, start=1):
        medal = ["🥇", "🥈", "🥉"][idx-1] if idx <= 3 else f"{idx}."
        career = result["career"]
        score = result["score"]
        reasons = result["reasons"]

        st.markdown('<div class="career-card">', unsafe_allow_html=True)
        col1, col2 = st.columns([4, 1])
        with col1:
            st.subheader(f"{medal} {career['name']}")
            st.caption(f"💡 {career['short_desc']}")
        with col2:
            st.markdown(f'<div class="match-score">{score}%</div><div class="small-text">Match</div>', unsafe_allow_html=True)
        st.progress(score / 100)

        st.markdown("### ✅ Why this fits YOU")
        unique_reasons = list(dict.fromkeys(reasons))
        if unique_reasons:
            for reason in unique_reasons[:4]:
                st.write(f"✓ {reason.capitalize()}.")
        else:
            st.write("Your profile shows strong potential — worth exploring!")

        st.markdown("### 🗺️ Your possible routes from HERE")
        for route in career["routes"]:
            st.write(f"• {route}")

        st.markdown("### 🛠️ Skills to START building TODAY")
        st.write(" • ".join(career["skills_to_build"]))
        st.markdown("</div>", unsafe_allow_html=True)

    # ========================================================
    # SUBMIT — SAVE ANONYMOUSLY (ONLY YOU SEE IT)
    # ========================================================
    st.markdown("---")
    if not st.session_state.submitted:
        st.subheader("📋 Submit your results")
        st.write("This helps us make PathPilot better — completely anonymous, no personal info shared! 💛")
        if st.button("✅ Submit My Results", type="primary", use_container_width=True):
            top_match = st.session_state.results[0]["career"]["name"]
            top_score = st.session_state.results[0]["score"]
            st.session_state.submissions.append({
                "time": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "stage": ", ".join(pathway[:2]) if pathway else "Not specified",
                "top_match": top_match,
                "top_score": top_score,
                "industries": ", ".join(industries[:2]) if industries else "Not specified"
            })
            st.session_state.submitted = True
            st.success("✅ Thank you! Your results have been submitted — anonymously! 💛")
    else:
        st.success("✅ Thank you for submitting! 💛")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.caption("💛 PathPilot — Your path, your playbook. No wrong moves — just what works for YOU.")
