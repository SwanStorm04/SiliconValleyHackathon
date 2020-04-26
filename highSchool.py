import tkinter

class HighSchooler:

    def __init__(self):
        self.highWindow = tkinter.Tk()
        self.highWindow.configure(bg = "bisque")

        self.topSpaceFrame = tkinter.Frame(self.highWindow, bg = "bisque", width = 300)
        self.howToFrame = tkinter.Frame(self.highWindow, bg = "bisque", width = 300)
        self.midSpace1Frame = tkinter.Frame(self.highWindow, bg = "bisque", width = 300)
        self.edFrame = tkinter.Frame(self.highWindow, bg = "bisque", width = 300)
        self.midSpace2Frame = tkinter.Frame(self.highWindow, bg = "bisque", width = 300)
        self.funFrame = tkinter.Frame(self.highWindow, bg = "bisque", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.highWindow, bg = "bisque", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "bisque", text = "   ")
        self.topSpace.pack()
        self.midSpace1 = tkinter.Label(self.midSpace1Frame, bg = "bisque", text = "   ")
        self.midSpace1.pack()
        self.midSpace2 = tkinter.Label(self.midSpace2Frame, bg = "bisque", text = "   ")
        self.midSpace2.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "bisque", text = "   ")
        self.botSpace.pack()

        self.howLabel = tkinter.Label(self.howToFrame, bg = "bisque", font = "times 14 bold", text = "How-To Information")
        self.howSpace = tkinter.Label(self.howToFrame, bg = "bisque", text = "   ")
        self.howLeftSpace = tkinter.Label(self.howToFrame, bg = "bisque", text = "   ")
        self.zoomButton = tkinter.Button(self.howToFrame, command = self.zoom, width = 20, height = 2, bg = "lightSteelBlue", font = "times 12 bold", text = "Zoom")
        self.howMidSpace = tkinter.Label(self.howToFrame, bg = "bisque", text = "   ")
        self.disButton = tkinter.Button(self.howToFrame, command = self.discord, width = 20, height = 2, bg = "mediumPurple", font = "times 12 bold", text = "Discord")
        self.howMidSpace2 = tkinter.Label(self.howToFrame, bg = "bisque", text = "   ")
        self.apButton = tkinter.Button(self.howToFrame, command = self.apply, width = 20, height = 2, bg = "rosyBrown", font = "times 12 bold", text = "College Applications")
        self.howRightSpace = tkinter.Label(self.howToFrame, bg = "bisque", text = "   ")

        self.howLabel.pack()
        self.howSpace.pack()
        self.howLeftSpace.pack(side = "left")
        self.zoomButton.pack(side = "left")
        self.howMidSpace.pack(side = "left")
        self.disButton.pack(side = "left")
        self.howMidSpace2.pack(side = "left")
        self.apButton.pack(side = "left")
        self.howRightSpace.pack(side = "left")

        self.edLabel = tkinter.Label(self.edFrame, bg = "bisque", font = "times 14 bold", text = "Educational Information")
        self.edSpace = tkinter.Label(self.edFrame, bg = "bisque", text = "   ")
        self.edLeftSpace = tkinter.Label(self.edFrame, bg = "bisque", text = "   ")
        self.elaButton = tkinter.Button(self.edFrame, command = self.ela, width = 20, height = 2, bg = "royalBlue", font = "times 12 bold", text = "ELA")
        self.edMidSpace1 = tkinter.Label(self.edFrame, bg = "bisque", text = "   ")
        self.mathButton = tkinter.Button(self.edFrame, command = self.math, width = 20, height = 2, bg = "crimson", font = "times 12 bold", text = "Math")
        self.edMidSpace2 = tkinter.Label(self.edFrame, bg = "bisque", text = "   ")
        self.histButton = tkinter.Button(self.edFrame, command = self.history, width = 20, height = 2, bg = "gold", font = "times 12 bold", text = "History")
        self.edMidSpace3 = tkinter.Label(self.edFrame, bg = "bisque", text = "   ")
        self.sciButton = tkinter.Button(self.edFrame, command = self.science, width = 20, height = 2, bg = "limeGreen", font = "times 12 bold", text = "Science")
        self.edMidSpace4 = tkinter.Label(self.edFrame, bg = "bisque", text = "   ")
        self.lgbtButton = tkinter.Button(self.edFrame, command = self.lgbt, width = 20, height = 2, bg = "chocolate", font = "times 12 bold", text = "LGBTQ+")
        self.edRightSpace = tkinter.Label(self.edFrame, bg = "bisque", text = "   ")

        self.edLabel.pack()
        self.edSpace.pack()
        self.edLeftSpace.pack(side = "left")
        self.elaButton.pack(side = "left")
        self.edMidSpace1.pack(side = "left")
        self.mathButton.pack(side = "left")
        self.edMidSpace2.pack(side = "left")
        self.histButton.pack(side = "left")
        self.edMidSpace3.pack(side = "left")
        self.sciButton.pack(side = "left")
        self.edMidSpace4.pack(side = "left")
        self.lgbtButton.pack(side = "left")
        self.edRightSpace.pack(side = "left")

        self.funLabel = tkinter.Label(self.funFrame, bg = "bisque", font = "times 14 bold", text = "Fun Things")
        self.funSpace = tkinter.Label(self.funFrame, bg = "bisque", text = "   ")
        self.funLeftSpace = tkinter.Label(self.funFrame, bg = "bisque", text = "   ")
        self.bookButton = tkinter.Button(self.funFrame, command = self.book, width = 20, height = 2, bg = "darkTurquoise", font = "times 12 bold", text = "Books")
        self.funMidSpace1 = tkinter.Label(self.funFrame, bg = "bisque", text = "   ")
        self.gameButton = tkinter.Button(self.funFrame, command = self.game, width = 20, height = 2, bg = "deepPink", font = "times 12 bold", text = "Games")
        self.funMidSpace2 = tkinter.Label(self.funFrame, bg = "bisque", text = "   ")
        self.movieButton = tkinter.Button(self.funFrame, command = self.movie, width = 20, height = 2, bg = "saddleBrown", font = "times 12 bold", text = "Movies")
        self.funMidSpace3 = tkinter.Label(self.funFrame, bg = "bisque", text = "   ")
        self.diyButton = tkinter.Button(self.funFrame, command = self.diy, width = 20, height = 2, bg = "darkViolet", font = "times 12 bold", text = "Do-It-Yourself")
        self.funRightSpace = tkinter.Label(self.funFrame, bg = "bisque", text = "   ")

        self.funLabel.pack()
        self.funSpace.pack()
        self.funLeftSpace.pack(side = "left")
        self.bookButton.pack(side = "left")
        self.funMidSpace1.pack(side = "left")
        self.gameButton.pack(side = "left")
        self.funMidSpace2.pack(side = "left")
        self.movieButton.pack(side = "left")
        self.funMidSpace3.pack(side = "left")
        self.diyButton.pack(side = "left")
        self.funRightSpace.pack(side = "left")

        self.topSpaceFrame.pack()
        self.howToFrame.pack()
        self.midSpace1Frame.pack()
        self.edFrame.pack()
        self.midSpace2Frame.pack()
        self.funFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop()


    def zoom(self):
        window = tkinter.Tk()
        window.configure(bg = "lightSteelBlue")

        infoFrame = tkinter.Frame(window, bg = "lightSteelBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "lightSteelBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "lightSteelBlue", fg = "sienna", font = "times 12 bold", text = "Zoom is a video call app where you can record calls,\nschedule meetings, and turn on and off your audio and video")
        genSpace = tkinter.Label(infoFrame, bg = "lightSteelBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "lightSteelBlue", fg = "sienna", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for a zoom download and tutorial")
        line = 1
        linkList = ["https://zoom.us/download", "https://support.zoom.us/hc/en-us/articles/206618765-Zoom-Video-Tutorials", "https://zoom.us/resources", "https://www.youtube.com/watch?v=bTSJ0YDoF7o"]
        linkBox = tkinter.Listbox(linkFrame, bg = "lightSteelBlue", fg = "sienna", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def discord(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumPurple")

        infoFrame = tkinter.Frame(window, bg = "mediumPurple", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumPurple", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumPurple", fg = "yellow", font = "times 12 bold", text = "Discord is a great app where you can send messages to groups,\nuse robots to do certain things, and have audio or video calls")
        genSpace = tkinter.Label(infoFrame, bg = "mediumPurple", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumPurple", fg = "yellow", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for")
        line = 1
        linkList = ["https://discordapp.com/download", "https://www.youtube.com/watch?v=le_CE--Mnvs", "https://support.discordapp.com/hc/en-us/articles/360033931551-Getting-Started", "https://www.tomsguide.com/us/what-is-discord,review-5203.html", "https://www.businessinsider.com/how-to-use-discord-the-messaging-app-for-gamers-2018-5"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumPurple", fg = "yellow", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    def apply(self):
        window = tkinter.Tk()
        window.configure(bg = "mistyRose")

        infoFrame = tkinter.Frame(window, bg = "mistyRose", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mistyRose", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mistyRose", fg = "darkGoldenrod", font = "times 12 bold", text = "College Applications are important to get right\nif you want to go into a field that needs a degree")
        genSpace = tkinter.Label(infoFrame, bg = "mistyRose", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mistyRose", fg = "darkGoldenrod", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for college information")
        line = 1
        linkList = ["https://studentaid.gov/h/apply-for-aid/fafsa", "https://www.usnews.com/education/best-colleges/articles/college-application-process", "https://www.universalcollegeapp.com/", "https://bigfuture.collegeboard.org/get-in/applying-101/college-applications-how-to-begin-admissions"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mistyRose", fg = "darkGoldenrod", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

    
    def ela(self):
        window = tkinter.Tk()
        window.configure(bg = "royalBlue")

        infoFrame = tkinter.Frame(window, bg = "royalBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "royalBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "royalBlue", fg = "orange", font = "times 12 bold", text = "It is important to learn grammar and writing skills for\nyour careers or college applications")
        genSpace = tkinter.Label(infoFrame, bg = "royalBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "royalBlue", fg = "orange", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for grammar lessons, writing tips,\nand citation information")
        line = 1
        linkList = ["http://www.dailygrammar.com/", "https://www.readingandwritinghaven.com/how-to-sequence-grammar-instruction/", "https://www.preppedandpolished.com/writing-tips/", "https://owl.purdue.edu/owl/research_and_citation/resources.html"]
        linkBox = tkinter.Listbox(linkFrame, bg = "royalBlue", fg = "orange", font = "times 12 bold", width = 70)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def math(self):
        window = tkinter.Tk()
        window.configure(bg = "crimson")

        infoFrame = tkinter.Frame(window, bg = "crimson", width = 300)
        linkFrame = tkinter.Frame(window, bg = "crimson", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "crimson", fg = "[aleGreen", font = "times 12 bold", text = "Math is really useful for budgeting, college,\nand probably your career")
        genSpace = tkinter.Label(infoFrame, bg = "crimson", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "crimson", fg = "paleGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some math tutorials")
        line = 1
        linkList = ["https://www.khanacademy.org/", "https://www.mathalicious.com/", "https://www.ck12.org/student/", "https://www.time4learning.com/homeschool/curriculum/high_school_math.html"]
        linkBox = tkinter.Listbox(linkFrame, bg = "crimson", fg = "paleGreen", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def history(self):
        window = tkinter.Tk()
        window.configure(bg = "gold")

        infoFrame = tkinter.Frame(window, bg = "gold", width = 300)
        linkFrame = tkinter.Frame(window, bg = "gold", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "gold", fg = "darkMagenta", font = "times 12 bold", text = "")
        genSpace = tkinter.Label(infoFrame, bg = "gold", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "gold", fg = "darkMagenta", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for")
        line = 1
        linkList = ["https://hiphomeschoolmoms.com/homeschool-high-school-history-curriculum/", "https://study.com/academy/course/high-school-us-history.html", "http://horrible-histories.co.uk/", "https://www.eachieve.com/OnlineSocialStudiesCourses/USHistoryClass",]
        linkBox = tkinter.Listbox(linkFrame, bg = "gold", fg = "darkMagenta", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def science(self):
        window = tkinter.Tk()
        window.configure(bg = "limeGreen")

        infoFrame = tkinter.Frame(window, bg = "limeGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "limeGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "limeGreen", fg = "maroon", font = "times 12 bold", text = "Science is really helpful to most careers, and also good\nin understanding the world around you")
        genSpace = tkinter.Label(infoFrame, bg = "limeGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "limeGreen", fg = "maroon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some science tutorials")
        line = 1
        linkList = ["https://www.strongmind.com/solutions/courseware/curriculum/high-school-curriculum/hs-science/", "https://www.khanacademy.org/science", "https://www.eachieve.com/OnlineHighSchoolCourses/Science", "https://www.fueleducation.com/curriculum/subject/science.html"]
        linkBox = tkinter.Listbox(linkFrame, bg = "limeGreen", fg = "maroon", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def lgbt(self):
        window = tkinter.Tk()
        window.configure(bg = "chocolate")

        infoFrame = tkinter.Frame(window, bg = "chocolate", width = 300)
        linkFrame = tkinter.Frame(window, bg = "chocolate", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "chocolate", fg = "paleTurquoise", font = "times 12 bold", text = "LGBT education is really important so you can learn about yourself\n and be able to better support your friends in the LGBTQIA+ community.\nThe letters stand for: Lesbian(women who like women),\nGay (men who like men), Bisexual (people who like two or more genders),\nTransgender (people who's gender does not match their birth sex), Queer (a catch-all for not straight-cisgender identities),\nIntersex (someone who is born with characteristics of two sexes),\nAsexual/Aromantic/Agender (someone who does not experience sexual attraction/romantic attraction/does not have a gender)")
        genSpace = tkinter.Label(infoFrame, bg = "chocolate", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "chocolate", fg = "paleTurquoise", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for ")
        line = 1
        linkList = ["https://www.itspronouncedmetrosexual.com/2013/01/a-comprehensive-list-of-lgbtq-term-definitions/", "https://www.thetrevorproject.org/trvr_support_center/in-school/", "https://www.joinonelove.org/learn/7-things-shouldve-taught-lgbt-inclusive-sex-ed-didnt/", "https://lgbtqia.ucdavis.edu/educated/glossary"]
        linkBox = tkinter.Listbox(linkFrame, bg = "chocolate", fg = "paleTurquoise", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def book(self):
        window = tkinter.Tk()
        window.configure(bg = "darkTurquoise")

        infoFrame = tkinter.Frame(window, bg = "darkTurquoise", width = 300)
        linkFrame = tkinter.Frame(window, bg = "darkTurquoise", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "darkTurquoise", fg = "brown", font = "times 12 bold", text = "Books are a good way to relax and\ninsert yourself into another world without the need\nfor an internet connection.")
        genSpace = tkinter.Label(infoFrame, bg = "darkTurquoise", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "darkTurquoise", fg = "brown", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some book suggestions")
        line = 1
        linkList = ["https://plexuss.com/news/article/books-to-read-in-high-school-reading-list", "https://www.npr.org/2012/08/07/157795366/your-favorites-100-best-ever-teen-novels", "https://www.barnesandnoble.com/blog/50-essential-high-school-stories/", "https://www.weareteachers.com/influential-books-high-school-students/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkTurquoise", fg = "brown", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()
        

    def game(self):
        window = tkinter.Tk()
        window.configure(bg = "deepPink")

        infoFrame = tkinter.Frame(window, bg = "deepPink", width = 300)
        linkFrame = tkinter.Frame(window, bg = "deepPink", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "deepPink", fg = "darkGreen", font = "times 12 bold", text = "Games are a fun way to relax and pass the time,\non or offline")
        genSpace = tkinter.Label(infoFrame, bg = "deepPink", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "deepPink", fg = "darkGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser forsome online games\nand card or board games")
        line = 1
        linkList = ["https://www.commonsense.org/education/top-picks/10-great-free-games-for-high-school-students", "https://www.quizalize.com/blog/2018/03/02/classroom-games/", "https://www.momjunction.com/articles/virtual-world-games-for-teens_00371568/", "https://www.addictinggames.com/tag/teen-games.jsp"]
        linkBox = tkinter.Listbox(linkFrame, bg = "deepPink", fg = "darkGreen", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def movie(self):
        window = tkinter.Tk()
        window.configure(bg = "saddleBrown")

        infoFrame = tkinter.Frame(window, bg = "saddleBrown", width = 300)
        linkFrame = tkinter.Frame(window, bg = "saddleBrown", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "saddleBrown", fg = "deepSkyBlue", font = "times 12 bold", text = "Movies and TV shows are a great way to pass the time mindlessly\nor to have playing in the background while you work")
        genSpace = tkinter.Label(infoFrame, bg = "saddleBrown", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "saddleBrown", fg = "deepSkyBlue", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some movie ideas")
        line = 1
        linkList = ["https://www.seventeen.com/celebrity/movies-tv/a47126/best-teen-movies/", "https://www.thrillist.com/entertainment/nation/best-teen-shows-on-netflix", "https://www.complex.com/pop-culture/best-teen-tv-dramas-of-all-time/", "https://www.imdb.com/list/ls050434244/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "saddleBrown", fg = "deepSkyBlue", font = "times 12 bold", width = 65)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def diy(self):
        window = tkinter.Tk()
        window.configure(bg = "darkViolet")

        infoFrame = tkinter.Frame(window, bg = "darkViolet", width = 300)
        linkFrame = tkinter.Frame(window, bg = "darkViolet", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "darkViolet", fg = "lemonChiffon", font = "times 12 bold", text = "Things that you make yourself are always fun because\nyou put effort into it, can customize it, and give it to friends.")
        genSpace = tkinter.Label(infoFrame, bg = "darkViolet", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "darkViolet", fg = "lemonChiffon", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some projects you can do")
        line = 1
        linkList = ["https://www.youtube.com/watch?v=VIVIegSt81k&t=2s", "https://www.thesprucecrafts.com/diy-projects-for-teens-4768728", "https://diyprojects.com/projects-for-teenagers/", "https://www.instructables.com/id/Origami-For-Everyone/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkViolet", fg = "lemonChiffon", font = "times 12 bold", width = 55)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

