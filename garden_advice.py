from typing import Dict, List

ADVICE: Dict[str, Dict[str, str]] = {
    'spring': {
        'flower': 'Start fertilising lightly and deadhead spent blooms.',
        'vegetable': 'Prepare beds and sow cool-season crops.',
        'herb': 'Transplant seedlings and pinch to encourage bushiness.',
    },
    'summer': {
        'flower': 'Water your plants regularly and provide some shade.',
        'vegetable': 'Mulch to retain moisture and watch for pests.',
        'herb': 'Harvest frequently to encourage new growth.',
    },
    'autumn': {
        'flower': 'Cut back perennials and collect seeds if desired.',
        'vegetable': 'Clear spent crops and add compost to beds.',
        'herb': 'Dry or preserve herbs before the cold sets in.',
    },
    'winter': {
        'flower': 'Protect your plants from frost with covers.',
        'vegetable': 'Use cold frames or move containers indoors.',
        'herb': 'Keep potted herbs in a bright, cool spot indoors.',
    },
}

RECOMMENDATIONS: Dict[str, List[str]] = {
    'spring': ['pansies', 'lettuce', 'parsley'],
    'summer': ['marigolds', 'tomatoes', 'basil'],
    'autumn': ['chrysanthemums', 'kale', 'rosemary'],
    'winter': ['hellebores', 'winter spinach (cold frames)', 'thyme'],
}


def normalize(text: str) -> str:
    """Return a normalized, lowercased string without surrounding whitespace."""
    return text.strip().lower()


def get_season_input(prompt: str = 'Enter season (spring, summer, autumn, winter): ') -> str:
    """Prompt for a season and validate against available seasons."""
    valid = set(ADVICE.keys())
    while True:
        season = normalize(input(prompt))
        if season in valid:
            return season
        print('Invalid season. Choose from: ' + ', '.join(sorted(valid)) + '.')


def get_plant_type_input(prompt: str = 'Enter plant type (flower, vegetable, herb): '
                         ) -> str:
    """Prompt for a plant type and validate against available types."""
    valid = {ptype for season in ADVICE.values() for ptype in season.keys()}
    while True:
        plant_type = normalize(input(prompt))
        if plant_type in valid:
            return plant_type
        print('Invalid plant type. Choose from: ' + ', '.join(sorted(valid)) + '.')


def get_advice(season: str, plant_type: str) -> str:
    """
    Return gardening advice for the given season and plant type.

    Falls back to a season-level summary or a generic message if needed.
    """
    season_dict = ADVICE.get(season, {})
    advice = season_dict.get(plant_type)
    if advice:
        return advice
    if season_dict:
        # Provide a concise fallback using the first available entry.
        first_entry = next(iter(season_dict.values()))
        return 'General seasonal advice: ' + first_entry
    return 'No advice available for that combination.'


def recommend_plants(season: str, limit: int = 3) -> str:
    """Return a short recommendation string of plants suitable for the season."""
    recs = RECOMMENDATIONS.get(season, [])
    if not recs:
        return 'No plant recommendations available for this season.'
    return 'Recommended plants for ' + season + ': ' + ', '.join(recs[:limit]) + '.'


def main() -> None:
    """Main program flow: get inputs, compute advice, and print results."""
    print('Welcome to Garden Advice!')
    season = get_season_input()
    plant_type = get_plant_type_input()

    advice_text = get_advice(season, plant_type)
    recommendations = recommend_plants(season)

    print('\n--- Gardening Advice ---')
    print(advice_text)
    print('\n--- Recommendations ---')
    print(recommendations)


if __name__ == '__main__':
    main()
