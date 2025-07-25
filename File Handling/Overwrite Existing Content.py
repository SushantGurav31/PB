with open ("C:/Users/susha/OneDrive/Desktop/FSD/Python Basic/File Handling/DEMO.txt","w") as f:
    f.write("Woops! I have deleted the content!")

    # open and read the file after the overwriting:

    with open ("C:/Users/susha/OneDrive/Desktop/FSD/Python Basic/File Handling/DEMO.txt") as f:
        print(f.read())