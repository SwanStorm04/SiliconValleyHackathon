import tkinter

class CollegeStudent:

    def __init__(self):
        self.collWindow = tkinter.Tk()
        self.collWindow.configure(bg = "peachPuff")

        self.topSpaceFrame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.foodFrame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.midSpace1Frame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.freeFrame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.midSpace2Frame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.edFrame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.midSpace3Frame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.actFrame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.collWindow, bg = "peachPuff", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "peachPuff", text = "   ")
        self.topSpace.pack()
        self.midSpace1 = tkinter.Label(self.midSpace1Frame, bg = "peachPuff", text = "   ")
        self.midSpace1.pack()
        self.midSpace2 = tkinter.Label(self.midSpace2Frame, bg = "peachPuff", text = "   ")
        self.midSpace2.pack()
        self.midSpace3 = tkinter.Label(self.midSpace3Frame, bg = "peachPuff", text = "   ")
        self.midSpace3.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "peachPuff", text = "   ")
        self.botSpace.pack()

        self.foodLabel = tkinter.Label(self.foodFrame, bg = "peachPuff", font = "times 14 bold", text = "Food Options")
        self.foodSpace = tkinter.Label(self.foodFrame, bg = "peachPuff", text = "   ")
        self.foodLeftSpace = tkinter.Label(self.foodFrame, bg = "peachPuff", text = "   ")
        self.gluButton = tkinter.Button(self.foodFrame, command = self.gluten, width = 20, height = 2, bg = "yellowGreen", font = "times 12 bold", text = "Gluten-Free")
        self.foodMidSpace1 = tkinter.Label(self.foodFrame, bg = "peachPuff", text = "   ")
        self.vegButton = tkinter.Button(self.foodFrame, command = self.veggie, width = 20, height = 2, bg = "green", font = "times 12 bold", text = "Vegetarian/Vegan")
        self.foodMidSpace2 = tkinter.Label(self.foodFrame, bg = "peachPuff", text = "   ")
        self.dairyButton = tkinter.Button(self.foodFrame, command = self.dairy, width = 20, height = 2, bg = "mediumSpringGreen", font = "times 12 bold", text = "Dairy-Free")
        self.foodMidSpace3 = tkinter.Label(self.foodFrame, bg = "peachPuff", text = "   ")
        self.cheapButton = tkinter.Button(self.foodFrame, command = self.cheap, width = 20, height = 2, bg = "limeGreen", font = "times 12 bold", text = "Cheap")
        self.foodRightSpace = tkinter.Label(self.foodFrame, bg = "peachPuff", text = "   ")

        self.foodLabel.pack()
        self.foodSpace.pack()
        self.foodLeftSpace.pack(side = "left")
        self.gluButton.pack(side = "left")
        self.foodMidSpace1.pack(side = "left")
        self.vegButton.pack(side = "left")
        self.foodMidSpace2.pack(side = "left")
        self.dairyButton.pack(side = "left")
        self.foodMidSpace3.pack(side = "left")
        self.cheapButton.pack(side = "left")
        self.foodRightSpace.pack(side = "left")

        self.freeLabel = tkinter.Label(self.freeFrame, bg = "peachPuff", font = "times 14 bold", text = "Free and Discounted Things")
        self.freeSpace = tkinter.Label(self.freeFrame, bg = "peachPuff", text = "   ")
        self.freeLeftSpace = tkinter.Label(self.freeFrame, bg = "peachPuff", text = "   ")
        self.internetButton = tkinter.Button(self.freeFrame, command = self.internet, width = 20, height = 2, bg = "red", font = "times 12 bold", text = "Internet")
        self.freeMidSpace1 = tkinter.Label(self.freeFrame, bg = "peachPuff", text = "   ")
        self.discountButton = tkinter.Button(self.freeFrame, command = self.discount, width = 20, height = 2, bg = "orangeRed", font = "times 12 bold", text = "Discounts")
        self.freeMidSpace2 = tkinter.Label(self.freeFrame, bg = "peachPuff", text = "   ")
        self.foodButton = tkinter.Button(self.freeFrame, command = self.food, width = 20, height = 2, bg = "firebrick", font = "times 12 bold", text = "Food")
        self.freeRightSpace = tkinter.Label(self.freeFrame, bg = "peachPuff", text = "   ")

        self.freeLabel.pack()
        self.freeSpace.pack()
        self.freeLeftSpace.pack(side = "left")
        self.internetButton.pack(side = "left")
        self.freeMidSpace1.pack(side = "left")
        self.discountButton.pack(side = "left")
        self.freeMidSpace2.pack(side = "left")
        self.foodButton.pack(side = "left")
        self.freeRightSpace.pack(side = "left")

        self.edLabel = tkinter.Label(self.edFrame, bg = "peachPuff", font = "times 14 bold", text = "Learning and Education")
        self.edSpace = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")
        self.edLeftSpace = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")
        self.learnButton = tkinter.Button(self.edFrame, command = self.classes, width = 20, height = 2, bg = "blue", font = "times 12 bold", text = "Online Classes")
        self.edMidSpace1 = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")
        self.callButton = tkinter.Button(self.edFrame, command = self.facetime, width = 20, height = 2, bg = "cornflowerBlue", font = "times 12 bold", text = "Face Calls")
        self.edMidSpace2 = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")
        self.healthButton = tkinter.Button(self.edFrame, command = self.health, width = 20, height = 2, bg = "deepSkyBlue", font = "times 12 bold", text = "Health")
        self.edMidSpace3 = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")
        self.fixButton = tkinter.Button(self.edFrame, command = self.fix, width = 20, height = 2, bg = "mediumBlue", font = "times 12 bold", text = "Fix-Ups")
        self.edMidSpace4 = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")
        self.orderButton = tkinter.Button(self.edFrame, command = self.order, width = 20, height = 2, bg = "darkTurquoise", font = "times 12 bold", text = "Ordering Online")
        self.edMidSpace5 = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")
        self.workButton = tkinter.Button(self.edFrame, command = self.work, width = 20, height = 2, bg = "steelBlue", font = "times 12 bold", text = "Career")
        self.edRightSpace = tkinter.Label(self.edFrame, bg = "peachPuff", text = "   ")

        self.edLabel.pack()
        self.edSpace.pack()
        self.edLeftSpace.pack(side = "left")
        self.learnButton.pack(side = "left")
        self.edMidSpace1.pack(side = "left")
        self.callButton.pack(side = "left")
        self.edMidSpace2.pack(side = "left")
        self.healthButton.pack(side = "left")
        self.edMidSpace3.pack(side = "left")
        self.fixButton.pack(side = "left")
        self.edMidSpace4.pack(side = "left")
        self.orderButton.pack(side = "left")
        self.edMidSpace5.pack(side = "left")
        self.workButton.pack(side = "left")
        self.edRightSpace.pack(side = "left")

        self.actLabel = tkinter.Label(self.actFrame, bg = "peachPuff", font = "times 14 bold", text = "Activities")
        self.actSpace = tkinter.Label(self.actFrame, bg = "peachPuff", text = "   ")
        self.actLeftSpace = tkinter.Label(self.actFrame, bg = "peachPuff", text = "   ")
        self.bookButton = tkinter.Button(self.actFrame, command = self.book, width = 20, height = 2, bg = "lemonChiffon", font = "times 12 bold", text = "Books")
        self.actMidSpace1 = tkinter.Label(self.actFrame, bg = "peachPuff", text = "   ")
        self.movieButton = tkinter.Button(self.actFrame, command = self.movie, width = 20, height = 2, bg = "darkGoldenrod", font = "times 12 bold", text = "Movies and TV Shows")
        self.actMidSpace2 = tkinter.Label(self.actFrame, bg = "peachPuff", text = "   ")
        self.diyButton = tkinter.Button(self.actFrame, command = self.diy, width = 20, height = 2, bg = "gold", font = "times 12 bold", text = "Do-It-Yourself Projects")
        self.actMidSpace3 = tkinter.Label(self.actFrame, bg = "peachPuff", text = "   ")
        self.gameButton = tkinter.Button(self.actFrame, command = self.game, width = 20, height = 2, bg = "goldenrod", font = "times 12 bold", text = "Games")
        self.actMidSpace4 = tkinter.Label(self.actFrame, bg = "peachPuff", text = "   ")
        self.exerButton = tkinter.Button(self.actFrame, command = self.exercise, width = 20, height = 2, bg = "yellow", font = "times 12 bold", text = "Exercises")
        self.actRightSpace = tkinter.Label(self.actFrame, bg = "peachPuff", text = "   ")

        self.actLabel.pack()
        self.actSpace.pack()
        self.actLeftSpace.pack(side = "left")
        self.bookButton.pack(side = "left")
        self.actMidSpace1.pack(side = "left")
        self.movieButton.pack(side = "left")
        self.actMidSpace2.pack(side = "left")
        self.diyButton.pack(side = "left")
        self.actMidSpace3.pack(side = "left")
        self.gameButton.pack(side = "left")
        self.actMidSpace4.pack(side = "left")
        self.exerButton.pack(side = "left")
        self.actRightSpace.pack(side = "left")

        self.topSpaceFrame.pack()
        self.foodFrame.pack()
        self.midSpace1Frame.pack()
        self.freeFrame.pack()
        self.midSpace2Frame.pack()
        self.edFrame.pack()
        self.midSpace3Frame.pack()
        self.actFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop()


    def gluten(self):
        window = tkinter.Tk()
        window.configure(bg = "yellowGreen")

        infoFrame = tkinter.Frame(window, bg = "yellowGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "yellowGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "yellowGreen", fg = "maroon", font = "times 12 bold", text = "Whether you have Celiac disease or are just on a diet,\ngluten-free meals are always a great choice")
        genSpace = tkinter.Label(infoFrame, bg = "yellowGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "yellowGreen", fg = "maroon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some gluten-free meal ideas")
        line = 1
        linkList = ["https://www.thespruceeats.com/gluten-free-budget-recipes-1451337", "https://www.cottercrunch.com/budget-friendly-gluten-free-meal-plan/", "https://urbantastebud.com/cheap-healthy-gluten-free-recipes/", "https://www.budgetbytes.com/category/recipes/gluten-free/", "https://mygluten-freekitchen.com/surviving-september-4-weeks-of-easy-gluten-free-dinner-ideas/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "yellowGreen", fg = "maroon", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def veggie(self):
        window = tkinter.Tk()
        window.configure(bg = "green")

        infoFrame = tkinter.Frame(window, bg = "green", width = 300)
        linkFrame = tkinter.Frame(window, bg = "green", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "green", fg = "mistyRose", font = "times 12 bold", text = "Whether you are allergic to meat or just on a diet,\n vegetarian and vegan meals are always good and healthy")
        genSpace = tkinter.Label(infoFrame, bg = "green", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "green", fg = "mistyRose", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some vegetarian and vegan meals")
        line = 1
        linkList = ["https://cookieandkate.com/29-best-vegetarian-recipes/", "https://www.womansday.com/food-recipes/food-drinks/g2373/vegetarian-recipes/", "https://www.feastingathome.com/vegan-dinner-recipes/", "https://www.goodhousekeeping.com/food-recipes/healthy/g807/vegan-recipes/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "green", fg = "mistyRose", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def dairy(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumSpringGreen")

        infoFrame = tkinter.Frame(window, bg = "mediumSpringGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumSpringGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumSpringGreen", fg = "brown", font = "times 12 bold", text = "Whether you are lactose-intolerant or just on a diet\ndairy-free food is always good")
        genSpace = tkinter.Label(infoFrame, bg = "mediumSpringGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumSpringGreen", fg = "brown", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some good dairy-free recipes")
        line = 1
        linkList = ["https://www.tasteofhome.com/collection/dairy-free-dinners/", "https://www.tasteofhome.com/collection/dairy-free-recipes/", "https://www.allrecipes.com/recipes/738/healthy-recipes/dairy-free/", "https://www.godairyfree.org/dairy-free-recipes"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumSpringGreen", fg = "brown", font = "times 12 bold", width = 55)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def cheap(self):
        window = tkinter.Tk()
        window.configure(bg = "limeGreen")

        infoFrame = tkinter.Frame(window, bg = "limeGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "limeGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "limeGreen", fg = "firebrick", font = "times 12 bold", text = "In times when you have a tight budget,\ncheap food is necessary but it still has to be good")
        genSpace = tkinter.Label(infoFrame, bg = "limeGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "limeGreen", fg = "firebrick", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some good, cheap, food")
        line = 1
        linkList = ["https://www.tasteofhome.com/collection/cheap-dinner-ideas/", "https://www.thesimpledollar.com/save-money/20-favorite-dirt-cheap-meals/", "https://blog.cheapism.com/cheap-easy-weeknight-dinners/", "https://www.bonappetit.com/gallery/cheap-recipes"]
        linkBox = tkinter.Listbox(linkFrame, bg = "limeGreen", fg = "firebrick", font = "times 12 bold", width = 70)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def internet(self):
        window = tkinter.Tk()
        window.configure(bg = "red")

        infoFrame = tkinter.Frame(window, bg = "red", width = 300)
        linkFrame = tkinter.Frame(window, bg = "red", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "red", fg = "lightGreen", font = "times 12 bold", text = "Many places are currently offering reduced price or free internet,\nbut it's always good to look at internet options")
        genSpace = tkinter.Label(infoFrame, bg = "red", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "red", fg = "lightGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for information on cheaper internet and internet plans")
        line = 1
        linkList = ["https://www.highspeedinternet.com/resources/internet-guide-during-coronavirus-outbreak", "https://www.nytimes.com/2020/03/26/business/coronavirus-internet-traffic-speed.html", "https://www.allconnect.com/internet", "https://www.reviews.org/internet-service/best-internet-service-providers/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "red", fg = "lightGreen", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def discount(self):
        window = tkinter.Tk()
        window.configure(bg = "orangeRed")

        infoFrame = tkinter.Frame(window, bg = "orangeRed", width = 300)
        linkFrame = tkinter.Frame(window, bg = "orangeRed", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "orangeRed", fg = "aquamarine", font = "times 12 bold", text = "There are many ways to get discounts online,\nfrom special promotions to coupons")
        genSpace = tkinter.Label(infoFrame, bg = "orangeRed", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "orangeRed", fg = "aquamarine", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for information on getting discounts")
        line = 1
        linkList = ["https://www.joinhoney.com/", "https://wikibuy.com/", "https://www.retailmenot.com/", "https://slickdeals.net/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "orangeRed", fg = "aquamarine", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

        
    def food(self):
        window = tkinter.Tk()
        window.configure(bg = "fireBrick")

        infoFrame = tkinter.Frame(window, bg = "fireBrick", width = 300)
        linkFrame = tkinter.Frame(window, bg = "fireBrick", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "fireBrick", fg = "yellowGreen", font = "times 12 bold", text = "Cheap food is always good, especially on a tight budget")
        genSpace = tkinter.Label(infoFrame, bg = "fireBrick", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "fireBrick", fg = "yellowGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some cheap grocery ideas")
        line = 1
        linkList = ["https://familiesforfinancialfreedom.com/cheapest-groceries-list/", "https://www.tasteofhome.com/collection/cheap-groceries/", "https://funcheaporfree.com/how-i-grocery-shop/", "https://www.cheatsheet.com/money-career/6-cheapest-grocery-stores-in-the-u-s.html/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "fireBrick", fg = "yellowGreen", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def classes(self):
        window = tkinter.Tk()
        window.configure(bg = "blue")

        infoFrame = tkinter.Frame(window, bg = "blue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "blue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "blue", fg = "moccasin", font = "times 12 bold", text = "You can take classes online or learn new skills in your freetime")
        genSpace = tkinter.Label(infoFrame, bg = "blue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "blue", fg = "moccasin", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some websites so you can learn new skills")
        line = 1
        linkList = ["https://www.udemy.com/", "https://www.coursera.org/", "https://www.skillshare.com/", "https://www.edx.org/", "https://www.masterclass.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "blue", fg = "moccasin", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def facetime(self):
        window = tkinter.Tk()
        window.configure(bg = "cornflowerBlue")

        infoFrame = tkinter.Frame(window, bg = "cornflowerBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "cornflowerBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "cornflowerBlue", fg = "orangeRed", font = "times 12 bold", text = "Whether for online classes, to see friends and family,\nor for interviews, ways to facetime others are very important")
        genSpace = tkinter.Label(infoFrame, bg = "cornflowerBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "cornflowerBlue", fg = "orangeRed", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some face call apps")
        line = 1
        linkList = ["https://zoom.us/", "https://discordapp.com/", "https://www.skype.com/en/", "https://hangouts.google.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "cornflowerBlue", fg = "orangeRed", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def health(self):
        window = tkinter.Tk()
        window.configure(bg = "deepSkyBlue")

        infoFrame = tkinter.Frame(window, bg = "deepSkyBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "deepSkyBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "deepSkyBlue", fg = "antiqueWhite", font = "times 12 bold", text = "Looking after your health, especially in close quarters with others,\nis important because you getting sick could get others sick")
        genSpace = tkinter.Label(infoFrame, bg = "deepSkyBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "deepSkyBlue", fg = "antiqueWhite", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for")
        line = 1
        linkList = ["https://www.onlinecolleges.net/for-students/student-health-wellness-guide/", "https://www.purdueglobal.edu/blog/student-life/health-and-wellness-guide-for-college-students/", "https://www.bestcolleges.com/blog/mental-physical-health-college/", "https://studenthealth.georgetown.edu/health-issues/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "deepSkyBlue", fg = "antiqueWhite", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def fix(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumBlue")

        infoFrame = tkinter.Frame(window, bg = "mediumBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumBlue", fg = "papayaWhip", font = "times 12 bold", text = "Knowing how to fix simple problems around the home\nsaves money and time as well as being more convenient")
        genSpace = tkinter.Label(infoFrame, bg = "mediumBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumBlue", fg = "papayaWhip", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for how-to fix simple problems")
        line = 1
        linkList = ["https://www.businessinsider.com/20-handyman-skills-that-everyone-should-have-2014-3", "https://www.realsimple.com/home-organizing/diy-home-improvement", "https://www.familyhandyman.com/smart-homeowner/100-home-repairs-you-can-do-yourself/", "https://lifehacker.com/the-most-common-home-repairs-you-can-easily-do-yourself-1445435125"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumBlue", fg = "papayaWhip", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def order(self):
        window = tkinter.Tk()
        window.configure(bg = "darkTurquoise")

        infoFrame = tkinter.Frame(window, bg = "darkTurquoise", width = 300)
        linkFrame = tkinter.Frame(window, bg = "darkTurquoise", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "darkTurquoise", fg = "tomato", font = "times 12 bold", text = "Online shopping is fun,\nbut it can be expensive or difficult to do")
        genSpace = tkinter.Label(infoFrame, bg = "darkTurquoise", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "darkTurquoise", fg = "tomato", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for information on online shopping")
        line = 1
        linkList = ["https://www.amazon.com/", "https://www.finder.com/online-shopping", "https://www.wish.com/", "https://www.joinhoney.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkTurquoise", fg = "tomato", font = "times 12 bold", width = 35)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def work(self):
        window = tkinter.Tk()
        window.configure(bg = "steelBlue")

        infoFrame = tkinter.Frame(window, bg = "steelBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "steelBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "steelBlue", fg = "salmon", font = "times 12 bold", text = "Knowing what your career options are\nand what the laws regarding that are is important\nin choosing a career you like")
        genSpace = tkinter.Label(infoFrame, bg = "steelBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "steelBlue", fg = "salmon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some career information")
        line = 1
        linkList = ["https://www.linkedin.com/", "https://www.irs.gov/", "https://www.usa.gov/labor-laws", "https://rica.rocklinusd.org/documents/GradPortfolioFiles/Standard%20Application.pdf", "https://zety.com/blog/resume-tips"]
        linkBox = tkinter.Listbox(linkFrame, bg = "steelBlue", fg = "salmon", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def book(self):
        window = tkinter.Tk()
        window.configure(bg = "lemonChiffon")

        infoFrame = tkinter.Frame(window, bg = "lemonChiffon", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lemonChiffon", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lemonChiffon", fg = "indigo", font = "times 12 bold", text = "Reading is a good way to relax and be in a different world\nand it's cheap as well as educational entertainment")
        genSpace = tkinter.Label(infoFrame, bg = "lemonChiffon", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lemonChiffon", fg = "indigo", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some books to read")
        line = 1
        linkList = ["https://www.lifehack.org/articles/lifestyle/25-essential-books-that-every-college-student-should-read.html", "https://grownandflown.com/books-college-students/", "https://www.collegemagazine.com/10-inspiring-books-college-students-read/", "https://www.barnesandnoble.com/b/books/school-teen-fiction/college-life-teen-fiction/_/N-29Z8q8Z1a2l", "https://elearningindustry.com/top-10-books-every-college-student-read"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lemonChiffon", fg = "indigo", font = "times 12 bold", width = 90)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def movie(self):
        window = tkinter.Tk()
        window.configure(bg = "darkGoldenrod")

        infoFrame = tkinter.Frame(window, bg = "darkGoldenrod", width = 300)
        linkFrame = tkinter.Frame(window, bg = "darkGoldenrod", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "darkGoldenrod", fg = "plum", font = "times 12 bold", text = "Movies and TV shows are good, mindless forms of entertainment,\nor nice to put on as background noise")
        genSpace = tkinter.Label(infoFrame, bg = "darkGoldenrod", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "darkGoldenrod", fg = "plum", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some movies and tv shows to watch")
        line = 1
        linkList = ["https://www.hercampus.com/school/bryant/14-must-watch-netflix-shows-college-students", "https://www.imdb.com/list/ls033093453/", "https://www.imdb.com/list/ls021701554/", "https://www.imdb.com/list/ls021701554/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkGoldenrod", fg = "plum", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def diy(self):
        window = tkinter.Tk()
        window.configure(bg = "gold")

        infoFrame = tkinter.Frame(window, bg = "gold", width = 300)
        linkFrame = tkinter.Frame(window, bg = "gold", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "gold", fg = "purple", font = "times 12 bold", text = "Projects are good, personal gifts\nor just fun things to make in your free time to decorate\nor add function to an area")
        genSpace = tkinter.Label(infoFrame, bg = "gold", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "gold", fg = "purple", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for project ideas")
        line = 1
        linkList = ["https://www.youtube.com/watch?v=VIVIegSt81k", "https://www.fastweb.com/student-life/articles/the-10-diy-dorm-room-projects", "https://www.instructables.com/id/Projects-for-College-Students/", "https://www.origami-resource-center.com/school-projects.html"]
        linkBox = tkinter.Listbox(linkFrame, bg = "gold", fg = "purple", font = "times 12 bold", width = 70)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def game(self):
        window = tkinter.Tk()
        window.configure(bg = "goldenrod")

        infoFrame = tkinter.Frame(window, bg = "goldenrod", width = 300)
        linkFrame = tkinter.Frame(window, bg = "goldenrod", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "goldenrod", fg = "thistle", font = "times 12 bold", text = "Games are a fun way to connect with others\nor pass the time without thinking too hard")
        genSpace = tkinter.Label(infoFrame, bg = "goldenrod", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "goldenrod", fg = "thistle", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some online games\nand card or board games")
        line = 1
        linkList = ["https://www.scholarshippoints.com/campuslife/best-party-games-for-college-students/", "https://www.collegeraptor.com/find-colleges/articles/student-life/7-great-college-party-games-for-your-study-breaks/", "https://www.collegemagazine.com/top-10-computer-games-for-college-kids/", "https://www.hercampus.com/school/ucd/best-party-games-college-students"]
        linkBox = tkinter.Listbox(linkFrame, bg = "goldenrod", fg = "thistle", font = "times 12 bold", width = 100)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def exercise(self):
        window = tkinter.Tk()
        window.configure(bg = "yellow")

        infoFrame = tkinter.Frame(window, bg = "yellow", width = 300)
        linkFrame = tkinter.Frame(window, bg = "yellow", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "yellow", fg = "darkOrchid", font = "times 12 bold", text = "Exercise is a good way to relieve stress\nand stay healthy")
        genSpace = tkinter.Label(infoFrame, bg = "yellow", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "yellow", fg = "darkOrchid", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for exercise tips")
        line = 1
        linkList = ["https://www.acmc.edu/top-exercise-tips-for-busy-students/", "https://www.affordablecollegesonline.org/college-resource-center/staying-fit-on-campus/", "https://www.accreditedschoolsonline.org/resources/student-workouts/", "https://www.theodysseyonline.com/10-exercises-college-student-accomplish"]
        linkBox = tkinter.Listbox(linkFrame, bg = "yellow", fg = "darkOrchid", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()



