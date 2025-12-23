from faker import Faker


fake = Faker()
user_data = {
    "name": fake.name(),
    "email": fake.email()

}
print(fake.name())
print(fake.address())
print(fake.email(domain="gmail.com"))

