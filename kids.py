import tkinter # importing the library for the GUI

class Kid:

    def __init__(self):
        self.kidWindow = tkinter.Tk() # The main window
        self.kidWindow.configure(bg = "khaki") # background color

        self.topSpaceFrame = tkinter.Frame(self.kidWindow, bg = "khaki", width = 300) # Separating the window into sections
        self.edLinksFrame = tkinter.Frame(self.kidWindow, bg = "khaki", width = 300)
        self.spaceFrame = tkinter.Frame(self.kidWindow, bg = "khaki", width = 300)
        self.funLinksFrame = tkinter.Frame(self.kidWindow, bg = "khaki", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.kidWindow, bg = "khaki", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "khaki", text = "                               ") # Putting space in between all of the information
        self.topSpace.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "khaki", text = "                           ")
        self.botSpace.pack()
        self.midTopSpace = tkinter.Label(self.spaceFrame, bg = "khaki", text = "                           ", font = "times 12 bold")
        self.separate = tkinter.Label(self.spaceFrame, bg = "khaki", text = "-------------------------------------------------------------------------------------------------------------------------------------------------------------")
        self.midBotSpace = tkinter.Label(self.spaceFrame, bg = "khaki", text = "                           ", font = "times 12 bold")
        self.midTopSpace.pack()
        self.separate.pack()
        self.midBotSpace.pack()

        self.edLabel = tkinter.Label(self.edLinksFrame, bg = "khaki", text = "Educational Information!", font = "times 16 bold") # The buttons that lead to educational stuff
        self.edSpace = tkinter.Label(self.edLinksFrame, bg = "khaki", text = "                           ", font = "times 12 bold")
        self.edLeftSpace = tkinter.Label(self.edLinksFrame, bg = "khaki", text = "   ")
        self.readButton = tkinter.Button(self.edLinksFrame, text = "Reading!", command = self.ela, width = 20, bg = "blue", font = "times 12 bold", height = 2)
        self.midEdSpace1 = tkinter.Label(self.edLinksFrame, bg = "khaki", text = "   ")
        self.mathButton = tkinter.Button(self.edLinksFrame, text = "Math!", command = self.math, width = 20, bg = "red", font = "times 12 bold", height = 2)
        self.midEdSpace2 = tkinter.Label(self.edLinksFrame, bg = "khaki", text = "   ")
        self.historyButton = tkinter.Button(self.edLinksFrame, text = "History!", command = self.history, width = 20, bg = "deepPink", font = "times 12 bold", height = 2)
        self.midEdSpace3 = tkinter.Label(self.edLinksFrame, bg = "khaki", text = "   ")
        self.sciButton = tkinter.Button(self.edLinksFrame, text = "Science!", command = self.science, width = 20, bg = "lime", font = "times 12 bold", height = 2)
        self.edRightSpace = tkinter.Label(self.edLinksFrame, bg = "khaki", text = "   ")

        self.edLabel.pack(side = "top") # Arranging everything how it should look in the GUI
        self.edSpace.pack()
        self.edLeftSpace.pack(side = "left")
        self.readButton.pack(side = "left")
        self.midEdSpace1.pack(side = "left")
        self.mathButton.pack(side = "left")
        self.midEdSpace2.pack(side = "left")
        self.historyButton.pack(side = "left")
        self.midEdSpace3.pack(side = "left")
        self.sciButton.pack(side = "left")
        self.edRightSpace.pack(side = "left")

        self.funLabel = tkinter.Label(self.funLinksFrame, bg = "khaki", text = "Fun Activities!", font = "times 16 bold") # The links for free time
        self.funSpace = tkinter.Label(self.funLinksFrame, bg = "khaki", text = "                           ", font = "times 12 bold")
        self.funLeftSpace = tkinter.Label(self.funLinksFrame, bg = "khaki", text = "   ")
        self.bookButton = tkinter.Button(self.funLinksFrame, text = "Things to Read!", command = self.books, width = 20, bg = "cyan", font = "times 12 bold", height = 2)
        self.funMidSpace1 = tkinter.Label(self.funLinksFrame, bg = "khaki", text = "   ")
        self.diyButton = tkinter.Button(self.funLinksFrame, text = "Things to Make!", command = self.diy, width = 20, bg = "yellow", font = "times 12 bold", height = 2)
        self.funMidSpace2 = tkinter.Label(self.funLinksFrame, bg = "khaki", text = "   ")
        self.movieButton = tkinter.Button(self.funLinksFrame, text = "Things to Watch!", command = self.movie, width = 20, bg = "magenta", font = "times 12 bold", height = 2)
        self.funMidSpace3 = tkinter.Label(self.funLinksFrame, bg = "khaki", text = "   ")
        self.gameButton = tkinter.Button(self.funLinksFrame, text = "Things to Play!", command = self.game, width = 20, bg = "darkOrange", font = "times 12 bold", height = 2)
        self.funRightSpace = tkinter.Label(self.funLinksFrame, bg = "khaki", text = "   ")

        self.funLabel.pack(side = "top") # Arranging for the fun stuff
        self.funSpace.pack()
        self.funLeftSpace.pack(side = "left")
        self.bookButton.pack(side = "left")
        self.funMidSpace1.pack(side = "left")
        self.diyButton.pack(side = "left")
        self.funMidSpace2.pack(side = "left")
        self.movieButton.pack(side = "left")
        self.funMidSpace3.pack(side = "left")
        self.gameButton.pack(side = "left")
        self.funRightSpace.pack(side = "left")
        

        self.topSpaceFrame.pack() # Packing the sections together
        self.edLinksFrame.pack()
        self.spaceFrame.pack()
        self.funLinksFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop() # Checking for updates



    def ela(self): # The information for English-:anguage Arts
        elaWindow = tkinter.Tk() # A new window has appeared
        elaWindow.configure(bg = "navy")
        linkFrame = tkinter.Frame(elaWindow, bg = "navy", width = 300)
        infoFrame = tkinter.Frame(elaWindow, bg = "navy", width = 300)

        line = 1 #What line it is for the listbox
        linkList = ["https://www.readbrightly.com/30-best-level-1-reading-books-for-children/", "readingrockets.org/article/six-games-reading", "https://pbskids.org/games/reading/", "https://www.kaplaninternational.com/blog/childrens-books-for-English-learners"] # A list of links
        linkInfo = tkinter.Label(linkFrame, bg = "navy", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser for some English information!", fg = "white", font = "times 12 bold") # Telling kids what to do to access the info
        linkLabel = tkinter.Listbox(linkFrame, bg = "navy", fg = "white", font = "times 12 bold", width = 75) # Tkinter text doesn't highlight normally so works better as a listbox

        for i in linkList:
            linkLabel.insert(line, i) # Putting a link on every line
            line += 1

        linkInfo.pack()
        linkLabel.pack()

        deviceInfo = tkinter.Label(infoFrame, text = "If you have a phone or tablet, here are some apps you can download to help learn to read:\nReading Eggs, Starfall, ABC Kids", bg = "navy", fg = "white", font = "times 12 bold") # Some apps for learning to read
        booksInfo = tkinter.Label(infoFrame, bg = "navy", fg = "white", text = "Here are some easy series you can read to improve your vocabulary and reading level:\n The Boxcar Children series, The Magic Treehouse Series", font = "times 12 bold") # Some reading suggestions for older kids in this age group

        deviceInfo.pack()
        booksInfo.pack()

        linkFrame.pack()
        infoFrame.pack()

    def math(self): # The math information
        mathWindow = tkinter.Tk()
        mathWindow.configure(bg = "firebrick")
        linkFrame = tkinter.Frame(mathWindow, bg = "firebrick", width = 300)
        infoFrame = tkinter.Frame(mathWindow, bg = "firebrick", width = 300)

        linkInfo = tkinter.Label(linkFrame, bg = "firebrick", fg = "white", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser for some information and games on how to do math!", font = "times 12 bold")
        line = 1 # I rearranged the lines for this and all consecutive functions
        linkList = ["https://www.khanacademy.org/", "http://www.mathgametime.com/", "https://corbettmaths.com/", "https://gregtangmath.com/", "https://illuminations.nctm.org/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "firebrick", fg = "white", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkInfo.pack()
        linkBox.pack()

        deviceInfo = tkinter.Label(infoFrame, text = "If you have a phone or tablet, here are some apps you can download to help learn math:\nKhan Academy, Math Learner, Monster Math", bg = "firebrick", fg = "white", font = "times 12 bold")

        deviceInfo.pack()

        linkFrame.pack()
        infoFrame.pack()

    def history(self): # History Information
        historyWindow = tkinter.Tk()
        historyWindow.configure(bg = "mediumVioletRed")
        linkFrame = tkinter.Frame(historyWindow, bg = "mediumVioletRed", width = 300)
        infoFrame = tkinter.Frame(historyWindow, bg = "mediumVioletRed", width = 300)

        linkInfo = tkinter.Label(linkFrame, bg = "mediumVioletRed", fg = "white", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser for some information on history!")
        line = 1
        linkList = ["https://www.ducksters.com/history/", "https://americanhistory.mrdonn.org/", "https://www.census.gov/programs-surveys/sis/activities/history.Grades_K-5.html", "https://www.education.com/activity/history/", "https://quizlet.com/415/us-state-capitals-flash-cards/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumVioletRed", font = "times 12 bold", width = 75, fg = "white")

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkInfo.pack()
        linkBox.pack()

        deviceInfo = tkinter.Label(infoFrame, bg = "mediumVioletRed", fg = "white", font = "times 12 bold", text = "If you have a phone or tablet, here are some apps you can download to help learn history:\nSmithsonian Channel, 50 States and Capitals")

        deviceInfo.pack()
        
        linkFrame.pack()
        infoFrame.pack()

    def science(self): # Science window
        sciWindow = tkinter.Tk()
        sciWindow.configure(bg = "darkGreen")
        linkFrame = tkinter.Frame(sciWindow, bg = "darkGreen", width = 300)
        infoFrame = tkinter.Frame(sciWindow, bg = "darkGreen", width = 300)

        linkInfo = tkinter.Label(linkFrame, bg = "darkGreen", fg = "white", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser to learn some science!")
        line = 1
        linkList = ["https://www.sciencekids.co.nz/", "https://www.scienceforkidsclub.com/", "https://www.ducksters.com/science/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkGreen", fg = "white", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkInfo.pack()
        linkBox.pack()

        deviceInfo = tkinter.Label(infoFrame, bg = "darkGreen", fg = "white", font = "times 12 bold", text = "If you have a phone or tablet, here are some apps you can download:\nElevate Science, K-5 Science for Kids")

        deviceInfo.pack()

        linkFrame.pack()
        infoFrame.pack()

    def books(self): # When they aren't doing educational stuff, there's some ideas to keep kids busy, especially during quarantine
        bookWindow = tkinter.Tk()
        bookWindow.configure(bg = "teal")
        linkFrame = tkinter.Frame(bookWindow, bg = "teal", width = 300)
        infoFrame = tkinter.Frame(bookWindow, bg = "teal", width = 300)

        linkInfo = tkinter.Label(linkFrame, bg = "teal", fg = "white", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser for some books to read!")
        line = 1
        linkList = ["https://www.commonsensemedia.org/lists/50-books-all-kids-should-read-before-theyre-12", "https://time.com/100-best-childrens-books/", "https://www.goodhousekeeping.com/life/entertainment/g3273/best-childrens-books/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "teal", fg = "white", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkInfo.pack()
        linkBox.pack()

        deviceInfo = tkinter.Label(infoFrame, bg = "teal", fg = "white", font = "times 12 bold", text = "If you have a phone or tablet, here are some apps you can download to get books:\nKindle, Goodreads, Libby")

        deviceInfo.pack()

        linkFrame.pack()
        infoFrame.pack()

    def diy(self): # Some at-home activities to be away from the screen
        diyWindow = tkinter.Tk()
        diyWindow.configure(bg = "gold")
        linkFrame = tkinter.Frame(diyWindow, bg = "gold", width = 300)
        infoFrame = tkinter.Frame(diyWindow, bg = "gold", width = 300)

        linkInfo = tkinter.Label(linkFrame, bg = "gold", fg = "white", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser for some do-it-yourself ideas!")
        line = 1
        linkList = ["https://www.goodhousekeeping.com/home/craft-ideas/how-to/g1389/diy-kids-activities/", "https://diyjoy.com/diy-ideas-for-kids-to-make/", "https://kinderart.com/art-lessons/seasons/5-creative-activities-kids-can/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "gold", fg = "white", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkInfo.pack()
        linkBox.pack()

        deviceInfo = tkinter.Label(infoFrame, bg = "gold", fg = "white", font = "times 12 bold", text = "If you have a phone or tablet, here are some apps you can download to make things online:\nPaint by Number, Coloring Book, Connect the Dots")

        deviceInfo.pack()

        linkFrame.pack()
        infoFrame.pack()

    def movie(self): # Some movies and tv shows with some places to watch them
        movieWindow = tkinter.Tk()
        movieWindow.configure(bg = "purple")
        linkFrame = tkinter.Frame(movieWindow, bg = "purple", width = 300)
        infoFrame = tkinter.Frame(movieWindow, bg = "purple", width = 300)

        linkInfo = tkinter.Label(linkFrame, bg = "purple", fg = "white", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser for some movies and tv shows to watch!")
        line = 1
        linkList = ["https://www.imdb.com/list/ls058077737/", "https://www.commonsensemedia.org/tv-lists", "https://tubitv.com/category/kids_shows", "https://classiccinemaonline.com/movie-billboards/family", "https://www.popcornflix.com/channels/details/familykids"]
        linkBox = tkinter.Listbox(linkFrame, bg = "purple", fg = "white", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkInfo.pack()
        linkBox.pack()

        deviceInfo = tkinter.Label(infoFrame, bg = "purple", fg = "white", font = "times 12 bold", text = "If you have a phone or tablet, here are some apps you can download to watch things on:\nTubi, Crunchy Roll, Netflix, Youtube, Amazon")

        deviceInfo.pack()

        linkFrame.pack()
        infoFrame.pack()

    def game(self): # Some games online
        gameWindow = tkinter.Tk()
        gameWindow.configure(bg = "chocolate")
        linkFrame = tkinter.Frame(gameWindow, bg = "chocolate", width = 300)
        infoFrame = tkinter.Frame(gameWindow, bg = "chocolate", width = 300)

        linkInfo = tkinter.Label(linkFrame, bg = "chocolate", fg = "white", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links into a browser for some fun games to play!")
        line = 1
        linkList = ["https://pbskids.org/games/", "http://www.nickjr.com/games/", "https://lol.disney.com/games", "https://www.coolmathgames.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "chocolate", fg = "white", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkInfo.pack()
        linkBox.pack()

        deviceInfo = tkinter.Label(infoFrame, bg = "chocolate", fg = "white", font = "times 12 bold", text = "If you have a phone or tablet, here are some apps you can download to play some games:\nSubway Surfers, Fruit Ninja, Crossy Road, Cut the Rope, Jetpack")

        deviceInfo.pack()

        linkFrame.pack()
        infoFrame.pack()

