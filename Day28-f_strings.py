
# Old way
letter = "hey my name is {} and I am from {}"

country = 'India'
name = 'siddesh'

letter.format(name, country)


# New Way

print(f'Hey my name is {name} and I am from {country}')


# old way
txt = 'For only {price:.2f} dollers!' # It will take only 2 digites after decimal

print(txt.format(price = 49.08343434))

# new way
price = 49.08343434
txt = f'For only {price:.2f} dollars!'
print(f"==>> txt: {txt}")

# If we want to showcase curly braces in our stirng, then we need to apply 2 curly braces over their
print(f'We user f-strings like this: Hey my name is {{name}} and I am from {{country}}')
