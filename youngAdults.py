import tkinter

class YoungAdult:
    
    def __init__(self):
        self.yaWindow = tkinter.Tk()
        self.yaWindow.configure(bg = "wheat")

        self.topSpaceFrame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.foodFrame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.midSpace1Frame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.edFrame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.midSpace2Frame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.actFrame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.midSpace3Frame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.freeFrame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.yaWindow, bg = "wheat", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "wheat", text = "   ")
        self.topSpace.pack()
        self.midSpace1 = tkinter.Label(self.midSpace1Frame, bg = "wheat", text = "   ")
        self.midSpace1.pack()
        self.midSpace2 = tkinter.Label(self.midSpace2Frame, bg = "wheat", text = "   ")
        self.midSpace2.pack()
        self.midSpace3 = tkinter.Label(self.midSpace3Frame, bg = "wheat", text = "   ")
        self.midSpace3.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "wheat", text = "   ")
        self.botSpace.pack()

        self.foodLabel = tkinter.Label(self.foodFrame, bg = "wheat", font = "times 14 bold", text = "Meal Options")
        self.foodSpace = tkinter.Label(self.foodFrame, bg = "wheat", text = "   ")
        self.foodLeftSpace = tkinter.Label(self.foodFrame, bg = "wheat", text = "   ")
        self.gluButton = tkinter.Button(self.foodFrame, command = self.gluten, width = 20, height = 2, bg = "mediumSeaGreen", font = "times 12 bold", text = "Gluten-Free")
        self.foodMidSpace1 = tkinter.Label(self.foodFrame, bg = "wheat", text = "   ")
        self.vegButton = tkinter.Button(self.foodFrame, command = self.veggie, width = 20, height = 2, bg = "forestGreen", font = "times 12 bold", text = "Vegetarian/Vegan")
        self.foodMidSpace2 = tkinter.Label(self.foodFrame, bg = "wheat", text = "   ")
        self.dairyButton = tkinter.Button(self.foodFrame, command = self.dairy, width = 20, height = 2, bg = "mediumSpringGreen", font = "times 12 bold", text = "Dairy-Free")
        self.foodMidSpace3 = tkinter.Label(self.foodFrame, bg = "wheat", text = "   ")
        self.kidButton = tkinter.Button(self.foodFrame, command = self.kid, width = 20, height = 2, bg = "limeGreen", font = "times 12 bold", text = "Kids")
        self.foodRightSpace = tkinter.Label(self.foodFrame, bg = "wheat", text = "   ")

        self.foodLabel.pack()
        self.foodSpace.pack()
        self.foodLeftSpace.pack(side = "left")
        self.gluButton.pack(side = "left")
        self.foodMidSpace1.pack(side = "left")
        self.vegButton.pack(side = "left")
        self.foodMidSpace2.pack(side = "left")
        self.dairyButton.pack(side = "left")
        self.foodMidSpace3.pack(side = "left")
        self.kidButton.pack(side = "left")
        self.foodRightSpace.pack(side = "left")

        self.edLabel = tkinter.Label(self.edFrame, bg = "wheat", font = "times 14 bold", text = "Information and Learning")
        self.edSpace = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")
        self.edLeftSpace = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")
        self.classButton = tkinter.Button(self.edFrame, command = self.classes, width = 20, height = 2, bg = "mediumOrchid", font = "times 12 bold", text = "Online Learning")
        self.edMidSpace1 = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")
        self.callButton = tkinter.Button(self.edFrame, command = self.facetime, width = 20, height = 2, bg = "mediumPurple", font = "times 12 bold", text = "Face calls")
        self.edMidSpace2 = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")
        self.fixButton = tkinter.Button(self.edFrame, command = self.fix, width = 20, height = 2, bg = "purple", font = "times 12 bold", text = "Fix-Ups")
        self.edMidSpace3 = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")
        self.healthButton = tkinter.Button(self.edFrame, command = self.health, width = 20, height = 2, bg = "violet", font = "times 12 bold", text = "Health")
        self.edMidSpace4 = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")
        self.shopButton = tkinter.Button(self.edFrame, command = self.shop, width = 20, height = 2, bg = "darkOrchid", font = "times 12 bold", text = "Online Shopping")
        self.edMidSpace5 = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")
        self.workButton = tkinter.Button(self.edFrame, command = self.work, width = 20, height = 2, bg = "blueViolet", font = "times 12 bold", text = "Career")
        self.edRightSpace = tkinter.Label(self.edFrame, bg = "wheat", text = "   ")

        self.edLabel.pack()
        self.edSpace.pack()
        self.edLeftSpace.pack(side = "left")
        self.classButton.pack(side = "left")
        self.edMidSpace1.pack(side = "left")
        self.callButton.pack(side = "left")
        self.edMidSpace2.pack(side = "left")
        self.fixButton.pack(side = "left")
        self.edMidSpace3.pack(side = "left")
        self.healthButton.pack(side = "left")
        self.edMidSpace4.pack(side = "left")
        self.shopButton.pack(side = "left")
        self.edMidSpace5.pack(side = "left")
        self.workButton.pack(side = "left")
        self.edRightSpace.pack(side = "left")

        self.actLabel = tkinter.Label(self.actFrame, bg = "wheat", font = "times 14 bold", text = "Activities")
        self.actSpace = tkinter.Label(self.actFrame, bg = "wheat", text = "   ")
        self.actLeftSpace = tkinter.Label(self.actFrame, bg = "wheat", text = "   ")
        self.bookButton = tkinter.Button(self.actFrame, command = self.book, width = 20, height = 2, bg = "lightPink", font = "times 12 bold", text = "Books")
        self.actMidSpace1 = tkinter.Label(self.actFrame, bg = "wheat", text = "   ")
        self.movieButton = tkinter.Button(self.actFrame, command = self.movie, width = 20, height = 2, bg = "maroon", font = "times 12 bold", text = "Movies")
        self.actMidSpace2 = tkinter.Label(self.actFrame, bg = "wheat", text = "   ")
        self.gameButton = tkinter.Button(self.actFrame, command = self.game, width = 20, height = 2, bg = "lightCoral", font = "times 12 bold", text = "Games")
        self.actMidSpace3 = tkinter.Label(self.actFrame, bg = "wheat", text = "   ")
        self.exerButton = tkinter.Button(self.actFrame, command = self.exercise, width = 20, height = 2, bg = "crimson", font = "times 12 bold", text = "Exercise")
        self.actMidSpace4 = tkinter.Label(self.actFrame, bg = "wheat", text = "   ")
        self.diyButton = tkinter.Button(self.actFrame, command = self.diy, width = 20, height = 2, bg = "firebrick", font = "times 12 bold", text = "Do-It-Yourself Projects")
        self.actRightSpace = tkinter.Label(self.actFrame, bg = "wheat", text = "   ")

        self.actLabel.pack()
        self.actSpace.pack()
        self.actLeftSpace.pack(side = "left")
        self.bookButton.pack(side = "left")
        self.actMidSpace1.pack(side = "left")
        self.movieButton.pack(side = "left")
        self.actMidSpace2.pack(side = "left")
        self.gameButton.pack(side = "left")
        self.actMidSpace3.pack(side = "left")
        self.exerButton.pack(side = "left")
        self.actMidSpace4.pack(side = "left")
        self.diyButton.pack(side = "left")
        self.actRightSpace.pack(side = "left")

        self.freeLabel = tkinter.Label(self.freeFrame, bg = "wheat", font = "times 14 bold", text = "Free and Discounted Things")
        self.freeSpace = tkinter.Label(self.freeFrame, bg = "wheat", text = "   ")
        self.freeLeftSpace = tkinter.Label(self.freeFrame, bg = "wheat", text = "   ")
        self.interButton = tkinter.Button(self.freeFrame, command = self.internet, width = 20, height = 2, bg = "mediumBlue", font = "times 12 bold", text = "Internet")
        self.freeMidSpace1 = tkinter.Label(self.freeFrame, bg = "wheat", text = "   ")
        self.disButton = tkinter.Button(self.freeFrame, command = self.discount, width = 20, height = 2, bg = "dodgerBlue", font = "times 12 bold", text = "Discounts")
        self.freeMidSpace2 = tkinter.Label(self.freeFrame, bg = "wheat", text = "   ")
        self.foodButton = tkinter.Button(self.freeFrame, command = self.food, width = 20, height = 2, bg = "lightSeaGreen", font = "times 12 bold", text = "Food")
        self.freeRightSpace = tkinter.Label(self.freeFrame, bg = "wheat", text = "   ")

        self.freeLabel.pack()
        self.freeSpace.pack()
        self.freeLeftSpace.pack(side = "left")
        self.interButton.pack(side = "left")
        self.freeMidSpace1.pack(side = "left")
        self.disButton.pack(side = "left")
        self.freeMidSpace2.pack(side = "left")
        self.foodButton.pack(side = "left")
        self.freeRightSpace.pack(side = "left")

        self.topSpaceFrame.pack()
        self.foodFrame.pack()
        self.midSpace1Frame.pack()
        self.edFrame.pack()
        self.midSpace2Frame.pack()
        self.actFrame.pack()
        self.midSpace3Frame.pack()
        self.freeFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop()


    def gluten(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumSeaGreen")

        infoFrame = tkinter.Frame(window, bg = "mediumSeaGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumSeaGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumSeaGreen", fg = "firebrick", font = "times 12 bold", text = "Whether you have Celiac disease or are on a diet,\ngluten-free meals are always good")
        genSpace = tkinter.Label(infoFrame, bg = "mediumSeaGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumSeaGreen", fg = "firebrick", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for gluten-free recipes")
        line = 1
        linkList = ["https://www.thespruceeats.com/gluten-free-budget-recipes-1451337", "https://www.cottercrunch.com/budget-friendly-gluten-free-meal-plan/", "https://urbantastebud.com/cheap-healthy-gluten-free-recipes/", "https://www.budgetbytes.com/category/recipes/gluten-free/", "https://mygluten-freekitchen.com/surviving-september-4-weeks-of-easy-gluten-free-dinner-ideas/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumSeaGreen", fg = "firebrick", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def veggie(self):
        window = tkinter.Tk()
        window.configure(bg = "forestGreen")

        infoFrame = tkinter.Frame(window, bg = "forestGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "forestGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "forestGreen", fg = "pink", font = "times 12 bold", text = "Whether you can't eat meat or are on a diet,\nvegetarian and vegan meals are always good and healthy")
        genSpace = tkinter.Label(infoFrame, bg = "forestGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "forestGreen", fg = "pink", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for")
        line = 1
        linkList = ["https://cookieandkate.com/29-best-vegetarian-recipes/", "https://www.womansday.com/food-recipes/food-drinks/g2373/vegetarian-recipes/", "https://www.feastingathome.com/vegan-dinner-recipes/", "https://www.goodhousekeeping.com/food-recipes/healthy/g807/vegan-recipes/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "forestGreen", fg = "pink", font = "times 12 bold", width = 75)

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

        genInfo = tkinter.Label(infoFrame, bg = "mediumSpringGreen", fg = "crimson", font = "times 12 bold", text = "Whether you are lactose-intolerant or on a diet,\ndairy-free meals are good")
        genSpace = tkinter.Label(infoFrame, bg = "mediumSpringGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumSpringGreen", fg = "crimson", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for dairy-free recipes")
        line = 1
        linkList = ["https://www.tasteofhome.com/collection/dairy-free-dinners/", "https://www.tasteofhome.com/collection/dairy-free-recipes/", "https://www.allrecipes.com/recipes/738/healthy-recipes/dairy-free/", "https://www.godairyfree.org/dairy-free-recipes"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumSpringGreen", fg = "crimson", font = "times 12 bold", width = 55)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def kid(self):
        window = tkinter.Tk()
        window.configure(bg = "limeGreen")

        infoFrame = tkinter.Frame(window, bg = "limeGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "limeGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "limeGreen", fg = "maroon", font = "times 12 bold", text = "If you have kids that are picky eaters,\nfinding healthy meals can be hard")
        genSpace = tkinter.Label(infoFrame, bg = "limeGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "limeGreen", fg = "maroon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for good meals for kids")
        line = 1
        linkList = ["https://www.momables.com/healthy-kid-friendly-recipes/", "https://www.foodnetwork.com/recipes/packages/recipes-for-kids/healthy-meals-for-kids", "http://www.eatingwell.com/gallery/13903/a-month-of-healthy-dinner-ideas-for-kids/", "https://www.tasteofhome.com/collection/healthy-dinners-for-kids/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "limeGreen", fg = "maroon", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def classes(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumOrchid")

        infoFrame = tkinter.Frame(window, bg = "mediumOrchid", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumOrchid", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumOrchid", fg = "yellow", font = "times 12 bold", text = "It is always fun to learn new skills, to help with a career\nor impress your friends")
        genSpace = tkinter.Label(infoFrame, bg = "mediumOrchid", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumOrchid", fg = "yellow", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some websites to learn new skills")
        line = 1
        linkList = ["https://www.udemy.com/", "https://www.coursera.org/", "https://www.skillshare.com/", "https://www.edx.org/", "https://www.masterclass.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumOrchid", fg = "yellow", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def facetime(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumPurple")

        infoFrame = tkinter.Frame(window, bg = "mediumPurple", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumPurple", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumPurple", fg = "lemonChiffon", font = "times 12 bold", text = "Contacting others is important, especially now.\nYou can use face calls for meetings or just talking to friends")
        genSpace = tkinter.Label(infoFrame, bg = "mediumPurple", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumPurple", fg = "lemonChiffon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some apps to contact others")
        line = 1
        linkList = ["https://zoom.us/", "https://discordapp.com/", "https://www.skype.com/en/", "https://hangouts.google.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumPurple", fg = "lemonChiffon", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def fix(self):
        window = tkinter.Tk()
        window.configure(bg = "purple")

        infoFrame = tkinter.Frame(window, bg = "purple", width = 300)
        linkFrame = tkinter.Frame(window, bg = "purple", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "purple", fg = "khaki", font = "times 12 bold", text = "Being able to fix small things is very important,\nespecially if you can't get someone else to do it")
        genSpace = tkinter.Label(infoFrame, bg = "purple", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "purple", fg = "khaki", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for how to fix small annoyances")
        line = 1
        linkList = ["https://www.businessinsider.com/20-handyman-skills-that-everyone-should-have-2014-3", "https://www.realsimple.com/home-organizing/diy-home-improvement", "https://www.familyhandyman.com/smart-homeowner/100-home-repairs-you-can-do-yourself/", "https://lifehacker.com/the-most-common-home-repairs-you-can-easily-do-yourself-1445435125"]
        linkBox = tkinter.Listbox(linkFrame, bg = "purple", fg = "khaki", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def health(self):
        window = tkinter.Tk()
        window.configure(bg = "violet")

        infoFrame = tkinter.Frame(window, bg = "violet", width = 300)
        linkFrame = tkinter.Frame(window, bg = "violet", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "violet", fg = "papayaWhip", font = "times 12 bold", text = "Looking after your health is important\nwhen you might contact others or diseases are spreading")
        genSpace = tkinter.Label(infoFrame, bg = "violet", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "violet", fg = "papayaWhip", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for tips on how to look after your health")
        line = 1
        linkList = ["https://www.eufic.org/en/healthy-living/article/10-healthy-lifestyle-tips-for-adults", "https://www.niddk.nih.gov/health-information/weight-management/healthy-eating-physical-activity-for-life/health-tips-for-adults", "http://watchfit.com/general-health/6-healthy-living-tips-for-young-adults/", "https://www.livestrong.com/article/526249-nutrition-guidelines-for-young-adults/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "violet", fg = "papayaWhip", font = "times 12 bold", width = 110)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def shop(self):
        window = tkinter.Tk()
        window.configure(bg = "darkOrchid")

        infoFrame = tkinter.Frame(window, bg = "darkOrchid", width = 300)
        linkFrame = tkinter.Frame(window, bg = "darkOrchid", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "darkOrchid", fg = "moccasin", font = "times 12 bold", text = "Shopping online is fun, but it can be expensive\nor difficult to do")
        genSpace = tkinter.Label(infoFrame, bg = "darkOrchid", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "darkOrchid", fg = "moccasin", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for websites to shop on")
        line = 1
        linkList = ["https://www.amazon.com/", "https://www.finder.com/online-shopping", "https://www.wish.com/", "https://www.joinhoney.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkOrchid", fg = "moccasin", font = "times 12 bold", width = 35)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def work(self):
        window = tkinter.Tk()
        window.configure(bg = "blueViolet")

        infoFrame = tkinter.Frame(window, bg = "blueViolet", width = 300)
        linkFrame = tkinter.Frame(window, bg = "blueViolet", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "blueViolet", fg = "sandyBrown", font = "times 12 bold", text = "Knowing what you can do with your\ncareer is important to make the best decisions")
        genSpace = tkinter.Label(infoFrame, bg = "blueViolet", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "blueViolet", fg = "sandyBrown", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for career information")
        line = 1
        linkList = ["https://www.linkedin.com/", "https://www.irs.gov/", "https://www.usa.gov/labor-laws", "https://rica.rocklinusd.org/documents/GradPortfolioFiles/Standard%20Application.pdf", "https://zety.com/blog/resume-tips"]
        linkBox = tkinter.Listbox(linkFrame, bg = "blueViolet", fg = "sandyBrown", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def book(self):
        window = tkinter.Tk()
        window.configure(bg = "lightPink")

        infoFrame = tkinter.Frame(window, bg = "lightPink", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lightPink", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightPink", fg = "green", font = "times 12 bold", text = "Reading is a good way to spend free time and go into a different world\nas well as exercise your mind")
        genSpace = tkinter.Label(infoFrame, bg = "lightPink", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightPink", fg = "green", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for books to read")
        line = 1
        linkList = ["https://www.goodreads.com/shelf/show/books-for-adults", "https://www.goodreads.com/shelf/show/adult-fiction", "https://www.purewow.com/books/books-to-read-in-your-20s", "https://www.goodreads.com/shelf/show/books-to-read-in-your-20s"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightPink", fg = "green", font = "times 12 bold", width = 60)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def movie(self):
        window = tkinter.Tk()
        window.configure(bg = "maroon")

        infoFrame = tkinter.Frame(window, bg = "maroon", width = 300)
        linkFrame = tkinter.Frame(window, bg = "maroon", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "maroon", fg = "paleGreen", font = "times 12 bold", text = "Movies and TV shows are good ways to pass the time or\nplay in the background while you work")
        genSpace = tkinter.Label(infoFrame, bg = "maroon", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "maroon", fg = "paleGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some ideas of movies and tv shows")
        line = 1
        linkList = ["https://www.imdb.com/list/ls054421000/", "https://www.independent.co.uk/arts-entertainment/34-movies-to-watch-in-your-20s-a7636926.html", "https://www.insider.com/netflix-movies-to-watch-in-your-20s-2017-3", "https://www.cosmopolitan.com/entertainment/celebs/videos/a17565/best-tv-shows-for-twentysomethings/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "maroon", fg = "paleGreen", font = "times 12 bold", width = 90)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def game(self):
        window = tkinter.Tk()
        window.configure(bg = "lightCoral")

        infoFrame = tkinter.Frame(window, bg = "lightCoral", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lightCoral", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightCoral", fg = "darkGreen", font = "times 12 bold", text = "Games are good ways to bond or\nmindlessly pass the time")
        genSpace = tkinter.Label(infoFrame, bg = "lightCoral", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightCoral", fg = "darkGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for online games and card or board games")
        line = 1
        linkList = ["https://www.thespruce.com/board-games-for-college-kids-3570593", "https://www.amazon.com/slp/games-for-20-year-olds/xwwd25fxazhn8sy", "https://brightestyoungthings.com/articles/10-video-games-from-the-10s-that-might-get-you-into-video-games-in-the-20s", "https://www.theguardian.com/games/2019/sep/19/50-best-video-games-of-the-21st-century"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightCoral", fg = "darkGreen", font = "times 12 bold", width = 100)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def exercise(self):
        window = tkinter.Tk()
        window.configure(bg = "crimson")

        infoFrame = tkinter.Frame(window, bg = "crimson", width = 300)
        linkFrame = tkinter.Frame(window, bg = "crimson", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "crimson", fg = "yellowGreen", font = "times 12 bold", text = "Exercising is important to stay healthy and it's a good\nway to pass time")
        genSpace = tkinter.Label(infoFrame, bg = "crimson", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "crimson", fg = "yellowGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some exercise ideas")
        line = 1
        linkList = ["https://www.active.com/fitness/articles/15-workout-habits-you-should-establish-in-your-20s", "https://www.oprah.com/health/exercise-for-your-20s-30s-40s-50s-and-60s_1", "https://www.health24.com/Fitness/Exercise/the-best-exercise-for-your-body-in-your-20s-30s-and-40s-20181218", "https://www.verywellfit.com/get-skinny-healthy-and-fit-in-your-20s-3495413"]
        linkBox = tkinter.Listbox(linkFrame, bg = "crimson", fg = "yellowGreen", font = "times 12 bold", width = 95)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def diy(self):
        window = tkinter.Tk()
        window.configure(bg = "firebrick")

        infoFrame = tkinter.Frame(window, bg = "firebrick", width = 300)
        linkFrame = tkinter.Frame(window, bg = "firebrick", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "firebrick", fg = "chartreuse", font = "times 12 bold", text = "Projects are fun things to do with your hands during your free time\nthat you can personalize and give away")
        genSpace = tkinter.Label(infoFrame, bg = "firebrick", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "firebrick", fg = "chartreuse", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some project ideas")
        line = 1
        linkList = ["https://www.favecrafts.com/Gifts/22-Easy-Craft-Projects-For-Adults", "https://diyprojects.com/diy-crafts-for-adults/", "https://origami.me/diagrams/", "https://www.bhg.com/home-improvement/remodeling/budget-remodels/weekend-home-projects/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "firebrick", fg = "chartreuse", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def internet(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumBlue")

        infoFrame = tkinter.Frame(window, bg = "mediumBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumBlue", fg = "peachPuff", font = "times 12 bold", text = "Many places are offering free or discounted internet,\nand it is always good to check internet prices")
        genSpace = tkinter.Label(infoFrame, bg = "mediumBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumBlue", fg = "peachPuff", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for websites to check internet prices")
        line = 1
        linkList = ["https://www.highspeedinternet.com/resources/internet-guide-during-coronavirus-outbreak", "https://www.nytimes.com/2020/03/26/business/coronavirus-internet-traffic-speed.html", "https://www.allconnect.com/internet", "https://www.reviews.org/internet-service/best-internet-service-providers/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumBlue", fg = "peachPuff", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def discount(self):
        window = tkinter.Tk()
        window.configure(bg = "dodgerBlue")

        infoFrame = tkinter.Frame(window, bg = "dodgerBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "dodgerBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "dodgerBlue", fg = "saddleBrown", font = "times 12 bold", text = "There are many ways to discount during shopping")
        genSpace = tkinter.Label(infoFrame, bg = "dodgerBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "dodgerBlue", fg = "saddleBrown", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for websites for discounts")
        line = 1
        linkList = ["https://www.joinhoney.com/", "https://wikibuy.com/", "https://www.retailmenot.com/", "https://slickdeals.net/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "dodgerBlue", fg = "saddleBrown", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def food(self):
        window = tkinter.Tk()
        window.configure(bg = "lightSeaGreen")

        infoFrame = tkinter.Frame(window, bg = "lightSeaGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lightSeaGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightSeaGreen", fg = "lightSalmon", font = "times 12 bold", text = "Food is often expensive, but shopping\nfor groceries online can be cheap")
        genSpace = tkinter.Label(infoFrame, bg = "lightSeaGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightSeaGreen", fg = "lightSalmon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for cheap online groceries")
        line = 1
        linkList = ["https://familiesforfinancialfreedom.com/cheapest-groceries-list/", "https://www.tasteofhome.com/collection/cheap-groceries/", "https://funcheaporfree.com/how-i-grocery-shop/", "https://www.cheatsheet.com/money-career/6-cheapest-grocery-stores-in-the-u-s.html/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightSeaGreen", fg = "lightSalmon", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


