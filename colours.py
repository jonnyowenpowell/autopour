from enum import Enum, auto


class Colour(Enum):

    DARK_BLUE   = auto()
    LIGHT_BLUE  = auto()
    BROWN       = auto()
    DARK_GREEN  = auto()
    LIGHT_GREEN = auto()
    NEON_GREEN  = auto()
    GREY        = auto()
    ORANGE      = auto()
    PINK        = auto()
    PURPLE      = auto()
    RED         = auto()
    YELLOW      = auto()

    __colour_codes__ = {
        DARK_BLUE:   'DBLU',
        LIGHT_BLUE:  'LBLU',
        BROWN:       'BRWN',
        DARK_GREEN:  'DGRN',
        LIGHT_GREEN: 'LGRN',
        NEON_GREEN:  'NGRN',
        GREY:        'GRAY',
        ORANGE:      'ORNG',
        PINK:        'PINK',
        PURPLE:      'PURP',
        RED:         'RED ',
        YELLOW:      'YLLW',
    }

    def __repr__(self) -> str:
        return self.__colour_codes__[self.value]
