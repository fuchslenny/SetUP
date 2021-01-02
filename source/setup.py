import platform
import psutil
from ui import gui


def main():

    app = gui.gui_start()
    app.mainloop()


if __name__ == "__main__":
    main()