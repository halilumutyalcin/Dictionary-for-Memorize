class Dictionary:

    def __init__(self):
        self.status = True
        self.run()

    def menu(self):
        x = "                                       "
        print(x, "\n", "#" * len(x), sep="")
        title = "Welcome to your dictionary for memorize"
        print(title, "\n", "-" * len(title), sep="")
        print("""
*** If you want to memorize these words, don't forget repeat it. ****
1- Add word.
2- Remove word for change.
3- Show all words.
4- Exit        
""")

    def menuChoose(self):
        global selection
        while True:
            try:
                selection = int(input("Enter your choice:"))
                while selection < 1 or selection > 4:
                    selection = int(input("Please enter your choice between 1-4: "))

            except ValueError:
                print("Please enter number!\n")
            break
        return selection

    def run(self):
        self.menu()
        selection = self.menuChoose()

        if selection == 1:
            self.add()

        if selection == 2:
            self.remove()

        if selection == 3:
            self.show()

        if selection == 4:
            self.exit()

    def add(self):

        word = input("Enter foreign word: ")
        mean = input("Enter mean of word: ")
        count = 1

        with open("dictionary.txt", "r") as file:
            wordlist = file.readlines()
        if len(wordlist) == 0:
            count = 1
        else:
            with open("dictionary.txt", "r") as file:
                count = int(file.readlines()[-1].split(")")[0]) + 1

        with open("dictionary.txt", "a+", encoding="utf-8") as file:
            file.write("{}) {} - {}\n".format(count, word, mean))
        self.run()

    def remove(self):
        with open("dictionary.txt", "r") as dosya:
            w = dosya.readlines()
        wn = []

        for wrd in w:
            wn.append(wrd[:-1])
        for wrd in wn:
            print(wrd)

        selection2 = int(
            input("Please enter the number of the word you want to remove [1- {}]: ".format(len(wn))))

        while selection2 < 0 or selection2 > len(wn):
            selection2 = int(input("Please enter a value between 1- {}:".format(len(wn))))

        w.pop(selection2 - 1)

        id = 1

        wr = []

        for wrd in w:
            wr.append(str(id) + ")" + wrd.split(")")[1])
            id += 1

        with open("dictionary.txt", "w") as file:
            file.writelines(wr)

        self.run()

    def show(self):
        with open("dictionary.txt", "r") as dosya:
            w = dosya.readlines()
        wn = []
        for wrd in w:
            wn.append(wrd[:-1])
        for wrd in wn:
            print(wrd)

        self.run()

    def exit(self):
        self.status = False


word = Dictionary()
while word.status:
    word.menu()
