data = open('data.txt', 'r')
row = -1
while True:
row = row + 1
word = data.readlines()[row]
print(html_p.find(word))