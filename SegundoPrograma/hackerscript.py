import os


def main():
    desktop_path = "C:\\Users\\" + os.getlogin() + "\\Desktop\\"
    a = open(desktop_path + "LEEME.txt", "w")
    a.write("Lo he logrado")
    a.close()


if __name__ == "__main__":
    main()
