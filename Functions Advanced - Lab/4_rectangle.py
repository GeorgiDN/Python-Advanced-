def rectangle(*args):
    length, width = args[0], args[1]
    result = ''

    def perimeter():
        return (length + width) * 2

    def area():
        return length * width

    if not isinstance(length, int) or not isinstance(width, int):
        return "Enter valid values!"

    result += f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
    return result


print(rectangle(2, 10))
print(rectangle('2', 10))




# def rectangle(length, width):
#     def rectangle_area():
#         return length * width
#
#     def rectangle_perimeter():
#         return (length * 2) + (width * 2)
#
#     if type(length) != int or type(width) != int:
#         return "Enter valid values!"
#
#     return f'''Rectangle area: {rectangle_area()}
# Rectangle perimeter: {rectangle_perimeter()}'''
#
#
# print(rectangle(2, 10))




# def rectangle(length, width):
#     def perimeter():
#         return (length + width) * 2
#
#     def area():
#         return length * width
#
#     if not isinstance(length, int) or not isinstance(width, int):
#         return "Enter valid values!"
#
#     return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"
#
# print(rectangle(2, 10))



#TEST
# import unittest
# 
# class RectangleTests(unittest.TestCase):
#     def test(self):
#         result = rectangle('2', 10)
#         self.assertEqual(result, "Enter valid values!")
# 
#     def test_2_result(self):
#         result = rectangle(2, 2)
#         self.assertEqual(result, "Rectangle area: 4\nRectangle perimeter: 8")
# 
# 
# if __name__ == "__main__":
#    unittest.main()
