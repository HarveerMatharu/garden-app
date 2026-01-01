"""
Data‑driven gardening advice using dictionaries.
"""

from typing import Dict, List

# Advice for each season and plant type
ADVICE: Dict[str, Dict[str, str]] = {
    "spring": {
        "flower": "Start fertilising lightly and remove dead blooms.",
        "vegetable": "Prepare soil and plant cool‑season crops.",
        "herb": "Transplant seedlings and pinch tips to encourage growth.",
    },
    "summer": {
        "flower": "Water regularly and provide shade during heatwaves.",
        "vegetable": "Mulch soil and watch for pests.",
        "herb": "Harvest often to promote new growth.",
    },
    "autumn": {
        "flower": "Cut back perennials and collect seeds.",
        "vegetable": "Clear old crops and add compost.",
        "herb": "Dry herbs before temperatures drop.",
    },
    "winter": {
        "flower": "Protect plants from frost using covers.",
        "vegetable": "Use cold frames or move pots indoors.",
        "herb": "Keep potted herbs in a bright indoor spot.",
    },
}

# Recommended plants for each season
RECOMMENDATIONS: Dict[str, List[str]] = {
    "spring": ["pansies", "lettuce", "parsley"],
    "summer": ["marigolds", "tomatoes", "basil"],
    "autumn": ["chrysanthemums", "kale", "rosemary"],
    "winter": ["hellebores", "winter spinach", "thyme"],
}


def get_advice(season: str, plant_type: str) -> str:
    """
    Return gardening advice based on season and plant type.
    Falls back to a general message if no specific advice exists.
    """
    season_data = ADVICE.get(season)
    if not season_data:
        return "No advice available for this season."

    advice = season_data.get(plant_type)
    if advice:
        return advice

    return "No advice available for this plant type."


def recommend_plants(season: str) -> str:
    """Return a list of recommended plants for the given season."""
    plants = RECOMMENDATIONS.get(season)
    if not plants:
        return "No plant recommendations available."

    return "Recommended plants for this season: " + ", ".join(plants)


def main() -> None:
    """Main program flow."""
    season = input("Enter season (spring, summer, autumn, winter): ").strip().lower()
    plant_type = input("Enter plant type (flower, vegetable, herb): ").strip().lower()

    print("\n--- Gardening Advice ---")
    print(get_advice(season, plant_type))

    print("\n--- Recommendations ---")
    print(recommend_plants(season))


if __name__ == "__main__":
    main()
