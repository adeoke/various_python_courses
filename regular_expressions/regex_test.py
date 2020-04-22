import re

string = 'This is a simple string that contains a few words in it'
substring_check = 'simple' in string
EXPECTED_RESULT = True

print(substring_check == EXPECTED_RESULT)

print(re.search('that', string))

pattern = '02215'

match_result = 'Match' if re.fullmatch(pattern, '02215') else 'No Match'
print(match_result)

raw_string_match = 'Match' if re.fullmatch(r'\d{5}', '02215') else 'No Match'
print(raw_string_match)

raw_string_match2 = 'Match' if re.fullmatch(r'\d{4}', '02215') else 'No Match'
print(raw_string_match2)

raw_string_match3 = 'Match' if re.fullmatch('[*+$]', '*') else 'No Match'
print(raw_string_match3)