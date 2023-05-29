# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FRAME_RATE = 60
ANIMATION_SPEED = 8

# colors
SKY_COLOR = '#DDC6A1'
SEA_COLOR = '#92A9CE'
HORIZON_COLOR = '#F5F1DE'
HORIZON_TOP_COLOR = '#D1AA9D'
LINE_COLOR = 'black'
BUTTON_BG_COLOR = '#33323D'
BUTTON_LINE_COLOR = '#F5F1DE'

# editor graphics
EDITOR_DATA = {
    0: {
        'style': 'player',
        'type': 'object',
        'menu': None,
        'menu_surf': None,
        'preview': None,
        'graphics': 'PirateMaker/graphics/player/idle_right'
    },
    1: {
        'style': 'sky',
        'type': 'object',
        'menu': None,
        'menu_surf': None,
        'preview': None,
        'graphics': None
    },
    2: {
        'style': 'terrain',
        'type': 'tile',
        'menu': 'terrain',
        'menu_surf': 'PirateMaker/graphics/menu/land.png',
        'preview': 'PirateMaker/graphics/preview/land.png',
        'graphics': None
    },
    3: {
        'style': 'water',
        'type': 'tile',
        'menu': 'terrain',
        'menu_surf': 'PirateMaker/graphics/menu/water.png',
        'preview': 'PirateMaker/graphics/preview/water.png',
        'graphics': 'PirateMaker/graphics/terrain/water/animation'
    },
    4: {
        'style': 'coin',
        'type': 'tile',
        'menu': 'coin',
        'menu_surf': 'PirateMaker/graphics/menu/gold.png',
        'preview': 'PirateMaker/graphics/preview/gold.png',
        'graphics': 'PirateMaker/graphics/items/gold'
    },
    5: {
        'style': 'coin',
        'type': 'tile',
        'menu': 'coin',
        'menu_surf': 'PirateMaker/graphics/menu/silver.png',
        'preview': 'PirateMaker/graphics/preview/silver.png',
        'graphics': 'PirateMaker/graphics/items/silver'
    },
    6: {
        'style': 'coin',
        'type': 'tile',
        'menu': 'coin',
        'menu_surf': 'PirateMaker/graphics/menu/diamond.png',
        'preview': 'PirateMaker/graphics/preview/diamond.png',
        'graphics': 'PirateMaker/graphics/items/diamond'
    },
    7: {
        'style': 'enemy',
        'type': 'tile',
        'menu': 'enemy',
        'menu_surf': 'PirateMaker/graphics/menu/spikes.png',
        'preview': 'PirateMaker/graphics/preview/spikes.png',
        'graphics': 'PirateMaker/graphics/enemies/spikes'
    },
    8: {
        'style': 'enemy',
        'type': 'tile',
        'menu': 'enemy',
        'menu_surf': 'PirateMaker/graphics/menu/tooth.png',
        'preview': 'PirateMaker/graphics/preview/tooth.png',
        'graphics': 'PirateMaker/graphics/enemies/tooth/idle'
    },
    9: {
        'style': 'enemy',
        'type': 'tile',
        'menu': 'enemy',
        'menu_surf': 'PirateMaker/graphics/menu/shell_left.png',
        'preview': 'PirateMaker/graphics/preview/shell_left.png',
        'graphics': 'PirateMaker/graphics/enemies/shell_left/idle'
    },
    10: {
        'style': 'enemy',
        'type': 'tile',
        'menu': 'enemy',
        'menu_surf': 'PirateMaker/graphics/menu/shell_right.png',
        'preview': 'PirateMaker/graphics/preview/shell_right.png',
        'graphics': 'PirateMaker/graphics/enemies/shell_right/idle'
    },
    11: {
        'style': 'palm_fg',
        'type': 'object',
        'menu': 'palm fg',
        'menu_surf': 'PirateMaker/graphics/menu/small_fg.png',
        'preview': 'PirateMaker/graphics/preview/small_fg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/small_fg'
    },
    12: {
        'style': 'palm_fg',
        'type': 'object',
        'menu': 'palm fg',
        'menu_surf': 'PirateMaker/graphics/menu/large_fg.png',
        'preview': 'PirateMaker/graphics/preview/large_fg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/large_fg'
    },
    13: {
        'style': 'palm_fg',
        'type': 'object',
        'menu': 'palm fg',
        'menu_surf': 'PirateMaker/graphics/menu/left_fg.png',
        'preview': 'PirateMaker/graphics/preview/left_fg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/left_fg'
    },
    14: {
        'style': 'palm_fg',
        'type': 'object',
        'menu': 'palm fg',
        'menu_surf': 'PirateMaker/graphics/menu/right_fg.png',
        'preview': 'PirateMaker/graphics/preview/right_fg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/right_fg'
    },
    15: {
        'style': 'palm_bg',
        'type': 'object',
        'menu': 'palm bg',
        'menu_surf': 'PirateMaker/graphics/menu/small_bg.png',
        'preview': 'PirateMaker/graphics/preview/small_bg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/small_bg'
    },
    16: {
        'style': 'palm_bg',
        'type': 'object',
        'menu': 'palm bg',
        'menu_surf': 'PirateMaker/graphics/menu/large_bg.png',
        'preview': 'PirateMaker/graphics/preview/large_bg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/large_bg'
    },
    17: {
        'style': 'palm_bg',
        'type': 'object',
        'menu': 'palm bg',
        'menu_surf': 'PirateMaker/graphics/menu/left_bg.png',
        'preview': 'PirateMaker/graphics/preview/left_bg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/left_bg'
    },
    18: {
        'style': 'palm_bg',
        'type': 'object',
        'menu': 'palm bg',
        'menu_surf': 'PirateMaker/graphics/menu/right_bg.png',
        'preview': 'PirateMaker/graphics/preview/right_bg.png',
        'graphics': 'PirateMaker/graphics/terrain/palm/right_bg'
    },
}

NEIGHBOR_DIRECTIONS = {
    'A': (0, -1),
    'B': (1, -1),
    'C': (1, 0),
    'D': (1, 1),
    'E': (0, 1),
    'F': (-1, 1),
    'G': (-1, 0),
    'H': (-1, -1)
}

LEVEL_LAYERS = {'clouds': 1, 'ocean': 2, 'bg': 3, 'water': 4, 'main': 5}
