import re


def complex_resolver(text, pattern):
    matches = re.findall(pattern, text)

    for match in matches:
        bool_condition = match[0]
        t_result, f_result = [num.strip() for num in match[3:].split(':')]

        if bool_condition == 't':
            text = text.replace(match, t_result)
        elif bool_condition == 'f':
            text = text.replace(match, f_result)

    if "?" in text:
        text = complex_resolver(text, pattern)

    return text


text = input()
pattern = r'[tf]\s\?\s\d\s\:\s\d'
print(complex_resolver(text, pattern))
