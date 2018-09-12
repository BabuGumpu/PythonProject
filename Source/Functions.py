# Functions

def welcome():
    print('Welcome to the Functions')


welcome()


def usernameAndPassowrd(user, password):
    print(user)
    print(password)
    print("USer Name is -->%s and password is -->%s" % ("BabuG", "Password"))


usernameAndPassowrd("BabuGumpu", "BreakingTheLaw")


def sumOfTwo(a, b):
    return a + b


result = sumOfTwo(1222, 3456)
print(result)


def list_benefits():
    print("More organized code")
    print("More readable code")
    print("Easier code reuse")


list_benefits()


def build_sentence(str):
    print("%s is a benefit of functions!" % str)
