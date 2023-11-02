from faker import Faker
fake = Faker(locale="ru_RU")
print("Name ->", fake.name())
print("Address ->", fake.address())
print("Text ->", fake.text())