# formatted strings

first_name = 'Adam'
last_name = 'Cole'

message = f'welcome {first_name} {last_name} to the arena!'
print(message)

# also f string

message_other_way = 'welcome {0} {1} to the arena'.format(first_name, last_name)
print(message_other_way)

# a couple of other ways:

message_ver_three = 'welcome {} {} to the arena'.format(first_name, last_name)
print(message_ver_three)

message_ver_four = 'welcome {f_name} {l_name} to the arena'.format(f_name='Adam', l_name='Cole')
print(message_ver_four)

selfish = '01234567'

# print just the last char
print(selfish[-1])

#  print from start to end of string
print(selfish[0:8])

# also from start till end
print(selfish[0:])

# print with step over 2 (skip one char)
print(selfish[0:8:2])

# print in reverse
# where -1 is the last char in the string
print(selfish[::-1])

print(len(selfish))

