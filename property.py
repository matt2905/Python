import qrcode


class human:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, newAge):
        img = qrcode.make(newAge)
        type(img)
        img.save("qrcode.png")
        self._age = newAge


matt = human()
matt.age = 10
print(matt.age)
