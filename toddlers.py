import tkinter

class Toddler:
    
    def __init__(self):
        self.toddWindow = tkinter.Tk()
        self.toddWindow.configure(bg = "gainsboro")

        self.topSpaceFrame = tkinter.Frame(self.toddWindow, bg = "gainsboro", width = 300)
        self.warningFrame = tkinter.Frame(self.toddWindow, bg = "gainsboro", width = 300)
        self.space1Frame = tkinter.Frame(self.toddWindow, bg = "gainsboro", width = 300)
        self.edFrame = tkinter.Frame(self.toddWindow, bg = "gainsboro", width = 300)
        self.space2Frame = tkinter.Frame(self.toddWindow, bg = "gainsboro", width = 300)
        self.funFrame = tkinter.Frame(self.toddWindow, bg = "gainsboro", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.toddWindow, bg = "gainsboro", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, bg = "gainsboro", text = "   ")
        self.topSpace.pack()
        self.midSpace1 = tkinter.Label(self.space1Frame, bg = "gainsboro", text = "   ")
        self.midSpace1.pack()
        self.midSpace2 = tkinter.Label(self.space2Frame, bg = "gainsboro", text = "   ")
        self.midSpace2.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, bg = "gainsboro", text = "   ")
        self.botSpace.pack()

        self.warnLabel = tkinter.Label(self.warningFrame, bg = "gainsboro", font = "times 16 bold", text = "Always watch what kids are doing online, with random clicking\nthere is always a chance of kids going somewhere not\nkid or family-friendly", fg = "lightCoral")

        self.warnLabel.pack()

        self.edLabel = tkinter.Label(self.edFrame, bg = "gainsboro", font = "times 14 bold", fg = "goldenrod", text = "Educational information!")
        self.edSpace = tkinter.Label(self.edFrame, bg = "gainsboro", text = "   ")
        self.edLeftSpace = tkinter.Label(self.edFrame, bg = "gainsboro", text = "   ")
        self.alphButton = tkinter.Button(self.edFrame, command = self.alphabet, width = 20, bg = "khaki", font = "times 12 bold", height = 2, text = "Alphabet!")
        self.edMidSpace1 = tkinter.Label(self.edFrame, bg = "gainsboro", text = "   ")
        self.numButton = tkinter.Button(self.edFrame, command = self.numbers, width = 20, bg = "khaki", font = "times 12 bold", height = 2, text = "Numbers!")
        self.edMidSpace2 = tkinter.Label(self.edFrame, bg = "gainsboro", text = "   ")
        self.colButton = tkinter.Button(self.edFrame, command = self.colors, width = 20, bg = "khaki", font = "times 12 bold", height = 2, text = "Colors!")
        self.edRightSpace = tkinter.Label(self.edFrame, bg = "gainsboro", text = "   ")

        self.edLabel.pack()
        self.edSpace.pack()
        self.edLeftSpace.pack(side = "left")
        self.alphButton.pack(side = "left")
        self.edMidSpace1.pack(side = "left")
        self.numButton.pack(side = "left")
        self.edMidSpace2.pack(side = "left")
        self.colButton.pack(side = "left")
        self.edRightSpace.pack(side = "left")

        self.funLabel = tkinter.Label(self.funFrame, bg = "gainsboro", font = "times 14 bold", fg = "mediumBlue", text = "Fun activities!")
        self.funSpace = tkinter.Label(self.funFrame, bg = "gainsboro", text = "   ")
        self.funLeftSpace = tkinter.Label(self.funFrame, bg = "gainsboro", text = "   ")
        self.showButton = tkinter.Button(self.funFrame, command = self.movie, width = 20, bg = "deepSkyBlue", font = "times 12 bold", height = 2, text = "Shows!")
        self.funMidSpace = tkinter.Label(self.funFrame, bg = "gainsboro", text = "   ")
        self.toyButton = tkinter.Button(self.funFrame, command = self.toy, width = 20, bg = "deepSkyBlue", font = "times 12 bold", height = 2, text = "Toys!")
        self.funRightSpace = tkinter.Label(self.funFrame, bg = "gainsboro", text = "   ")

        self.funLabel.pack()
        self.funSpace.pack()
        self.funLeftSpace.pack(side = "left")
        self.showButton.pack(side = "left")
        self.funMidSpace.pack(side = "left")
        self.toyButton.pack(side = "left")
        self.funRightSpace.pack(side = "left")
        
        self.topSpaceFrame.pack()
        self.warningFrame.pack()
        self.space1Frame.pack()
        self.edFrame.pack()
        self.space2Frame.pack()
        self.funFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop()


    def alphabet(self):
        window = tkinter.Tk()
        window.configure(bg = "khaki")

        infoFrame = tkinter.Frame(window, bg = "khaki", width = 300)
        linkFrame = tkinter.Frame(window, bg = "khaki", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "khaki", font = "times 12 bold", text = "Learning the alphabet is important for learning how to read")
        genSpace = tkinter.Label(infoFrame, bg = "khaki", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "khaki", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for videos on the alphabet\nand how to teach it to kids")
        line = 1
        linkList = ["https://www.youtube.com/watch?v=2XGuSlGMphY", "prekinders.com/teaching-the-alphabet-part-1/", "https://teachingmama.org/5-ways-to-teach-the-alphabet/", "https://www.youtube.com/watch?v=_UR-l3QI2nE", "https://www.youtube.com/watch?v=75p-N9YKqNo"]
        linkBox = tkinter.Listbox(linkFrame, bg = "khaki", font = "times 12 bold", width = 50)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def numbers(self):
        window = tkinter.Tk()
        window.configure(bg = "khaki")

        infoFrame = tkinter.Frame(window, bg = "khaki", width = 300)
        linkFrame = tkinter.Frame(window, bg = "khaki", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "khaki", font = "times 12 bold", text = "Learning to count helps kids get a headstart in math")
        genSpace = tkinter.Label(infoFrame, bg = "khaki", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "khaki", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for how to teach the numbers\nand numbers songs")
        line = 1
        linkList = ["https://www.k5learning.com/free-preschool-kindergarten-worksheets/numbers-counting", "https://funlearningforkids.com/learning-numbers-hands-number-activities/", "https://www.youtube.com/watch?v=EjT5SA9WrY4", "https://www.youtube.com/watch?v=72L2zoCIpng"]
        linkBox = tkinter.Listbox(linkFrame, bg = "khaki", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def colors(self):
        window = tkinter.Tk()
        window.configure(bg = "khaki")

        infoFrame = tkinter.Frame(window, bg = "khaki", width = 300)
        linkFrame = tkinter.Frame(window, bg = "khaki", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "khaki", font = "times 12 bold", text = "Teaching kids to identify colors helps them with art")
        genSpace = tkinter.Label(infoFrame, bg = "khaki", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "khaki", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for how to teach colors\nand videos teaching colors")
        line = 1
        linkList = ["https://www.youtube.com/watch?v=xW2bjae5LPM", "https://www.youtube.com/watch?v=yfbHlMNo79s", "https://www.youtube.com/watch?v=aPM3h9UV2S0", "https://teaching2and3yearolds.com/how-to-teach-toddler-colors-fun-15-activities/", "https://stayathomeeducator.com/6-ways-to-teach-colors-to-toddlers/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "khaki", font = "times 12 bold", width = 70)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def movie(self):
        window = tkinter.Tk()
        window.configure(bg = "deepSkyBlue")

        infoFrame = tkinter.Frame(window, bg = "deepSkyBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "deepSkyBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "deepSkyBlue", font = "times 12 bold", text = "Movies and TV shows are good to calm down kids\nand give them a chance to relax")
        genSpace = tkinter.Label(infoFrame, bg = "deepSkyBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "deepSkyBlue", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some good movies and tv shows\nfor toddlers")
        line = 1
        linkList = ["https://www.commonsensemedia.org/lists/best-preschool-tv-shows", "https://www.commonsensemedia.org/lists/best-kids-tv-shows-on-netflix", "https://www.goodhousekeeping.com/life/entertainment/g25436424/best-toddler-movies/", "https://www.pastemagazine.com/tv/netflix/the-10-best-netflix-shows-for-toddlers/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "deepSkyBlue", font = "times 12 bold", width = 75)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


    def toy(self):
        window = tkinter.Tk()
        window.configure(bg = "deepSkyBlue")

        infoFrame = tkinter.Frame(window, bg = "deepSkyBlue", width = 300)
        linkFrame = tkinter.Frame(window, bg = "deepSkyBlue", width = 300)

        genInfo = tkinter.Label(infoFrame, bg = "deepSkyBlue", font = "times 12 bold", text = "Toys are good for kids to play with")
        genSpace = tkinter.Label(infoFrame, bg = "deepSkyBlue", text = "   ")

        genInfo.pack()
        genSpace.pack()

        linkLabel = tkinter.Label(linkFrame, bg = "deepSkyBlue", font = "times 12 bold", text = "Copy (ctrl + c) and paste (ctrl + v) these links\ninto a browser for some toys you can make\nor buy")
        line = 1
        linkList = ["https://www.goodhousekeeping.com/childrens-products/toy-reviews/g26670041/educational-toys-for-toddlers/", "https://www.amazon.com/Best-Sellers-Toys-Games-Toddler/zgbs/toys-and-games/251945011", "https://www.diyncrafts.com/27127/homemade/30-fun-educational-baby-toys-can-diy-spare-time", "https://lalymom.com/50-cool-diy-toys-fine-motor-skills/", "https://rhythmsandgraceblog.com/cheap-homemade-toddler-toys-and-activities/"]
        linkBox = tkinter.Listbox(linkFrame, bg = "deepSkyBlue", font = "times 12 bold", width = 90)

        for i in linkList:
            linkBox.insert(line, i)
            line += 1

        linkLabel.pack()
        linkBox.pack()

        infoFrame.pack()
        linkFrame.pack()


