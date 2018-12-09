"""
Student Name: Jihun Park
Student ID:13561315
Date: 09/12/2018
This is the program with song list that allows people to add a user track song.The program reads and writes a list of songs in a file.
Github: https://github.com/JihunPark98/Songs_A1/blob/master/Songs_A1.py
"""

def main():
    print("Songs To Learn 1.0 - by Jihun Park")
    menu = programMenu()


def programMenu():
    menu = input("L - List songs\nA - Add new song\nC - Complete a song\nQ - Quit")

    if menu == "L":
        load = loadSong()
        menu = programMenu()
        return menu

    elif menu == "A":
        add = addSong()
        menu = programMenu()
        return menu

    elif menu == "C":
        markLearned = ("Enter the number of a song to mark as learned")
        menu = programMenu()
        return menu

    elif menu == "Q":
        data = open("list.csv", "r")
        readLines = data.read().strip()
        numLines = len(readLines.splitlines())
        print(numLines, "songs saved to song.csv\nHave a nie day:)")
        data.close()

    else:
        print("Invalid menu")
        menu = programMenu()

def loadSong():
    load_song = open("list.csv", "r")
    name = load_song.read().strip()
    print(name)
    load_song.close()

def addSong():
    song_list = 'list.csv'
    with open(song_list) as fb:
        line = fb.readline()
        cnt = 0
        while line:
            ("{}. {}".format(cnt, line.strip()))
            line = fb.readline()
            cnt += 1

    add_song = open("list.csv", "a+")

    songTitle = input("Title: ")
    while len(songTitle) <= 0:
        print("Input cannot be blank")
        songTitle = input("Title: ")

    songArtist = input("Artist: ")
    while len(songArtist) <= 0:
        print("Input cannot be blank")
        songArtist = input("Artist: ")

    valid_input = False
    while not valid_input:
        try:
            songYear = int(input("Year: "))
            valid_input = True
            if songYear > 0:
                print(songTitle, "by", songArtist, "(", songYear, ") added to song list")
            else:
                print("Number must be >= 0")
                songYear = int(input("Year: "))
        except ValueError:
            print("Invalid input; enter a valid number")
    list = [cnt, "*", songTitle, songArtist, songYear]
    print(list, file=add_song)
    add_song.close()


main()