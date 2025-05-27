#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

# Connect to database
engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="InnovateX", founding_year=2019)
company3 = Company(name="Xspace", founding_year=20114)
company4 = Company(name="Moringa Technologies", founding_year=2022)

dev1 = Dev(name="Chloe")
dev2 = Dev(name="Sam")
dev3 = Dev(name="Rashid")
dev4 = Dev(name="Rachael")

freebie1 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker Pack", value=5, dev=dev2, company=company2)
freebie3 = Freebie(item_name="Laptop", value=5, dev=dev3, company=company3)
freebie4 = Freebie(item_name="Macbook", value=5, dev=dev4, company=company4)

session.add_all([company1, company2, company3, company4, dev1, dev2, dev3, dev4,freebie1, freebie2, freebie3, freebie4])

session.commit()

print("Seed data added successfully!")
session.close()

# Script goes here!
