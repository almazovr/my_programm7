def rectangle_area(wight, height):
    return wight * height
wight = float(input("какая ширина прямоугольника?-"))
height = float(input("какая высота прямоугольника?-"))
area = rectangle_area(wight, height)
print("Площадь прямоугольника-",area)