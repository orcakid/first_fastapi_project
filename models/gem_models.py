from sqlmodel import SQLModel, Field
from enum import Enum, IntEnum
from typing import Optional


# прозрачность камня
class Clarity(IntEnum):
    # самый грязный
    Si = 1
    Vs = 2
    Vvs = 3
    Fl = 4


class Gen_types(str, Enum):
    diamond = "Diamond"
    emerald = "Emerald"
    ruby = "Ruby"


class Color(str, Enum):
    D = "D"
    E = "E"
    G = "G"
    F = "F"
    H = "H"
    I = "I"


class GemProperties(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    size: float = 1
    clarity: Optional[Clarity] = None
    color: Optional[Color] = None


class Gem(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    price: float
    available: bool = True
    gen_type: Optional[Gen_types] = Gen_types.diamond

    gen_properties_id: Optional[int] = Field(default=None, foreign_key="gemproperties.id")
