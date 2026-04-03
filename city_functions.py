def city_country(city, country, population=None):
    """Return a formatted string like City, Country, with optional population."""
    
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"
    