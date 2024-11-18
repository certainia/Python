cities = {
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Known as the "City of Light".'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Famous for its cherry blossoms and technology.'
    },
    'Cairo': {
        'country': 'Egypt',
        'population': '10 million',
        'fact': 'Home to the Great Pyramid of Giza.'
    }
}

for city, details in cities.items():
    print(f"{city}:")
    print(f"  Country: {details['country']}")
    print(f"  Population: {details['population']}")
    print(f"  Fact: {details['fact']}\n")
