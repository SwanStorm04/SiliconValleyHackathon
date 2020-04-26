import tkinter

class Adult:
    
    def __init__(self):
        adWindow = tkinter.Tk()
        adWindow.configure(bg = "cornsilk")

        self.topSpaceFrame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.edFrame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.midSpace1Frame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.healthFrame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.midSpace2Frame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.actFrame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.midSpace3Frame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.shopFrame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)
        self.botSpaceFrame = tkinter.Frame(adWindow, bg = "cornsilk", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "cornsilk", text = "   ")
        self.topSpace.pack()
        self.midSpace1 = tkinter.Label(self.midSpace1Frame, bg = "cornsilk", text = "   ")
        self.midSpace1.pack()
        self.midSpace2 = tkinter.Label(self.midSpace2Frame, bg = "cornsilk", text = "   ")
        self.midSpace2.pack()
        self.midSpace3 = tkinter.Label(self.midSpace3Frame, bg = "cornsilk", text = "   ")
        self.midSpace3.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "cornsilk", text = "   ")
        self.botSpace.pack()

        self.edLabel = tkinter.Label(self.edFrame, bg = "cornsilk", font = "times 14 bold", text = "Online Learning")
        self.edSpace = tkinter.Label(self.edFrame, bg = "cornsilk", text = "   ")
        self.edLeftSpace = tkinter.Label(self.edFrame, bg = "cornsilk", text = "   ")
        self.classButton = tkinter.Button(self.edFrame, command = self.classes, width = 20, height = 2, bg = "lightSkyBlue", font = "times 12 bold", text = "Online Classes")
        self.edMidSpace1 = tkinter.Label(self.edFrame, bg = "cornsilk", text = "   ")
        self.callButton = tkinter.Button(self.edFrame, command = self.facetime, width = 20, height = 2, bg = "powderBlue", font = "times 12 bold", text = "Connecting With Others")
        self.edMidSpace2 = tkinter.Label(self.edFrame, bg = "cornsilk", text = "   ")
        self.fixButton = tkinter.Button(self.edFrame, command = self.fix, width = 20, height = 2, bg = "paleTurquoise", font = "times 12 bold", text = "Fix-ups")
        self.edRightSpace = tkinter.Label(self.edFrame, bg = "cornsilk", text = "   ")

        self.edLabel.pack()
        self.edSpace.pack()
        self.edLeftSpace.pack(side = "left")
        self.classButton.pack(side = "left")
        self.edMidSpace1.pack(side = "left")
        self.callButton.pack(side = "left")
        self.edMidSpace2.pack(side = "left")
        self.fixButton.pack(side = "left")
        self.edRightSpace.pack(side = "left")

        self.healthLabel = tkinter.Label(self.healthFrame, bg = "cornsilk", font = "times 14 bold", text = "Health")
        self.healthSpace = tkinter.Label(self.healthFrame, bg = "cornsilk", text = "   ")
        self.heLeftSpace = tkinter.Label(self.healthFrame, bg = "cornsilk", text = "   ")
        self.infoButton = tkinter.Button(self.healthFrame, command = self.information, width = 20, height = 2, bg = "salmon", font = "times 12 bold", text = "Information")
        self.heMidSpace1 = tkinter.Label(self.healthFrame, bg = "cornsilk", text = "   ")
        self.retireButton = tkinter.Button(self.healthFrame, command = self.retirement, width = 20, height = 2, bg = "pink", font = "times 12 bold", text = "Retirement")
        self.heMidSpace2 = tkinter.Label(self.healthFrame, bg = "cornsilk", text = "   ")
        self.exerButton = tkinter.Button(self.healthFrame, command = self.exercise, width = 20, height = 2, bg = "lightCoral", font = "times 12 bold", text = "Exercise")
        self.heRightSpace = tkinter.Label(self.healthFrame, bg = "cornsilk", text = "   ")

        self.healthLabel.pack()
        self.healthSpace.pack()
        self.heLeftSpace.pack(side = "left")
        self.infoButton.pack(side = "left")
        self.heMidSpace1.pack(side = "left")
        self.retireButton.pack(side = "left")
        self.heMidSpace2.pack(side = "left")
        self.exerButton.pack(side = "left")
        self.heRightSpace.pack(side = "left")

        self.actLabel = tkinter.Label(self.actFrame, bg = "cornsilk", font = "times 14 bold", text = "Activities")
        self.actSpace = tkinter.Label(self.actFrame, bg = "cornsilk", text = "   ")
        self.actLeftSpace = tkinter.Label(self.actFrame, bg = "cornsilk", text = "   ")
        self.bookButton = tkinter.Button(self.actFrame, command = self.book, width = 20, height = 2, bg = "paleGreen", font = "times 12 bold", text = "Books")
        self.actMidSpace1 = tkinter.Label(self.actFrame, bg = "cornsilk", text = "   ")
        self.movieButton = tkinter.Button(self.actFrame, command = self.movie, width = 20, height = 2, bg = "mediumAquamarine", font = "times 12 bold", text = "Movies and TV Shows")
        self.actMidSpace2 = tkinter.Label(self.actFrame, bg = "cornsilk", text = "   ")
        self.diyButton = tkinter.Button(self.actFrame, command = self.diy, width = 20, height = 2, bg = "lightGreen", font = "times 12 bold", text = "Do-It-Yourself Projects")
        self.actMidSpace3 = tkinter.Label(self.actFrame, bg = "cornsilk", text = "   ")
        self.gameButton = tkinter.Button(self.actFrame, command = self.game, width = 20, height = 2, bg = "yellowGreen", font = "times 12 bold", text = "Games")
        self.actRightSpace = tkinter.Label(self.actFrame, bg = "cornsilk", text = "   ")

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
        self.actRightSpace.pack(side = "left")

        self.shopLabel = tkinter.Label(self.shopFrame, bg = "cornsilk", font = "times 14 bold", text = "Shopping")
        self.shopSpace = tkinter.Label(self.shopFrame, bg = "cornsilk", text = "   ")
        self.shopLeftSpace = tkinter.Label(self.shopFrame, bg = "cornsilk", text = "   ")
        self.disButton = tkinter.Button(self.shopFrame, command = self.discount, width = 20, height = 2, bg = "lemonChiffon", font = "times 12 bold", text = "Discounts")
        self.shopMidSpace1 = tkinter.Label(self.shopFrame, bg = "cornsilk", text = "   ")
        self.grocButton = tkinter.Button(self.shopFrame, command = self.groceries, width = 20, height = 2, bg = "khaki", font = "times 12 bold", text = "Groceries Online")
        self.shopMidSpace2 = tkinter.Label(self.shopFrame, bg = "cornsilk", text = "   ")
        self.otherButton = tkinter.Button(self.shopFrame, command = self.other, width = 20, height = 2, bg = "papayaWhip", font = "times 12 bold", text = "Other Shopping Online")
        self.shopMidSpace3 = tkinter.Label(self.shopFrame, bg = "cornsilk", text = "   ")
        self.storeButton = tkinter.Button(self.shopFrame, command = self.store, width = 20, height = 2, bg = "moccasin", font = "times 12 bold", text = "Shopping in Stores")
        self.shopRightSpace = tkinter.Label(self.shopFrame, bg = "cornsilk", text = "   ")

        self.shopLabel.pack()
        self.shopSpace.pack()
        self.shopLeftSpace.pack(side = "left")
        self.disButton.pack(side = "left")
        self.shopMidSpace1.pack(side = "left")
        self.grocButton.pack(side = "left")
        self.shopMidSpace2.pack(side = "left")
        self.otherButton.pack(side = "left")
        self.shopMidSpace3.pack(side = "left")
        self.storeButton.pack(side = "left")
        self.shopRightSpace.pack(side = "left")

        self.topSpaceFrame.pack()
        self.edFrame.pack()
        self.midSpace1Frame.pack()
        self.healthFrame.pack()
        self.midSpace2Frame.pack()
        self.actFrame.pack()
        self.midSpace3Frame.pack()
        self.shopFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop()


    def classes(self):
        window = tkinter.Tk()
        window.configure(bg = "lightSkyBlue")

        infoFrame = tkinter.Frame(window, bg = "lightSkyBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lightSkyBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightSkyBlue", fg = "chocolate", font = "times 12 bold", text = "It's never too late to learn a new skill\nand there are many places to learn online")
        genSpace = tkinter.Label(infoFrame, bg = "lightSkyBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightSkyBlue", fg = "chocolate", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some websites with online classes")
        line = 1
        linkList = ["https://www.udemy.com/", "https://www.coursera.org/", "https://www.skillshare.com/", "https://www.edx.org/", "https://www.masterclass.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightSkyBlue", fg = "chocolate", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def facetime(self):
        window = tkinter.Tk()
        window.configure(bg = "powderBlue")

        infoFrame = tkinter.Frame(window, bg = "powderBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "powderBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "powderBlue", fg = "darkOrange", font = "times 12 bold", text = "There are many ways to contact others,\neven without face to face")
        genSpace = tkinter.Label(infoFrame, bg = "powderBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "powderBlue", fg = "darkOrange", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some websites to contact others")
        line = 1
        linkList = ["https://zoom.us/", "https://discordapp.com/", "https://www.skype.com/en/", "https://hangouts.google.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "powderBlue", fg = "darkOrange", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def fix(self):
        window = tkinter.Tk()
        window.configure(bg = "paleTurquoise")

        infoFrame = tkinter.Frame(window, bg = "paleTurquoise", width = 300)
        linkFrame = tkinter.Frame(window, bg = "paleTurquoise", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "paleTurquoise", fg = "orange", font = "times 12 bold", text = "It's important to be able to fix things,\nespecially when you might not be able to hire someone to do it")
        genSpace = tkinter.Label(infoFrame, bg = "paleTurquoise", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "paleTurquoise", fg = "orange", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for tips on small fixes")
        line = 1
        linkList = ["https://www.businessinsider.com/20-handyman-skills-that-everyone-should-have-2014-3", "https://www.realsimple.com/home-organizing/diy-home-improvement", "https://www.familyhandyman.com/smart-homeowner/100-home-repairs-you-can-do-yourself/", "https://lifehacker.com/the-most-common-home-repairs-you-can-easily-do-yourself-1445435125"]
        linkBox = tkinter.Listbox(linkFrame, bg = "paleTurquoise", fg = "orange", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def information(self):
        window = tkinter.Tk()
        window.configure(bg = "salmon")

        infoFrame = tkinter.Frame(window, bg = "salmon", width = 300)
        linkFrame = tkinter.Frame(window, bg = "salmon", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "salmon", fg = "darkGreen", font = "times 12 bold", text = "Looking after your health is important, and it's good\nto know what your body is doing")
        genSpace = tkinter.Label(infoFrame, bg = "salmon", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "salmon", fg = "darkGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for information on your health")
        line = 1
        linkList = ["https://www.nia.nih.gov/health", "http://bok.ahima.org/PdfView?oid=301370", "https://www.mayoclinic.org/healthy-lifestyle/adult-health/basics/staying-healthy/hlv-20049421", "http://www.anchormedical.org/patient-resources/health-information"]
        linkBox = tkinter.Listbox(linkFrame, bg = "salmon", fg = "darkGreen", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def retirement(self):
        window = tkinter.Tk()
        window.configure(bg = "pink")

        infoFrame = tkinter.Frame(window, bg = "pink", width = 300)
        linkFrame = tkinter.Frame(window, bg = "pink", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "pink", fg = "seaGreen", font = "times 12 bold", text = "It's never too early to start planning\nfor retirement and know what the options are")
        genSpace = tkinter.Label(infoFrame, bg = "pink", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "pink", fg = "seaGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for")
        line = 1
        linkList = ["https://www.ssa.gov/pubs/EN-05-10035.pdf", "http://www.pensionrights.org/publications/statistic/sources-income-older-adults", "https://www.nia.nih.gov/sites/default/files/2017-06/health_and_retirement_study_0.pdf", "https://www.urban.org/features/nine-charts-about-future-retirement"]
        linkBox = tkinter.Listbox(linkFrame, bg = "pink", fg = "seaGreen", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def exercise(Self):
        window = tkinter.Tk()
        window.configure(bg = "lightCoral")

        infoFrame = tkinter.Frame(window, bg = "lightCoral", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lightCoral", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightCoral", fg = "green", font = "times 12 bold", text = "Exercise is important to maintain\nyour health and be able to do whatever you want")
        genSpace = tkinter.Label(infoFrame, bg = "lightCoral", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightCoral", fg = "green", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for exercise tips")
        line = 1
        linkList = ["https://www.mayoclinic.org/healthy-lifestyle/fitness/expert-answers/exercise/faq-20057916", "https://www.who.int/dietphysicalactivity/factsheet_adults/en/", "https://www.heart.org/en/healthy-living/fitness/fitness-basics/aha-recs-for-physical-activity-in-adults", "https://www.cdc.gov/physicalactivity/basics/adults/index.htm"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightCoral", fg = "green", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def book(self):
        window = tkinter.Tk()
        window.configure(bg = "paleGreen")

        infoFrame = tkinter.Frame(window, bg = "paleGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "paleGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "paleGreen", fg = "crimson", font = "times 12 bold", text = "Books are good ways to keep the mind sharp\nand potentially get some time away from the screen into a different world")
        genSpace = tkinter.Label(infoFrame, bg = "paleGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "paleGreen",fg = "crimson", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some book suggestions")
        line = 1
        linkList = ["https://www.goodreads.com/shelf/show/books-for-adults", "https://www.realsimple.com/work-life/entertainment/what-to-read-right-now", "https://www.goodreads.com/shelf/show/adult-fiction", "https://www.penguinrandomhouse.com/the-read-down/ya-books-that-are-also-great-reads-for-adults"]
        linkBox = tkinter.Listbox(linkFrame, bg = "paleGreen", fg = "crimson", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def movie(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumAquamarine")

        infoFrame = tkinter.Frame(window, bg = "mediumAquamarine", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumAquamarine", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumAquamarine", fg = "maroon", font = "times 12 bold", text = "Movies and TV shows are good to relax,\nplay while you're working, or learn some new information")
        genSpace = tkinter.Label(infoFrame, bg = "mediumAquamarine", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumAquamarine", fg = "maroon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for movie and tv show ideas")
        line = 1
        linkList = ["https://www.imdb.com/list/ls006301965/", "https://www.digitaltrends.com/movies/best-shows-on-netflix/", "https://www.digitaltrends.com/movies/best-movies-on-netflix/", "https://www.imdb.com/list/ls063720163/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumAquamarine", fg = "maroon", font = "times 12 bold", width = 55)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def diy(self):
        window = tkinter.Tk()
        window.configure(bg = "lightGreen")

        infoFrame = tkinter.Frame(window, bg = "lightGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lightGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightGreen", fg = "fireBrick", font = "times 12 bold", text = "Projects are always fun and you can use them as decorations,\nor you can personalize them and give them away")
        genSpace = tkinter.Label(infoFrame, bg = "lightGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightGreen", fg = "fireBrick", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for project ideas")
        line = 1
        linkList = ["https://diyprojects.com/diy-crafts-for-adults/", "https://diyjoy.com/fun-diy-ideas-adults/", "https://www.favecrafts.com/Gifts/22-Easy-Craft-Projects-For-Adults", "https://www.lifehack.org/articles/lifestyle/30-easy-and-awesome-diy-projects.html"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightGreen", fg = "fireBrick", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def game(self):
        window = tkinter.Tk()
        window.configure(bg = "yellowGreen")

        infoFrame = tkinter.Frame(window, bg = "yellowGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "yellowGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "yellowGreen", fg = "darkRed", font = "times 12 bold", text = "Games are fun and mindless ways to pass time,\nor bond with friends or family")
        genSpace = tkinter.Label(infoFrame, bg = "yellowGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "yellowGreen", fg = "darkRed", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some online,\ncard, or board games")
        line = 1
        linkList = ["https://www.cosmopolitan.com/uk/worklife/a29427158/house-party-games-for-adults/", "https://www.thespruce.com/affordable-party-games-for-adults-4154485", "https://www.bustle.com/p/the-14-most-popular-board-games-for-adults-2309694", "https://www.wealthwords.com/blog/free-online-games-adult-popular/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "yellowGreen", fg = "darkRed", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def discount(self):
        window = tkinter.Tk()
        window.configure(bg = "lemonChiffon")

        infoFrame = tkinter.Frame(window, bg = "lemonChiffon", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lemonChiffon", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lemonChiffon", fg = "darkViolet", font = "times 12 bold", text = "Discounts are good for saving money\nwhen the budget's tight")
        genSpace = tkinter.Label(infoFrame, bg = "lemonChiffon", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lemonChiffon", fg = "darkViolet", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some ways to get discounts")
        line = 1
        linkList = ["https://www.joinhoney.com/", "https://wikibuy.com/", "https://www.retailmenot.com/", "https://slickdeals.net/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lemonChiffon", fg = "darkViolet", font = "times 12 bold", width = 25)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def groceries(self):
        window = tkinter.Tk()
        window.configure(bg = "khaki")

        infoFrame = tkinter.Frame(window, bg = "khaki", width = 300)
        linkFrame = tkinter.Frame(window, bg = "khaki", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "khaki", fg = "indigo", font = "times 12 bold", text = "Shopping online for groceries is important\nright now and a good thing to know for the future")
        genSpace = tkinter.Label(infoFrame, bg = "khaki", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "khaki", fg = "indigo", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some online grocery shopping information")
        line = 1
        linkList = ["https://familiesforfinancialfreedom.com/cheapest-groceries-list/", "https://www.tasteofhome.com/collection/cheap-groceries/", "https://funcheaporfree.com/how-i-grocery-shop/", "https://www.cheatsheet.com/money-career/6-cheapest-grocery-stores-in-the-u-s.html/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "khaki", fg = "indigo", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def other(self):
        window = tkinter.Tk()
        window.configure(bg = "papayaWhip")

        infoFrame = tkinter.Frame(window, bg = "papayaWhip", width = 300)
        linkFrame = tkinter.Frame(window, bg = "papayaWhip", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "papayaWhip", fg = "mediumOrchid", font = "times 12 bold", text = "There are many places online to shop for other necessities\nand luxuries that are simple to use")
        genSpace = tkinter.Label(infoFrame, bg = "papayaWhip", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "papayaWhip", fg = "mediumOrchid", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for online shopping information")
        line = 1
        linkList = ["https://www.amazon.com/", "https://www.finder.com/online-shopping", "https://www.wish.com/", "https://www.lifehack.org/315603/10-best-online-shopping-sites-wish-knew-earlier"]
        linkBox = tkinter.Listbox(linkFrame, bg = "papayaWhip", fg = "mediumOrchid", font = "times 12 bold", width = 70)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def store(self):
        window = tkinter.Tk()
        window.configure(bg = "moccasin")

        infoFrame = tkinter.Frame(window, bg = "moccasin", width = 300)
        linkFrame = tkinter.Frame(window, bg = "moccasin", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "moccasin", fg = "purple", font = "times 12 bold", text = "Many stores have also modified their hours")
        genSpace = tkinter.Label(infoFrame, bg = "moccasin", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "moccasin", fg = "purple", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for information on different hours")
        line = 1
        linkList = ["https://corporate.walmart.com/important-store-info", "https://www.cnet.com/news/whole-foods-walmart-target-change-store-hours-amid-coronavirus-pandemic/", "https://www.kroger.com/i/coronavirus-update/store-information", "https://www.dollartreeinfo.com/news-releases/news-release-details/dollar-tree-family-dollar-modifying-store-hours-best-provide"]
        linkBox = tkinter.Listbox(linkFrame, bg = "moccasin", fg = "purple", font = "times 12 bold", width = 110)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

