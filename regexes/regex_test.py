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

new_string = 'Very new thing, this is a simple string that contains a few words in it one repeated, this'

pattern_looking_for = 'this'
pattern = re.compile(pattern_looking_for)
pattern_result = pattern.search(new_string)

# group function returns the part of he string where there was a match
print(pattern_result.group())
print(len(pattern.findall(new_string)) == 2)

new_pattern_looking_for = 'Very (\w+) thing'
new_pattern = re.compile(new_pattern_looking_for)
print(list(new_pattern.match(new_string).groups()))

print(list(re.search(r'Very (new) thing', new_string).groups()))

print(list(new_pattern.match(new_string).groups()) == \
list(re.search(r'Very (new) thing', new_string).groups()))

# https://regex101.com


