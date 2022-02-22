from credentials.credentials import *
from bot.main import AirQualityBot

print(Credentials)


def main():
    bot = AirQualityBot(credentials=Credentials, mock=False)
    bot.run()


if __name__ == "__main__":
    main()
