def main():
    with open("alice.txt", "r") as file:
        contents = file.readlines()
    
    chapter1 = contents[52:272]
    with open("chapter1.txt", "w") as file:
        file.writelines(chapter1)

main()