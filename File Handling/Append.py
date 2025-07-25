with open("C:/Users/susha/OneDrive/Desktop/FSD/Python Basic/File Handling/demo.txt") as f:
    f.write("now the file has more content!")

    # open and read the file after the appending:
    with open("C:/Users/susha/OneDrive/Desktop/FSD/Python Basic/File Handling/demo.txt") as f:
        print(f.read())