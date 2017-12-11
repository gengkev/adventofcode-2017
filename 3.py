from collections import defaultdict

n = 361527

lol = defaultdict(lambda: 0)
lol[(0, 0)] = 1

def check():
    global x, y
    lol[(x, y)] = (lol[(x-1, y)] + lol[(x+1, y)] +
                   lol[(x, y-1)] + lol[(x, y+1)] +
                   lol[(x-1, y-1)] + lol[(x-1, y+1)] +
                   lol[(x+1, y-1)] + lol[(x+1, y+1)])
    print(x, y, lol[(x, y)])
    if lol[(x, y)] >= n:
        print('yay', lol[(x, y)])
        exit(0)

x = 1
y = -1

level = 1
while True:
    for i in range(level * 2):
        y += 1; check()
    for i in range(level * 2):
        x -= 1; check()
    for i in range(level * 2):
        y -= 1; check()
    for i in range(level * 2):
        x += 1; check()

    # yay
    x += 1; y -= 1
    level += 1


