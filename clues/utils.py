import random
import datetime

from faker import Faker

from clues.models import Publisher, Crossword, Clue


def generate_dummy_data():
    faker = Faker()
    today = datetime.date.today()

    print("Adding publishers ...")
    for _ in range(20):
        publisher = Publisher(
            name=faker.company(),
            url=faker.url(),
        )
        publisher.save()
        print(f"\t{publisher} added")

        crossword_count = random.randint(20, 50)
        print(f"\n\tAdd crosswords for {publisher}")
        for i in range(crossword_count):
            pub_date = today - datetime.timedelta(days=i)

            crossword = Crossword(
                publisher=publisher,
                published_on=pub_date,
                url=faker.url(),
            )
            crossword.save()
            print(f"\t\t{crossword} added")

            clues_count = random.randint(25, 45)
            print(f"\n\t\tAdding clues for {crossword}")
            for j in range(clues_count):
                clue = Clue(
                    clue=faker.sentence(),
                    answer=faker.word().upper(),
                    crossword=crossword,
                )
                clue.save()
                print(f"\t\t\t{clue} added")
