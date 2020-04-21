# Lambdas will follow the format that you write lambda forllowed by the input
# Then colon and the body of the expression

# so the function hello function which takes a single input
def hello(name):
    return f'hello {name}'


# becomes
expression = lambda name: f'hello {name}'
print(expression('Adam'))

first_name_var = '      John   '
last_name_var = '  Doe   '


# multiple arg method
def full_name(first_name, last_name):
    return f'{first_name.strip()} {last_name.strip()}'


print(full_name(first_name_var, last_name_var))

# lambda version of multiple arg method
full_name_lambda = lambda first_name, \
                          last_name: f'{first_name.strip()} {last_name.strip()}'

print(full_name_lambda(first_name_var, last_name_var))

result = full_name_lambda(first_name_var, last_name_var) == \
         full_name(first_name_var, last_name_var)

print(result)
