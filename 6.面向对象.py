# 1.类和实例

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print ("调用父类构造函数")

   def parentMethod(self):
      print ('调用父类方法')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("父类属性 :", Parent.parentAttr)

class Child(Parent): # 定义子类
   def __init__(self):
      print ("调用子类构造方法")

   def childMethod(self):
      print ('调用子类方法 child method')

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法

# 2.访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__scor

# 3.继承和多态

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的

# 4.获取对象信息 

# 1).使用type()

# 2).使用isinstance() isinstance([1, 2, 3], (list, tuple))
 
# 3).使用dir() 获得一个对象的所有属性和方法

# 4.实例属性和类属性 由于Python是动态语言，根据类创建的实例可以任意绑定属性