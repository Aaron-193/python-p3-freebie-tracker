#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie, Base

# Connect to database
engine = create_engine('sqlite:///lib/freebies.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
company1 = Company(name="Tech Corp", founding_year=2000)
company2 = Company(name="InnovateX", founding_year=2015)

dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

freebie1 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Sticker Pack", value=5, dev=dev2, company=company2)

# Add instances to the session
session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])

# Commit changes
session.commit()

print("Seed data added successfully!")
session.close()