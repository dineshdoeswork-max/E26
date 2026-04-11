import random
import os

playlist = "playlist_app.txt"

def playlist_app():
    songs = []

    if os.path.exists(playlist):
        with open(playlist, "r") as f:
            songs = [line.strip() for line in f.readlines()]

    while True:
        print("\n------ PLAYLIST MANAGER ------")
        print("1.View    2.Add    3.Remove    4.Shuffle    5.Exit")
        choice = input("Select an Option(1-5):- ")

        if choice == "1":
            print("\nYour Songs:-")
            if not songs:
                print("Playlist is empty.")
            else:
                for s in songs:
                    print(" ", s)

        elif choice == "2":
            new_song = input("Enter A Song Name To Add:- ")
            songs.append(new_song)
            print("SONG ADDED SUCCESSFULLY")

        elif choice == "3":
            rem_song = input("Enter Song Name To Remove:- ")
            if rem_song in songs:
                songs.remove(rem_song)
                print("SONG REMOVED SUCCESSFULLY")
            else:
                print("SONG NOT FOUND IN LIST")

        elif choice == "4":
            random.shuffle(songs)
            print("PLAYLIST SHUFFLED SUCCESSFULLY")

        elif choice == "5":
            with open(playlist, "w") as f:
                for s in songs:
                    f.write(s + "\n")
            print("PLAYLIST SAVED. GOODBYE!")
            break

        else:
            print("INVALID CHOICE. SELECT BETWEEN 1-5")

playlist_app()