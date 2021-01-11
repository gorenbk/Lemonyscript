file = open('test.lmy','r')
code = file.read()
for line in code.splitlines():
    words = line.split()
    if words[0]=='ask':
        answer = input(line[4:])
    elif words[0] == 'write':
        print((line[6:]).replace('{answer}',answer))