# formatted strings

first_name = 'Adam'
last_name = 'Cole'

message = f'welcome {first_name} {last_name} to the arena!'
print(message)

# also

message_other_way = 'welcome {0} {1} to the arena'.format(first_name, last_name)
print(message_other_way)

# a couple of other ways:

message_ver_three = 'welcome {} {} to the arena'.format(first_name, last_name)
print(message_ver_three)

message_ver_four = 'welcome {f_name} {l_name} to the arena'.format(f_name='Adam', l_name='Cole')
print(message_ver_four)
