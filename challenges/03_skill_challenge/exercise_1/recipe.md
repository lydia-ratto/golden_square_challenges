Reading Time Function Design Recipe
Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem
> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature
Include the name of the function, its parameters, return value, and side effects.

    def reading_time_calcularor(text):
        """Calculates time based on word count in string

        Parameters:
            text: a string containing words (e.g. 'Learn to code at Makers')

        Returns: a time as seconds, minutes or hours and minutes (e.g. '30 seconds', '45 minutes', '9 hours, 23 minutes')   

        Side effects: none

3. Create Examples as Tests
    Given a non-string object it returns an error
    reading_time(0) => 'Parameter must be a string"

    Given a string with 200 words it returns 1
    reading_time("(Text with 200 words)") => '1 minute"

    Given a string with less than 100 words it converts to seconds
    reading_time("(Text with 100 words)") => '30 seconds"

    Given a string with 12,000 words it converts to hours
    reading_time("(Text with 12,000 words)") => '1 hour"
    
    Given a string with more than 12,000 words it converts to hours and minutes
    reading_time("(Text with 12,600 words)") => '1 hour, 3 minutes"