def diary_app():
    entry = input("Write Your Diary Entry For Today:- ")

    with open("my_diary.txt", "a") as f:
        f.write(entry + "\n") 
        
    with open("my_diary.txt", "r") as f:
        content = f.read().lower().split()
    
    i_count = 0
    happy_count = 0
    
    for word in content:
        if word == "i":
            i_count += 1
        if word == "happy":
            happy_count += 1
    
    print("\n---------Diary Analysis------------")
    print(f"Times you used 'I' : {i_count}")
    print(f"Times you used 'happy' : {happy_count}")

diary_app()