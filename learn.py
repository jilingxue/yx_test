class Request():
    name = 'xiaoming'
    age = '13'
    def __init__(self,name,age):
        self.name = name
        self.age = age
re = Request('xiaohong','28')
print(re)