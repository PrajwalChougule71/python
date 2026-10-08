#  F string

letter = 'Hey my name is {} and I am From {}'
dis = 'Sangli'
name = 'Prajwal'

print(letter.format(name,dis))
print(f"Hey my name is {name} and I'm From {dis}")
price = 49.09999
txt = f'For only{price:.2f}dollars!'
print(txt)
print(type(f"{2*30}"))

# We also can print it like this

print(f"We use f-stirngs like this: Hey my name is {{name}} and im from {{dis}}")
