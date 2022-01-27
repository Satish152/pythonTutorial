from faker import Faker

fake_Data=Faker()
print(fake_Data.name())
print(fake_Data.email())

#we can also get the data in Locale format i,e. we can get the fake data in available langs
fake=Faker("hi_IN")
print(fake.name())
#we can get the locale format names in faker python documentation