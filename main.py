import scrape

LIST_PATH = "./list.txt"
MENTIONED_PATH = "./mention.json"


def run():
    scrape.makeList(MENTIONED_PATH, LIST_PATH)
    scrape.scraping(LIST_PATH)


def main():
    run()


if __name__ == '__main__':
    main()