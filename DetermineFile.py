import fileinput
lines = []
for line in fileinput.input():
    lines.append(line)

tokens = '\n'.join(lines).split()

python_points = 0
ruby_points = 0
js_points = 0

for token in tokens:
    if 'print' in token:
        python_points += 1
    if token == 'def':
        python_points += 1
    if token == 'import':
        python_points += 1
    if 'def' in token:
        ruby_points += 1
    if 'end' in token:
        ruby_points += 1
    if '.new' in token:
        ruby_points += 1
    if token == '{' or token == 'function' or token == '=>':
        js_points += 1

if python_points > ruby_points and python_points > js_points:
    print('python')
elif ruby_points > python_points and ruby_points > js_points:
    print('ruby')
else:
    print('javascript')