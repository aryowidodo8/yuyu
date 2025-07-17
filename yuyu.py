import turtle
import math

# Fungsi menggambar satu kelopak bunga
def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

# Fungsi menggambar bunga dengan jumlah kelopak tertentu
def draw_flower(petal_count, radius, angle, color):
    t = turtle.Turtle()
    t.color(color)
    t.speed(0)
    t.pensize(2)

    for _ in range(petal_count):
        draw_petal(t, radius, angle)
        t.left(360 / petal_count)

    t.hideturtle()

# Fungsi utama
def main():
    screen = turtle.Screen()
    screen.bgcolor("black")
    print("=== PROGRAM BUNGA INTERAKTIF ===")
    try:
        petals = int(input("Masukkan jumlah kelopak (misal 6, 12, 36): "))
        radius = int(input("Masukkan radius kelopak (misal 60): "))
        angle = int(input("Masukkan besar sudut kelopak (misal 60): "))
        color = input("Masukkan warna (misal 'red', 'magenta', 'yellow'): ").lower()
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk radius dan kelopak.")
        return

    draw_flower(petals, radius, angle, color)
    print("Tekan jendela gambar untuk keluar.")
    screen.exitonclick()

main()
