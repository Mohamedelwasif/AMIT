def is_playing_banjo(name):
    """Check if a person plays banjo based on their name."""
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# Test Cases
print(is_playing_banjo("Rick"))   # Rick plays banjo
print(is_playing_banjo("Alice"))  # Alice does not play banjo
print(is_playing_banjo("rob"))    # rob plays banjo
print(is_playing_banjo("Bob"))    # Bob does not play banjo
