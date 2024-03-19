class My_Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

my_class = My_Numbers()
my_iter = iter(my_class)

for x in my_iter:
    print(x)
