from sqlalchemy import ForeignKey, Column, Integer, String, MetaData 
from sqlalchemy.orm import relationship, backref, session
from sqlalchemy.ext.declarative import declarative_base

# Define naming convention for foreign keys
convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    founding_year = Column(Integer(), nullable=False)

    # Relationship with Freebie
    freebies = relationship('Freebie', backref='company', lazy=True)

    def __repr__(self):
        return f'<Company {self.name}>'

    def give_freebie(self, dev, item_name, value):
        item_name=item_name 
        value= value 
        dev=dev 
        company=self
        freebie = Freebie(item_name, value, dev, company)
        session.add(freebie)
        session.commit()
    
    @classmethod
    def oldest_company(cls, session):
        oldest = None
        for company in session.query(cls).all():
            if oldest is None or company.founding_year < oldest.founding_year:
                oldest = company
        return oldest


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)

    # Relationship with Freebie
    freebies = relationship('Freebie', backref='dev', lazy=True)

    def __repr__(self):
        return f'<Dev {self.name}>'
    
    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            freebie.dev = dev
            session.commit()

    def received_one(self, item_name):
        for freebie in self.freebies:
            if freebie.item_name == item_name:
                return True
        return False
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String(), nullable=False)
    value = Column(Integer(), nullable=False)
    dev_id = Column(Integer(), ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer(), ForeignKey('companies.id'), nullable=False)

    def __repr__(self):
        return f'<Freebie {self.item_name} worth {self.value} from {self.company.name}>'
    
    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"
