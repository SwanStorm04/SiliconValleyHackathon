import toddlers
import kids
import preTeens
import highSchool
import college
import youngAdults
import adults
import retired
import tkinter #importing all of the other files with the GUIs, as well as the library I use for GUIs

class mainMenu:
    def __init__(self):

        self.mainWindow = tkinter.Tk() #The main screen
        self.mainWindow.configure(bg = "mistyRose")

        self.topSpaceFrame = tkinter.Frame(self.mainWindow, bg = "mistyRose", width = 300) #Sectioning off the screen, separating the buttons for space
        self.topButtonFrame = tkinter.Frame(self.mainWindow, bg = "mistyRose", width = 300)
        self.mid1SpaceFrame = tkinter.Frame(self.mainWindow, bg = "mistyRose", width = 300)
        self.infoFrame = tkinter.Frame(self.mainWindow, bg = "mistyRose", width = 300)
        self.mid2SpaceFrame = tkinter.Frame(self.mainWindow, bg = "mistyRose", width = 300)
        self.botButtonFrame = tkinter.Frame(self.mainWindow, bg = "mistyRose", width = 300)
        self.botSpaceFrame = tkinter.Frame(self.mainWindow, bg = "mistyRose", width = 300)

        self.topSpace = tkinter.Label(self.topSpaceFrame, text="                 ", bg="mistyRose") #Putting some space in each of the space frames
        self.topSpace.pack()
        self.midFrameSpace = tkinter.Label(self.mid1SpaceFrame, text="              ", bg="mistyRose")
        self.midFrameSpace.pack()
        self.mid2FrameSpace = tkinter.Label(self.mid2SpaceFrame, text="              ", bg="mistyRose")
        self.mid2FrameSpace.pack()
        self.botSpace = tkinter.Label(self.botSpaceFrame, text="              ", bg="mistyRose")
        self.botSpace.pack()

        self.topLeftSpace = tkinter.Label(self.topButtonFrame, bg = "mistyRose", text = "   ") # The first half of the buttons, with some space between them and at the ends
        self.toddButton = tkinter.Button(self.topButtonFrame, text = "Toddlers!", command = self.toddler, width = 20, bg = "salmon", font = "times 12 bold")
        self.topSpaceMid1 = tkinter.Label(self.topButtonFrame, bg = "mistyRose", text = "   ")
        self.kidButton = tkinter.Button(self.topButtonFrame, text = "Kids!", command = self.kid, width = 20, bg = "orange", font = "times 12 bold")
        self.topSpaceMid2 = tkinter.Label(self.topButtonFrame, bg = "mistyRose", text = "   ")
        self.preButton = tkinter.Button(self.topButtonFrame, text = "Preteens!", command = self.preTeen, width = 20, bg = "gold", font = "times 12 bold")
        self.topSpaceMid3 = tkinter.Label(self.topButtonFrame, bg = "mistyRose", text = "   ")
        self.highButton = tkinter.Button(self.topButtonFrame, text = "High-Schoolers!", command = self.highSchool, width = 20, bg = "Chartreuse", font = "times 12 bold")
        self.topRightSpace = tkinter.Label(self.topButtonFrame, bg = "mistyRose", text = "   ")

        self.topLeftSpace.pack(side = "left") # Packing everything so it's recognized
        self.toddButton.pack(side = "left")
        self.topSpaceMid1.pack(side = "left")
        self.kidButton.pack(side = "left")
        self.topSpaceMid2.pack(side = "left")
        self.preButton.pack(side = "left")
        self.topSpaceMid3.pack(side = "left")
        self.highButton.pack(side = "left")
        self.topRightSpace.pack(side = "left")

        self.info = tkinter.Label(self.infoFrame, bg = "mistyRose", text = "Pick your age group!", font = "times 12 bold") # Instructions!
        self.info.pack()

        self.botLeftSpace = tkinter.Label(self.botButtonFrame, bg = "mistyRose", text = "   ") # The other half of the buttons and space
        self.colButton = tkinter.Button(self.botButtonFrame, text = "College Students!", command = self.college, width = 20, bg = "limeGreen", font = "times 12 bold")
        self.botSpaceMid1 = tkinter.Label(self.botButtonFrame, bg = "mistyRose", text = "   ")
        self.yaButton = tkinter.Button(self.botButtonFrame, text = "Young Adults!", command = self.youngAdult, width = 20, bg = "mediumBlue", font = "times 12 bold")
        self.botSpaceMid2 = tkinter.Label(self.botButtonFrame, bg = "mistyRose", text = "   ")
        self.adButton = tkinter.Button(self.botButtonFrame, text = "Adults!", command = self.adult, width = 20, bg = "slateBlue", font = "times 12 bold")
        self.botSpaceMid3 = tkinter.Label(self.botButtonFrame, bg = "mistyRose", text = "   ")
        self.senButton = tkinter.Button(self.botButtonFrame, text = "Seniors!", command = self.senior, width = 20, bg = "darkViolet", font = "times 12 bold")
        self.botRightSpace = tkinter.Label(self.botButtonFrame, bg = "mistyRose", text = "   ")

        self.botLeftSpace.pack(side = "left") # Packing again
        self.colButton.pack(side = "left")
        self.botSpaceMid1.pack(side = "left")
        self.yaButton.pack(side = "left")
        self.botSpaceMid2.pack(side = "left")
        self.adButton.pack(side = "left")
        self.botSpaceMid3.pack(side = "left")
        self.senButton.pack(side = "left")
        self.botRightSpace.pack(side = "left")


        self.topSpaceFrame.pack() # Packing every frame
        self.topButtonFrame.pack()
        self.mid1SpaceFrame.pack()
        self.infoFrame.pack()
        self.mid2SpaceFrame.pack()
        self.botButtonFrame.pack()
        self.botSpaceFrame.pack()

        tkinter.mainloop() # Starting the check-up loop


    def toddler(self): # Every button has a function that destroys the selection window and runs that group's program
        self.mainWindow.destroy()
        toddlers.Toddler()
    
    def kid(self):
        self.mainWindow.destroy()
        kids.Kid()

    def preTeen(self):
        self.mainWindow.destroy()
        preTeens.PreTeen()

    def highSchool(self):
        self.mainWindow.destroy()
        highSchool.HighSchooler()

    def college(self):
        self.mainWindow.destroy()
        college.CollegeStudent()

    def youngAdult(self):
        self.mainWindow.destroy()
        youngAdults.YoungAdult()

    def adult(self):
        self.mainWindow.destroy()
        adults.Adult()

    def senior(self):
        self.mainWindow.destroy()
        retired.Senior()






run = mainMenu() # Starting the menu
