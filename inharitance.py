
# İnharitance(Kalıtım) = miras alma

# Person => name,lastname,age,eat,run,drink
# Student(Person) , Theacher(Person)

# Animal => Dog(Animal) , Cat(Animal)

class Person():
    def __init__(self,fname,lname):
        Person.firstname=fname
        Person.lastname=lname
        print('Person created') 

    def who_am_ı(self):
        print('I am a person')

    def eat(self):
        print('I am eatıng')
        

class Student(Person): # Persondan kalıtım ile bilgileri student'a attık.
    def __init__(self,fname,lname,number): #student ıcerısınde tekrar fırsname lastname olusturmamız gerek onları person dan aldık
        Person.__init__(self,fname,lname) # bunu demezsek student'ın initi person'ın initini ezer. 
        # oyuzden tekrar person'ın initini cagırmamız gerekır. çünkü student için de ozel ısteklerde bulunabılırız arada person kaynar.
        print('student created')
        self.studentnumber=number # student a ozel oldugu ıcın burda atamasını yaptık.Yanı class attrıbutes tanımladık 
       
        # Overrride : student uzerınden who am I 'ı cagırırsak person classındakı who am I 'ı ezer buna overrıde denır
        # 26. line da peron.__init__ ile tekrardan cagırmamızın nedenı oydu override olmamasını ıstedık ve ıkı sefer person created yazdırdık
    def who_am_ı(self):
        print('I am a Student')  

    def sayhello(self):
        print('Hello I am a Student')


class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname) # line 26 da oldugu gıbı person'ın overrıde olmasını ıstemedıgımız ıcın tekrar init ile
        # cagırmamız gerekırdı super() metodunu cagırdıgımız zaman self ıslemını kullanmamıza gerek kalmadı.
        # super().__init__(fname,lname) methodunun karsılıgı => Person.__init__(self,fname,lname)' dir
        self.branch=branch
    def who_am_ı(self):
        print(f'I am a {self.branch} teacher')


p1=Person('ahmet','samıl')  
s1=Student('turan','arslan',1245)   
t1=Teacher('yusuf','arslan','math')

print(p1.firstname+' '+p1.lastname)
print(s1.firstname+' '+s1.lastname+' '+str(s1.studentnumber))

p1.who_am_ı()
s1.who_am_ı()
t1.who_am_ı()

p1.eat()
s1.eat()

s1.sayhello()

