from hashlib import sha256


ADJECTIVES = [
    "autumn", "hidden", "bitter", "misty", "silent", "empty", "dry", "dark",
    "summer", "icy", "delicate", "quiet", "white", "cool", "spring", "winter",
    "patient", "twilight", "dawn", "crimson", "wispy", "weathered", "blue",
    "billowing", "broken", "cold", "damp", "falling", "frosty", "green",
    "long", "late", "lingering", "bold", "little", "morning", "muddy", "old",
    "red", "rough", "still", "small", "sparkling", "throbbing", "shy",
    "wandering", "withered", "wild", "black", "young", "holy", "solitary",
    "fragrant", "aged", "snowy", "proud", "floral", "restless", "divine",
    "polished", "ancient", "purple", "lively", "nameless"
]

NOUNS = [
    "waterfall", "river", "breeze", "moon", "rain", "wind", "sea", "morning",
    "snow", "lake", "sunset", "pine", "shadow", "leaf", "dawn", "glitter",
    "forest", "hill", "cloud", "meadow", "sun", "glade", "bird", "brook",
    "butterfly", "bush", "dew", "dust", "field", "fire", "flower", "firefly",
    "feather", "grass", "haze", "mountain", "night", "pond", "darkness",
    "snowflake", "silence", "sound", "sky", "shape", "surf", "thunder",
    "violet", "water", "wildflower", "wave", "water", "resonance", "sun",
    "wood", "dream", "cherry", "tree", "fog", "frost", "voice", "paper",
    "frog", "smoke", "star"
]

# Simulating samples from one uniform discrete variable by using
# samples from another one (with different amount of outcomes)
# is a rather complicated thing in a general form (because of uniformity requirement).
# But happily we can do it with ease for our special case, where
# source random variable has 16^k outcomes and target one — 64
assert len(ADJECTIVES) == 64
assert len(NOUNS) == 64


def hasheroku(text:str, separator:str='-', digits_suffix_len:int=0):
    """
    Generates heroku hash from the given string.

    Args:
        text (str):
            String to hash.

        separator (str, optional):
            String to separate heroku adjective, noun and digits suffix.
            Default: '-'

        digits_suffix_len (int, optional):
            Number of digits to append to the end of the hash.
            Cant be larger than 36, because there is not enough symbols
            in the sha256 hex, which is used under the hood.

            Default: 0.
    """

    assert len(text) > 0
    assert 0 <= digits_suffix_len <= 36

    hash = sha256(text.encode('utf-8')).hexdigest()
    source_vars = [int(s, 16) for s in hash[:4]]

    # We use first two symbols of the hash to generate the adjective
    # and second two symbols two generate the noun
    adj_index = (source_vars[0] * 16 + source_vars[1]) % 64
    noun_index = (source_vars[2] * 16 + source_vars[3]) % 64

    adj = ADJECTIVES[adj_index]
    noun = NOUNS[noun_index]

    if digits_suffix_len == 0:
        heroku_hash = adj + separator + noun
    else:
        digits = str(int(hash, 16))[-digits_suffix_len:]

        # Let's reverse our digits so prefixes are the same
        # for identical strings with different suffix lengths
        digits = digits[::-1]

        heroku_hash = adj + separator + noun + separator + digits

    return heroku_hash
