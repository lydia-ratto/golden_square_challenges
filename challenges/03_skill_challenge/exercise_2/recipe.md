Verify Grammar Function Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem
> As a user
> So that I can improve my grammar
> I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature
def verify_text_grammar(text):
    Parameters:
        Text as a string
    Returns:
        Boolean: true if text has capital letter and ends with a punctuation mark (.)

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

# EXAMPLE

Given a text with capitalised first word and a full stop, returns true
    verify_text_grammar('Hello and welcome to Makers.') => true

Given a text with a non capitalised first words and a full stop, returns false
    verify_text_grammar('hello and welcome to Makers.') => false

Given a text with a capitalised first words and no full stop, returns false
    verify_text_grammar('Hello and welcome to Makers') => false

Given a text with no capitalised first words and no full stop, returns false
    verify_text_grammar('hello and welcome to Makers') => false

4. Implement the Behaviour