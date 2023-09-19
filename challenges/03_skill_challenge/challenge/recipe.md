Tasks Function Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem
> As a user
> So that I can keep track of my tasks
> I want to check if a text includes the string #TODO.

2. Design the Function Signature

def check_if_task(text):
    """Verifies if #TODO word is in a string

    Parameters:
        text: a string containing words

    Returns:
        a boolean, True if the word #TODO is included, False otherwise

    Side effects:
        This function doesn't print anything or have any other side-effects
    """

3. Create Examples as Tests

"""Given a text with the word #TODO included
    returns True
"""
check_if_task('#TODO: Laundry') => True

"""Given a text without the word #TODO included
    returns False
"""
check_if_task('Do Laundry') => False

"""Given a text with the word #todo lowercase included
    returns True
"""
check_if_task('#todo Laundry') => True

"""Given a text with the word TODO included without # symbol
    returns False
"""
check_if_task('TODO Laundry') => False