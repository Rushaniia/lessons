class Matrix:
    def __init__(self,my_list):
        self.my_list = my_list

    def __str__(self):
        return '\n'.join('\t'.join([str(el) for el in i]) for i in self.my_list)
        # return '\n'.join(map(str, self.my_list))

    def __add__(self, other):
        a = []
        b = []
        for i in range(len(self.my_list)):
            for i_2 in range (len(other.my_list[i])):
                c = self.my_list[i][i_2]+other.my_list[i][i_2]
                b.append(c)
                if len(b) == len(self.my_list):
                    a.append(b)
                    b = []
        return Matrix(a)




m1 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
m2 = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2]])
print(m1.__str__())
print(m2.__str__())
print(m1.__add__(m2))