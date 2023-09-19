def verify_text_grammar(string):
    return string.split()[0] == string.split()[0].capitalize() and string.split()[-1][-1] == '.'