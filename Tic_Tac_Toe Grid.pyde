grid = [[1] * 3 for n in range(3)]
w = 100


def setup():
    size(500, 300)


def draw():
    x, y = 0, 0
    for row in grid:
        for col in row:
            rect(x, y, w, w)
            x += w
        y += w
        x = 0
