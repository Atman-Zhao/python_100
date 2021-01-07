# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     #访问器 -getter 方法
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     #修改器 —getter方法
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
#
# def main():
#     person = Person('王大锤', 12)
#     print(person.name)
#     person.play()
#     person.age = 22
#     person.play()
#     # person.name = '白元芳'  # AttributeError: can't set attribute
#
#
# if __name__ == '__main__':
#     main()

# def use_logging(func):
#     logging.warn("%s is running" % func.__name__)
#     func()
#
# def bar():
#     print('i am bar')
#
# use_logging(bar)

# def test_kwargs(**kwargs):
#     if kwargs is not None:
#         for key, value in kwargs.items():
#             print(type(kwargs))
#             print("{} = {}".format(key,value))
#         # Or you can visit kwargs like a dict() object
#         # for key in kwargs:
#         #    print("{} = {}".format(key, kwargs[key]))
# test_kwargs(name="python", value="5")


