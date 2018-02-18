def foo():
    print("foo")

print(foo.__name__)
foo
#      # µËÔÇÑÕ, ËÌÑÕ×ÇÙÕ×â ÓÌßÇåÙ ÔÕ×ÓÇÒãÔÕÓÚ ÜÕËÚ ËÌÒ:
def bar(func):
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

    print(foo.__name__)

