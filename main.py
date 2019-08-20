from core.color import color
from core.color import header
from core.config import config
from core.console import console
from core.config import xmllib


def printBanner():
    color.ClearConsole()
    print header.Banner(config.VERSION)


def loadConfiguration():
    xmllib.load()


if __name__ == '__main__':
    printBanner()
    loadConfiguration()
    console.CLI.console()
