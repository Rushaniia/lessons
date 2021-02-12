class Example(Exception):

    def my_func(*args):
        try:
            arg1 = int(input("Enter first number: "))
            arg2 = int(input("Enter second number: "))
            if arg2 == 0:
                raise Example('Error. Division by zero')
            else:
                result = arg1 / arg2
                return result

        except ValueError:
            return 'Value error'
        except Example as err:
            return err


e = Example()

print(e.my_func())