def does_play_banjo(name):
    """Check if a person plays banjo based on their name."""
    if name.startswith('R') or name.startswith('r'):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
# Test cases
print(does_play_banjo("Rick"))    # Should return "Rick plays banjo"
print(does_play_banjo("Alice"))   # Should return "Alice does not play banjo"
print(does_play_banjo("Roger"))    # Should return "Roger plays banjo"
print(does_play_banjo("ben"))      # Should return "ben does not play banjo"
print(does_play_banjo("Rita"))     # Should return "Rita plays banjo"
print(does_play_banjo("Tom"))      # Should return "Tom does not play banjo"
print(does_play_banjo("randy"))    # Should return "randy plays banjo"
