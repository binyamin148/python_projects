def print_stars(n):
    print("*" * n)


def draw_rectangle(rows, cols):
    for _ in range(rows):
        print_stars(cols)
        

def draw_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


def draw_rhombus(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
        
print("Line of stars:")
print_stars(5)

print("\nRectangle:")
draw_rectangle(3, 4)

print("\nTriangle:")
draw_triangle(4)

print("\nRhombus:")
draw_rhombus(3)
