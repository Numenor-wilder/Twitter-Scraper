import twint
import scraper

LIST_PATH = "./list.txt"
MENTIONED_PATH = "./mentioned.json"

# def run():
#     config1 = twint.Config()
#     scraper.mentioned(config1, MENTIONED_PATH, 'iingwen')


def main():
    config = twint.Config()
    scraper.userlistThread(config, MENTIONED_PATH, LIST_PATH)


if __name__ == '__main__':
    main()
