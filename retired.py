import tkinter

class Senior:

    def __init__(self):
        self.senWindow = tkinter.Tk()
        self.senWindow.configure(bg = "lightBlue")

        self.topSpaceFrame = tkinter.Frame(self.senWindow, bg = "lightBlue", width = 300)
        self.healthFrame = tkinter.Frame(self.senWindow, bg = "lightBlue", width = 300)
        self.midSpace1Frame = tkinter.Frame(self.senWindow, bg = "lightBlue", width = 300)
        self.edFrame = tkinter.Frame(self.senWindow, bg = "lightBlue", width = 300)
        self.midSpace2Frame = tkinter.Frame(self.senWindow, bg = "lightBlue", width = 300)
        self.actFrame = tkinter.Frame(self.senWindow, bg = "lightBlue", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.senWindow, bg = "lightBlue", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "lightBlue", text = "   ")
        self.topSpace.pack()
        self.midSpace1 = tkinter.Label(self.midSpace1Frame, bg = "lightBlue", text = "   ")
        self.midSpace1.pack()
        self.midSpace2 = tkinter.Label(self.midSpace2Frame, bg = "lightBlue", text = "   ")
        self.midSpace2.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "lightBlue", text = "   ")
        self.botSpace.pack()

        self.heLabel = tkinter.Label(self.healthFrame, bg = "lightBlue", font = "times 16 bold", text = "Health")
        self.heSpace = tkinter.Label(self.healthFrame, bg = "lightBlue", text = "   ")
        self.heLeftSpace = tkinter.Label(self.healthFrame, bg = "lightBlue", text = "   ")
        self.healthButton = tkinter.Button(self.healthFrame, command = self.health, width = 20, height = 2, bg = "pink", font = "times 14 bold", text = "Health")
        self.heMidSpace1 = tkinter.Label(self.healthFrame, bg = "lightBlue", text = "   ")
        self.inButton = tkinter.Button(self.healthFrame, command = self.insurance, width = 20, height = 2, bg = "lightCoral", font = "times 14 bold", text = "Health Insurance")
        self.heMidSpace2 = tkinter.Label(self.healthFrame, bg = "lightBlue", text = "   ")
        self.exerButton = tkinter.Button(self.healthFrame, command = self.exercise, width = 20, height = 2, bg = "mistyRose", font = "times 14 bold", text = "Exercise")
        self.heRightSpace = tkinter.Label(self.healthFrame, bg = "lightBlue", text = "   ")

        self.heLabel.pack()
        self.heSpace.pack()
        self.heLeftSpace.pack(side = "left")
        self.healthButton.pack(side = "left")
        self.heMidSpace1.pack(side = "left")
        self.inButton.pack(side = "left")
        self.heMidSpace2.pack(side = "left")
        self.exerButton.pack(side = "left")
        self.heRightSpace.pack(side = "left")

        self.edLabel = tkinter.Label(self.edFrame, bg = "lightBlue", font = "times 16 bold", text = "Online Learning")
        self.edSpace = tkinter.Label(self.edFrame, bg = "lightBlue", text = "   ")
        self.edLeftSpace = tkinter.Label(self.edFrame, bg = "lightBlue", text = "   ")
        self.callButton = tkinter.Button(self.edFrame, command = self.facetime, width = 20, height = 2, bg = "mediumPurple", font = "times 14 bold", text = "Contacting Others")
        self.edMidSpace1 = tkinter.Label(self.edFrame, bg = "lightBlue", text = "   ")
        self.classesButton = tkinter.Button(self.edFrame, command = self.classes, width = 20, height = 2, bg = "plum", font = "times 14 bold", text = "Classes")
        self.edMidSpace2 = tkinter.Label(self.edFrame, bg = "lightBlue", text = "   ")
        self.fixButton = tkinter.Button(self.edFrame, command = self.fix, width = 20, height = 2, bg = "orchid", font = "times 14 bold", text = "Fix-ups")
        self.edMidSpace3 = tkinter.Label(self.edFrame, bg = "lightBlue", text = "   ")
        self.shopButton = tkinter.Button(self.edFrame, command = self.shop, width = 20, height = 2, bg = "thistle", font = "times 14 bold", text = "Shopping")
        self.edMidSpace4 = tkinter.Label(self.edFrame, bg = "lightBlue", text = "   ")
        self.relButton = tkinter.Button(self.edFrame, command = self.reliable, width = 20, height = 2, bg = "violet", font = "times 14 bold", text = "Reliable News Sources")
        self.edRightSpace = tkinter.Label(self.edFrame, bg = "lightBlue", text = "   ")

        self.edLabel.pack()
        self.edSpace.pack()
        self.edLeftSpace.pack(side = "left")
        self.callButton.pack(side = "left")
        self.edMidSpace1.pack(side = "left")
        self.classesButton.pack(side = "left")
        self.edMidSpace2.pack(side = "left")
        self.fixButton.pack(side = "left")
        self.edMidSpace3.pack(side = "left")
        self.shopButton.pack(side = "left")
        self.edMidSpace4.pack(side = "left")
        self.relButton.pack(side = "left")
        self.edRightSpace.pack(side = "left")

        self.actLabel = tkinter.Label(self.actFrame, bg = "lightBlue", font = "times 16 bold", text = "Activities")
        self.actSpace = tkinter.Label(self.actFrame, bg = "lightBlue", text = "   ")
        self.actLeftSpace = tkinter.Label(self.actFrame, bg = "lightBlue", text = "   ")
        self.bookButton = tkinter.Button(self.actFrame, command = self.book, width = 20, height = 2, bg = "lemonChiffon", font = "times 14 bold", text = "Books")
        self.actMidSpace1 = tkinter.Label(self.actFrame, bg = "lightBlue", text = "   ")
        self.movieButton = tkinter.Button(self.actFrame, command = self.movie, width = 20, height = 2, bg = "khaki", font = "times 14 bold", text = "Movies")
        self.actMidSpace2 = tkinter.Label(self.actFrame, bg = "lightBlue", text = "   ")
        self.gameButton = tkinter.Button(self.actFrame, command = self.game, width = 20, height = 2, bg = "papayaWhip", font = "times 14 bold", text = "Games")
        self.actMidSpace3 = tkinter.Label(self.actFrame, bg = "lightBlue", text = "   ")
        self.diyButton = tkinter.Button(self.actFrame, command = self.diy, width = 20, height = 2, bg = "paleGoldenrod", font = "times 14 bold", text = "Projects")
        self.actRightSpace = tkinter.Label(self.actFrame, bg = "lightBlue", text = "   ")

        self.actLabel.pack()
        self.actSpace.pack()
        self.actLeftSpace.pack(side = "left")
        self.bookButton.pack(side = "left")
        self.actMidSpace1.pack(side = "left")
        self.movieButton.pack(side = "left")
        self.actMidSpace2.pack(side = "left")
        self.gameButton.pack(side = "left")
        self.actMidSpace3.pack(side = "left")
        self.diyButton.pack(side = "left")
        self.actRightSpace.pack(side = "left")

        self.topSpaceFrame.pack()
        self.healthFrame.pack()
        self.midSpace1Frame.pack()
        self.edFrame.pack()
        self.midSpace2Frame.pack()
        self.actFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop()


    def health(self):
        healthWindow = tkinter.Tk()
        healthWindow.configure(bg = "pink")

        infoFrame = tkinter.Frame(healthWindow, bg = "pink", width = 300)
        linkFrame = tkinter.Frame(healthWindow, bg = "pink", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "pink", font = "times 14 bold", text = "Make sure to look after your health!\nIt's always important to schedule and keep doctor's appointments\nand listen to their advice.")
        infoSpace = tkinter.Label(infoFrame, bg = "pink", text = "   ")
        genInfo.pack()
        infoSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "pink", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some information on\nhow to look after your health!")
        line = 1
        linkList = ["https://www.nia.nih.gov/health", "https://medlineplus.gov/olderadulthealth.html", "https://www.healthline.com/health/senior-health", "https://www.medicinenet.com/senior_health/article.htm", "https://www.medicalnewstoday.com/articles/coronavirus-vs-flu"]
        linkBox = tkinter.Listbox(linkFrame, bg = "pink", font = "times 14 bold", width = 55)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def insurance(self):
        inWindow = tkinter.Tk()
        inWindow.configure(bg = "lightCoral")

        infoFrame = tkinter.Frame(inWindow, bg = "lightCoral", width = 300)
        linkFrame = tkinter.Frame(inWindow, bg = "lightCoral", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightCoral", font = "times 14 bold", text = "Life and health insurance are important if you get sick,\nso you can pay the medical bills.")
        infoSpace = tkinter.Label(infoFrame, bg = "lightCoral", text = "   ")

        genInfo.pack()
        infoSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightCoral", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some information on\nhealth and life insurance.")
        line = 1
        linkList = ["https://seniorcarelife.com/", "https://www.aginginplace.org/life-insurance-for-seniors-over-70-what-they-dont-tell-you/", "https://lifepolicyshopper.com/senior-care-final-expense-insurance-for-seniors-usa/", "https://www.debt.org/medical/senior-options-costs/", "https://www.gerberlife.com/senior-life-insurance"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightCoral", font = "times 14 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()
        
        infoFrame.pack()
        linkFrame.pack()

    def exercise(self):
        exWindow = tkinter.Tk()
        exWindow.configure(bg = "mistyRose")

        infoFrame = tkinter.Frame(exWindow, bg = "mistyRose", width = 300)
        linkFrame = tkinter.Frame(exWindow, bg = "mistyRose", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mistyRose", font = "times 14 bold", text = "Remember to exercise mor a bit each day, but don't push yourself.\nAbout two hours of moderate exercise or an hour\nof vigorous exercise each week is good.")
        infoSpace = tkinter.Label(infoFrame, bg = "mistyRose", text = "   ")

        genInfo.pack()
        infoSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mistyRose", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some exercise suggestions and staying healthy\nwhile exercising.")
        line = 1
        linkList = ["https://familydoctor.org/exercise-seniors/", "https://www.elmcroft.com/blog/2019/may/how-much-exercise-is-too-much-for-seniors/", "https://www.nhs.uk/live-well/exercise/physical-activity-guidelines-older-adults/", "https://www.silversneakers.com/blog/best-exercise-older-adults/", "https://www.everydayhealth.com/senior-health-photos/exercise-ideas-for-seniors.aspx"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mistyRose", font = "times 14 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def facetime(self):
        ftWindow = tkinter.Tk()
        ftWindow.configure(bg = "mediumPurple")

        zoomInfo = tkinter.Label(ftWindow, bg = "mediumPurple", font = "times 14 bold", text = "Zoom is a popular video chat app,\nwhere you can schedule meetings with links and join with\nthe option to turn on or off audio and video. Download it with:\nzoom.us/download")
        disInfo = tkinter.Label(ftWindow, bg = "mediumPurple", font = "times 14 bold", text = "Discord is another popular chatting app,\nwhere you can send messages to a group as well as audio\nor video calls. There are also robots you can interact with. Download it with:\ndiscordapp.com/download")
        genInfo = tkinter.Label(ftWindow, bg = "mediumPurple", font = "times 14 bold", text = "There are many other apps for videochatting. For example:\nskype, facetime (between apple products), and google hangouts")
        botSpace = tkinter.Label(ftWindow, bg = "mediumPurple", text = "   ")

        zoomInfo.pack()
        disInfo.pack()
        genInfo.pack()
        botSpace.pack()

    def classes(self):
        clWindow = tkinter.Tk()
        clWindow.configure(bg = "plum")

        infoFrame = tkinter.Frame(clWindow, bg = "plum", width = 300)
        linkFrame = tkinter.Frame(clWindow, bg = "plum", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "plum", font = "times 14 bold", text = "There are many websites where you can learn new skills, here are a few:\nSkillShare, Coursera, and Udacity\nIf you want to learn a new language, here are some places for that too:\nDuolingo, Rossetta Stone")
        genSpace = tkinter.Label(infoFrame, bg = "plum", text = "   ")
        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "plum", font = "times 14 bold", text = "Here are some links you can copy (ctrl + c) and paste (ctrl + v)\ninto a browser for online class information")
        line = 1
        linkList = ["https://vocal.media/education/14-free-online-courses-for-senior-citizens", "https://www.coursera.org/", "https://www.skillshare.com/", "https://www.duolingo.com/", "https://www.rosettastone.com/", "https://www.udacity.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "plum", font = "times 14 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def fix(self):
        fixWindow = tkinter.Tk()
        fixWindow.configure(bg = "orchid")

        infoFrame = tkinter.Frame(fixWindow, bg = "orchid", width = 300)
        linkFrame = tkinter.Frame(fixWindow, bg = "orchid", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "orchid", font = "times 14 bold", text = "Many small problems can be easily fixed\nif you know how. Here's some information\non how.")
        infoSpace = tkinter.Label(infoFrame, bg = "orchid", text = "   ")

        genInfo.pack()
        infoSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "orchid", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser to learn simple handyman information")
        line = 1
        linkList = ["https://www.realsimple.com/home-organizing/diy-home-improvement", "https://www.familyhandyman.com/smart-homeowner/100-home-repairs-you-can-do-yourself/", "https://www.diynetwork.com/how-to/maintenance-and-repair/repairing", "https://home.howstuffworks.com/home-improvement/repair/5-home-repairs-you-should-do-yourself.htm"]
        linkBox = tkinter.Listbox(linkFrame, bg = "orchid", font = "times 14 bold", width = 100)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def shop(self):
        shWindow = tkinter.Tk()
        shWindow.configure(bg = "thistle")

        infoFrame = tkinter.Frame(shWindow, bg = "thistle", width = 300)
        linkFrame = tkinter.Frame(shWindow, bg = "thistle", width = 300)

        storeInfo = tkinter.Label(infoFrame, bg = "thistle", font = "times 14 bold", text = "During this lockdown, many stores have changed their hours.\nThe first few links will let you see which stores have done so.")
        genInfo = tkinter.Label(infoFrame, bg = "thistle", font = "times 14 bold", text = "Online shopping is also very easy, the last few links will help you buy what you want online.")
        infoSpace = tkinter.Label(infoFrame, bg = "thistle", text = "   ")

        storeInfo.pack()
        genInfo.pack()
        infoSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "thistle", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for help with online and in-store shopping.")
        line = 1
        linkList = ["https://corporate.walmart.com/newsroom/2020/03/18/latest-walmart-store-changes-to-support-associates-and-customers", "https://www.usatoday.com/story/money/2020/03/17/coronavirus-store-closings-hours-changes-list/5068211002/", "https://www.amazon.com/", "https://www.finder.com/online-shopping"]
        linkBox = tkinter.Listbox(linkFrame, bg = "thistle", font = "times 14 bold", width = 100)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def reliable(self):
        reWindow = tkinter.Tk()
        reWindow.configure(bg = "violet")

        infoFrame = tkinter.Frame(reWindow, bg = "violet", width = 300)
        linkFrame = tkinter.Frame(reWindow, bg = "violet", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "violet", font = "times 14 bold", text = "It is always good to check if news sources are reliable\nand presenting an unbiased and truthful version\nof the news.")
        infoSpace = tkinter.Label(infoFrame, bg = "violet", text = "   ")

        genInfo.pack()
        infoSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "violet", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for information on how to check\nwhether a news source is reliable")
        line = 1
        linkList = ["https://www.moneycrashers.com/fake-news-determine-reliable-story/", "https://www.npr.org/sections/alltechconsidered/2016/12/05/503581220/fake-or-real-how-to-self-check-the-news-and-get-the-facts", "https://www.americanpressinstitute.org/publications/six-critical-questions-can-use-evaluate-media-content/", "https://www.adfontesmedia.com/interactive-media-bias-chart/?v=402f03a963ba"]
        linkBox = tkinter.Listbox(linkFrame, bg = "violet", font = "times 14 bold", width = 105)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def book(self):
        boWindow = tkinter.Tk()
        boWindow.configure(bg = "lemonChiffon")

        infoFrame = tkinter.Frame(boWindow, bg = "lemonChiffon", width = 300)
        linkFrame = tkinter.Frame(boWindow, bg = "lemonChiffon", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lemonChiffon", font = "times 14 bold", text = "Reading is always good to do,\nespecially when you can't go out. Here are some book lists\nand websites for audio books.")
        genSpace = tkinter.Label(infoFrame, bg = "lemonChiffon", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lemonChiffon", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) thes links\ninto a browser for")
        line = 1
        linkList = ["https://www.leisurecare.com/resources/must-read-books-for-seniors/", "https://www.ihps.com/best-books-seniors/", "https://www.goodreads.com/shelf/show/senior-citizens", "https://www.audible.com/?ref=a_hp_t1_nav_header_logo&pf_rd_p=30becf1e-3e44-465c-9d5e-640fe163f79b&pf_rd_r=G3TG5J1MWMHD7YF4MSVA", "https://www.amazon.com/Kindle-eBooks/b?ie=UTF8&node=154606011"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lemonChiffon", font = "times 14 bold", width = 125)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def movie(self):
        moWindow = tkinter.Tk()
        moWindow.configure(bg = "khaki")

        infoFrame = tkinter.Frame(moWindow, bg = "khaki", width = 300)
        linkFrame = tkinter.Frame(moWindow, bg = "khaki", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "khaki", font = "times 14 bold", text = "Movies and TV shows are great when you don't feel like doing anything\nor want something playing in the background while you're busy")
        genSpace = tkinter.Label(infoFrame, bg = "khaki", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "khaki", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some good movies and tv shows")
        line = 1
        linkList = ["https://www.ihps.com/top-tv-shows-seniors-alzheimers/", "https://insigniaseniorliving.com/netflix-for-seniors/", "https://www.imdb.com/search/keyword/?keywords=seniors", "https://www.lcbseniorliving.com/2018/04/24/binge-worthy-tv-shows-for-seniors/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "khaki", font = "times 14 bold", width = 65)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def game(self):
        gaWindow = tkinter.Tk()
        gaWindow.configure(bg = "papayaWhip")

        infoFrame = tkinter.Frame(gaWindow, bg = "papayaWhip", width = 300)
        linkFrame = tkinter.Frame(gaWindow, bg = "papayaWhip", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "papayaWhip", font = "times 14 bold", text = "Games are good for mindless activities\nor bonding with others.")
        genSpace = tkinter.Label(infoFrame, bg = "papayaWhip", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "papayaWhip", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some online games\nor card and board games")
        line = 1
        linkList = ["https://guideforseniors.com/blog/senior-online-games/", "https://onlinegamesforseniors.com/", "https://seniors.lovetoknow.com/Games_for_Senior_Citizens", "https://www.greatseniorliving.com/articles/games-for-seniors"]
        linkBox = tkinter.Listbox(linkFrame, bg = "papayaWhip", font = "times 14 bold", width = 55)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def diy(self):
        diyWindow = tkinter.Tk()
        diyWindow.configure(bg = "paleGoldenrod")

        infoFrame = tkinter.Frame(diyWindow, bg = "paleGoldenrod", width = 300)
        linkFrame = tkinter.Frame(diyWindow, bg = "paleGoldenrod", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "paleGoldenrod", font = "times 14 bold", text = "If you want something to do, there are always projects\nwhere you can make things yourself!")
        genSpace = tkinter.Label(infoFrame, bg = "paleGoldenrod", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "paleGoldenrod", font = "times 14 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some project ideas")
        line = 1
        linkList = ["https://feltmagnet.com/crafts/senior-crafts", "https://www.presbyterianseniorliving.org/blog/5-diy-craft-activities-for-caregivers-to-do-with-seniors", "https://dailycaring.com/activities-for-seniors-with-alzheimers-10-inexpensive-diy-ideas/", "https://craftsbyamanda.com/category/craft-tutorials/adult-crafts/crafts-for-seniors/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "paleGoldenrod", font = "times 14 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


##window = tkinter.Tk()
##        window.configure(bg = "")
##
##        infoFrame = tkinter.Frame(window, bg = "", width = 300)
##        linkFrame = tkinter.Frame(window, bg = "", width = 300)
##
##        genInfo = tkinter.Label(infoFrame, bg = "", font = "times 12 bold", text = "")
##        genSpace = tkinter.Label(infoFrame, bg = "", text = "   ")
##
##        genInfo.pack()
##        genSpace.pack()
##
##        linkLabel = tkinter.Label(linkFrame, bg = "", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for")
##        line = 1
##        linkList = []
##        linkBox = tkinter.Listbox(linkFrame, bg = "", font = "times 12 bold", width = 75)
##
##        for i in linkList:
##            linkBox.insert(line, i)
##            line += 1
##
##        linkLabel.pack()
##        linkBox.pack()
##
##        infoFrame.pack()
##        linkFrame.pack()
