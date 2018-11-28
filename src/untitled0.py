from faker import Faker
fake = Faker()

fake.text()
for _ in range(10):
  print(fake.text())
