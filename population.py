from models.gem_models import Gem, GemProperties
import random
import string
from main import engine
from sqlmodel import Session

color_grade = string.ascii_uppercase[3:9]


def create_gem_props():
    size = random.randint(3, 70) / 10
    color = color_grade[random.randint(0, 5)]
    clarity = random.randint(1, 4)
    gem_prop = GemProperties(size=size, color=color, clarity=clarity)
    return gem_prop


def create_gem(gem_id):
    gem = Gem(price=1000, gen_properties_id=gem_id)
    return gem


def create_gems_db():
    #print("KU")
    gem_p = create_gem_props()
    print(gem_p)
    with Session(engine) as session:
        session.add(gem_p)
        session.commit()
        g = create_gem(gem_p.id)
        session.add(g)
        session.commit()


create_gems_db()
