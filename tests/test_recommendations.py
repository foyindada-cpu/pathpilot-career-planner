from app import calculate_score, generate_recommendations


def test_software_engineer_matches_computer_science():
    score = calculate_score(
        ["Computer Science"],
        ["Programming"],
        "Software Engineer",
        "University",
        {
            "career": "Software Engineer",
            "routes": ["University"],
            "subjects": ["Computer Science"],
            "skills": ["Programming"],
            "description": "Software development",
            "skills_to_develop": ["Python"]
        }
    )

    assert score == 100


def test_recommendations_are_ranked():
    recommendations = generate_recommendations(
        ["Computer Science", "Maths"],
        ["Programming", "Problem Solving"],
        "Software Engineer",
        "Either"
    )

    scores = [
        recommendation["score"]
        for recommendation in recommendations
    ]

    assert scores == sorted(scores, reverse=True)
