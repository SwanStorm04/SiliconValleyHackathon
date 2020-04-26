import tkinter

class PreTeen:

    def __init__(self):
        self.preWindow = tkinter.Tk()
        self.preWindow.configure(bg = "indianRed")

        self.topSpaceFrame = tkinter.Frame(self.preWindow, bg = "indianRed", width = 300)
        self.edFrame = tkinter.Frame(self.preWindow, bg = "indianRed", width = 300)
        self.spaceFrame = tkinter.Frame(self.preWindow, bg = "indianRed", width = 300)
        self.funFrame = tkinter.Frame(self.preWindow, bg = "indianRed", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.preWindow, bg = "indianRed", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "indianRed", text = "   ")
        self.topSpace.pack()
        self.midSpace = tkinter.Label(self.spaceFrame, bg = "indianRed", text = "   ")
        self.midSpace.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "indianRed", text = "   ")
        self.botSpace.pack()

        self.edLabel = tkinter.Label(self.edFrame, bg = "indianRed", font = "times 14 bold", text = "Educational information")
        self.edSpace = tkinter.Label(self.edFrame, bg = "indianRed", text = "   ")
        self.edLeftSpace = tkinter.Label(self.edFrame, bg = "indianRed", text = "   ")
        self.elaButton = tkinter.Button(self.edFrame, command = self.ela, width = 20, height = 2, bg = "mediumBlue", font = "times 12 bold", text = "ELA")
        self.edMidSpace1 = tkinter.Label(self.edFrame, bg = "indianRed", text = "   ")
        self.mathButton = tkinter.Button(self.edFrame, command = self.math, width = 20, height = 2, bg = "crimson", font = "times 12 bold", text = "Math")
        self.edMidSpace2 = tkinter.Label(self.edFrame, bg = "indianRed", text = "   ")
        self.histButton = tkinter.Button(self.edFrame, command = self.history, width = 20, height = 2, bg = "purple", font = "times 12 bold", text = "History")
        self.edMidSpace3 = tkinter.Label(self.edFrame, bg = "indianRed", text = "   ")
        self.sciButton = tkinter.Button(self.edFrame, command = self.science, width = 20, height = 2, bg = "darkGreen", font = "times 12 bold", text = "Science")
        self.edMidSpace4 = tkinter.Label(self.edFrame, bg = "indianRed", text = "   ")
        self.lgbtButton = tkinter.Button(self.edFrame, command = self.lgbt, width = 20, height = 2, bg = "goldenrod", font = "times 12 bold", text = "LGBTQ+")
        self.edRightSpace = tkinter.Label(self.edFrame, bg = "indianRed", text = "   ")

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

        self.funLabel = tkinter.Label(self.funFrame, bg = "indianRed", font = "times 14 bold", text = "Fun Things to Do")
        self.funSpace = tkinter.Label(self.funFrame, bg = "indianRed", text = "   ")
        self.funLeftSpace = tkinter.Label(self.funFrame, bg = "indianRed", text = "   ")
        self.bookButton = tkinter.Button(self.funFrame, command = self.book, width = 20, height = 2, bg = "teal", font = "times 12 bold", text = "Books")
        self.funMidSpace1 = tkinter.Label(self.funFrame, bg = "indianRed", text = "   ")
        self.diyButton = tkinter.Button(self.funFrame, command = self.diy, width = 20, height = 2, bg = "darkOrange", font = "times 12 bold", text = "Do-It-Yourself")
        self.funMidSpace2 = tkinter.Label(self.funFrame, bg = "indianRed", text = "   ")
        self.movieButton = tkinter.Button(self.funFrame, command = self.movie, width = 20, height = 2, bg = "indigo", font = "times 12 bold", text = "Movies and TV Shows")
        self.funMidSpace3 = tkinter.Label(self.funFrame, bg = "indianRed", text = "   ")
        self.gameButton = tkinter.Button(self.funFrame, command = self.game, width = 20, height = 2, bg = "mediumVioletRed", font = "times 12 bold", text = "Games")
        self.funRightSpace = tkinter.Label(self.funFrame, bg = "indianRed", text = "   ")

        self.funLabel.pack()
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

        self.topSpaceFrame.pack()
        self.edFrame.pack()
        self.spaceFrame.pack()
        self.funFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop()

    def ela(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumBlue")

        infoFrame = tkinter.Frame(window, bg = "mediumBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumBlue", fg = "antiqueWhite", font = "times 12 bold", text = "Improving vocabulary and learning grammar is important for writing")
        genSpace = tkinter.Label(infoFrame, bg = "mediumBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumBlue", fg = "antiqueWhite", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some help learning grammer\nand reading exercises")
        line = 1
        linkList = ["https://www.slj.com/?detailStory=13-books-for-tweens-booklist-libraries", "https://www.commonsensemedia.org/lists/best-book-series-for-tweens", "https://learnenglishteens.britishcouncil.org/grammar/beginner-grammar", "https://www.talkenglish.com/grammar/grammar.aspx"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumBlue", font = "times 12 bold", width = 65, fg = "antiqueWhite")

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

        genInfo = tkinter.Label(infoFrame, bg = "crimson", fg = "honeydew", font = "times 12 bold", text = "Learning math is really useful in science, high school subjects,\nand in life.")
        genSpace = tkinter.Label(infoFrame, bg = "crimson", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "crimson", fg = "honeydew", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some math tutorials and information")
        line = 1
        linkList = ["https://www.khanacademy.org/", "https://mathtv.com/", "https://curriculum.illustrativemathematics.org/MS/teachers/index.html", "https://sso.prodigygame.com/signup", "https://lpb.pbslearningmedia.org/collection/mathcore/", "https://www.nctm.org/publications/mathematics-teaching-in-the-middle-school/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "crimson", fg = "honeydew", font = "times 12 bold", width = 70)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def history(self):
        window = tkinter.Tk()
        window.configure(bg = "purple")

        infoFrame = tkinter.Frame(window, bg = "purple", width = 300)
        linkFrame = tkinter.Frame(window, bg = "purple", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "purple", fg = "lightYellow", font = "times 12 bold", text = "History is really useful in discussion, so people can learn from\nthe mistakes of others and improve")
        genSpace = tkinter.Label(infoFrame, bg = "purple", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "purple", fg = "lightYellow", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some information\non world and US history")
        line = 1
        linkList = ["https://teachinghistory.org/quick-links-middle", "https://www.history.com/classroom", "https://study.com/academy/course/middle-school-world-history.html", "https://nmaahc.si.edu/", "https://historyexplorer.si.edu/", "https://study.com/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "purple", fg = "lightYellow", font = "times 12 bold", width = 60)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def science(self):
        window = tkinter.Tk()
        window.configure(bg = "darkGreen")

        infoFrame = tkinter.Frame(window, bg = "darkGreen", width = 300)
        linkFrame = tkinter.Frame(window, bg = "darkGreen", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "darkGreen", fg = "mistyRose", font = "times 12 bold", text = "Science is important for understanding the world and making\nnew technology")
        genSpace = tkinter.Label(infoFrame, bg = "darkGreen", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "darkGreen", fg = "mistyRose", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for online science classes")
        line = 1
        linkList = ["https://www.weareteachers.com/best-science-websites/", "https://www.calacademy.org/learn-explore", "https://ssec.si.edu/", "https://www.howtosmile.org/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkGreen", fg = "mistyRose", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def lgbt(self):
        window = tkinter.Tk()
        window.configure(bg = "goldenrod")

        infoFrame = tkinter.Frame(window, bg = "goldenrod", width = 300)
        linkFrame = tkinter.Frame(window, bg = "goldenrod", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "goldenrod", fg = "lavender", font = "times 12 bold", text = "In this time of self-discovery, it is important to learn about\nall the identities out there that could apply to you,\nif you want them. If not, it's good to know this information\nso you can support your friends in the community. The letters in LGBTQIA+ stand for:\nLesbian (girls who like girls), Gay (boys who like boys), Bisexual (people who like two or more genders),\nTransgender (someone who's gender does not match their birth sex), Queer (a cover-all for not straight and cisgender),\nIntersex (someone who was born with traits of multiple sexes), and Asexual/Aromantic/Agender (someone who does not feel sexual attraction, romantic attraction, or does not have a gender)")
        genSpace = tkinter.Label(infoFrame, bg = "goldenrod", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "goldenrod", fg = "lavender", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some basic information on the LGBTQ comminity and using pronouns,\nas well as some support information")
        line = 1
        linkList = ["http://vos.ucsb.edu/browse.asp?id=994", "https://www.thetrevorproject.org/", "https://www.cdc.gov/lgbthealth/youth-resources.htm", "https://www.aclu.org/library-lgbt-youth-schools-resources-and-links", "https://www.genderspectrum.org/", "https://www.usatoday.com/story/news/2017/06/15/lgbtq-glossary-slang-ally-learn-language/101200092/", "https://www.itspronouncedmetrosexual.com/2013/01/a-comprehensive-list-of-lgbtq-term-definitions/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "goldenrod", fg = "lavender", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def book(self):
        window = tkinter.Tk()
        window.configure(bg = "teal")

        infoFrame = tkinter.Frame(window, bg = "teal", width = 300)
        linkFrame = tkinter.Frame(window, bg = "teal", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "teal", fg = "navajoWhite", font = "times 12 bold", text = "Reading is a good way to pass the time and keep your mind sharp.\nMany people also use books to put themselves into the character's shoes and live\ndifferent lives for a bit.")
        genSpace = tkinter.Label(infoFrame, bg = "teal", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "teal", fg = "navajoWhite", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some good books to read of many genres.")
        line = 1
        linkList = ["https://www.weareteachers.com/best-middle-school-books/", "https://www.readbrightly.com/books-for-middle-schoolers/", "https://www.goodreads.com/list/show/1606.Top_100_Middle_School_Must_Reads", "https://www.scholastic.com/parents/books-and-reading/book-lists-and-recommendations/favorites-classics/top-picks-middle-schoolers.html", "https://k-12readinglist.com/category/reading-lists-for-middle-school-children/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "teal", fg = "navajoWhite", font = "times 12 bold", width = 115)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def diy(self):
        window = tkinter.Tk()
        window.configure(bg = "darkOrange")

        infoFrame = tkinter.Frame(window, bg = "darkOrange", width = 300)
        linkFrame = tkinter.Frame(window, bg = "darkOrange", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "darkOrange", fg = "lightCyan", font = "times 12 bold", text = "Making things is really fun and personal,\nand you can use them as gifts!")
        genSpace = tkinter.Label(infoFrame, bg = "darkOrange", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "darkOrange", fg = "lightCyan", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some ideas on projects to make")
        line = 1
        linkList = ["https://www.instructables.com/id/6-8-Projects-Middle-School/", "https://www.thesprucecrafts.com/origami-projects-for-kids-4142802", "https://www.youtube.com/watch?v=VIVIegSt81k", "https://www.scholastic.com/teachers/articles/teaching-content/37-amazing-craft-ideas/", "https://www.allfreekidscrafts.com/Miscellaneous-Crafts-for-Kids/Cool-Crafts-for-Tweens-Tween-Crafts-for-Middle-School-Kids"]
        linkBox = tkinter.Listbox(linkFrame, bg = "darkOrange", fg = "lightCyan", font = "times 12 bold", width = 110)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def movie(self):
        window = tkinter.Tk()
        window.configure(bg = "indigo")

        infoFrame = tkinter.Frame(window, bg = "indigo", width = 300)
        linkFrame = tkinter.Frame(window, bg = "indigo", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "indigo", fg = "moccasin", font = "times 12 bold", text = "Movies and TV shows are a good way to relax\nor to use as some background noise.")
        genSpace = tkinter.Label(infoFrame, bg = "indigo", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "indigo", fg = "moccasin", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some movies and tv shows to watch.")
        line = 1
        linkList = ["https://www.commonsensemedia.org/lists/best-tween-tv-shows", "https://www.commonsensemedia.org/lists/best-tween-movies", "https://www.imdb.com/search/keyword/?keywords=junior-high-school", "https://www.goodhousekeeping.com/life/entertainment/g26977251/netflix-shows-for-tweens/", "https://www.imdb.com/list/ls068292073/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "indigo", fg = "moccasin", font = "times 12 bold", width = 80)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def game(self):
        window = tkinter.Tk()
        window.configure(bg = "mediumVioletRed")

        infoFrame = tkinter.Frame(window, bg = "mediumVioletRed", width = 300)
        linkFrame = tkinter.Frame(window, bg = "mediumVioletRed", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "mediumVioletRed", fg = "paleGreen", font = "times 12 bold", text = "Games are a good bonding experience or a way to pass the time")
        genSpace = tkinter.Label(infoFrame, bg = "mediumVioletRed", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "mediumVioletRed", fg = "paleGreen", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some online games\nand some card or board games")
        line = 1
        linkList = ["https://www.greatgroupgames.com/middle-school-group-games.htm", "https://www.weareteachers.com/team-building-games-and-activities/", "https://www.commonsense.org/education/top-picks/10-great-free-games-for-middle-school-students", "https://thecornerstoneforteachers.com/15-fun-indoor-recess-games-and-activities/", "https://www.sldirectory.com/studf/cool.html"]
        linkBox = tkinter.Listbox(linkFrame, bg = "mediumVioletRed", fg = "paleGreen", font = "times 12 bold", width = 85)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()

