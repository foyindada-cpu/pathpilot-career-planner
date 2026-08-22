import json
"""
PathPilot - Career & Education Pathway Planner

A Python application that recommends career pathways based on:
- Subjects
- Skills
- Career interests
- Preferred route

Author: Foyin Dada
"""

# -----------------------------
# PATHWAY DATA
# -----------------------------

PATHWAYS = [def load_pathways():
    """Load career pathway data from the JSON dataset."""
    with open("data/pathways.json", "r", encoding="utf-8") as file:
        return json.load(file)


PATHWAYS = load_pathways()
    
]


# -----------------------------
# INPUT FUNCTIONS
# -----------------------------

def get_user_name():
    """Ask the user for their name."""
    while True:
        name = input("\nWhat is your name? ").strip()

        if name:
            return name

        print("Please enter your name.")


def get_subjects():
    """Collect the user's subjects."""
    print("\nEnter your subjects.")
    print("Type 'done' when you have finished.")

    subjects = []

    while True:
        subject = input("> ").strip()

        if subject.lower() == "done":
            break

        if subject:
            subjects.append(subject.title())

    return subjects


def get_skills():
    """Collect the user's current skills."""
    print("\nEnter your current skills.")
    print("Type 'done' when you have finished.")

    skills = []

    while True:
        skill = input("> ").strip()

        if skill.lower() == "done":
            break

        if skill:
            skills.append(skill.title())

    return skills


def get_career_interest():
    """Ask the user for their career interest."""
    print("\nWhat career area interests you?")
    print("Examples: Software Engineer, Cybersecurity, Finance, Data")

    return input("> ").strip().lower()


def get_preferred_route():
    """Ask the user which education route they prefer."""
    print("\nWhat route are you interested in?")
    print("1. University")
    print("2. Degree Apprenticeship")
    print("3. Either")

    while True:
        choice = input("> ").strip()

        if choice == "1":
            return "University"

        if choice == "2":
            return "Degree Apprenticeship"

        if choice == "3":
            return "Either"

        print("Please choose 1, 2 or 3.")


# -----------------------------
# RECOMMENDATION ALGORITHM
# -----------------------------

def calculate_score(user_subjects, user_skills, career_interest,
                    preferred_route, pathway):
    """
    Calculate how well a pathway matches the user's profile.

    Scoring:
    - Subject match: 30 points
    - Skill match: 30 points
    - Career interest: 25 points
    - Route match: 15 points

    Maximum score = 100
    """

    score = 0

    # Subject matching
    subject_matches = 0

    for subject in user_subjects:
        for pathway_subject in pathway["subjects"]:
            if subject.lower() == pathway_subject.lower():
                subject_matches += 1
                break

    if subject_matches > 0:
        score += 30

    # Skill matching
    skill_matches = 0

    for skill in user_skills:
        for pathway_skill in pathway["skills"]:
            if skill.lower() == pathway_skill.lower():
                skill_matches += 1
                break

    if skill_matches > 0:
        score += 30

    # Career interest matching
    career = pathway["career"].lower()

    if career_interest in career or career in career_interest:
        score += 25
    elif (
        "software" in career_interest
        and "software" in career
    ):
        score += 25
    elif (
        "cyber" in career_interest
        and "cyber" in career
    ):
        score += 25
    elif (
        "data" in career_interest
        and "data" in career
    ):
        score += 25
    elif (
        "finance" in career_interest
        and "investment" in career
    ):
        score += 25

    # Route matching
    if preferred_route == "Either":
        score += 15
    elif preferred_route in pathway["routes"]:
        score += 15

    return score


def generate_recommendations(user_subjects, user_skills,
                             career_interest, preferred_route):
    """Generate and rank pathway recommendations."""

    recommendations = []

    for pathway in PATHWAYS:
        score = calculate_score(
            user_subjects,
            user_skills,
            career_interest,
            preferred_route,
            pathway
        )

        recommendations.append({
            "pathway": pathway,
            "score": score
        })

    # Sort recommendations from highest to lowest score
    recommendations.sort(
        key=lambda recommendation: recommendation["score"],
        reverse=True
    )

    return recommendations


# -----------------------------
# DISPLAY FUNCTIONS
# -----------------------------

def display_recommendations(recommendations):
    """Display the top three recommendations."""

    print("\n" + "=" * 60)
    print("YOUR PATHPILOT RECOMMENDATIONS")
    print("=" * 60)

    for position, recommendation in enumerate(
        recommendations[:3],
        start=1
    ):
        pathway = recommendation["pathway"]
        score = recommendation["score"]

        print(f"\n#{position} {pathway['career']}")
        print(f"Match score: {score}/100")
        print(f"Routes: {', '.join(pathway['routes'])}")
        print(f"About: {pathway['description']}")

        print("\nSkills to develop:")
        for skill in pathway["skills_to_develop"]:
            print(f"  • {skill}")

        print("-" * 60)


def display_profile(name, subjects, skills, career_interest,
                    preferred_route):
    """Display the user's profile."""

    print("\n" + "=" * 60)
    print("YOUR PROFILE")
    print("=" * 60)

    print(f"Name: {name}")
    print(f"Subjects: {', '.join(subjects)}")
    print(f"Skills: {', '.join(skills)}")
    print(f"Career interest: {career_interest.title()}")
    print(f"Preferred route: {preferred_route}")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():
    """Run the PathPilot application."""

    print("=" * 60)
    print("WELCOME TO PATHPILOT")
    print("Your Career & Education Pathway Planner")
    print("=" * 60)

    name = get_user_name()
    subjects = get_subjects()
    skills = get_skills()
    career_interest = get_career_interest()
    preferred_route = get_preferred_route()

    display_profile(
        name,
        subjects,
        skills,
        career_interest,
        preferred_route
    )

    print("\nAnalysing your profile...")

    recommendations = generate_recommendations(
        subjects,
        skills,
        career_interest,
        preferred_route
    )

    display_recommendations(recommendations)

    print("\nThank you for using PathPilot!")
    print("Your results can help guide your future research.")


if __name__ == "__main__":
    main()
    Implement initial PathPilot recommendation engine
