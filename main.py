class CleanUp():

    title = 'Android Bloatware CleanUp'
    font = ('Comic Sans MS', 15)
    apps = {'Google Music':'com.google.android.music', 'Google Movies & TV':'com.google.android.videos','Google Photos':'com.google.android.apps.photos', 'Google Duo':'com.google.android.apps.tachyon', 'Google Books':'com.google.android.apps.books', 'Google Magazines':'com.google.android.apps.magazines', 'Google Talkback':'com.google.android.marvin.talkback', 'Google Lens':'com.google.ar.lens', 'Google Wellbeing':'com.google.android.apps.wellbeing', 'Google Search Box':'com.google.android.googlequicksearchbox'}
    path = 'apps.txt'

    def __init__(self):
        self.selApps = []
        self.main()

    def main(self):

        def updateList():
            try:
                with open(self.path,'r') as f:
                    for i in f.readlines():
                        if len(i.strip()) != 0:
                            entry = i.split()
                            createSpace(entry[0], entry[1])
            except:
                pass

        def addAppWind():
            def addApp():
                n = e1.get().strip()
                p = e2.get().strip()
                with open(self.path,'a') as f:
                    f.write('{} {}\n'.format(n,p))
                createSpace(n,p)
                addWindow.destroy()
            
            addWindow = Tk()

            mf = Frame(master = addWindow)
            mf.pack(padx = 7, pady = 7)
            
            f1 = Frame(master = mf)
            f1.pack()
            l1 = Label(master = f1, text = 'App Name:       ', font = self.font)
            l1.pack(side = 'left', fill = 'x', expand = 'true')
            e1 = Entry(master = f1, width = 15, font = self.font)
            e1.focus_set()
            e1.pack(side = 'right')
            
            f2 = Frame(master = mf)
            f2.pack()
            l2 = Label(master = f2, text = 'Package Name: ', font = self.font)
            l2.pack(side = 'left', fill = 'x', expand = 'true')
            e2 = Entry(master = f2, width = 15, font = self.font)
            e2.pack(side = 'right')

            b = Button(master = mf, text = 'Add', font = self.font, command = addApp)
            b.pack(pady = 6)

            addWindow.mainloop()

        def clean():
            apkNames = self.selApps.copy()
            for i in range(len(apkNames)):
                apkNames[i] = apkNames[i].get()
            
            while '' in apkNames:
                apkNames.remove('')

            for i in range(len(apkNames)):
                apkNames[i] = 'adb shell pm uninstall --user 0 '+apkNames[i]

            from os import system
            command = ' & '.join(apkNames)
            system('cmd /k "adb devices & {} & exit"'.format(command))

        def createSpace(name, apkName):
            self.selApps.append(StringVar())
            cb = Checkbutton(master = scroll, text = name, onvalue = apkName, offvalue = '', variable = self.selApps[-1], font = self.font, bg = 'white', anchor = 'w', cursor = 'arrow')
            scroll.window_create('end', window = cb)
            scroll.insert('end', '\n')

        ##GUI Design
        from tkinter import Tk, Label, Frame, Button, Checkbutton, StringVar, Entry
        from tkinter.scrolledtext import ScrolledText

        ##Main Window
        window = Tk()
        window.title(self.title)

        ##Frames
        frameMain = Frame(master = window)
        frameMain.pack(fill = 'both', expand = 'true', padx = 10, pady = 10)
        frame1 = Frame(master = frameMain)
        frame1.pack(pady = 5)
        frame2 = Frame(master = frameMain)
        frame2.pack(pady = 5)
        frame3 = Frame(master = frameMain)
        frame3.pack(fill = 'x', pady = 5)
        
        ## Frame 1
        qLabel = Label(master = frame1, text = 'Which apps do you want to remove?', font = self.font)
        qLabel.pack(fill = 'x', expand = 'true')

        ## Frame 2
        scroll = ScrolledText(master = frame2, width = 50, height = 30)
        scroll.pack()
        for i in self.apps:
            createSpace(i, self.apps[i])
        updateList()

        ## Frame 3
        logLabel = Label(master = frame3, text = '--Status--', font = self.font)
        logLabel.pack(side = 'left', fill = 'x', expand = 'true')
        frameButtons = Frame(master = frame3)
        frameButtons.pack(side = 'right')
        addButton = Button(master = frameButtons, text = '+', width = 3, height = 1, command = addAppWind, font = self.font)
        addButton.pack(side = 'left', padx = 5)
        cleanButton = Button(master = frameButtons, text = 'Clean', command = clean, font = self.font)
        cleanButton.pack(side = 'right')

        window.mainloop()

CleanUp()
