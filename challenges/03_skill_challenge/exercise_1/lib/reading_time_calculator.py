def reading_time_calculator(string):
    if type(string) is not str:
        raise Exception("Parameter must be a string")
    
    word_count = len(string.split())
    hours_count = int(word_count / 200 / 60)
    mins_count = int(word_count / 200)
    sec_count = int(word_count / 200 * 60)
    mins_left = mins_count - hours_count * 60

    if word_count < 200:
        return f"{sec_count} second{'s' if sec_count > 3 else ''}"
    if word_count >= 12000:
        result = f"{hours_count} hour{'s' if mins_count > 200 else ''}"
        if mins_left > 0:
          result += f" , {mins_left} minute{'s' if mins_count > 200 else ''}"
        return result
    if word_count >= 200:
        return f"{mins_count} minute{'s' if mins_count > 200 else ''}"