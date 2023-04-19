class MainClass:
    def __init__(self, text):
        self.text_field = text

    def set_text_field(self, text=None):
        if text is None:
            self.text_field = input("Введите новое значение для текстового поля: ")
        else:
            self.text_field = text


class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self.number_field = number


main_object = MainClass("начальное значение")
print(main_object.text_field)


main_object.set_text_field("новое значение")
print(main_object.text_field)


sub_object = SubClass("текстовое значение", 42)
print(sub_object.text_field)
print(sub_object.number_field)


sub_object.set_text_field("новое текстовое значение")
print(sub_object.text_field)




##############################################################
class MainClass:
    def __init__(self, text):
        self._text_field = text

    def set_text_field(self, text=None):
        if text is None:
            self._text_field = input("Введите новое значение для текстового поля: ")
        else:
            self._text_field = text

    def get_text_field(self):
        return self._text_field


class SubClass(MainClass):
    def __init__(self, text, number):
        super().__init__(text)
        self._number_field = number

    def set_number_field(self, number):
        self._number_field = number

    def get_number_field(self):
        return self._number_field

    def get_text_field(self):
        return f"Текстовое поле из класса-потомка: {self._text_field}"

main_object = MainClass("начальное значение")
print(main_object.get_text_field())


main_object.set_text_field("новое значение")
print(main_object.get_text_field())


sub_object = SubClass("текстовое значение", 42)
print(sub_object.get_text_field())
print(sub_object.get_number_field())


sub_object.set_number_field(13)
print(sub_object.get_number_field())
##############################################################
class Roman:
    def __init__(self, roman_numeral):
        self.value = self.roman_to_int(roman_numeral)

    def __str__(self):
        return self.int_to_roman(self.value)

    def __add__(self, other):
        return Roman(self.int_to_roman(self.value + other.value))

    def __sub__(self, other):
        return Roman(self.int_to_roman(self.value - other.value))

    def __mul__(self, other):
        return Roman(self.int_to_roman(self.value * other.value))

    def __truediv__(self, other):
        return Roman(self.int_to_roman(self.value // other.value))

    @staticmethod
    def roman_to_int(roman_numeral):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(roman_numeral)):
            if i > 0 and roman_map[roman_numeral[i]] > roman_map[roman_numeral[i - 1]]:
                result += roman_map[roman_numeral[i]] - 2 * roman_map[roman_numeral[i - 1]]
            else:
                result += roman_map[roman_numeral[i]]
        return result

    @staticmethod
    def int_to_roman(integer):
        if not 0 < integer < 4000:
            raise ValueError("number out of range (must be 1..3999)")
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for i in range(len(ints)):
            count = int(integer / ints[i])
            result.append(nums[i] * count)
            integer -= ints[i] * count
        return ''.join(result)
