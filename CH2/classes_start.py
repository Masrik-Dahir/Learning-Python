#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print("myClass method1")
    def method2(self, someString):
        print ("Good Morning", someString)
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print ("anotherClass method2")
    def method2(self, someString):
        myClass.method2(self,someString)
        print("Good Evening", someString)

def main():
    c = myClass()
    c.method1()
    c.method2("Masrik")
    
    c2 = anotherClass()
    c2.method1()
    c2.method2("Dewey Taylor")
    
if __name__ == "__main__":
    main()
