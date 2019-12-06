import pygame as pg
pg.init()

WIDTH = 1700
HEIGHT = 800
MAX_ITR = 100
FPS = 10
MANDELBROT = False
JULIA_CONST = complex(-0, -0.82376)

if MANDELBROT:
	LENGTH = 400
	CENTERX = LENGTH * 3
	CENTERY = LENGTH
else:
	LENGTH = 200
	CENTERX = WIDTH / 2
	CENTERY = HEIGHT / 2

COLOR_PEGS = [
	(0,   7,   100),
	(32,  107, 203),
	(237, 255, 255),
	(255, 170, 0),
	(0,   2,   0)
]

def quit():
	pg.quit()
	exit()

def get_coords(x, y):
	x = x -CENTERX
	y = HEIGHT - y - CENTERY
	return (x/LENGTH, y/LENGTH)

def map_col(value, start, end, start_col, end_col):
	ratio = (value - start) / (end - start)
	r_range = end_col[0] - start_col[0]
	g_range = end_col[1] - start_col[1]
	b_range = end_col[2] - start_col[2]

	r = round(start_col[0] + r_range * ratio)
	g = round(start_col[1] + g_range * ratio)
	b = round(start_col[2] + b_range * ratio)

	return (r, g, b)

def get_color(x, y):
	z = complex(x, y)

	if MANDELBROT:
		c = complex(x, y)
	else:
		c = JULIA_CONST

	for i in range(MAX_ITR):
		if abs(z) > 16:
			q = i/MAX_ITR
			if q < 0.32:
				return map_col(q, 0, 0.32, COLOR_PEGS[0], COLOR_PEGS[1])
			elif q < 0.45:
				return map_col(q, 0.32, 0.45, COLOR_PEGS[1], COLOR_PEGS[2])
			elif q < 0.6425:
				return map_col(q, 0.45, 0.6425, COLOR_PEGS[2], COLOR_PEGS[3])
			elif q < 0.86:
				return map_col(q, 0.6425, 0.86, COLOR_PEGS[3], COLOR_PEGS[4])
			else:
				return (0,0,0)
		z = z * z + c

	return (0, 0, 0)

def mainLoop():
	pg.display.set_caption("Mandelbrot Set")
	screen = pg.display.set_mode((WIDTH, HEIGHT))

	clock = pg.time.Clock()

	for x in range(WIDTH):
		for y in range(HEIGHT):
			r, g, b = get_color(*get_coords(x, y))
			# print(r, g, b)
			screen.set_at((x, y), pg.Color(r, g, b))
			print(x, y, "DONE")

		pg.display.update()

	while True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					quit()

		clock.tick(FPS)

mainLoop()