"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, theme, words, text):
        """Create story with words and template text."""
        self.theme = theme
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story0 = Story( "Story-Tale",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story1 = Story("Climbing",
    ["weather_condition", "mountain_hazard", "name"],
    """The climbers struggled through deteriorating {weather_condition} and high {mountain_hazard}. Eventually they reached the summmit of Mount {name}."""
)

story2 = Story("Animals",
    ["plural_animal", "place"],
    """ The {plural_animal} of the {place} slept in peace."""
)

stories_list = [story0, story1, story2]