import pygame
import sys
import random
import math
import time
from collections import Counter

from shapely.geometry import LineString


# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghostbusters")
TOP_LINE_POSITION = 100
linePosition = TOP_LINE_POSITION # MENU START LINE FOR TEXT

# draw bars 
BAR_COUNT = 7
BAR_WIDTH = 80  # Width of each bar
BAR_HEIGHT = 20
BAR_SPACING = 10  # Space between bars
TOP_OFFSET = 100  # Distance from the top of the screen
# ===== 

# INDEX FEE CARD
CARD_WIDTH = 400
CARD_HEIGHT = 450
CARD_COLOR = (225, 225, 225)  # off-White
CARD_BORDER_COLOR = (0, 0, 0)  # Black border
TEXT_COLOR = (0, 0, 0)  # Black text
CARD_DISPLAY_TIME = 320  # ticks
CARD_ORIGIN_Y = 220

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
OFF_WHITE = (225, 225, 225)
GREY = (138, 138, 138)
BROWN = (153, 105, 45)
RED  = (255, 0, 0)
DARK_RED = (146,74,64)
ORANGE = (255, 165, 0)
BLUE = (72, 58, 170)
TRUE_BLUE = (0, 0, 255)
SKY_BLUE = (135, 206, 235)
LIGHT_BLUE = (132, 197, 204)
ABS_GREEN = (0, 255, 0)
ABS_BLUE = (0, 0, 255)
GREEN = (114, 177, 75)
DARK_GREEN = (104, 167, 65)
STREET_GREY = (100, 100, 100)  # Grey background for the street

DARK_GREY = (25, 25, 25)  # Grey background for the street
YELLOW = (255, 255, 0)  # Yellow color for the street line
DARK_YELLOW = (150, 150, 0)
TRANS_WHITE = (255, 255, 255, 100)
TRANS_YELLOW = (255, 255, 0, 100)
PURPLE = (128,0,128)

DARK_PURPLE = (75, 0, 130)
BRIGHT_PURPLE = (138, 43, 226)


# UNIFORM COLORS:

ORIGINAL_UNIFORM_YELLOW = (248, 252, 107)
RAY_BROWN = (191, 176, 155) # too light? just looks yellow? 
PETER_BROWN = (145, 102, 85) # good, tho may conflict with BROWN too much
EGON_BLUE = (117, 181, 183) # good
WINSTON_BLUE = (187, 225, 202)
JANINE_PINK = (255,20,147)
GBII_BLUE = (51, 60, 67)
HAUNTED_PURPLE = (138, 43, 226)
CAUTION_ORANGE = (255, 165, 0)

global uniform_index
global uniform_choices
uniform_index = 0
uniform_choices = [ORIGINAL_UNIFORM_YELLOW, RAY_BROWN, PETER_BROWN, EGON_BLUE, WINSTON_BLUE, JANINE_PINK, 
                    GBII_BLUE, HAUNTED_PURPLE, CAUTION_ORANGE, OFF_WHITE]
random.shuffle(uniform_choices)

# HAIR_COLORS:
HAIR_Blond = (255, 230, 158)
HAIR_DarkBlond = (224, 192, 146)
HAIR_MediumBrown = (109, 71, 48)
HAIR_DarkBrown = (77, 45, 26)
HAIR_ReddishBrown = (168, 66, 45)
HAIR_RedBlack = (62, 0, 0)
HAIR_BLACK = (0, 0, 0)
HAIR_Gray = (154, 158, 159)
HAIR_White = (245, 245, 245)

hair_choices = [HAIR_Blond, HAIR_DarkBlond, HAIR_MediumBrown, HAIR_DarkBrown, HAIR_ReddishBrown, HAIR_RedBlack, HAIR_BLACK, HAIR_Gray, HAIR_White]
hair_weight = (6,6,6,6,6,6,50,6,6)


GHOST_CLASSES = ["Class I", "Class II", "Class III", "Class IV", "Class V", "Class VI"] # Class VII
GHOST_TRAITS = ["Focused", "Free-Floating", "Full-Torso", "Repeating", "Vapor", "Anchored", 
    "Animating", "Caustic", "Composite", "Corporeal", "Ethereal", "Inhabiting", "Kinetic", 
    "Paranormal", "Planar", "Possessor", "Reactive", "Remnant", "Secretion", "Swarmer", 
    "Telekinetic", "Transdimensional", "Ultradimensional", "Wandering"
    ]

# Get player's choice of vehicle
VEHICLE_CHOICES = {
    # 1: {"name": "Motorcycle", "cost": 1000, "speed": 120, "capacity": 3, "tank_size": 50},
    1: {"name": "Compact", "cost": 2000, "speed": 75, "capacity": 5, "tank_size": 60},
    2: {"name": "Hearse", "cost": 4800, "speed": 90, "capacity": 9, "tank_size": 100},
    3: {"name": "Wagon", "cost": 6000, "speed": 90, "capacity": 11, "tank_size": 120},
    4: {"name": "Utility-Truck", "cost": 9000, "speed": 90, "capacity": 14, "tank_size": 140},
    5: {"name": "High-Performance", "cost": 15000, "speed": 160, "capacity": 8, "tank_size": 140}
}


CITY_FINE_TYPES = [
    {"name": "Property Damage Fine", "amount": 1500},
    {"name": "Noise Complaints and City Ordinance", "amount": 1500},
    {"name": "Environmental Cleanup Fee", "amount": 1200},
    {"name": "Civilian Lawsuit", "amount": 5000},
    {"name": "Equipment Repair and Maintenance", "amount": 1500},
    {"name": "Government Permits and Licensing Fee", "amount": 3000},
    {"name": "Ecto-1 Parking Ticket", "amount": 1000},
    {"name": "Environmental Protection Fine", "amount": 6000}
]

GHOSTBUSTER_GOALS = ["Fame","Serving Humanity","Relationships","Science","Wealth", "Redemption", "Survival"]
GHOSTBUSTER_ORIGINS = ["Parapsychologist","Psychologist","Engineer","Seismologist","Military","Security",
    "Police","Detective","Scientist","Professor","Doctor","Archaeologist","Anthropologist", "Teacher", 
    "Exorcist","Spiritual Medium","Firefighter","Criminal","Lawyer","Entertainer", "Accountant", 
    "Journalist", "Electrician", "Chemist", "Mechanic", "Philosopher", "Librarian", "Physicist", "Plumber",
    "Pilot", "Skeptic", "Musician", "Historian", "Film Producer"]


# Set up fonts

FONT36 = pygame.font.Font(None, 36)
FONT32 = pygame.font.Font(None, 32)
FONT24 = pygame.font.Font(None, 24)
FONT22 = pygame.font.Font(None, 22)
FONT20 = pygame.font.Font(None, 20)
FONT18 = pygame.font.Font(None, 18)
under_line_FONT18 = pygame.font.Font(None, 18, underline=True)
under_line_FONT18.set_underline(True)



running = False
navigating = False
shopping_equipment = False
game_mode = 0
sell_mode = False
for_hire_roster = []
shopping_equipment = False
choosing_car = False



NUMBER_OF_MAX_ACTIVE_BUILDINGS = 4
PROTON_CHARGE_PER_TICK = 0.025 #0.020
VACUUM_PROTON_CHARGE_PER_TICK = 0.1

ADDED_FUEL_FROM_GENERATOR = 10


GHOST_VACUUM_FUNCTIONAL_DISTANCE = 175

EXTRA_CAPACITY_FROM_CARGO_EXPANSION = 5
EXTRA_SPEED_FROM_GENERATOR = 40



CASH_PER_STREET_GHOST_CAUGHT = 100 
FIRST_GHOST_REMOVAL_FEE = 4000
SUBSEQUENT_GHOST_FEE = 1000
ON_SITE_INSPECTION_FEE = 500
FIRST_TIME_STORAGE_FEE = 1500
CLEANUP_FEE = 350
BATTERY_FEE = 100
HAZARD_FEE = 250
GHOST_HUNTER_TIP_FEE_MIN = 50
GHOST_HUNTER_TIP_FEE_MAX = 200
COUNSELING_FEE = 250
VICTORY_OVER_GOZER_FEE = 5000

DESTROYED_BUILDING_FINE = 1500
STAY_PUFT_AT_ZUUL_FINE = 5000

FIRST_RESPONDERS_DISCOUNT_PERCENT = 0.50

CAR_SPEED_ON_MAP_FACTOR = 18

# ****
START_GAME = 1 # 0 for regular start, 1 for shortcut during tests
# ****
MUSIC_ON = 1


NEW_GAME_CASH_ADVANCE = 10000
ZUUL_END_GAME_PK_REQUIREMENT = 1000
NUM_FOORS_IN_ZUUL_BUILDING = 4 # MUST BE EVEN
NUM_BUSTER_REQUIRED_FOR_ZUUL_ROOF = 2

GHOST_PK_MIN = 50
GHOST_PK_MAX = 200

INSIDE_GHOST_PK_MIN = 10 
INSIDE_GHOST_PK_MAX = 50

GHOST_SPEED_MIN = 3 
GHOST_SPEED_MAX = 5
INSIDE_GHOST_SPEED_MIN = 1
INSIDE_GHOST_SPEED_MAX = 2

PROTON_BEAM_CIRCLE_LINE_WIDTH = 3

PLC_MAX_STORAGE = 12
MINIMUM_PROTON_CHARGE_FOR_MISSION = 10
MAX_NUM_OF_SPECIAL_FEES = 2

MIN_BEFORE_STREAM_CROSS = 20
CROSS_STEAMS_DEATH_TIMER = 200
GHOST_ESCAPE_TIME = 30000 # 1 minute = 60,000 milliseconds

# AUDIO CONSTANTS --------------------------------------------------------------------------
pygame.mixer.init()
pygame.mixer.set_num_channels(16)
CLOCK_SOUND = pygame.mixer.Sound("./tock.wav")
CASH_SOUND = pygame.mixer.Sound("./cash.mp3")
TYPE_SOUND  = pygame.mixer.Sound("./beep.mp3")
CHARGE_SOUND = pygame.mixer.Sound("./charge.mp3")
WOOSH_SOUND = pygame.mixer.Sound("./woosh.mp3")
SIREN_SOUND = pygame.mixer.Sound("./ecto1.mp3")
VOICE_GHOSTBUSTERS = pygame.mixer.Sound("./voice_ghostbusters.mp3")
VOICE_SLIMED = pygame.mixer.Sound("./voice_slimed.mp3")
VOICE_LAUGH = pygame.mixer.Sound("./voice_laugh.mp3")
VOICE_YELL = pygame.mixer.Sound("./voice_ahh.mp3") 
TRAP_OPEN_SOUND = pygame.mixer.Sound("./trap_open_fix_2.wav")
TRAP_CLOSE_SOUND = pygame.mixer.Sound("./trap_close_fix_4.wav")
TRAP_NO_SOUND = pygame.mixer.Sound("./trap_bar.wav")
PROTON_FIRE_SOUND = pygame.mixer.Sound("./proton_fire.mp3")
EMPTY_TRAPS_SOUND = pygame.mixer.Sound("./ecu_flush.mp3")
PK_LOW_SOUND = pygame.mixer.Sound("./pke_low_1.wav")
PK_MED1_SOUND = pygame.mixer.Sound("./pke_mid_1.wav")
PK_MED2_SOUND = pygame.mixer.Sound("./pke_mid_2.wav")
PK_HIGH_SOUND = pygame.mixer.Sound("./pke_hi_1.wav")
THEME = pygame.mixer.Sound("./GB_C64_theme1.mp3")
WATER_DROP = pygame.mixer.Sound("./water.wav")
LAB_BUBBLES = pygame.mixer.Sound("./lab_bubbles.mp3")

IM_KEYMASTER_VOICE = pygame.mixer.Sound("./im_keymaster.mp3")
IM_GATEKEEPER_VOICE = pygame.mixer.Sound("./im_gatekeeper.mp3")

FORK_SHORT_SOUND = pygame.mixer.Sound("./fork_short.mp3")
FORK_MED_SOUND = pygame.mixer.Sound("./fork_med.mp3")
FORK_LONG_SOUND = pygame.mixer.Sound("./fork_long.mp3")
OVERHEAT_BEEP = pygame.mixer.Sound("./overheat.mp3") 

TRAP_CHANNEL = pygame.mixer.Channel(2)
PROTON_PACK_CHANNEL = pygame.mixer.Channel(3)
SIREN = pygame.mixer.Channel(4)
MUSIC = pygame.mixer.Channel(5)
VOICE_CHANNEL = pygame.mixer.Channel(6)
PKE_CHANNEL = pygame.mixer.Channel(7)
FORK_CHANNEL = pygame.mixer.Channel(8)

LAB_BUBBLES.set_volume(0.75)

WOOSH_SOUND.set_volume(0.20)
CHARGE_SOUND.set_volume(0.15)
PROTON_FIRE_SOUND.set_volume(0.50)
SIREN_SOUND.set_volume(0.25)
VOICE_GHOSTBUSTERS.set_volume(0.50)
PKE_CHANNEL.set_volume(0.10)
EMPTY_TRAPS_SOUND.set_volume(0.50)
TYPE_SOUND.set_volume(0.25)
CASH_SOUND.set_volume(0.25)
THEME.set_volume(0.15)
WATER_DROP.set_volume(0.15)
OVERHEAT_BEEP.set_volume(0.25)
IM_KEYMASTER_VOICE.set_volume(0.50)
IM_GATEKEEPER_VOICE.set_volume(0.50)

MUSIC.set_volume(0.75)
PK_LOW_SOUND.set_volume(0.5)
PK_MED1_SOUND.set_volume(0.5)
PK_MED2_SOUND.set_volume(0.5)
PK_HIGH_SOUND.set_volume(0.5)


# ----------------------------------------------------------------------------------



# GRAPHICS ------------------------------------------------------------------------------------
GB_LOGO = pygame.image.load("./gb_logo.png")  # Replace with your sprite sheet image path
GB_SMALL = pygame.image.load("./gb_small.png")  # Replace with your sprite sheet image path
REDCROSS = pygame.image.load("./redcross.png")
POLICE = pygame.image.load("./police.png")
CROSS = pygame.image.load("./church_cross.png")

MAP_GHOST_IMAGE = pygame.image.load("./ghost1.png")  # Replace with your sprite sheet image path
GHOST2_IMAGE = pygame.image.load("./ghost2.png")  # Replace with your sprite sheet image path
GHOST3_IMAGE = pygame.image.load("./ghost3.png")
GHOST4_IMAGE = pygame.image.load("./ghost4.png")
GHOST5_IMAGE = pygame.image.load("./slimer.png")
GHOST6_IMAGE = pygame.image.load("./orb.png")
GHOST7_IMAGE = pygame.image.load("./mist.png")
GHOST8_IMAGE = pygame.image.load("./ghost8.png")
GHOST9_IMAGE = pygame.image.load("./ghost9.png")
GHOST10_IMAGE = pygame.image.load("./ghost10.png")
GHOST11_IMAGE = pygame.image.load("./ghost11.png")
GHOST12_IMAGE = pygame.image.load("./ghost12.png")
GHOST13_IMAGE = pygame.image.load("./ghost13.png")


DRIP_OF_GOO_IMAGE = pygame.image.load("./goo_drip.png")

GHOST_IMAGE_LIST = [MAP_GHOST_IMAGE,GHOST2_IMAGE,GHOST3_IMAGE,GHOST4_IMAGE,GHOST5_IMAGE,GHOST6_IMAGE,
    GHOST7_IMAGE,GHOST8_IMAGE, GHOST9_IMAGE, GHOST10_IMAGE, GHOST11_IMAGE, GHOST12_IMAGE, GHOST13_IMAGE
    ]

# BUSTER_MAN_IMAGE1 = pygame.image.load("./gb/gb2.png")
# BUSTER_MAN_IMAGE2 = pygame.image.load("./gb/gb2_w.png")

BUSTER_MAN_IMAGE1 = pygame.image.load("./gb2_G.png") # GREEN FOR EDITING
BUSTER_MAN_IMAGE2 = pygame.image.load("./gb2_w_G.png") # GREEN FOR EDITING

FUEL_BARREL_IMAGE = pygame.image.load("./barrel.png")
DOOR1_IMAGE = pygame.image.load("./door1.png")
DOOR2_IMAGE = pygame.image.load("./door2.png")
DOOR3_IMAGE = pygame.image.load("./door3.png") # REVOLVING DOORS
DOOR4_IMAGE = pygame.image.load("./door4.png") # DOOR WITH COLUMNS
DOOR5_IMAGE = pygame.image.load("./door5.png") # BIG DOOR
DOOR_HQ_IMAGE = pygame.image.load("./hq_door.png") # GB HQ BIG DOOR

DOOR_IMAGE_LIST = [DOOR1_IMAGE, DOOR2_IMAGE, DOOR3_IMAGE,DOOR4_IMAGE,DOOR5_IMAGE]

WINDOW1_IMAGE = pygame.image.load("./window1.png")
WINDOW2_IMAGE = pygame.image.load("./window2.png")
WINDOW3_IMAGE = pygame.image.load("./window3.png")
WINDOW4_IMAGE = pygame.image.load("./window4.png") # GB HW WINDOW
WINDOW5_IMAGE = pygame.image.load("./window5.png")
WINDOW6_IMAGE = pygame.image.load("./window6.png")

WINDOW_IMAGE_LIST = [WINDOW1_IMAGE, WINDOW2_IMAGE, WINDOW3_IMAGE, WINDOW4_IMAGE, WINDOW5_IMAGE, WINDOW6_IMAGE]

KEY_IMAGE = pygame.image.load("./keymaster.png")
GATE_IMAGE = pygame.image.load("./gatekeeper.png")

FORKLIFT_IMAGE = pygame.image.load("./forklift.png")

BUILDING01_IMAGE = pygame.image.load("./building1.png") # FACTORY 
BUILDING02_IMAGE = pygame.image.load("./building2.png")
BUILDING03_IMAGE = pygame.image.load("./building3.png") # GHOSTBUSTERS HQ
BUILDING04_IMAGE = pygame.image.load("./building4.png")
BUILDING05_IMAGE = pygame.image.load("./building5.png")
BUILDING06_IMAGE = pygame.image.load("./building6.png")
BUILDING07_IMAGE = pygame.image.load("./building7.png") # PARK
BUILDING08_IMAGE = pygame.image.load("./building8.png") # GAS
BUILDING09_IMAGE = pygame.image.load("./building9.png") # Train

HQ_FACADE = pygame.image.load("./hq_facade.png") # GHOSTBUSTERS HQ FACADE
BRICKS_FACADE = pygame.image.load("./bricks.png") # bricks FACADE
PARK_FACADE = pygame.image.load("./park_facade.png") # bricks FACADE

ZUUL_FACADE = pygame.image.load("./zuul_building_facade.png") # ZUUL buidling facade


stayPuft_images = [
        pygame.image.load("./staypuft1.png"),
        pygame.image.load("./staypuft2.png"),
        pygame.image.load("./staypuft3.png"),
        pygame.image.load("./staypuft4.png"),

    ]



vehicle_images = {
            # 'motorcycle': pygame.image.load("./motorcycle.png"),
            'compact': pygame.image.load("./car1.png"),
            'hearse': pygame.image.load("./car2.png"),
            'wagon': pygame.image.load("./car3.png"),
            'utility-truck': pygame.image.load("./car4.png"),
            'high-performance': pygame.image.load("./car5.png"),
            # Add more mappings as needed
        }



vehicle__side_images = {
            # 'motorcycle': pygame.image.load("./car2_side.png"),
            'compact': pygame.image.load("./car1_side.png"),
            'hearse': pygame.image.load("./car2_side.png"),
            'wagon': pygame.image.load("./car3_side.png"),
            'utility-truck': pygame.image.load("./car2_side.png"),
            'high-performance': pygame.image.load("./car5_side.png"),
            # Add more mappings as needed
        } 

equipment_images = {
            
            'PK Energy Detector': pygame.image.load("./pke.png"),
            'Giga Meter': pygame.image.load("./gigameter.png"),
            'Image Intensifier': pygame.image.load("./image.png"),
            'Marshmallow Sensor': pygame.image.load("./marshmallow.png"),
            'Infrared Camera': pygame.image.load("./camera.png"),
            'Barometric Analyzer': pygame.image.load("./barometric.png"),

            'Cargo Expansion' : pygame.image.load("./storage.png"),

            'Ghost Bait': pygame.image.load("./bait.png"),
            'Ghost Trap': pygame.image.load("./trap.png"),
            'Open Trap': pygame.image.load("./open_trap.png"),
            '*Full Trap*': pygame.image.load("./full_trap.png"),
            'Ghost Vacuum': pygame.image.load("./vacuum.png"),
            'Ghost Vacuum On': pygame.image.load("./vacuum_on.png"),
            'Remote Control Trap Vehicle': pygame.image.load("./remote.png"),
            'Extendable Gunner Seat': pygame.image.load("./seat.png"),
            'Mobile Proton Charger': pygame.image.load("./tank.png"),
            'Portable Lazer Confinement': pygame.image.load("./portable2.png"),

            'Muon Scrubber': pygame.image.load("./scrubber.png"),
            'Aerosol Slime Cleaner': pygame.image.load("./spray.png"),
            'Portable Shield Generator' : pygame.image.load("./shield.png"),
            'Sonic Disruptor' : pygame.image.load("./horn.png"),
            'EMP Emitter' : pygame.image.load("./emp.png"),
            'Ecto-Repellent Field Generator' : pygame.image.load("./anti_ecto.png"),
            'Ecto-Fusion Fuel Generator' : pygame.image.load("./fuel_gen.png")
    
        }
# ----------------------------------------------------------------------------------

list_of_names = ["Arthur", "Ali", "Aaliyah", "Evelyn", "Samuel", "Clara", "Algernon", "Rosalind", "Cornelius", "Adeline", "Thaddeus", "Isadora",
    "Ambrose", "Seraphina", "Eudora", "Percival", "Octavia", "Reginald", "Lavinia", "Archibald", "Constance",
    "Ignatius", "Genevieve", "Rupert", "Ophelia", "Ezekiel", "Evangeline", "Montgomery", "Lucinda", "Bartholomew",
    "Arabella", "Percival", "Cordelia", "Mortimer", "Theodora", "Atticus", "Seraphine", "Horatio", "Gwendolyn",
    "Ambrosia", "Theron", "James","Robert","John","Michael","David","William","Joseph","Thomas","Christopher",
    "Charles","Daniel","Matthew","Anthony","Mark","Donald","Steven","Andrew","Paul","Joshua","Kenneth",
    "Brian","George","Timothy","Ronald","Jason","Edward","Jeffrey","Ryan","Jacob", "Nicholas","Eric",
    "Jonathan","Stephen","Larry","Justin","Scott","Brandon","Benjamin","Samuel","Gregory","Alexander","Patrick",
    "Frank","Raymond","Jack","Dennis","Jerry","Tyler","Aaron","Jose","Adam","Nathan","Henry","Zachary","Douglas",
    "Kyle","Noah","Ethan","Jeremy", "Christian","Keith","Roger","Terry","Austin","Sean","Gerald",
    "Carl","Harold","Dylan","Arthur","Lawrence","Jesse","Bryan","Billy","Bruce","Gabriel","Joe",
    "Alan","Juan","Albert","Willie","Elijah","Wayne","Randy","Vincent","Mason","Roy","Ralph","Bobby","Russell",
    "Philip","Eugene","Mary","Jennifer","Linda","Elizabeth","Barbara","Susan","Jessica",
    "Sarah","Karen","Lisa","Nancy","Betty","Sandra","Margaret","Ashley","Kimberly","Emily","Donna","Michelle",
    "Carol","Amanda","Melissa","Deborah","Stephanie","Dorothy","Rebecca","Sharon","Laura","Cynthia","Amy",
    "Kathleen","Angela","Shirley","Brenda","Emma","Anna","Pamela","Nicole","Samantha","Katherine","Christine",
    "Helen","Debra","Rachel","Carolyn","Janet","Maria","Catherine", "Diane","Olivia","Julie","Joyce",
    "Victoria","Ruth","Virginia","Lauren","Kelly","Christina","Joan","Evelyn","Judith","Andrea","Hannah",
    "Megan","Cheryl","Jacqueline","Martha","Madison","Teresa","Gloria","Sara","Janice","Ann","Kathryn",
    "Sophia","Frances","Jean","Alice","Judy","Isabella","Julia","Grace","Amber","Denise","Danielle",
    "Marilyn","Beverly","Charlotte","Natalie","Theresa","Diana","Brittany","Doris","Kayla","Alexis","Lori",
    "Marie", "Peter", "Egon", "Winston", "Ray", "Louis", "Dana", "Janine", "Lenny", "Walter", 
    "Oscar", "Eduardo", "Kylie", "Roland", "Garrett", "Abigail", "Erin", "Jillian", "Patricia", "Kevin",
    "Phoebe", "Trevor", "Gary", "Lucky", "Callie", "Sherman", "Lars", "Nadeem", "Hubert", "Logan"
    ]



class Player():
    def __init__(self):
        super().__init__()

        self.name = ""
        self.cash_balance = 0
        self.vehicle = None
        self.vehicle_items = []
        self.base = []
        self.roster = pygame.sprite.Group()
        self.mapSprite = None

        self.fuel = 66
        self.proton_charge = 100
        self.max_proton_charge = 100
        # self.proton_charge_per = PROTON_CHARGE_PER_TICK

        # Define the aspects of research
        self.research_aspects = ["Ghost Physiology\nand Behavior", "Technological\nAdvancements", "Ectoplasmic\nStudies", "Paranormal\nPhenomena", "Environmental\nAnalysis", "Psychic\nand Occult\nKnowledge"]
        self.research_allocations = [10] * len(self.research_aspects)

        self.portable_storage = 0 

    def has(self, check_item_name):

        for item in self.vehicle_items:
            if item['name'] == check_item_name:
                return True 
        return False

    def num_available_ghostbusters(self):
        count = 0
        for buster in self.roster:
            if not buster.slimed:
                count += 1
        return count

def spritePixelColorChange(sprite, old=ABS_GREEN, new=ORIGINAL_UNIFORM_YELLOW):
    # Define the green color range (you can adjust these values)
    # lower = (0, 100, 0)  # Lower range of green
    # upper = (100, 255, 100)  # Upper range of green

    lower = old 
    upper = old

    # Create a copy of the image to modify
    modified_sprite = sprite.copy()



    # Iterate through the pixels and replace green pixels with red
    for x in range(modified_sprite.get_width()):
        for y in range(modified_sprite.get_height()):
            pixel_color = modified_sprite.get_at((x, y))

            # Check if the pixel is green
            if (lower[0] <= pixel_color[0] <= upper[0] and
                lower[1] <= pixel_color[1] <= upper[1] and
                lower[2] <= pixel_color[2] <= upper[2]):
                # Replace green with red

                modified_sprite.set_at((x, y), (*new, pixel_color.a))  # Change to red

    return modified_sprite




def is_obstacle_between(sprite, direction):
    global buildings
    sprite_rect = sprite.rect
    obstacles = buildings.sprites()

    if direction == "up":
        # Check if any obstacle is above the sprite
        for obstacle in obstacles:
            if obstacle.rect.bottom < sprite_rect.top and \
                    sprite_rect.centerx in range(obstacle.rect.left - 1, obstacle.rect.right + 1):
                return True

    elif direction == "down":
        # Check if any obstacle is below the sprite
        for obstacle in obstacles:
            if obstacle.rect.top > sprite_rect.bottom and \
                    sprite_rect.centerx in range(obstacle.rect.left - 1 , obstacle.rect.right + 1):
                return True

    elif direction == "left":
        # Check if any obstacle is left of the sprite
        for obstacle in obstacles:
            if obstacle.rect.right < sprite_rect.left and \
                    sprite_rect.centery in range(obstacle.rect.top - 1, obstacle.rect.bottom + 1):
                return True

    elif direction == "right":
        # Check if any obstacle is right of the sprite
        for obstacle in obstacles:
            if obstacle.rect.left > sprite_rect.right and \
                    sprite_rect.centery in range(obstacle.rect.top - 1, obstacle.rect.bottom + 1):
                return True

    return False



# Return true if line segments AB and CD intersect
def line_intersection(A,B,C,D):
    line = LineString([A, B])
    other = LineString([C, D])
    return line.intersects(other)

    


class FloorLevelSprite(pygame.sprite.Sprite):
    def __init__(self, level, x, y):
        super().__init__()
        self.level = level
        self.image = FONT32.render(f"Floor {level}", True, WHITE)  # Adjust the color if needed
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Position of the floor level sprite

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Position of the door


class Equipment_Sprite(pygame.sprite.Sprite):
    def __init__(self, name, cost, unique):
        super(Equipment_Sprite, self).__init__()
        self.name = name 
        self.cost = cost 
        self.unique = unique

        if self.name in equipment_images:
            self.image = equipment_images[self.name]

            if self.name == "Muon Scrubber":
                self.image = pygame.transform.rotate(self.image,-90)

        else:
            self.image = equipment_images['Portable Lazer Confinement'] # default image

        self.rect = self.image.get_rect()
        self.rect.x = 0  # Adjust the initial x position
        self.rect.y = 0 # Adjust the initial x position


class Forklift(pygame.sprite.Sprite):
    def __init__(self):
        super(Forklift, self).__init__()
        self.image = pygame.transform.scale(FORKLIFT_IMAGE, (FORKLIFT_IMAGE.get_width()*.85, FORKLIFT_IMAGE.get_height()*.85))
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = 790  # Adjust the initial x position
        self.rect.y = 195 # Adjust the initial x position
        self.speedX = 2
        self.speedY = 1

        self.gotoX = self.rect.x
        self.gotoY = self.rect.y
        self.selection = 0

        self.loading = False
        self.target_sprite = None

        self.loaded = False
        self.mounting = False

        self.selected_equipment = None

    def update(self):
        global selected_index
        global player
        global equipment_choices
        # Move to the goto Coords at self.speed if not already there
        movingX = False
        movingY = False 

        # print(self.rect.x , self.rect.y)

        if self.loaded:
            self.image = pygame.transform.flip(self.orig_image,True,False)
             
            
        else:
            self.image = self.orig_image
            


        

        if selected_index != self.selection:
            
            self.selection = selected_index


        if abs(self.gotoX - self.rect.x) <= self.speedX:
            self.rect.x = self.gotoX
        elif self.rect.x != self.gotoX:
            if self.rect.x < self.gotoX:
                self.rect.x += self.speedX
                movingX = True
            else:
                self.rect.x -= self.speedX
                movingX = True

        if abs(self.gotoY - self.rect.y) <= self.speedY:
            self.rect.y = self.gotoY 
        elif self.rect.y != self.gotoY:
            if self.rect.y < self.gotoY:
                self.rect.y += self.speedY
                movingY = True
            else:
                self.rect.y -= self.speedY
                movingY = True

        
        if self.loading and not self.loaded and not self.mounting and self.target_sprite is not None:
            if (self.rect.x != self.target_sprite.rect.x) or (self.rect.y != self.target_sprite.rect.y):
                if not movingX and not movingY:
                    self.goto(self.target_sprite.rect.x, self.target_sprite.rect.y)
                    movingX = True
                    movingY = True
                    # print("A")

            elif (self.rect.x == self.target_sprite.rect.x) and (self.rect.y == self.target_sprite.rect.y):
                if not self.loaded and not self.mounting:
                    if not movingX and not movingY:
                        self.loaded = True
                        self.goto(WIDTH//2, self.rect.y)
                        movingX = True
                        movingY = True

                        # print("B")

        if self.loaded and not self.mounting:
            if not movingX and not movingY:
                self.mounting = True
                self.goto(WIDTH//2 + 200,  self.rect.y+100)
                movingX = True
                movingY = True
                # print("C")

        if self.loaded and self.mounting:
            if not movingX and not movingY:
                self.loading = False
                self.loaded = False
                self.mounting = False
                equipment_cost = self.selected_equipment['cost']
                player.cash_balance -= equipment_cost
                player.vehicle_items.append(self.selected_equipment)
                self.target_sprite = None
                self.selected_equipment = None
                # print("D")
                


        if not movingX and not movingY:
            FORK_CHANNEL.stop()

        elif not FORK_CHANNEL.get_busy():
            FORK_CHANNEL.play(FORK_LONG_SOUND)



    def goto(self, x, y):
        # Change the goto coords

        if (self.rect.x != x) or (self.rect.y != y):
        
            self.gotoX = x
            self.gotoY = y



    def load(self, selected_equipment):
        global equipment_sprites

        self.loading = True

        self.selected_equipment = selected_equipment

        # player.vehicle_items.append(equipment_choices[selected_equipment])

        for sprite in equipment_sprites.sprites():
            if sprite.name == self.selected_equipment['name']:
                self.target_sprite = sprite
                


    def unload(self, selected_equipment):
        ...





class PointText(pygame.sprite.Sprite):
    def __init__(self, position, points, timeToLive=180, color=WHITE):
        super(PointText, self).__init__()

        self.image = FONT36.render(f"{points}", True, color)
        self.rect = self.image.get_rect(center=position)
        self.time_to_live = timeToLive  # Number of frames the text will be displayed
        self.current_frame = 0
        
    def update(self):
        self.current_frame += 1
        if self.current_frame >= self.time_to_live:
            self.kill()  # Remove the sprite when its time to live is up
        else:
            alpha = int(255 * (1 - self.current_frame / self.time_to_live))  # Calculate alpha for fading
            self.image.set_alpha(alpha) 

class Center_line_dash(pygame.sprite.Sprite):
    def __init__(self, y):
        super(Center_line_dash, self).__init__()
        self.image = pygame.Surface((10, 50))
        self.image.fill(YELLOW)  # White color for stars
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH//2
        self.rect.y = y
        self.rel_speed = 1

    def update(self,street_speed):
        speed = street_speed

        self.rect.y += speed*self.rel_speed
        if self.rect.y > HEIGHT:
            self.rect.y = 0

class CurbStone(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super(CurbStone, self).__init__()
        self.image = pygame.Surface((20, size))
        self.image.fill(DARK_GREY)  # White color for stars
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rel_speed = 1
        self.size = size

    def update(self,street_speed):
        ...
        speed = street_speed

        if self.rect.y > HEIGHT:
            self.rect.y = -self.size

        self.rect.y += speed*self.rel_speed


class FuelBarrel(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super().__init__()
        self.image = pygame.transform.scale(FUEL_BARREL_IMAGE, (45, 56))
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(BUILDING_MARGIN, WIDTH - BUILDING_MARGIN - self.image.get_width())  # Adjust the initial x position
        self.rect.y = -self.image.get_height()  # Start just above the top of the screen
        self.speed = speed

    def update(self, vacuum_center):
        global player

        self.rect.y += self.speed

        # Check if the barrel has moved off the screen
        if self.rect.y > HEIGHT:
            self.kill()  # Remove the sprite when it goes off the screen


        car_x_center, car_y_center = vacuum_center

        distX = abs(self.rect.centerx - car_x_center)
        distY = abs(self.rect.centery - car_y_center)

        dist = math.hypot(distX,distY)

        if dist < 100:
            player.fuel += 25
            if player.fuel > player.vehicle['tank_size']:
                player.fuel = player.vehicle['tank_size']
            WOOSH_SOUND.play()
            self.kill()

            
                
# Breadcrumb class
class Breadcrumb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))


# Create player class
class Player_On_Map(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()


        # -- NAVIGATING MAP 
        self.size = size
        self.logo = pygame.transform.scale(GB_LOGO, (self.size, self.size))
        self.circle_color = BLUE  # Initial color

        # Create a blue circle surface
        self.circle = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(self.circle, self.circle_color, (self.size // 2, self.size // 2), self.size // 2)

        # Combine the blue circle and the centered Ghostbusters logo
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.image.blit(self.circle, (0, 0))
        self.image.blit(self.logo, ((self.size - self.logo.get_width()) // 2, (self.size - self.logo.get_height()) // 2))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.prev_x = x
        self.prev_y = y

        car_speed = player.vehicle["speed"] // CAR_SPEED_ON_MAP_FACTOR


        self.Xspeed = car_speed #Xspeed
        self.Yspeed = car_speed #Yspeed
        self.color_timer = 0

        self.below_building = None

        # Warning text variables
        self.charging_timer = 0
        self.charging_interval = 8  # Adjust the flashing interval as needed
        self.charging = False

        self.lastBreadCrumb = Breadcrumb(self.rect.x, self.rect.y)

        self.number_of_sucked_ghosts = 0
        self.passed_gas_station = False

    def update(self):
        global buildings
        global game_mode
        # global running
        global navigating
        global breadcrumbs
        global textShown
        global mrStayPuft

        global marshmallowed
        global end_game
        global game_over
        global fee_card

        global ghosts_captured
        global player

        

        # Change the color of the blue circle every few frames
        self.color_timer += 1
        if self.color_timer % 20 == 0:
            # Red color during every even frame
            if self.color_timer % 60 == 0:
                self.circle_color = RED
            elif self.color_timer % 40 == 0:
                # White color during every 40th frame
                self.circle_color = WHITE
            else:
                # Blue color during every odd frame
                self.circle_color = TRUE_BLUE

            # Update the Player sprite's image
            self.circle = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            pygame.draw.circle(self.circle, self.circle_color, (self.size // 2, self.size // 2), self.size // 2)
            self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
            self.image.blit(self.circle, (0, 0))
            self.image.blit(self.logo, ((self.size - self.logo.get_width()) // 2, (self.size - self.logo.get_height()) // 2))



        car_speed = player.vehicle["speed"] // CAR_SPEED_ON_MAP_FACTOR
        self.Xspeed = car_speed #Xspeed
        self.Yspeed = car_speed #Yspeed

        # Update the position of the player sprite
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.Xspeed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.Xspeed
        if keys[pygame.K_UP]:
            self.rect.y -= self.Yspeed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.Yspeed

        # Limit player movement to the screen
        self.rect.x = max(0, min(WIDTH - self.size, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.size, self.rect.y))



        # Check for collisions with buildings
        collisions = pygame.sprite.spritecollide(self, buildings, False)
        if collisions:
            above = False
            below = False
            left = False 
            right = False

            building = collisions[0]
            # print(player.mapSprite.rect.top, building.rect.bottom)

            if self.rect.top >= building.rect.bottom - 3: # completely below building
                # print("below")
                below = True

            if self.rect.bottom <= building.rect.top + 5:# completely above building
                # print("above")
                above = True

            if self.rect.right <= building.rect.left + 3 : #complely left of building
                # print("left")
                left = True 

            if self.rect.left >= building.rect.right - 5: #complely right of building
                # print("right")
                right = True


            above = True
            below = True
            left = True 
            right = True

            # If player collides with building, move them back to their previous position

            if left:
                if (self.rect.y) < building.rect.top:
                    self.rect.y -= self.Yspeed
                    if not (above or below):
                        self.rect.x = player.mapSprite.prev_x

                elif (self.rect.y + self.size - self.size//4) > building.rect.bottom - 5:
                    self.rect.y += self.Yspeed
                    if not (above or below):
                        self.rect.x = player.mapSprite.prev_x 


                else:
                    self.rect.x = player.mapSprite.prev_x
                    self.rect.y = player.mapSprite.prev_y

                

            elif right:
                if (self.rect.y + self.size//4) < building.rect.top + 5:
                    self.rect.y -= self.Yspeed
                    if not (above or below):
                        self.rect.x = player.mapSprite.prev_x

                elif (self.rect.y + self.size - self.size//4) > building.rect.bottom - 5:
                    self.rect.y += self.Yspeed
                    if not (above or below):
                        self.rect.x = player.mapSprite.prev_x  
                else:
                    self.rect.x = player.mapSprite.prev_x
                    self.rect.y = player.mapSprite.prev_y 

               

            if above:
                if (self.rect.x + self.size//4) < building.rect.left + 5:
                    self.rect.x -= self.Xspeed
                    if not (left or right):
                        self.rect.y = player.mapSprite.prev_y

                elif (self.rect.x + self.size - self.size//4) > building.rect.right - 5:
                    self.rect.x += self.Xspeed
                    if not (left or right):
                        self.rect.y = player.mapSprite.prev_y

                else:
                    self.rect.x = player.mapSprite.prev_x
                    self.rect.y = player.mapSprite.prev_y

            elif below:
                if (self.rect.x + self.size//4) < building.rect.left + 5:
                    self.rect.x -= self.Xspeed
                    if not (left or right):
                        self.rect.y = player.mapSprite.prev_y

                elif (self.rect.x + self.size - self.size//4) > building.rect.right - 5:
                    self.rect.x += self.Xspeed
                    if not (left or right):
                        self.rect.y = player.mapSprite.prev_y
                else:
                    self.rect.x = player.mapSprite.prev_x
                    self.rect.y = player.mapSprite.prev_y 

            else:
                self.rect.x = player.mapSprite.prev_x
                self.rect.y = player.mapSprite.prev_y
            ...


        if not collisions:

            ...

        # Check if the player is below a building
        self.below_building = None
        for building in buildings:
            if self.rect.centerx > building.rect.left and self.rect.centerx < building.rect.right:
                if (self.rect.centery - building.rect.bottom <= self.size):
                    self.below_building = building
                    if self.below_building.name == "Gas":
                        if player.fuel + 10 < player.vehicle['tank_size']:
                            self.passed_gas_station = True
                            # print(self.passed_gas_station)
                    break


        # check if the player has the mobile containment system:
        if player.has("Mobile Proton Charger"):
            if player.proton_charge < player.max_proton_charge:
                self.charging_timer += 1
                if self.charging_timer % self.charging_interval == 0:
                    self.charging = not self.charging
                    player.proton_charge += 1

        if keys[pygame.K_SPACE]:
            if fee_card:
                fee_card.clear_card_manually()
                

        if keys[pygame.K_RETURN]:
            if self.below_building != None:

                # we don't need to give player a barrel if going to gas station
                if self.below_building.name == "Gas":
                        self.passed_gas_station = False 

                driving_time_to_destination = 0
                for breadcrumb in breadcrumbs.sprites():
                    # add up breadcrumbs first  toget driving time and distance 
                    driving_time_to_destination += 1
                    breadcrumb.kill()

                if (driving_time_to_destination <= 1) and (self.number_of_sucked_ghosts == 0):
                    ...
                else:
                    # print(self.passed_gas_station)


                    ### DRIVE TO DESTINATION ###
                    # ----------------------------------------------------------------
                    
                    drive_to_destination(driving_time_to_destination, self.number_of_sucked_ghosts, self.passed_gas_station)
                    fee_card = None
                    self.passed_gas_station = False # reset
                    
                self.number_of_sucked_ghosts = 0 


                if self.below_building.name == "Gas":
                    cashdif= round(player.vehicle['tank_size'] - player.fuel)
                    player.cash_balance -= cashdif
                    CASH_SOUND.play()
                    point_text = PointText((player.mapSprite.rect.centerx, player.mapSprite.rect.y),"$ -" + str(cashdif) + " for Fuel", color=RED)
                    textShown.add(point_text)
                    all_sprites.add(point_text)

                    player.fuel = player.vehicle['tank_size']

                if self.below_building.name == "Zuul":
                    if (not game_over) and active_buildings.has(self.below_building):

                        # EVADE MR STAY PUFT AT DOORWAY !!!
                        ghostbusters_entered_door = evade_staypuft_at_doorway()

                        if len(ghostbusters_entered_door) >= NUM_BUSTER_REQUIRED_FOR_ZUUL_ROOF:

                            # end game climb stairs in zuul building
                            success, num_ghost_busted = climb_stairs_in_building(ghostbusters_entered_door)
                            MUSIC.unpause()
                            if success:
                                active_buildings.remove(self.below_building)
                                marshmallowed = False 
                                end_game = False 
                                game_over = True

                                fee = VICTORY_OVER_GOZER_FEE
                                player.cash_balance += fee # VICTORY !!!!
                                CASH_SOUND.play()
                                point_text = PointText((player.mapSprite.rect.centerx, player.mapSprite.rect.y),"$" + str(fee) + " Reward", color=GREEN)
                                textShown.add(point_text)
                                all_sprites.add(point_text)

                                mrStayPuft.sucked = True
                                # VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)

                                marshmallowed = False
                                
                                mrStayPuft.kill()
                                mrStayPuft = None
                                fee_card = create_victory_card(screen, fee, self.below_building) 

                if self.below_building.name == "HQ":
                    enterOrExit_building(building=self.below_building)
                    navigating = False

                    player.proton_charge = player.max_proton_charge
                    CHARGE_SOUND.play()

                    # for buster in player.roster.sprites():
                    #     if buster.slimed:
                    #         buster.slimed = False

                    if player.has("*Full Trap*"):
                        EMPTY_TRAPS_SOUND.play()

                    player.portable_storage = 0

                    # Replace all occurrences of "*Full Trap*" with a new "Ghost Trap"
                    player.vehicle_items = [
                        {"name": "Ghost Trap", "cost": 600, 'unique': False}
                        if item['name'] == "*Full Trap*"
                        else item
                        for item in player.vehicle_items
            ]



                if active_buildings.has(self.below_building) and self.below_building.name != "Zuul":

                    hasTrapAvailable = False

                    for item in player.vehicle_items:
                        if item['name'] == "Ghost Trap" and not hasTrapAvailable:
                            hasTrapAvailable = True
                            break  # just one trap needed


                    if hasTrapAvailable and player.num_available_ghostbusters() > 0 and (player.proton_charge >= MINIMUM_PROTON_CHARGE_FOR_MISSION):
                        num_ghost_busted, ghosts_captured = bust_ghost_at_building(building=self.below_building)
                        MUSIC.unpause()


                        if num_ghost_busted >= 1:
                            for item in player.vehicle_items:
                                if item['name'] == "Ghost Trap":
                                    player.vehicle_items.append({"name": "*Full Trap*", "cost": 600, 'unique': False})
                                    player.vehicle_items.remove(item)


                                    fee = ON_SITE_INSPECTION_FEE # on-site inspection
                                    if self.below_building.first_ghost_removal_done:
                                        fee += SUBSEQUENT_GHOST_FEE * num_ghost_busted # subsequent removal of ghost
                                    else:
                                        fee += FIRST_GHOST_REMOVAL_FEE + (SUBSEQUENT_GHOST_FEE * (num_ghost_busted-1)) # first time removal of ghost
                                    if not self.below_building.paid_storage_fee:
                                        fee += FIRST_TIME_STORAGE_FEE # first time storage fee

                                    # Chance to add additional fees
                                    
                                    specials = []
                                    # DON"T EXCEED MAX # OF SPECIALS
                                    if random.randint(0, 100) < 30:  # 30% chance for cleanup fee
                                        if len(specials) < MAX_NUM_OF_SPECIAL_FEES:
                                            fee += CLEANUP_FEE
                                            specials.append(f"- Ectoplasm Cleanup Fee - ${CLEANUP_FEE}")
                                    
                                    if random.randint(0, 100) < 20:  # 20% chance for proton pack battery surcharge
                                        if len(specials) < MAX_NUM_OF_SPECIAL_FEES:
                                            fee += BATTERY_FEE
                                            specials.append(f"- Proton Pack Battery Surcharge - ${BATTERY_FEE}")
                                    
                                    if random.randint(0, 100) < 10:  # 10% chance for hazardous materials disposal fee
                                        if len(specials) < MAX_NUM_OF_SPECIAL_FEES:
                                            fee += HAZARD_FEE
                                            specials.append(f"- Hazardous Materials Disposal - ${HAZARD_FEE}")

                                    if random.randint(0, 100) < 10:  # 10% chance for a tip
                                        if len(specials) < MAX_NUM_OF_SPECIAL_FEES:
                                            tip_fee = random.randint(GHOST_HUNTER_TIP_FEE_MIN, GHOST_HUNTER_TIP_FEE_MAX)  # Random tip between $50 and $200
                                            fee += tip_fee
                                            specials.append(f"- Ghost Hunter's Tip - ${tip_fee}")

                                    if random.randint(0, 100) < 10:  # 10% chance for counseling fee
                                        if len(specials) < MAX_NUM_OF_SPECIAL_FEES:
                                            fee += COUNSELING_FEE
                                            specials.append(f"- Post-Incident Counseling - ${COUNSELING_FEE}")
                                    

                                    if self.below_building.name == "Library":
                                        specials.append(f"- Library Research Bonus")

                                    if self.below_building.name == "University":
                                        specials.append(f"- University Research Bonus")

                                    if self.below_building.name == "Police":
                                        fee -= int(fee * FIRST_RESPONDERS_DISCOUNT_PERCENT) # 50 % discount
                                    elif self.below_building.name == "Hospital":
                                        fee -= int(fee * FIRST_RESPONDERS_DISCOUNT_PERCENT) # 50 % discount
                                    elif self.below_building.name == "Church":
                                        fee = 0 # 100 % discount
                                        

                                    # Create the card
                                    fee_card = create_fee_card(screen, fee, self.below_building, num_ghost_busted, ghosts_captured, specials) 
                                    # fee_card.start_animation()

                                    if not self.below_building.first_ghost_removal_done:
                                        self.below_building.first_ghost_removal_done = True
                                    if not self.below_building.paid_storage_fee:
                                        self.below_building.paid_storage_fee = True
                                    
                                    player.cash_balance += fee
                                    active_buildings.remove(self.below_building)
                                    point_text = PointText((player.mapSprite.rect.centerx, player.mapSprite.rect.y),"$" + str(fee), color=GREEN)
                                    textShown.add(point_text)
                                    all_sprites.add(point_text)
                                    TRAP_CHANNEL.stop()
                                    WOOSH_SOUND.play()
                                    CASH_SOUND.play()
                                    


                                    # Check if the player has the mobile containment system:
                                    if player.has("Portable Lazer Confinement"):
                                        # store the ghosts and clear the trap. 
                                        if player.portable_storage < PLC_MAX_STORAGE:
                                            for item in player.vehicle_items:
                                                if item['name'] == "*Full Trap*":
                                                    player.portable_storage += num_ghost_busted
                                                    item['name'] = "Ghost Trap"
                                                    item['cost'] = 600
                                                    item['unique'] = False
                                        else:
                                            # Portable grid is full
                                            ...

                                    break  # just one trap needed

                        else: # not hasTrapAvailable:
                            active_buildings.remove(self.below_building)

                    else:# not hasTrapAvailable:
                        active_buildings.remove(self.below_building)



        xdif = abs(self.rect.centerx - self.lastBreadCrumb.rect.centerx)
        ydif = abs(self.rect.centery - self.lastBreadCrumb.rect.centery)
        distance = math.hypot(xdif, ydif)

        if (xdif >= self.size) or (ydif >= self.size):
            # Add breadcrumb at the player's current position
            
            self.lastBreadCrumb = Breadcrumb(self.rect.centerx, self.rect.centery)
            breadcrumbs.add(self.lastBreadCrumb)
            all_sprites.add(self.lastBreadCrumb)

            if len(breadcrumbs) >= 50: # if there are too many crumbs
                breadcrumbs.sprites()[0].kill() # kill the oldest

        # Store player's previous position for fuel consumption
        xdif = abs(self.prev_x - self.rect.x)
        ydif = abs(self.prev_y - self.rect.y)
        player.fuel -= math.hypot(xdif, ydif) / 100 # consume fuel 

        # Store player's previous position for collision checking
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y


# a floor inside the building that can be walked upon
class Floor_in_building(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=GREY):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = x #random.randint(0, width - self.rect.width)
        self.rect.y = y #-self.rect.height  # Start above the top of the screen

    #     # Create a sprite for dripping goo
    #     self.goo_sprite = Drip_of_goo(self.rect.x,self.rect.x+self.width,self.rect.bottom)  # Adjust position as needed

    # def update(self):
    #     # Update the position of the goo sprite
    #     # self.goo_sprite.rect.midtop = self.rect.bottomleft
    #     self.goo_sprite.update()


class Drip_of_goo(pygame.sprite.Sprite):
    def __init__(self, minX,maxX,Y, radius=12,falling=False):
        super().__init__()
        # Create a circular image for the goo
        self.radius = radius  # Adjust the radius of the circle
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GREEN, (self.radius, self.radius), self.radius)
        # The above line draws a green circle with the given radius centered at (self.radius, self.radius)
        
        if falling:
            self.image = DRIP_OF_GOO_IMAGE
            original_width, original_height = self.image.get_size()
            aspect_ratio = original_height / original_width  # Calculate aspect ratio based on the width

            # Set the new width and calculate the corresponding height
            new_width = int(self.radius*2)  # `self.size` now represents the desired width
            new_height = int(new_width * aspect_ratio)

            # Scale the image
            self.image = pygame.transform.scale(self.image, (new_width, new_height))


        self.rect = self.image.get_rect()
        position = [random.randint(minX,maxX),Y-5]
        self.rect.midtop = position  # Position the goo sprite at the bottom-left corner of the floor

        # Variables for dripping behavior
        numOfSeconds = random.randint(1,5)
        self.drip_interval = 1000*numOfSeconds  # Drip interval in milliseconds (adjust as needed)
        self.last_drip_time = pygame.time.get_ticks() + random.randint(0,self.drip_interval)

        self.falling = falling



    def update(self):
        global floors_of_building
        # Add any dripping animation or movement logic here

        if self.falling:
            self.rect.y += 4

            if pygame.sprite.spritecollide(self, floors_of_building, False):
                self.kill()

        else:

            # Check if it's time to drip
            current_time = pygame.time.get_ticks()
            if current_time - self.last_drip_time >= self.drip_interval:
                self.drip()
                self.last_drip_time = current_time

    def drip(self):
        global goo_in_building
        global selected_ghostbuster
        # Create a new drop of goo below the current position
        new_drop = Drip_of_goo(self.rect.centerx,self.rect.centerx, self.rect.bottom + self.radius * 2,radius=10,falling=True) # Position the new drop below the current one
        goo_in_building.add(new_drop)  # Add the new drop to the sprite group

        if 0 < self.rect.y < HEIGHT : # IS THE BUSTER NEAR ENOUGH TO HEAR
            WATER_DROP.play()

    def draw(self, surface):
        # Draw the goo sprite onto the given surface
        surface.blit(self.image, self.rect)
                

class IndexCard:
    def __init__(self, fee, fee_text, below_building, position, slide_direction="right"):
        """
        Initialize the index card.
        
        Args:
            fee_text (list): List of strings to display on the card.
            position (tuple): Final position of the card (centered).
            slide_direction (str): Direction to slide in from ("left" or "right").
        """
        self.fee = fee
        self.isFine = False
        if self.fee < 0:
            self.isFine = True
        self.fee_text = fee_text
        self.below_building = below_building
        self.position = position
        self.slide_direction = slide_direction
        # Start fully off-screen based on the slide direction
        self.current_x = -CARD_WIDTH if slide_direction == "left" else WIDTH
        self.state = "sliding_in"
        self.speed = 20
        self.visible_time = 0
        
        self.header_logo_size = (52, 52)
        self.scaled_header_logo = pygame.transform.scale(GB_LOGO, self.header_logo_size)
        # logo_height = font.size("Tg")[1]
        # logo_width = int(logo_height * (GB_SMALL.get_width() / GB_SMALL.get_height()))
        self.scaled_logo = pygame.transform.scale(GB_SMALL, (26,26))

    def update(self):
        global fee_card
        """
        Update the position of the card as it slides in, stays, and slides out.
        """
        if self.state == "sliding_in":
            # speed = 500 * dt
            if self.slide_direction == "right":
                self.current_x -= self.speed
                if self.current_x <= self.position[0]:
                    self.current_x = self.position[0]
                    self.state = "visible"
            else:  # Slide in from the left
                self.current_x += self.speed
                if self.current_x >= self.position[0]:
                    self.current_x = self.position[0]
                    self.state = "visible"

        elif self.state == "visible":
            self.visible_time += 1
            if self.visible_time >= CARD_DISPLAY_TIME:  # Display for ...
                self.state = "sliding_out"

        elif self.state == "sliding_out":
            # speed = 500 * dt
            if self.slide_direction == "right":
                self.current_x += self.speed
                if self.current_x >= WIDTH:
                    self.state = "destroyed"
                    fee_card = None
                    self = None
            else:  # Slide out to the left
                self.current_x -= self.speed
                if self.current_x + CARD_WIDTH <= 0:
                    self.state = "destroyed"
                    fee_card = None
                    self = None


    def clear_card_manually(self):
        self.visible_time = CARD_DISPLAY_TIME
        self.state = "sliding_out"

    def draw(self, screen):
        """
        Draw the card on the screen.
        """
        if self.state == "destroyed":
            fee_card = None
            self = None
            return

        # Draw the card background
        this_card_height = CARD_HEIGHT
        this_card_color = CARD_COLOR
        if self.isFine:
            this_card_height = CARD_HEIGHT//2
            this_card_color = DARK_RED

        pygame.draw.rect(screen, this_card_color, (self.current_x, self.position[1], CARD_WIDTH, this_card_height))
        pygame.draw.rect(screen, CARD_BORDER_COLOR, (self.current_x, self.position[1], CARD_WIDTH, this_card_height), 3)

        # Render the header logo
        branding_text = []
        header_logo_x = self.current_x + (CARD_WIDTH - self.header_logo_size[0]) // 2
        header_logo_y = self.position[1] + 10
        line_spacing = 24
        line_y = header_logo_y + self.header_logo_size[1] + 5

        if not self.isFine:
            
            screen.blit(self.scaled_header_logo, (header_logo_x, header_logo_y))
            # Render the company branding text
            branding_text = ["Ghostbusters Inc.", "We're Ready to Believe You!"]

        if self.isFine:
            line_y = self.position[1] + 20
            branding_text = ["Fine from the City"]

        

        for i, line in enumerate(branding_text):
            text_surface = FONT24.render(line, True, TEXT_COLOR)
            text_width = text_surface.get_width()
            text_x = self.current_x + (CARD_WIDTH - text_width) // 2
            line_y += i*line_spacing
            screen.blit(text_surface, (text_x, line_y))

        line_spacing = 20
        

        if not self.isFine and self.below_building is not None:


            client_text = []

            

            if self.below_building.name == "Police":
                client_text.append(f"Client: City Police")
            elif self.below_building.name == "Hospital":
                client_text.append(f"Client: City Hospital")
            elif self.below_building.name == "University":
                client_text.append(f"Client: City University")
            elif self.below_building.name == "Gas":
                client_text.append(f"Client: City Gas")
            elif self.below_building.name == "Park":
                client_text.append(f"Client: City Park")
            elif self.below_building.name == "Hotel":
                client_text.append(f"Client: City Hotel")
            elif self.below_building.name == "Library":
                client_text.append(f"Client: City Library")
            elif self.below_building.name == "Train":
                client_text.append(f"Client: City Train Station")
            elif self.below_building.name == "Museum":
                client_text.append(f"Client: City Museum")
            elif self.below_building.name == "City Hall":
                client_text.append(f"Client: City Hall")
            elif self.below_building.name == "Church":
                client_text.append(f"Client: City Church")
            elif self.below_building.name == "Bank":
                client_text.append(f"Client: City Bank")

            if len(client_text) > 0:

            
                for i, line in enumerate(client_text):
                    line_y += line_spacing
                    text_surface = FONT20.render(line, True, TEXT_COLOR)
                    text_width = text_surface.get_width()
                    text_x = self.current_x + 10
                    screen.blit(text_surface, (text_x, line_y))

                

        line_y += line_spacing
        line_spacing = 24
        line = ("Fee: $ " + str(self.fee))
        amount_color = GREEN
        if self.isFine: 
            line = ("Fine: $  " + str(self.fee))
            amount_color = RED
        text_surface = FONT24.render(line, True, amount_color)
        text_width = text_surface.get_width()
        text_x = self.current_x + 10
        screen.blit(text_surface, (text_x, line_y))



        line = ("Details:")
        line_spacing = 22
        text_surface = FONT22.render(line, True, TEXT_COLOR)
        text_width = text_surface.get_width()
        text_x = self.current_x + (CARD_WIDTH - text_width) // 2
        line_y += line_spacing
        screen.blit(text_surface, (text_x, line_y))

        # Draw a horizontal line below the details text
        line_start_x = self.current_x + 15  # Left margin
        line_end_x = self.current_x + CARD_WIDTH - 15  # Right margin
        line_y += line_spacing * 0.75  # Position slightly below the last text line
        pygame.draw.line(screen, TEXT_COLOR, (line_start_x, line_y), (line_end_x, line_y), 2)  # 2px thick line

        # Render the fee details text
        # line_y = line_y + line_spacing

        logo_height = FONT22.size("Tg")[1] * 1.5
        logo_width = int(logo_height * (GB_SMALL.get_width() / GB_SMALL.get_height()))
        scaled_logo = pygame.transform.scale(GB_SMALL, (logo_width, logo_height))


        for i, line in enumerate(self.fee_text):
            text_surface = FONT22.render(line, True, TEXT_COLOR)
            text_width = text_surface.get_width()

            # Calculate positions for right alignment
            line_y += line_spacing
            text_x = self.current_x + CARD_WIDTH - 10 - text_width  # Right margin with 10px padding
            if self.below_building is not None:
                if self.below_building.name == "Zuul":
                    text_x = self.current_x + (CARD_WIDTH - text_width) // 2  # Centered horizontally

            if "Class" in line or "Removal" in line:
                # Adjust for the logo width
                logo_x = text_x - logo_width - 5
                screen.blit(scaled_logo, (logo_x, line_y-5))
                screen.blit(text_surface, (text_x, line_y))
            else:
                screen.blit(text_surface, (text_x, line_y))



       # Render the final notes at the bottom of the card

        final_notes = [
            "Thank you for choosing Ghostbusters Inc!",
            "Press Space to Clear"
        ]
        if self.isFine:
            final_notes = [
            "Thank you",
            "Press Space to Clear"
        ]


        
        line_y = self.position[1] + this_card_height - line_spacing * 3
        line_spacing = 20
        for i, line in enumerate(final_notes):
            text_surface = FONT20.render(line, True, TEXT_COLOR)
            text_width = text_surface.get_width()
            text_x = self.current_x + (CARD_WIDTH - text_width) // 2  # Centered horizontally
            line_y += line_spacing
            screen.blit(text_surface, (text_x, line_y))

    def is_destroyed(self):
        """
        Check if the card is ready to be removed.
        """
        return self.state == "destroyed"


# Function to handle the card creation
def create_fee_card(screen, fee, below_building, num_ghost_busted, ghosts_captured, specials):

    fee_text = []
    # fee_text.append(f"- On-Site Inspection - ${ON_SITE_INSPECTION_FEE}")
    # fee_text.append(f"- Ghosts Busted: {num_ghost_busted}")
    
    
    # Subsequent removal of ghosts
    if below_building.first_ghost_removal_done:
        fee_text.append(f"- Subsequent Visit - On-Site Inspection - ${ON_SITE_INSPECTION_FEE}")
        for captured_ghost in ghosts_captured:
            traits_line = " ".join(map(str, captured_ghost.traits))  # Convert all elements to strings
            fee_text.append(f" {captured_ghost.ghost_class}: {traits_line} - ${SUBSEQUENT_GHOST_FEE}")
             

    # First-time removal of ghosts
    else:
        fee_text.append(f"- First Visit - On-Site Inspection - ${ON_SITE_INSPECTION_FEE}")
        for captured_ghost in ghosts_captured:
            traits_line = " ".join(map(str, captured_ghost.traits))  # Convert all elements to strings
            if captured_ghost == list(ghosts_captured)[0]:
                fee_text.append(f" {captured_ghost.ghost_class}: {traits_line} - ${FIRST_GHOST_REMOVAL_FEE}")
            else:
                fee_text.append(f" {captured_ghost.ghost_class}: {traits_line} - ${SUBSEQUENT_GHOST_FEE}")
             


        below_building.first_ghost_removal_done = True

    if not below_building.paid_storage_fee:

        fee_text.append(f"- Storage Fee Applied - ${FIRST_TIME_STORAGE_FEE}")
        below_building.paid_storage_fee = True

    # Chance to add additional fees
    fee_text.append("- Specials :")

    for i, line in enumerate(specials):
        fee_text.append(line)
    
    if below_building.name == "Police":
        fee_text.append(f"- First Responders Discount -50%")
    elif below_building.name == "Hospital":
        fee_text.append(f"- First Responders Discount -50%")
    elif below_building.name == "Church":
        fee_text.append("- Church Discount -100%")
        fee_text.append("Nobody steps on a church in my town!")

    else:
        if len(specials) > 0:
            ...
        else:
            fee_text.append("          - None - ")

    if below_building.rect.x >= WIDTH//2:
        fee_card = IndexCard(fee, fee_text, below_building, (10, CARD_ORIGIN_Y), slide_direction="left")
    else:
        fee_card = IndexCard(fee, fee_text, below_building, (WIDTH - CARD_WIDTH - 10, CARD_ORIGIN_Y), slide_direction="right")

    for captured_ghost in ghosts_captured:
        captured_ghost.kill()
    return fee_card

# Function to handle the card creation
def create_victory_card(screen, fee, below_building):

    fee_text = []
    fee_text.append(f"Congratulations!")
    fee_text.append(f"Thanks to you, {player.name}")
    fee_text.append(f"The Portal to the Spirit World,")
    fee_text.append(f"has been closed. You earn a $ {fee}")
    fee_text.append(f"reward from the city!")
    fee_text.append(f"")
    fee_text.append(f"")
    
    if below_building.rect.x >= WIDTH//2:
        fee_card = IndexCard(fee, fee_text, below_building, (10, CARD_ORIGIN_Y), slide_direction="left")
    else:
        fee_card = IndexCard(fee, fee_text, below_building, (WIDTH - CARD_WIDTH - 10 , CARD_ORIGIN_Y), slide_direction="right")

    # for captured_ghost in ghosts_captured:
    #     captured_ghost.kill()
    return fee_card


# Create building class
class Building(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, name="None"):
        super().__init__()
        self.name = name
        self.color = GREEN
        self.width = width
        self.height = height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        selected_image = random.choice([BUILDING01_IMAGE, BUILDING02_IMAGE, BUILDING03_IMAGE, BUILDING04_IMAGE, BUILDING05_IMAGE, BUILDING06_IMAGE])
        self.overlay_image = pygame.transform.scale(selected_image, (self.width, self.height))  # Resize to fit the building

        self.rect = self.image.get_rect()
        self.rect.x = x #random.randint(0, width - self.rect.width)
        self.rect.y = y #-self.rect.height  # Start above the top of the screen

        # Flashing outline variables
        self.flash_timer = 0
        self.flash_interval = 10  # Adjust the flashing interval as needed
        self.show_outline = False
        self.active_duration = 0
        self.max_active_duration = 500  # Adjust the maximum halted duration (in frames)

        self.first_ghost_removal_done = False # 4000?
        self.paid_storage_fee = False # 1500

        self.isSmashed = False

        self.target_building = False



    def update(self):
        global player
        global active_buildings

        if self.name != "None":
            if self.name == "HQ": 
                self.color = TRUE_BLUE
                self.overlay_image = pygame.transform.scale(BUILDING03_IMAGE, (self.width, self.height))

            elif self.name == "Park": 
                self.overlay_image = pygame.transform.scale(BUILDING07_IMAGE, (self.width, self.height))

            elif self.name == "Train": 
                self.overlay_image = pygame.transform.scale(BUILDING09_IMAGE, (self.width, self.height))

            
            elif self.name == "Gas": 
                self.color = DARK_YELLOW
                self.overlay_image = pygame.transform.scale(BUILDING08_IMAGE, (self.width, self.height))


            # elif self.name == "Zuul": self.color = DARK_RED


            else: self.color = GREEN

        if self.isSmashed:
            self.color = DARK_GREY

            if self.target_building: # prevents losing key buildings
                self.isSmashed = False 
                self.color = GREEN

        if self.target_building:
            self.color = DARK_RED
        
        self.image.fill(self.color)

        


        if active_buildings.has(self):
            # Update flashing outline
            self.flash_timer += 1
            if self.flash_timer % self.flash_interval == 0:
                self.show_outline = not self.show_outline

            if self.show_outline:
                self.image.fill(RED)

            self.active_duration += 1
            if self.active_duration >= self.max_active_duration:
                # if self.name != "Zuul":
                if not self.target_building:
                    active_buildings.remove(self)
                self.active_duration = 0

        if (self == player.mapSprite.below_building) and (active_buildings.has(self) or self.name in ["HQ", "Gas"]): 
            # Update flashing outline
            self.flash_timer += 1
            if self.flash_timer % self.flash_interval == 0:
                self.show_outline = not self.show_outline

            if self.show_outline:
                self.image.fill(WHITE)

            elif active_buildings.has(self):
                self.image.fill(RED)

        # Draw the overlay image on top
        self.image.blit(self.overlay_image, (0, 0))  # Position the overlay to cover the entire surface


        if self.name != "None" and not self.isSmashed:        
            # Render the text
            text_surface = FONT24.render(self.name, True, WHITE)
            text_rect = text_surface.get_rect(center=(self.rect.width // 2, self.rect.height - FONT24.get_height()))

            sign = None
            if self.name == "HQ"      : 
                sign = GB_LOGO
                sign_size_w = 40
                sign_size_h = 40
            if self.name == "Hospital": 
                sign = REDCROSS
                sign_size_w = 30
                sign_size_h = 30
            if self.name == "Police": 
                sign = POLICE
                sign_size_w = 35
                sign_size_h = 45
            if self.name == "Church":
                sign = CROSS
                sign_size_w = 35
                sign_size_h = 50

            if sign is not None:
                # Create a small image surface (replace 'your_image_path.png' with the actual path of your image)
                small_image = pygame.transform.scale(sign, (sign_size_w, sign_size_h))
                small_image_rect = small_image.get_rect()

                # Position the small image centered just above the text
                if self.name == "HQ":
                    small_image_rect.center = (self.rect.width // 2 + small_image_rect.width // 4, text_rect.top - small_image_rect.height)
                elif self.name == "Church":
                    small_image_rect.center = (self.rect.width // 2, text_rect.bottom - small_image_rect.height // 2)
                
                else:
                    small_image_rect.center = (self.rect.width // 2 , text_rect.top - small_image_rect.height)
                # Blit the small image onto the building's surface
                self.image.blit(small_image, small_image_rect)



            # Blit the text onto the building's surface
            self.image.blit(text_surface, text_rect)

class Street_Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        global BUILDING_MARGIN
        global textShown
        self.size = 85
        self.image = MAP_GHOST_IMAGE
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        new_width = int(self.size * aspect_ratio)
        self.image = pygame.transform.scale(self.image, (new_width, self.size))
        self.orig_image = self.image

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(BUILDING_MARGIN, WIDTH - BUILDING_MARGIN - self.size)  # Adjust the initial x position
        self.rect.y = -self.size  # Start just above the top of the screen

        self.speedY = random.randint(3,6)
        self.speedX = 1

        self.direction_x = 1

        self.sucked = False

    def update(self, vacuum_center, vacuum_on):

        if self.direction_x >= 0:
            self.image = self.orig_image
        else:
            self.image = pygame.transform.flip(self.orig_image, True, False)


        # Randomly change the left/right movement direction
        if random.randint(0, 100) < 1:
            self.direction_x *= -1

        if self.rect.x > 0 + BUILDING_MARGIN:
            self.rect.x += self.speedX * self.direction_x
        else:
            self.direction_x = 1
            self.rect.x = 0 + BUILDING_MARGIN


        if self.rect.x < WIDTH - self.size - BUILDING_MARGIN:
            self.rect.x += self.speedX * self.direction_x
        
        else:
            self.direction_x = -1
            self.rect.x = WIDTH - self.size - BUILDING_MARGIN


        self.rect.y += self.speedY
        if self.rect.y > HEIGHT:
            self.kill()  # Remove the sprite when it goes below the bottom of the screen


        car_x_center, car_y_center = vacuum_center

        distX = abs(self.rect.centerx - car_x_center)
        distY = abs(self.rect.centery - car_y_center)

        dist = math.hypot(distX,distY)



        if dist < GHOST_VACUUM_FUNCTIONAL_DISTANCE and vacuum_on:

            self.size -= self.size*.05
            if random.randint(0, 100) < 10:
                self.image = pygame.transform.flip(self.image, True, False)

            self.image = pygame.transform.scale(self.image, (self.size , self.size))

            


            # Recenter the scaled image
            new_rect = self.image.get_rect(center=self.rect.center)
            self.rect = new_rect
            if not self.sucked:
                WOOSH_SOUND.play()
                self.sucked = True


            # Draw a circle at the ghost's position
            circle_size = self.size*0.75 + random.randint(-3,3)
            current_color = random.choice([RED, RED, DARK_RED, ORANGE, YELLOW, WHITE]) 
            # Calculate offsets for left and right circles
            offset = int(self.size * 0.15)  # Adjust offset as needed for spacing
            left_center = (self.rect.centerx - offset, self.rect.centery)
            right_center = (self.rect.centerx + offset, self.rect.centery)

            # Draw left circle
            pygame.draw.circle(screen, current_color, left_center, circle_size, PROTON_BEAM_CIRCLE_LINE_WIDTH)

            # Draw right circle
            pygame.draw.circle(screen, current_color, right_center, circle_size, PROTON_BEAM_CIRCLE_LINE_WIDTH)



            if self.size < 25:
                CASH_SOUND.play()
                player.cash_balance += CASH_PER_STREET_GHOST_CAUGHT
                point_text = PointText((self.rect.centerx, self.rect.y - 50),"$" + str(CASH_PER_STREET_GHOST_CAUGHT), color=GREEN)

                if player.has("Ecto-Fusion Fuel Generator"):
                    player.fuel += ADDED_FUEL_FROM_GENERATOR
                    if player.fuel > player.vehicle['tank_size']:
                        player.fuel = player.vehicle['tank_size']

                textShown.add(point_text)
                all_sprites.add(point_text)
                self.kill()

            # Move the ghost towards the player's center
            vector = pygame.Vector2(car_x_center - self.rect.centerx, car_y_center - self.rect.centery)
            if vector.length() != 0:
                vector.normalize_ip()
                self.rect.move_ip(5 * vector.x, 5 * vector.y)






# Ghost class
class Ghost_at_building(pygame.sprite.Sprite):
    def __init__(self,inside=False,inside_level=0):
        super().__init__()


        self.ghost_class = random.choice(GHOST_CLASSES)

        num_of_traits = random.randint(1, 2)
        self.traits = []

        for _ in range(num_of_traits):
            while True:
                new_trait = random.choice(GHOST_TRAITS)
                if new_trait not in self.traits:
                    self.traits.append(new_trait)
                    break


        

        self.image = random.choice(GHOST_IMAGE_LIST)
        
        # self.image = GHOST13_IMAGE # OVERRIDE IMAGE FOR TESTS

        self.size = 48
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        new_width = int(self.size * aspect_ratio)
        self.image = pygame.transform.scale(self.image, (new_width, self.size))
        self.orig_image = self.image

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0 + 150, WIDTH - self.image.get_width() - 150)
        self.rect.y = random.randint(0, (HEIGHT-(HEIGHT*2/3)) - self.rect.height)
        self.inside = inside
        self.speed = random.randint(GHOST_SPEED_MIN,GHOST_SPEED_MAX)  # Adjust speed as needed

        self.pk_health = random.randint(GHOST_PK_MIN,GHOST_PK_MAX)
        self.full_pk_health = self.pk_health

        if self.inside:
            self.rect.x = random.randint(0 + 150, WIDTH - self.image.get_width() - 150)
            self.rect.y = inside_level
            self.speed = random.randint(INSIDE_GHOST_SPEED_MIN,INSIDE_GHOST_SPEED_MAX)  # Adjust speed as needed
            self.pk_health = random.randint(INSIDE_GHOST_PK_MIN,INSIDE_GHOST_PK_MAX)
            self.full_pk_health = self.pk_health


        self.full_speed = self.speed
        self.orig_y = self.rect.y
        self.direction_x = random.choice([-1,1])
        self.direction_y = random.choice([-1,1])
        
        self.trap = None
        self.trapped = False
        self.escaped = False




        self.climbed_height = self.rect.y


        self.taking_damage = False

    def update(self):
        global ghostbusters_at_building
        global num_ghosts_busted
        global elapsed_time
        global ghosts_captured
        # global leavePackSoundOn

        yA = self.rect.y

        self.taking_damage = False

        if self.pk_health >= (self.full_pk_health - (self.full_pk_health//4)):
            self.speed = self.full_speed


        if self.escaped:
            # print("ESCAPED!")
            ...

        else:
            constraint1 = 0
            constraint2 = 0
            constraint3 = 0
            left_constraint = 0 + 150
            right_constraint = WIDTH - self.image.get_width() - 150

            if not self.inside:
                ...


                # if ghostbusters_at_building.sprites()[0].proton_pack_on:
                #         constraint1 = ghostbusters_at_building.sprites()[0].proton_tip

                # if len(ghostbusters_at_building.sprites()) >= 2:
                #     if ghostbusters_at_building.sprites()[1].proton_pack_on:
                #             constraint2 = ghostbusters_at_building.sprites()[1].proton_tip

                # if len(ghostbusters_at_building.sprites()) >= 3:
                #     if ghostbusters_at_building.sprites()[2].proton_pack_on:
                #             constraint3 = ghostbusters_at_building.sprites()[2].proton_tip

            
            if not self.trapped:

                #Move the ghost randomly in the top 2/3rds of the screen
                if random.randint(0,50) <= 1: 
                    self.direction_y = random.choice([-1,1])
                self.rect.y += random.randint(self.speed-1,self.speed) * self.direction_y
                


                if random.randint(0,100) <= 1: 
                    self.direction_x = random.choice([-1,1])
                self.rect.x += random.randint(self.speed-1,self.speed) * self.direction_x
                if self.direction_x >= 0:
                    self.image = self.orig_image
                else:
                    self.image = pygame.transform.flip(self.orig_image, True, False)

                

                # Keep the ghost within the top 2/3rds of the screen

                if constraint1 != 0 and constraint2 != 0 and constraint3 != 0:
                    # Determine left and right constraints based on proton pack positions
    
                    left_constraint = min(constraint1, constraint2, constraint3)
                    right_constraint = max(constraint1, constraint2, constraint3)


                elif constraint1 != 0 and constraint2 != 0:
                    # Determine left and right constraints based on proton pack positions
                    left_constraint = min(constraint1, constraint2)
                    right_constraint = max(constraint1, constraint2)

                elif constraint1 != 0:
                    if ghostbusters_at_building.sprites()[0].rect.x <= self.rect.x:
                        left_constraint = constraint1


                    elif ghostbusters_at_building.sprites()[0].rect.x > self.rect.x:
                        right_constraint = constraint1

                elif constraint2 != 0:
                    if len(ghostbusters_at_building.sprites()) > 1:
                        if ghostbusters_at_building.sprites()[1].rect.x <= self.rect.x:
                            left_constraint = constraint2


                        elif ghostbusters_at_building.sprites()[1].rect.x > self.rect.x:
                            right_constraint = constraint2

                elif constraint3 != 0:
                    if len(ghostbusters_at_building.sprites()) > 1:
                        if ghostbusters_at_building.sprites()[2].rect.x <= self.rect.x:
                            left_constraint = constraint3


                        elif ghostbusters_at_building.sprites()[2].rect.x > self.rect.x:
                            right_constraint = constraint3

                # if both streams are on the left side, can't catch this way
                if (left_constraint <= self.rect.x) and (right_constraint < self.rect.x):
                    left_constraint = right_constraint
                    right_constraint = WIDTH - self.image.get_width() - 150

                # if both streams are on the right side, can't catch this way
                elif (left_constraint >= self.rect.x) and (right_constraint > self.rect.x):
                    right_constraint = left_constraint
                    left_constraint = 0 + 150


                # if left_constraint > self.rect.x:
                #     left_constraint = 0


                # if right_constraint < self.rect.x:
                #     right_constraint = WIDTH - self.image.get_width()    

                # print(str(left_constraint), str(right_constraint))



                if self.rect.x <= left_constraint + self.image.get_width():
                    self.rect.x = left_constraint + self.image.get_width()
                    self.direction_x = 1
                    if left_constraint > 0 + 150:
                        self.take_damage(damage=0)

                if self.rect.x >= right_constraint - self.image.get_width():
                    self.rect.x = right_constraint - self.image.get_width()
                    self.direction_x = -1
                    if right_constraint < WIDTH - self.image.get_width() - 150:
                        self.take_damage(damage=0)

                if not self.inside: # OUTSIDE
                    if self.rect.y >= (HEIGHT-(HEIGHT*2/3)) - self.rect.height:
                        self.rect.y = (HEIGHT-(HEIGHT*2/3)) - self.rect.height
                        self.direction_y = -1

                    if self.rect.y <= 0 + self.rect.height:
                        self.rect.y = 0 + self.rect.height
                        self.direction_y = 1

                    self.rect.y = max(0 + self.rect.height, min((HEIGHT-(HEIGHT*2/3)) - self.rect.height, self.rect.y))

                else: # INSIDE
                    if self.rect.y >= self.orig_y + 200:
                            self.rect.y = self.orig_y + 200
                            self.direction_y = -1

                    if self.rect.y <= self.orig_y - 200:
                        self.rect.y = self.orig_y - 200
                        self.direction_y = 1

                    self.rect.y = max(self.orig_y - 200, min(self.orig_y + 200, self.rect.y))



            elif self.trapped:
                self.take_damage(damage=0)

                for buster in ghostbusters_at_building:
                    if self == buster.ghost_target:
                        buster.proton_pack_on = False
                        # leavePackSoundOn = False
                        # for buster in ghostbusters_at_building.sprites():
                        #     if buster.proton_pack_on:
                        #         leavePackSoundOn = True
                        #         break
                        buster.ghost_target = None
                        # if not leavePackSoundOn:
                        #     PROTON_PACK_CHANNEL.stop()


                allTrapped = True
                for ghost in ghosts_at_building:
                    if not ghost.trapped:
                        allTrapped = False

                if allTrapped:
                    MUSIC.pause()
                    PKE_CHANNEL.stop()
                    elapsed_time = 0
                    for buster in ghostbusters_at_building:
                        buster.proton_pack_on = False
                        # leavePackSoundOn = False
                        buster.ghost_target = None
                        # PROTON_PACK_CHANNEL.stop()

                ...
                self.rect.y = self.trap.rect.y - self.trap.light_size
                # Shrink the sprite's size
                # self.rect.inflate_ip(-1, -1)
                # self.image = pygame.transform.scale(self.image, self.rect.size)

                if self.rect.centerx < self.trap.rect.centerx:
                    self.rect.x += 1
                elif self.rect.centerx > self.trap.rect.centerx:
                    self.rect.x -= 1
                    # self.size -= 1 # shrink the ghost once trapped
                    

                if self.rect.y >= self.trap.rect.y - self.size//2:
                    # print("KILL!")
                    TRAP_CHANNEL.stop()
                    WOOSH_SOUND.play() 
                    num_ghosts_busted += 1
                    # self.kill()
                    ghosts_captured.add(self)
                    ghosts_at_building.remove(self)

        yB = self.rect.y

        if yB > yA:
            self.climbed_height -= abs(yB-yA)
        if yB < yA:
            self.climbed_height += abs(yB-yA)

        # RECHARGE, IE: HEAL PK ENERGY IF LEFT ALONE
        if self.taking_damage == False:
            if not self.inside:
                if self.pk_health < self.full_pk_health:
                    self.pk_health += 0.5
                    if self.pk_health > self.full_pk_health: 
                        self.pk_health = self.full_pk_health


    def display_pk_health(self, screen):
        textcolor = GREEN
        if self.pk_health < self.full_pk_health:
            textcolor = YELLOW
            
        if self.pk_health < self.full_pk_health//3:
            textcolor = RED

        health_text = round(self.pk_health)
            
        text = under_line_FONT18.render(str(health_text), True, textcolor)
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))  # Adjust vertical offset as needed
        screen.blit(text, text_rect)

    def take_damage(self, damage=1):
        global num_ghosts_busted
        global ghostbusters_at_building


        self.pk_health -= damage
        self.taking_damage = True

        if not self.inside:
            if self.pk_health <= 0:
                self.pk_health = 1




        if self.pk_health < (self.full_pk_health - (self.full_pk_health//4)):
            self.speed = self.full_speed - self.full_speed//4

        if self.pk_health < self.full_pk_health//2:
            self.speed = self.full_speed//2

        if self.pk_health == 1:
            num_streams_on_ghost = 0
            for buster in ghostbusters_at_building.sprites():
                if buster.ghost_target is not None:
                    if self == buster.ghost_target:
                        num_streams_on_ghost += 1
                        self.speed = 1
            if num_streams_on_ghost > 1:
                self.speed = 0
            else:
                ...
        

        if self.pk_health <= 0:
            TRAP_CHANNEL.stop()
            WOOSH_SOUND.play() 
            num_ghosts_busted += 1
            self.kill()
        else:
            # Draw a circle at the ghost's position
            ...
            self.taking_damage = True

    def draw_damage(self):
        if self.taking_damage:
            # Draw a circle at the ghost's position
            circle_size = self.size*0.75 + random.randint(-3,3)
            current_color = random.choice([RED, RED, DARK_RED, ORANGE, YELLOW, WHITE]) 
            # Calculate offsets for left and right circles
            offset = int(self.size * 0.15)  # Adjust offset as needed for spacing
            left_center = (self.rect.centerx - offset, self.rect.centery)
            right_center = (self.rect.centerx + offset, self.rect.centery)

            # Draw left circle
            pygame.draw.circle(screen, current_color, left_center, circle_size, PROTON_BEAM_CIRCLE_LINE_WIDTH)

            # Draw right circle
            pygame.draw.circle(screen, current_color, right_center, circle_size, PROTON_BEAM_CIRCLE_LINE_WIDTH)
        

class JumpingGhost(pygame.sprite.Sprite):  # STAY PUFT AT DOORWAY
    def __init__(self, x, y, jump_radius, jump_speed):
        """
        Initialize the Jumping Ghost sprite.

        Args:
            x (int): The x-coordinate of the center point for jumping.
            y (int): The y-coordinate of the base point (ground level).
            jump_radius (int): The horizontal distance the ghost will cover in one arc.
            jump_speed (float): The speed of the ghost's jump (in radians per frame).
        """
        super().__init__()

        # Load all images into a list for animation
        self.images = [pygame.transform.scale(img, (300, 300)) for img in stayPuft_images]
        self.image_index = 0  # Index to track the current image
        self.image = self.images[self.image_index]

        self.animation_timer = pygame.time.get_ticks()

        # Position and movement properties
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x  # Center point of the jumping motion
        self.y = y  # Ground level
        self.jump_radius = jump_radius
        self.jump_speed = jump_speed
        self.angle = 0 if random.choice([True, False]) else math.pi  # Start at left or right
        self.direction = 1 if self.angle == 0 else -1  # Move toward the opposite side

    def update(self):
        """
        Update the ghost's position based on its jumping behavior.
        """
        now = pygame.time.get_ticks()

        # Move the ghost along the arc
        self.angle += self.jump_speed * self.direction

        # Check if the ghost has reached the end of the arc
        if self.angle >= math.pi or self.angle <= 0:
            self.direction *= -1  # Reverse direction
            self.angle = max(0, min(math.pi, self.angle))  # Clamp the angle to avoid overshoot

        # Calculate the position along the arc
        vertical_scale = 0.25  # Adjust for flatter arcs
        arc_x = self.x + self.jump_radius * math.cos(self.angle)
        arc_y = self.y - (self.jump_radius * vertical_scale) * math.sin(self.angle)
        self.rect.center = (arc_x, arc_y)

        # WALKING ANIMATION -------
        if now - self.animation_timer >= 500:  # Check if half a second has passed
            # Rotate to the next image
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.animation_timer = now  # Reset the timer

    def draw(self, screen):
        """
        Draw the ghost on the screen.

        Args:
            screen (pygame.Surface): The game screen.
        """
        screen.blit(self.image, self.rect)


class StayPuft(pygame.sprite.Sprite):
    def __init__(self, target_building, speed=1):
        super().__init__()

        # Load all images into a list for animation
        self.images = [pygame.transform.scale(img, (150, 150)) for img in stayPuft_images]

        self.image_index = 0  # Index to track the current image
        self.image = self.images[self.image_index]

        self.animation_timer = pygame.time.get_ticks()


        spawn = random.randint(-75, WIDTH + 75), -75 # DEFAULT TO TOP

        spawn_side = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn_side == 'top':
            spawn = random.randint(-150, WIDTH), -150
        elif spawn_side == 'bottom':
            spawn = random.randint(-150, WIDTH), HEIGHT
        elif spawn_side == 'left':
            spawn = -75, random.randint(-150, HEIGHT)
        elif spawn_side == 'right':
            spawn = WIDTH-75, random.randint(-150, HEIGHT)


        self.rect = self.image.get_rect(topleft=(spawn[0], spawn[1]))
        self.target_building = target_building
        self.speed = speed
        self.random_movement = 1  # Adjust the random movement factor
        self.halted = False
        self.halted_duration = 0
        self.max_halted_duration = 500  # Adjust the maximum halted duration (in frames)


        self.sucked = False

    def update(self):
        global pk_energy
        global textShown
        global buildings
        global marshmallowed
        global mrStayPuft

        now = pygame.time.get_ticks()

        # WALKING ANIMATION -------
        if now - self.animation_timer >= 500: # Check if half a second has passed = 150
            # rotate to the next image
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.animation_timer = now  # Reset the timer



        if pygame.sprite.collide_rect(self, player.mapSprite):
            if not self.sucked:
                ...
                # self.sucked = True
                # VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)
                # CASH_SOUND.play()
                # player.cash_balance += 5000
                # point_text = PointText((self.rect.centerx, self.rect.y - 50),"$ 5000 Reward", color=GREEN)
                # textShown.add(point_text)
                # all_sprites.add(point_text)
                # marshmallowed = False
                # mrStayPuft = None
                # self.kill()

        for building in pygame.sprite.spritecollide(self,buildings, False):
            if building.rect.centery > (self.rect.y + self.image.get_height()//2):
                if  building.rect.x < self.rect.centerx < (building.rect.x + building.width):
                    if not building.isSmashed and building.name not in ["HQ", "Zuul"]:
                        VOICE_CHANNEL.play(VOICE_LAUGH)
                        player.cash_balance -= DESTROYED_BUILDING_FINE
                        point_text = PointText((self.rect.centerx, self.rect.y - 50),f"$ {DESTROYED_BUILDING_FINE} Fine", color=RED)
                        textShown.add(point_text)
                        all_sprites.add(point_text)
                        building.isSmashed = True


        # Calculate the vector from the ghost to the target center

        if self.halted:
            self.halted_duration += 1
            if self.halted_duration >= self.max_halted_duration:
                # Reset the halted ghost's movement
                self.halted = False
                self.halted_duration = 0

        margin = self.image.get_width()//2

        puft_dist_to_player = pygame.math.Vector2(self.rect.x + margin, self.rect.y + margin ).distance_to((player.mapSprite.rect.x + player.mapSprite.size//2 , player.mapSprite.rect.y + player.mapSprite.size//2))
        puft_dist_to_zuul =  pygame.math.Vector2(self.rect.x + margin, self.rect.y + margin ).distance_to((self.target_building.rect.x + self.target_building.width//2 , self.target_building.rect.y + self.target_building.height//2))
        # print(str(puft_dist_to_zuul))

        if player.has("Ghost Bait") and (puft_dist_to_player <= 400 and not puft_dist_to_zuul <= 100):
                target_center = (
                    player.mapSprite.rect.x + player.mapSprite.size // 2,
                    player.mapSprite.rect.y + player.mapSprite.size// 2
                )
                vector = pygame.Vector2(target_center[0] - self.rect.centerx, target_center[1] - self.rect.centery)

                if vector != 0:
                    # Normalize the vector (convert it to a unit vector)
                    vector.normalize_ip()

                    # Add a small random movement
                    vector.x += random.uniform(-self.random_movement, self.random_movement)
                    vector.y += random.uniform(-self.random_movement, self.random_movement)

                    # Move the ghost towards the center
                    self.rect.move_ip(self.speed * vector.x, self.speed * vector.y)

  
        elif not self.halted:
            target_center = (
                self.target_building.rect.x + self.target_building.rect.width // 2,
                self.target_building.rect.y + self.target_building.rect.height // 2
            )
            vector = pygame.Vector2(target_center[0] - self.rect.centerx, target_center[1] - self.rect.centery)

            # Normalize the vector (convert it to a unit vector)
            vector.normalize_ip()

            # Add a small random movement
            vector.x += random.uniform(-self.random_movement, self.random_movement)
            vector.y += random.uniform(-self.random_movement, self.random_movement)

            # Move the ghost towards the center
            self.rect.move_ip(self.speed * vector.x, self.speed * vector.y)

            # Check if the distance between centers is within the margin
            margin = self.image.get_width()//2
            

            if puft_dist_to_zuul <= margin:
                # Remove the ghost from sprite groups
                VOICE_CHANNEL.play(VOICE_LAUGH)
                pk_energy += 5000
                player.cash_balance -= STAY_PUFT_AT_ZUUL_FINE
                point_text = PointText((self.rect.centerx, self.rect.y - 50),f"$ {STAY_PUFT_AT_ZUUL_FINE} Fine", color=RED)
                textShown.add(point_text)
                all_sprites.add(point_text)
                marshmallowed = False
                mrStayPuft = None
                self.kill()    



class MapGhost(pygame.sprite.Sprite):
    def __init__(self, target_building, speed=2):
        super().__init__()

        self.target_building = target_building
        self.speed = speed
        self.random_movement = 1  # Adjust the random movement factor
        self.halted = False
        self.halted_duration = 0
        self.max_halted_duration = 500  # Adjust the maximum halted duration (in frames)
        self.sucked = False

        spawn_side = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn_side == 'top':
            x, y = random.randint(0, WIDTH - 20), -20
        elif spawn_side == 'bottom':
            x, y = random.randint(0, WIDTH - 20), HEIGHT
        elif spawn_side == 'left':
            x, y = -20, random.randint(0, HEIGHT - 20)
        elif spawn_side == 'right':
            x, y = WIDTH, random.randint(0, HEIGHT - 20)

        self.image = pygame.transform.scale(MAP_GHOST_IMAGE, (50, 50))
        self.orig_image = self.image
        self.rect = self.image.get_rect(topleft=(x, y))


        self.prev_x = self.rect.x
        self.prev_y = self.rect.y



    def update(self):
        global pk_energy
        global marshmallowed
        global end_game
        global mrStayPuft


        if self.rect.x < self.prev_x:
            if self.prev_x - self.rect.x > self.random_movement:
                self.image = pygame.transform.flip(self.orig_image, True, False)
        else:
            if self.rect.x  - self.prev_x > self.random_movement:
                self.image = self.orig_image


        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

        # Calculate the vector from the ghost to the target center

        if pygame.sprite.collide_rect(self, player.mapSprite):
            if player.has("Ghost Vacuum"):
                # if not self.halted:
                #     WOOSH_SOUND.play()
                # self.halted = True

                if not self.sucked:
                    WOOSH_SOUND.play()

                    self.sucked = True  


        if self.halted:
            self.halted_duration += 1
            if self.halted_duration >= self.max_halted_duration:
                # Reset the halted ghost's movement
                self.halted = False
                self.halted_duration = 0

        if self.sucked:
            # Move the ghost towards the player's center
            player_center = (
                player.mapSprite.rect.x + player.mapSprite.rect.width // 2,
                player.mapSprite.rect.y + player.mapSprite.rect.height // 2
            )
            vector = pygame.Vector2(player_center[0] - self.rect.centerx, player_center[1] - self.rect.centery)
            vector.normalize_ip()
            self.rect.move_ip(self.speed * vector.x, self.speed * vector.y)

            # Shrink the ghost
            scale_factor = 0.50  # You can adjust the scale factor as needed
            new_width = int(self.image.get_width() * scale_factor)
            new_height = int(self.image.get_height() * scale_factor)
            self.image = pygame.transform.scale(self.orig_image, (new_width, new_height))
            self.orig_image = self.image

            

            # Recenter the scaled image
            new_rect = self.image.get_rect(center=self.rect.center)
            self.rect = new_rect

            # Check if the distance between the ghost and player's center is small enough
            margin = 10
            distance = math.dist(self.rect.center, player_center)
            if (distance <= margin) or (self.image.get_width() < 12):
                # Remove the ghost from sprite groups
                player.mapSprite.number_of_sucked_ghosts += 1
                self.kill()
                # player.cash_balance += 100
                # point_text = PointText((player.mapSprite.rect.centerx, player.mapSprite.rect.y),"$100", color=GREEN)
                # textShown.add(point_text)
                # all_sprites.add(point_text)
                # CASH_SOUND.play()
                


        dist_to_player = pygame.math.Vector2(self.rect.x + 25, self.rect.y + 25 ).distance_to((player.mapSprite.rect.x + player.mapSprite.size//2 , player.mapSprite.rect.y + player.mapSprite.size//2))
        dist_to_zuul =  pygame.math.Vector2(self.rect.x + 25, self.rect.y + 25 ).distance_to((self.target_building.rect.x + self.target_building.width//2 , self.target_building.rect.y + self.target_building.height//2))
        
        if player.has("Ghost Bait") and (dist_to_player <= 200 and not dist_to_zuul <= 200):
                target_center = (
                    player.mapSprite.rect.x + player.mapSprite.size // 2,
                    player.mapSprite.rect.y + player.mapSprite.size// 2
                )
                vector = pygame.Vector2(target_center[0] - self.rect.centerx, target_center[1] - self.rect.centery)

                # Normalize the vector (convert it to a unit vector)
                if vector.length() > 0:
                    vector.normalize_ip()

                    # Add a small random movement
                    vector.x += random.uniform(-self.random_movement, self.random_movement)
                    vector.y += random.uniform(-self.random_movement, self.random_movement)

                    # Move the ghost towards the center
                    self.rect.move_ip(self.speed * vector.x, self.speed * vector.y)

  
        elif not self.halted and not self.sucked:
            target_center = (
                self.target_building.rect.x + self.target_building.rect.width // 2,
                self.target_building.rect.y + self.target_building.rect.height // 2
            )
            if (marshmallowed or end_game) and mrStayPuft is not None :
                target_center = (
                mrStayPuft.rect.x + mrStayPuft.rect.width // 2,
                mrStayPuft.rect.y + mrStayPuft.rect.height // 2
            )

            vector = pygame.Vector2(target_center[0] - self.rect.centerx, target_center[1] - self.rect.centery)

            # Normalize the vector (convert it to a unit vector)
            vector.normalize_ip()

            

            # Move the ghost towards the center
            if marshmallowed or end_game:
                self.rect.move_ip(self.speed*5 * vector.x, self.speed*5 * vector.y)
            else:
                # Add a small random movement
                vector.x += random.uniform(-self.random_movement, self.random_movement)
                vector.y += random.uniform(-self.random_movement, self.random_movement)
                self.rect.move_ip(self.speed * vector.x, self.speed * vector.y)

            # Check if the distance between centers is within the margin
            margin = 5
            distance = math.dist(self.rect.center, target_center)
            if distance <= margin:
                # Remove the ghost from sprite groups
                self.kill()
                pk_energy += 50

class Keymaster(pygame.sprite.Sprite):
    def __init__(self, x, y, zuul_building):
        super().__init__()
        self.size = 22 
        
        self.zuul_building = zuul_building

        # self.target_building = random.choice(buildings.sprites())

        # self.target_center = (
        #         self.target_building.rect.x + self.target_building.rect.width // 2,
        #         self.target_building.rect.y + self.target_building.rect.height // 2
        #         )

        self.direction = random.choice(["up","down","left","right"])

        self.speed = 3
        self.random_movement = 0.5  # Adjust the random movement factor
        self.xHalted = False
        self.yHalted = False
        self.halted_duration = 0
        self.max_halted_duration = 500  # Adjust the maximum halted duration (in frames)
        self.sucked = False


        self.image = pygame.transform.scale(KEY_IMAGE, (self.size, self.size))
        self.rect = self.image.get_rect(topleft=(x, y))


        self.prev_x = self.rect.x
        self.prev_y = self.rect.y

    # def random_target(self):
    #     x = random.randint(0, WIDTH)
    #     y = random.randint(0, HEIGHT)
    #     return [x,y]


    def update(self):
        global buildings
        global end_game
        global keymaster
        global gatekeeper


        



        if random.randint(0,200) == 0:
            # self.target_building = random.choice(buildings.sprites())
            self.direction = random.choice(["up","down","left","right"])

        if end_game:
            # self.xHalted = False
            # self.yHalted = False

            self.speed = 5

            if not self.yHalted:

                if not is_obstacle_between(self, "up") and not is_obstacle_between(self, "down"):
                    if self.rect.y < self.zuul_building.rect.bottom: 
                        self.direction = "down"
                        # self.rect.y += self.speed
                    elif self.rect.y > self.zuul_building.rect.bottom + 10: 
                        self.direction = "up"
                        # self.rect.y -= self.speed
                    else: 
                        if self.zuul_building.rect.bottom < self.rect.y < self.zuul_building.rect.bottom + 10:
                            self.yHalted = True
                else:
                    if self.rect.x < self.zuul_building.rect.x: 
                        self.direction = "right"
                        self.rect.x += self.speed
                    elif self.rect.x > self.zuul_building.rect.x + self.zuul_building.rect.width: 
                        self.direction = "left"
                        self.rect.x -= self.speed




            if (self.yHalted) and (not self.xHalted):
                if not is_obstacle_between(self, "left") and not is_obstacle_between(self, "right"):
                    if self.rect.x < self.zuul_building.rect.x + self.zuul_building.rect.width//2.5 : 
                        self.direction = "right"
                        self.rect.x += self.speed
                    elif self.rect.x > self.zuul_building.rect.x + self.zuul_building.rect.width//2.5: 
                        self.direction = "left"
                        self.rect.x -= self.speed
                    else:
                        ...
                    if self.rect.centerx > self.zuul_building.rect.left and self.rect.centerx < self.zuul_building.rect.right: 
                    # if (self.zuul_building.rect.x + self.rect.width*2) < self.rect.x <= (self.zuul_building.rect.x + self.zuul_building.rect.width - self.rect.width*2):
                        if not VOICE_CHANNEL.get_busy():
                            self.xHalted = True
                            if self == gatekeeper:
                                    VOICE_CHANNEL.play(IM_GATEKEEPER_VOICE)
                                    
                            elif self == keymaster:
                                    VOICE_CHANNEL.play(IM_KEYMASTER_VOICE)


 
            if self.xHalted and self.yHalted:
                if self == keymaster: 
                    if gatekeeper.yHalted and gatekeeper.xHalted:
                        if not VOICE_CHANNEL.get_busy():
                            all_sprites.remove(self)
                            all_sprites.remove(gatekeeper)
                            self.kill()
                            gatekeeper.kill()
                            keymaster = None
                            gatekeeper = None                 

  
        else: # NOT END GAME
            self.xHalted = False
            self.yHalted = False


        self.prev_x = self.rect.x
        self.prev_y = self.rect.y


        if not self.yHalted:
            if not is_obstacle_between(self, self.direction):
                    if self.direction == "up" and not self.yHalted:
                        self.rect.y -= self.speed
                        if not is_obstacle_between(self, "left") and not is_obstacle_between(self,"right"):
                            if (random.randint(0,50) == 0) and not end_game: 
                                self.direction = random.choice(["left","right"])

                    elif self.direction == "down" and not self.yHalted:
                        self.rect.y += self.speed
                        if not is_obstacle_between(self, "left") and not is_obstacle_between(self, "right"):
                            if (random.randint(0,50) == 0) and not end_game:
                                self.direction = random.choice(["left","right"])


                    elif self.direction == "left" and not self.xHalted:
                        self.rect.x -= self.speed
                        if not is_obstacle_between(self, "up") and not is_obstacle_between(self, "down"):
                            if (random.randint(0,50) == 0) and not end_game:
                                self.direction = random.choice(["up","down"])


                    elif self.direction == "right" and not self.xHalted:
                        self.rect.x += self.speed
                        if not is_obstacle_between(self, "up") and not is_obstacle_between(self, "down"):
                            if (random.randint(0,50) == 0) and not end_game:
                                self.direction = random.choice(["up","down"])
            else:
                self.direction = random.choice(["up","down","left","right"])


            if self.rect.x <= 0+60:
                self.direction = random.choice(["up","down","right"])

            elif self.rect.x >= WIDTH-self.size-60:
                self.direction = random.choice(["up","down","left"])

            if self.rect.y >= HEIGHT-self.size-60:
                self.direction = random.choice(["up","left", "right"])

            if self.rect.y <= 0+60:
                self.direction = random.choice(["down","left", "right"])


        # Check for collisions with buildings
        collisions = pygame.sprite.spritecollide(self, buildings, False)
        if collisions and not end_game:
            
            self.rect.x = self.prev_x 
            self.rect.y = self.prev_y
            self.direction = random.choice(["up","down","left","right"])

        # Limit player movement to the screen
        self.rect.x = max(0+60, min(WIDTH - self.size - 60, self.rect.x))
        self.rect.y = max(0+60, min(HEIGHT - self.size - 60, self.rect.y))



class Gatekeeper(Keymaster):
    def __init__(self, x, y, zuul_building):
        super().__init__(x, y, zuul_building)
        self.size = 20
        self.image = pygame.transform.scale(GATE_IMAGE, (self.size, self.size))


    def update(self):
        super().update()


# Trap class
class Trap(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()

        self.closed_image = equipment_images.get('Ghost Trap')
        self.open_image = equipment_images.get('Open Trap')
        self.full_image = equipment_images.get('*Full Trap*')
        self.image = self.closed_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.opened = False
        self.light_size = 0
        self.full = False

    def open_trap(self):
        self.opened = True
        
        
        TRAP_CHANNEL.stop()
        TRAP_CHANNEL.play(TRAP_CLOSE_SOUND)

    def close_trap(self):
        self.opened = False
        
        
        # self.light_size = 0
        # TRAP_CHANNEL.stop()
        # TRAP_CHANNEL.play(TRAP_CLOSE_SOUND)

    def toggle_trap(self):
        if self.opened:
            self.close_trap()
        else:
            self.open_trap()


    def update(self):
        global ghosts_at_building
        global ghostbusters_at_building
        global ghosts_captured

        if self.opened:
            self.image = self.open_image
            # Expand the light column
            self.light_size += 5
            self.light_size = min(self.light_size, self.rect.y - 50)

            # Check for collisions with ghosts in the light column

            traplight = pygame.Rect(self.rect.centerx - 20, self.rect.centery - self.light_size, 45, self.light_size)
            


            ghosts_here = ghosts_at_building.sprites()
            for ghost in ghosts_here:
                if ghost.rect.colliderect(traplight):
                    # print("TRAP!!")
                    ghost.trapped = True
                    ghost.trap = self
                    ghosts_captured.add(ghost)
                    # self.close_trap()
                    self.full = True
            

            if self.light_size >= self.rect.y - 50:
                self.close_trap()


        # not open
        elif self.light_size > 0:
            self.image = self.open_image
            # Shrink the light column
            self.light_size -= 5
            self.light_size = max(self.light_size, 0)

        elif self.full: 
            self.image = self.full_image

        else: 
            self.image = self.closed_image



        # self.draw_light_column()

    def draw_light_column(self):
        if self.light_size > 0:
            # Draw the light column beam
            current_color = random.choice([TRANS_WHITE, TRANS_WHITE, TRANS_YELLOW])
            pygame.draw.rect(screen, current_color, (self.rect.x, self.rect.centery - self.light_size, self.image.get_width(), self.light_size))

            # Fixed size for ellipses
            ellipse_width = self.image.get_width() + 6 # Fixed width in pixels
            ellipse_height = ellipse_width - ellipse_width // 4 # Fixed height in pixels
            ellipse_color = random.choice([RED, RED, DARK_RED, ORANGE, YELLOW, WHITE, LIGHT_BLUE])

            # Offset for left and right ellipses relative to beam center
            offset_x = int(self.image.get_width() * 0.1)  # Horizontal offset
            ellipse_y = self.rect.centery - self.light_size + ellipse_height // 3  # Always at the top of the light beam

            # Left ellipse rectangle
            left_ellipse_rect = pygame.Rect(
                self.rect.centerx - offset_x - ellipse_width // 2,
                ellipse_y - ellipse_height // 2,
                ellipse_width,
                ellipse_height
            )

            # Right ellipse rectangle
            right_ellipse_rect = pygame.Rect(
                self.rect.centerx + offset_x - ellipse_width // 2,
                ellipse_y - ellipse_height // 2,
                ellipse_width,
                ellipse_height
            )

            # Draw fixed-size ellipses
            pygame.draw.ellipse(screen, ellipse_color, left_ellipse_rect, PROTON_BEAM_CIRCLE_LINE_WIDTH)
            pygame.draw.ellipse(screen, ellipse_color, right_ellipse_rect, PROTON_BEAM_CIRCLE_LINE_WIDTH)

            # Set buster completion status
            for buster in ghostbusters_at_building.sprites():
                buster.complete = True


            



# Ghostbuster class
class Ghostbuster(pygame.sprite.Sprite):
    def __init__(self, name, color=WHITE, x=50, y=50):
        super().__init__()
        global uniform_index
        global uniform_choices
        self.name = name
        self.points = 8 # plus the 4 that must be spent to bring each trait to a minimum of 1. = 12 traits point
        self.traits = {
            'Brains': 1,
            'Muscle': 1,
            'Moves': 1,
            'Cool': 1
        }

        self.experience = 0 # 0
        self.level = 1
        self.levelPoints = 0 # 0

        self.color = color

        self.goal = random.choice(GHOSTBUSTER_GOALS)
        self.origin = random.choice(GHOSTBUSTER_ORIGINS)
        self.hiring_cost = 200
        self.assign_traits_randomly()

        self.size = 50

        self.image_index = 0
        image0 = pygame.transform.scale(BUSTER_MAN_IMAGE1, (self.size, self.size))  # Adjust size as needed
        image1 = pygame.transform.scale(BUSTER_MAN_IMAGE2, (self.size, self.size))  # Adjust size as needed

        
        
        uniform_color = uniform_choices[uniform_index]
        self.hair_color = random.choices(hair_choices,weights=hair_weight)
        uniform_index = (uniform_index +1 ) % len(uniform_choices)
        if uniform_index == 0:
            random.shuffle(uniform_choices)
        
            
        
        image0 = spritePixelColorChange(image0, new=uniform_color)
        image1 = spritePixelColorChange(image1, new=uniform_color)

        # print(hair_color)

        image0 = spritePixelColorChange(image0, old=ABS_BLUE, new=self.hair_color[0])
        image1 = spritePixelColorChange(image1, old=ABS_BLUE, new=self.hair_color[0])


        self.images = [image0, image1]
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 5  # Adjust speed as needed

        self.animation_timer = pygame.time.get_ticks()

        self.last_left = True

        self.proton_tip = 0 

        # Scale the trap image if needed
        self.trap_image = equipment_images.get('Ghost Trap')  # Adjust size as needed
        self.full_trap_image = equipment_images.get('*Full Trap*')  # Adjust size as needed

        self.has_trap = False  # Initially holding a trap
        self.has_full_trap = False  # holding a full trap
        self.proton_pack_on = False
        self.line_start = (self.rect.x, self.rect.y)
        self.line_end = (self.rect.x, self.rect.y)
        self.ghost_target = None
        self.slimed = False
        self.proton_death_timer = 0
        self.crossing_steams = False

        self.stream_angle = 22

        self.ascendingStairs = False
        self.climbed_height = 0
        self.complete = False

        self.evading_stay_puft = False

    

    def change_worn_outfit(self):
        FORK_SHORT_SOUND.play()
        """Set the uniform color based on the global uniform_index and uniform_choices."""
        global uniform_index, uniform_choices
        # Select the current uniform color based on uniform_index
        uniform_color = uniform_choices[uniform_index]
        # Update uniform_index for the next cycle, wrap around if needed
        uniform_index = (uniform_index + 1) % len(uniform_choices)
        if uniform_index == 0:
            random.shuffle(uniform_choices)

        # print(uniform_color)
        
        # Apply the color to images
        image0 = pygame.transform.scale(BUSTER_MAN_IMAGE1, (self.size, self.size))  # Adjust size as needed
        image1 = pygame.transform.scale(BUSTER_MAN_IMAGE2, (self.size, self.size))  # Adjust size as needed

        image0 = spritePixelColorChange(image0, new=uniform_color)
        image1 = spritePixelColorChange(image1, new=uniform_color)

        image0 = spritePixelColorChange(image0, old=ABS_BLUE, new=self.hair_color[0])
        image1 = spritePixelColorChange(image1, old=ABS_BLUE, new=self.hair_color[0])
        
        self.images = [image0, image1]
        self.image = self.images[self.image_index]





    def set_for_building(self, color, x, y, has_trap=False):
        self.color = color
        self.rect.x = x
        self.rect.y = y
        self.has_trap = has_trap
        self.has_full_trap = False
        self.last_left = True
        self.stream_angle = 22
        self.animation_timer = pygame.time.get_ticks()
        self.complete = False
        self.evading_stay_puft = False
        self.ascendingStairs = False
        self.proton_death_timer = 0
        self.ghost_target = None

    def set_for_stairs(self, color, x, y, has_trap=False):
        self.color = color
        self.rect.x = x
        self.rect.y = y
        self.has_trap = has_trap
        self.has_full_trap = False
        self.last_left = True
        self.stream_angle = 22
        self.animation_timer = pygame.time.get_ticks()
        self.climbed_height = 0
        self.ascendingStairs = True
        self.evading_stay_puft = False
        self.complete = False
        self.proton_death_timer = 0
        self.ghost_target = None

    def gain_experience(self, amount):
        self.experience += amount
        # Check if the Ghostbuster has earned enough experience to level up
        if self.experience >= self.level * 30:
            self.level += 1
            self.levelPoints += 1
            # You can also grant additional attributes or bonuses here

    def display_name(self, screen):
        global selected_ghostbuster
        textcolor = SKY_BLUE
        if self == selected_ghostbuster: 
            textcolor = GREEN
            text = under_line_FONT18.render(self.name, True, textcolor)
        else:
            text = FONT18.render(self.name, True, textcolor)
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.bottom + 10))  # Adjust vertical offset as needed
        screen.blit(text, text_rect)

    def draw_slime_circle(self, screen):
        if self.slimed:
            # Draw the top half of a circle around the sprite
            pygame.draw.arc(screen, GREEN, (self.rect.x, self.rect.y, self.size, self.size), 0, math.pi, 4)


    def drop_trap(self):
        # Drop the trap
        if self.has_trap:
            if self.last_left:
                trap = Trap(self.trap_image, self.rect.x - self.trap_image.get_width()*0.75, self.rect.y + self.image.get_height() - self.trap_image.get_height())
                self.has_trap = False
                return trap
                
            else:
                trap = Trap(self.trap_image, self.rect.x + self.image.get_width()*0.75, self.rect.y + self.image.get_height() - self.trap_image.get_height())
                self.has_trap = False
                return trap
                

        if self.has_full_trap: 
            if self.last_left:
                trap = Trap(self.full_trap_image, self.rect.x - self.trap_image.get_width()*0.75, self.rect.y + self.image.get_height() - self.full_trap_image.get_height())
                trap.full = True
                self.has_trap = False
                return trap
                
            else:
                trap = Trap(self.full_trap_image, self.rect.x + self.image.get_width()*0.75, self.rect.y + self.image.get_height() - self.full_trap_image.get_height())
                trap.full = True
                self.has_trap = False
                return trap
                


    def draw_Proton_Stream(self, current_color=None):
        global floors_of_building
        global floor_gap
        global ghosts_at_building
        global ghostbusters_at_building
        global left_most_buster
        # global leavePackSoundOn

        if self.proton_pack_on:

            if self.last_left:
                self.line_start = (self.rect.x, self.rect.y)
                # Set the desired angle in degrees
                desired_angle_degrees = 90 + self.stream_angle

            else:
                self.line_start = (self.rect.x + self.rect.width, self.rect.y)
                # Set the desired angle in degrees
                desired_angle_degrees = 90 - self.stream_angle

             #-------

            current_color = random.choice([RED, RED, DARK_RED, ORANGE, YELLOW, WHITE])
            if self.crossing_steams: current_color=WHITE
                # Draw a red line at a 45-degree angle from the Ghostbuster
            line_length = 600
            # if self.ascendingStairs:
            #     line_length = 200 - 20 - self.image.get_height()
                # line_start = (self.rect.x, self.rect.y)

                # Set the desired angle in degrees
                # desired_angle_degrees = 90 + 22

            # Convert the angle to radians
            angle_radians = math.radians(desired_angle_degrees)


            # Calculate the line_end based on the angle
            if self.ghost_target is None:
                self.line_end = (self.line_start[0] + int(line_length * math.cos(angle_radians)),
                            self.line_start[1] - int(line_length * math.sin(angle_radians)))

            if self.ghost_target is not None:
                self.ghost_target.take_damage(damage=1)
                if self.last_left:
                    self.line_end = [self.ghost_target.rect.right,self.ghost_target.rect.centery]
                    if self.line_end[0] >= self.rect.center[0]:
                        # GHOST GOES OVER OUR HEAD !
                        self.ghost_target = None 
                        self.proton_pack_on = False
                        # leavePackSoundOn = False
                        # for buster in ghostbusters_at_building.sprites():
                        #     if buster.proton_pack_on:
                        #         leavePackSoundOn = True
                        # buster.ghost_target = None
                        # if not leavePackSoundOn:
                        #     PROTON_PACK_CHANNEL.stop()
                else:
                    self.line_end = [self.ghost_target.rect.left,self.ghost_target.rect.centery]
                    if self.line_end[0] <= self.rect.center[0]:
                        # GHOST GOES OVER OUR HEAD !
                        self.ghost_target = None 
                        self.proton_pack_on = False
                        # leavePackSoundOn = False
                        # for buster in ghostbusters_at_building.sprites():
                        #     if buster.proton_pack_on:
                        #         leavePackSoundOn = True
                        # buster.ghost_target = None
                        # if not leavePackSoundOn:
                        #     PROTON_PACK_CHANNEL.stop()




            if self.ascendingStairs:


                # Check for collision with FloorLevelSprite
                for floor_in_building in floors_of_building.sprites():  # Assuming floors_of_building contains all FloorLevelSprite objects
                    if line_intersects_sprite(self.line_start, self.line_end, floor_in_building.rect):
                        # floor_in_building.image.fill(RED)
                        # Adjust line_end to the collision point
                        collision_point, line_length = find_collision_point(self.line_start, self.line_end, floor_in_building.rect)
                        # line_end = collision_point
                        break  # Exit loop if collision detected
                    else:
                        # floor_in_building.image.fill(floor_in_building.color)
                        ...

                # line_length = min(line_length, floor_gap-self.image.get_height())

                line_length = min(line_length, floor_gap*2)         

                self.line_end = (self.line_start[0] + int(line_length * math.cos(angle_radians)),
                 self.line_start[1] - int(line_length * math.sin(angle_radians)))

            else:
                ...
                # for ghost in ghosts_at_building.sprites():
                #     if not ghost.inside:
                #         if line_intersects_sprite(self.line_start, self.line_end, ghost.rect):
                #             self.line_end = ghost.rect.center # MOVE PROTON BEAM TO STRIKE THE GHOST


            # print(line_length)
            pygame.draw.line(screen, current_color, self.line_start, self.line_end, 4)

            if self.ascendingStairs:
                # Iterate over ghosts and check for collision with the line
                for ghost in ghosts_at_building.sprites():
                    if ghost.inside:
                        if line_intersects_sprite(self.line_start, self.line_end, ghost.rect):
                            # Apply appropriate action (e.g., damage the ghost)
                            ghost.take_damage(damage=1)  # Example method to apply damage to the ghost
            else:

                for ghost in ghosts_at_building.sprites():
                    if not ghost.inside:
                        if line_intersects_sprite(self.line_start, self.line_end, ghost.rect):
                            # Apply appropriate action (e.g., damage the ghost)
                            ghost.take_damage(damage=1)  # Example method to apply damage to the ghost
                            self.ghost_target = ghost
                        else:
                            ...
                            # self.ghost_target = None

            # Draw the sin-wave along the line
            num_points = int(line_length // 6) 
                
            for i in range(num_points):
                if num_points - 1 != 0:
                    t = i / (num_points - 1)  # t ranges from 0 to 1
                    amp = random.randint(2, 6)
                    particle_color = random.choice([TRUE_BLUE, GREEN, DARK_RED, WHITE])
                    x = int(self.line_start[0] + t * (self.line_end[0] - self.line_start[0]))
                    y = int(self.line_start[1] + t * (self.line_end[1] - self.line_start[1]) + 50 * math.sin(t * amp * math.pi))  # Adjust the amplitude as needed
                    pygame.draw.circle(screen, particle_color, (x, y), 2)

            self.proton_tip = self.line_end[0]
            # if not PROTON_PACK_CHANNEL.get_busy():
            #     PROTON_PACK_CHANNEL.play(PROTON_FIRE_SOUND)





    def update(self, keys):
        global selected_ghostbuster
        global ghosts_at_building
        global player
        global floors_of_building
        global goo_in_building
        global ghostbusters_at_building
        global traps_at_building

        now = pygame.time.get_ticks()
        yA = self.rect.y

        if self.slimed:
            # self.image = pygame.transform.scale(self.images[self.image_index], (self.size, self.size//2.5))  # Adjust size as needed
            self.image = pygame.transform.scale(BUSTER_MAN_IMAGE1, (self.size, self.size))
            # self.image = pygame.transform.flip(self.image, True, True)  # Adjust size as needed
            self.image = pygame.transform.rotate(self.image, 270)  # Adjust size as needed
         
        else:

            # WALKING ANIMATION -------
            if now - self.animation_timer >= 150: # Check if half a second has passed
                if self == selected_ghostbuster:
                    # rotate to the next image
                    self.image_index = (self.image_index + 1) % len(self.images)

                elif self.ascendingStairs:
                    if self.complete:
                        self.image_index = (self.image_index + 1) % len(self.images)
                    else:
                        # stay standing still
                        self.image_index = 0

                elif self.evading_stay_puft:
                    # stay standing still
                        self.image_index = 0

                else:
                    trapped = True  
                    for ghost in ghosts_at_building.sprites():
                        if not ghost.trapped:
                            trapped = False
                        
                    if trapped:
                        self.image_index = (self.image_index + 1) % len(self.images)
                    else:
                        # stay standing still
                        self.image_index = 0
                self.animation_timer = now  # Reset the timer

            
            # MOVEMENT -----------------------------------
            trap_open = False
            for trap in traps_at_building:
                if trap.opened: trap_open = True
                if trap.light_size > 0: trap_open = True

            if self == selected_ghostbuster and not self.complete:# and not trap_open:
                # print(self.rect.y)
                if keys[pygame.K_LEFT]:
                    self.rect.x -= self.speed

                    if self.proton_pack_on and self.ghost_target is not None:
                        if self.ghost_target.pk_health <= self.ghost_target.full_pk_health//3:
                            self.ghost_target.rect.x -= self.speed
                    if not self.proton_pack_on:
                        self.last_left = True

                elif keys[pygame.K_RIGHT]:
                    self.rect.x += self.speed

                    if self.proton_pack_on and self.ghost_target is not None:
                        if self.ghost_target.pk_health <= self.ghost_target.full_pk_health//3:
                            self.ghost_target.rect.x += self.speed

                    if not self.proton_pack_on:
                        self.last_left = False


                if keys[pygame.K_UP]:

                    if self.ascendingStairs:
                        floor_here = pygame.sprite.spritecollide(self,floors_of_building,False)
                        if floor_here:
                            self.rect.y -= self.speed

                    else:
                        self.rect.y -= self.speed

                        if self.proton_pack_on and self.ghost_target is not None:
                            if self.ghost_target.pk_health <= self.ghost_target.full_pk_health//3:
                                self.ghost_target.rect.y -= self.speed




                elif keys[pygame.K_DOWN]:

                    if self.ascendingStairs:
                        ...

                    else:
                        self.rect.y += self.speed

                        if self.proton_pack_on and self.ghost_target is not None:
                            if self.ghost_target.pk_health <= self.ghost_target.full_pk_health//3:
                                self.ghost_target.rect.y += self.speed

                if keys[pygame.K_KP_PLUS]:
                    self.stream_angle += 1
                    if self.stream_angle > 66: self.stream_angle = 66
                    # print(self.stream_angle)

                elif keys[pygame.K_KP_MINUS]:
                    self.stream_angle -= 1
                    if self.stream_angle < 0: self.stream_angle = 0
                    # print(self.stream_angle)


            if self.last_left: # FACING LEFT
                self.image = pygame.transform.scale(self.images[self.image_index], (self.size, self.size))  # Adjust size as needed
                # if self.has_trap:
                #     screen.blit(self.trap_image, (self.rect.x - self.trap_image.get_width(), self.rect.y + self.size//3))

            else: # FACING RIGHT
                self.image = pygame.transform.scale(self.images[self.image_index], (self.size, self.size))  # Adjust size as needed
                self.image = pygame.transform.flip(self.image, True, False)  # Adjust size as needed
                # if self.has_trap:
                #     screen.blit(self.trap_image, (self.rect.x + self.image.get_width(), self.rect.y + self.size//3))

                

            if self.ascendingStairs:
                # print(self.rect.x,self.climbed_height)
                self.rect.x = max(0 + self.trap_image.get_width(), min(WIDTH - self.rect.width - self.trap_image.get_width(), self.rect.x))
                self.rect.y += self.speed # GRAVITY !!!!


                floor_here = pygame.sprite.spritecollide(self,floors_of_building,False)
                if floor_here:
                    ...
                    if self.rect.y < floor_here[0].rect.y:
                        self.rect.y = floor_here[0].rect.y - self.image.get_height() - 1
                    else:
                        # self.rect.y = floor_here[0].rect.y + floor_here[0].image.get_height() +1

                        ...
                else:
                    ...


                if pygame.sprite.spritecollide(self,ghosts_at_building,False):
                    self.getSlimed()


                if pygame.sprite.spritecollide(self,goo_in_building,False):
                    self.getSlimed()
                    


            else:
                if not self.complete:
                    self.rect.x = max(0 + self.trap_image.get_width(), min(WIDTH - self.rect.width - self.trap_image.get_width(), self.rect.x))
                    
                    if self.evading_stay_puft:
                        # Limit movement within the lower third of the screen
                        self.rect.y = max(665, min(HEIGHT - 110, self.rect.y))


                    else:
                        # Limit movement within the lower third of the screen
                        self.rect.y = max((HEIGHT-(HEIGHT//3)), min(HEIGHT - 110, self.rect.y))

        yB = self.rect.y

        if yB > yA:
            self.climbed_height -= abs(yB-yA)
        if yB < yA:
            self.climbed_height += abs(yB-yA)

        if self.proton_pack_on:
            # self.proton_death_timer = 0
            self.crossing_steams = False
            for other_buster in ghostbusters_at_building:
                if self is not other_buster:
                    if other_buster.proton_pack_on:
                        intersect_point = line_intersection(self.line_start, self.line_end, other_buster.line_start, other_buster.line_end)
                        if intersect_point is False:
                            # print("NO INTERSECT")
                            self.proton_death_timer = 0
                            other_buster.proton_death_timer = 0 
                            self.crossing_steams = False
                            other_buster.crossing_steams = False
                        else:
                            if (self.ghost_target != other_buster.ghost_target) or (self.ghost_target == None):
                                self.proton_death_timer += 1
                                if self.proton_death_timer > MIN_BEFORE_STREAM_CROSS:
                                    if not SIREN.get_busy():
                                        SIREN.play(OVERHEAT_BEEP)
                                    self.crossing_steams = True
                                    self.proton_death_timer += 1
                                    if self.proton_death_timer > CROSS_STEAMS_DEATH_TIMER:
                                        MUSIC.pause()
                                        PKE_CHANNEL.stop()
                                        self.getSlimed()
                                        other_buster.getSlimed(voice=VOICE_LAUGH)
                                        # PROTON_PACK_CHANNEL.stop()
                                        
                    else:
                        self.proton_death_timer = 0
                        other_buster.proton_death_timer = 0 
                        self.crossing_steams = False
                        other_buster.crossing_steams = False
        else:# PACK OFF
            self.proton_death_timer = 0
            self.crossing_steams = False
            self.ghost_target = None

                                


    def getSlimed(self, voice=VOICE_SLIMED):
        global ghostbusters_at_building
        global traps_at_building
        # global leavePackSoundOn
        
        if not self.slimed:

            if self.has_trap:
                trap = selected_ghostbuster.drop_trap()
                self.has_trap = False
                self.has_full_trap = False
                traps_at_building.add(trap)


            VOICE_CHANNEL.play(voice)
            self.slimed = True
            self.rect.y = self.rect.y + self.image.get_height()//2
            if self.last_left:
                self.rect.x = self.rect.x + self.image.get_width()//2
            else:
                self.rect.x = self.rect.x - self.image.get_width()//2
            self.experience -= random.randint(0,5) + 5
            self.proton_pack_on = False
            # leavePackSoundOn = False
            # for buster in ghostbusters_at_building.sprites():
            #     if buster.proton_pack_on and buster is not self:
            #         leavePackSoundOn = True
            # buster.ghost_target = None
            # if not leavePackSoundOn:
            #     PROTON_PACK_CHANNEL.stop()

    def assign_traits_randomly(self):

        elite = random.randint(0,120)
        if elite <= 20:
            self.points += 1
            self.hiring_cost += 50
        if elite <= 10:
            self.points += 1
            self.hiring_cost += 50
        if elite <= 5:
            self.points += 1
            self.hiring_cost += 50
        if elite <= 1:
            self.points += 1
            self.hiring_cost += 50

        if elite > 100:
            self.points -= 1
            self.hiring_cost -= 25

        if elite > 110:
            self.points -= 1
            self.hiring_cost -= 25

        trait_list = list(self.traits.keys())
        while self.points > 0:
            trait = random.choice(trait_list)
            points_to_assign = random.randint(1, min(5, self.points))
            # Ensure the trait does not go above 5
            if self.traits[trait] + points_to_assign <= 7:
                self.traits[trait] += points_to_assign
                self.points -= points_to_assign

                

    def display_traits(self):
        returnText = f"{self.name}:".ljust(14)
        for trait, score in self.traits.items():
            returnText += f"{score}".rjust(8)  # Adjust the width as needed

        return returnText

def line_intersects_sprite(start, end, sprite_rect):
    # Check if line defined by start and end intersects with sprite_rect
    line_segment = pygame.Rect(start[0], start[1], end[0] - start[0], end[1] - start[1])
    return line_segment.colliderect(sprite_rect)


def find_collision_point(start, end, sprite_rect):
    # Find the collision point between the line and the sprite_rect
    line_vector = pygame.Vector2(end[0] - start[0], end[1] - start[1])
    sprite_vector = pygame.Vector2(sprite_rect.centerx - start[0], sprite_rect.centery - start[1])

    # Check if the sprite_rect intersects with the line
    if sprite_rect.colliderect(pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))):
        collision_point = sprite_rect.center
    else:
        projection_length = sprite_vector.dot(line_vector.normalize())  # Length of the projection of sprite_vector onto line_vector
        collision_point = start + line_vector.normalize() * projection_length  # Intersection point of the line and sprite_rect

    collision_distance = pygame.math.Vector2(collision_point[0] - start[0], collision_point[1] - start[1]).length()
    line_length = min(collision_distance, line_vector.length())

    return collision_point, line_length


def draw_bars(screen, game_mode):
    """
    Draw 7 horizontal bars in a row, highlighting one based on the game_mode (1-7).
    :param screen: The pygame surface to draw on.
    :param game_mode: The 1-based index (1-7) of the bar to highlight.
    """
    global starting
    if starting: 
        BAR_COUNT = 5
    else:
        BAR_COUNT = 7
    total_width = BAR_COUNT * BAR_WIDTH + (BAR_COUNT - 1) * BAR_SPACING
    start_x = (WIDTH - total_width) // 2  # Center the bars horizontally
    y = TOP_OFFSET  # Vertical position for all bars

    for i in range(BAR_COUNT):
        # Calculate the x position for each bar
        x = start_x + i * (BAR_WIDTH + BAR_SPACING)
        
        # Determine the color based on the game_mode
        color = BRIGHT_PURPLE if (i + 1) == game_mode else DARK_PURPLE  # Convert game_mode to 0-based
        
        # Draw the rectangle
        pygame.draw.rect(screen, color, (x, y, BAR_WIDTH, BAR_HEIGHT))



def spawn_fresh_base():
    player.base.append({"name": "Office", "cost": 200, 'unique': False, 'color': GREY})
    player.base.append({"name": "Auto Mechanic Shop", "cost": 200, 'unique': True, 'color': GREY})
    player.base.append({"name": "Vehicle Garage", "cost": 200, 'unique': True, 'color': WHITE})
    player.base.append({"name": "Protection Grid / Containment System", "cost": 2000, 'unique': True, 'color': RED})

def draw_pk_meter(reading=None, alertLevel="none", silent=False):
    global pk_energy
    global marshmallowed

    if player.has("PK Energy Detector"):

        fontColor = WHITE
        pk_meter_color = BLUE

        if marshmallowed:
            alertLevel = "high"

        if not silent:
            # PK READING SOUNDS:
            if alertLevel == "high":
                pk_meter_color = DARK_RED
                if PKE_CHANNEL.get_sound() != PK_HIGH_SOUND:
                    PKE_CHANNEL.play(PK_HIGH_SOUND)

            elif alertLevel == "med":
                pk_meter_color = DARK_YELLOW
                if PKE_CHANNEL.get_sound() != PK_MED1_SOUND:
                    PKE_CHANNEL.play(PK_MED1_SOUND)

            elif alertLevel == "low":
                pk_meter_color = DARK_GREEN
                if PKE_CHANNEL.get_sound() != PK_LOW_SOUND:
                    PKE_CHANNEL.play(PK_LOW_SOUND)

            elif alertLevel == "very low":
                pk_meter_color = DARK_GREEN
                PKE_CHANNEL.stop()

            elif alertLevel == "none":
                pk_meter_color = BLUE
                PKE_CHANNEL.stop()

            else:
                PKE_CHANNEL.stop()
        else:
            PKE_CHANNEL.stop()

        # Display PK energy reading in the bottom right corner with a box background
        pk_energy_text = ""
        if reading is None:
            pk_energy_text = f"City's PK Energy: {pk_energy:04d}"
        else:
            pk_energy_text = f"Local PK Energy: {reading:04d}"

        pk_energy_rendered = FONT24.render(pk_energy_text, True, fontColor)

        # Draw a box background for the PK energy text
        box_width = 200 # pk_energy_rendered.get_width() + 20

        box_height = pk_energy_rendered.get_height() + 10
        box_x = WIDTH - box_width - 10
        box_y = HEIGHT - box_height - 10
        pygame.draw.rect(screen, pk_meter_color, (box_x, box_y, box_width, box_height))  # Adjust the color based on alert level
        screen.blit(pk_energy_rendered, (box_x + 10, box_y + 5))  # Adjust position as needed

        # Draw the three 'little lights' above the box background
        light_radius = 8  # Radius for the 'little lights'
        light_spacing = 20  # Spacing between the lights
        light_y = box_y - 20  # Position just above the box
        # Calculate positions for the lights
        green_light_pos = (WIDTH + light_radius - light_spacing*3, light_y)
        yellow_light_pos = (WIDTH + light_radius - light_spacing*2, light_y)
        red_light_pos = (WIDTH + light_radius - light_spacing, light_y)

        # Draw the lights based on the alert level
        if alertLevel == "low" or alertLevel == "very low":
            pygame.draw.circle(screen, GREEN, green_light_pos, light_radius)
            pygame.draw.circle(screen, YELLOW, yellow_light_pos, light_radius, 1)
            pygame.draw.circle(screen, RED, red_light_pos, light_radius, 1)

        elif alertLevel == "med":
            pygame.draw.circle(screen, GREEN, green_light_pos, light_radius)
            pygame.draw.circle(screen, YELLOW, yellow_light_pos, light_radius)
            pygame.draw.circle(screen, RED, red_light_pos, light_radius,1)


        elif alertLevel == "high":
            pygame.draw.circle(screen, GREEN, green_light_pos, light_radius)
            pygame.draw.circle(screen, YELLOW, yellow_light_pos, light_radius)
            pygame.draw.circle(screen, RED, red_light_pos, light_radius)

        else:
            pygame.draw.circle(screen, GREEN, green_light_pos, light_radius,1)
            pygame.draw.circle(screen, YELLOW, yellow_light_pos, light_radius, 1)
            pygame.draw.circle(screen, RED, red_light_pos, light_radius, 1)


        





def draw_credits():
    global player
    # Display player credits at the top
    player_credits_text = FONT24.render(f'Credit: $ {player.cash_balance:04}', True, WHITE)
    player_credits_box_width = 150
    player_credits_box_height = player_credits_text.get_height() * 2
    player_credits_box_x = WIDTH - player_credits_box_width - 10
    player_credits_box_y = 10
    pygame.draw.rect(screen, BLUE, (player_credits_box_x, player_credits_box_y, player_credits_box_width, player_credits_box_height))
    screen.blit(player_credits_text, (player_credits_box_x + 10, player_credits_box_y + 10))

def draw_trap_warning():
    global player
    global trap_warning_timer
    global trap_warning_interval
    global trap_show_warning
    global marshmallowed
    # Display warning if out of traps
    trapCount = 0
    for item in player.vehicle_items:
        if item['name'] == "Ghost Trap":
            trapCount += 1

    warning_text_rendered = None
    # Calculate position to center the text at the bottom of the screen
    warning_x = 0
    warning_y = 0


    if marshmallowed:
        ... #HERE I WANT TO ADD TEXT THAT WILL FLASH
        # Update flashing warning
        trap_warning_timer += 1
        if trap_warning_timer % trap_warning_interval == 0:
            trap_show_warning = not trap_show_warning

        # Render warning text
        warning_text_rendered = FONT36.render(" - MARSHMALLOW ALERT! - ", True, WHITE)

        # Calculate position to center the text at the bottom of the screen
        warning_x = (WIDTH - warning_text_rendered.get_width()) // 2
        warning_y = HEIGHT - warning_text_rendered.get_height() - 10


       

    elif trapCount == 0:
        ... #HERE I WANT TO ADD TEXT THAT WILL FLASH
        # Update flashing warning
        trap_warning_timer += 1
        if trap_warning_timer % trap_warning_interval == 0:
            trap_show_warning = not trap_show_warning

        # Render warning text
        warning_text_rendered = FONT36.render("OUT OF TRAPS !    RETURN TO HQ !", True, RED)

        # Calculate position to center the text at the bottom of the screen
        warning_x = (WIDTH - warning_text_rendered.get_width()) // 2
        warning_y = HEIGHT - warning_text_rendered.get_height() - 10



    elif player.proton_charge <= MINIMUM_PROTON_CHARGE_FOR_MISSION:
        ... #HERE I WANT TO ADD TEXT THAT WILL FLASH
        # Update flashing warning
        trap_warning_timer += 1
        if trap_warning_timer % trap_warning_interval == 0:
            trap_show_warning = not trap_show_warning

        # Render warning text
        warning_text_rendered = FONT36.render("PROTON PACK POWER LOW !    RETURN TO HQ !", True, RED)

        # Calculate position to center the text at the bottom of the screen
        warning_x = (WIDTH - warning_text_rendered.get_width()) // 2
        warning_y = HEIGHT - warning_text_rendered.get_height() - 10




    elif player.num_available_ghostbusters() == 0:
        ... #HERE I WANT TO ADD TEXT THAT WILL FLASH
        # Update flashing warning
        trap_warning_timer += 1
        if trap_warning_timer % trap_warning_interval == 0:
            trap_show_warning = not trap_show_warning

        # Render warning text
        warning_text_rendered = FONT36.render("ALL BUSTERS OUT OF ACTION !    RETURN TO HQ !", True, RED)

        # Calculate position to center the text at the bottom of the screen
        warning_x = (WIDTH - warning_text_rendered.get_width()) // 2
        warning_y = HEIGHT - warning_text_rendered.get_height() - 10

    else:
        levelUp_Yes = False
        for buster in player.roster:
            if buster.levelPoints > 0:
                levelUp_Yes = True
            ... #HERE I WANT TO ADD TEXT THAT WILL FLASH

        if levelUp_Yes:
            # Update flashing warning
            trap_warning_timer += 1
            if trap_warning_timer % trap_warning_interval == 0:
                trap_show_warning = not trap_show_warning

            # Render warning text
            warning_text_rendered = FONT36.render("LEVELED UP !      RETURN TO HQ !", True, GREEN)

            # Calculate position to center the text at the bottom of the screen
            warning_x = (WIDTH - warning_text_rendered.get_width()) // 2
            warning_y = HEIGHT - warning_text_rendered.get_height() - 10

    # Blit the warning text onto the screen
    if warning_text_rendered is not None and trap_show_warning:
        screen.blit(warning_text_rendered, (warning_x, warning_y))





# Inside your game loop or update function
def draw_fuel_meter():
    global player

    # Fuel meter settings
    
    meter_width = 20
    meter_height = 200
    meter_x = 10
    meter_y = HEIGHT - 10 - meter_height
    border_color = WHITE
    meter_color = DARK_YELLOW

    fuel_percentage = (player.fuel / player.vehicle['tank_size']) 

    # Draw the border of the fuel meter
    pygame.draw.rect(screen, border_color, (meter_x, meter_y, meter_width, meter_height), 2)

    # Calculate the height of the filled portion based on the fuel percentage
    filled_height = int(meter_height * fuel_percentage)

    # Draw the filled portion of the fuel meter
    pygame.draw.rect(screen, meter_color, (meter_x, meter_y + meter_height - filled_height, meter_width, filled_height))

    # Display the fuel information
    player_fuel_text = FONT24.render(f'Fuel: {round(fuel_percentage*100)}%', True, WHITE)

    player_fuel_box_width = player_fuel_text.get_width() + 20 
    player_fuel_box_height = player_fuel_text.get_height() + 10
    player_fuel_box_x = meter_x + meter_width + 10
    player_fuel_box_y = HEIGHT - player_fuel_box_height - 10
    pygame.draw.rect(screen, BLUE, (player_fuel_box_x, player_fuel_box_y, player_fuel_box_width, player_fuel_box_height))
    
    screen.blit(player_fuel_text, (player_fuel_box_x +10, player_fuel_box_y + 5))

# Inside your game loop or update function
def draw_proton_charge_meter(color=DARK_RED):
    global player

    # Proton charge meter settings
    meter_width = 20
    meter_height = 200
    meter_x = 10
    meter_y = 10
    border_color = WHITE
    meter_color = color  # Choose an appropriate color for the proton charge meter

    proton_percentage = (player.proton_charge / player.max_proton_charge) 

    # Draw the border of the proton charge meter
    pygame.draw.rect(screen, border_color, (meter_x, meter_y, meter_width, meter_height), 2)

    # Calculate the height of the filled portion based on the proton charge percentage
    filled_height = int(meter_height * proton_percentage)

    # Draw the filled portion of the proton charge meter
    pygame.draw.rect(screen, meter_color, (meter_x, meter_y + meter_height - filled_height, meter_width, filled_height))



    # Display the proton charge information
    max_trap_cap = 0
    num_traps = 0
    for equipment in player.vehicle_items:
        if equipment['name'] == 'Ghost Trap': 
            num_traps += 1
            max_trap_cap += 1
        if equipment['name'] == '*Full Trap*': 
            max_trap_cap += 1

    plc_text = ""
    if player.has("Portable Lazer Confinement"):
        plc_text = f'  PLC: {player.portable_storage}/{str(PLC_MAX_STORAGE)}'


    player_proton_text = FONT24.render(f'Proton Charge: {round(proton_percentage*100)}%      Traps: {num_traps} {plc_text}', True, WHITE) #' / {max_trap_cap}', True, WHITE)
    
    player_proton_box_x = meter_x + meter_width + 10
    player_proton_box_y = 0 + player_proton_text.get_height()  # Center the text vertically within the meter


    player_proton_box_width = player_proton_text.get_width() + 20 
    player_proton_box_height = player_proton_text.get_height() + 10

    pygame.draw.rect(screen, BLUE, (player_proton_box_x, player_proton_box_y, player_proton_box_width, player_proton_box_height))
    

    screen.blit(player_proton_text, (player_proton_box_x + 10, player_proton_box_y + 5))




def display_credits_while():
    global linePosition
    global player

    linePosition = TOP_LINE_POSITION
    # screen.fill(BROWN, (WIDTH - 300, linePosition, WIDTH, font.get_height() * 1))
    rendered_textA = FONT36.render("Credit: ", True, BLACK)
    screen.blit(rendered_textA, (WIDTH - 200, linePosition))

    rendered_textB = FONT36.render(" $" + str(player.cash_balance), True, WHITE)
    screen.blit(rendered_textB, (WIDTH - 200 + rendered_textA.get_width() , linePosition))
    linePosition += (rendered_textB.get_height() * 2)

        # display_two_color_typewriter("Credit:",player_balance, WIDTH - 200, linePosition)

def display_ghostbuster_hq_text():
    global player

    text = "Ghostbuster HQ"
    
    # Load and resize the image
    # image = pygame.image.load("your_image_path.png")
    image = pygame.transform.scale(GB_LOGO, (100, 100))

    # Calculate the position for the image (centered at the top)
    x_image = (WIDTH - image.get_width()) // 2
    y_image = 10  # Adjust as needed for vertical positioning

    # Calculate the position for the text (just below the image)
    x_text = (WIDTH - FONT36.size(text)[0]) // 2
    y_text = y_image + image.get_height()//2 + 10  # Adjust as needed for vertical spacing

    # Render and display the image
    screen.blit(image, (x_image, y_image))

    # Render and display the text
    rendered_text = FONT36.render(text, True, BLACK)
    screen.blit(rendered_text, (x_text, y_text))

   

def showCar(vehicle_image, x_vehicle_image, y_vehicle_image):
    global player 
    global vacuum_on


# Render and display the vehicle image
    screen.blit(vehicle_image, (x_vehicle_image, y_vehicle_image))


    # render stuff on top of the car
    num_traps = 0
    for equipment in player.vehicle_items:
        if equipment['name'] in equipment_images:
            equipment_image = equipment_images.get(equipment['name'])
            if equipment_image is not None:
                if equipment['name'] == 'PK Energy Detector':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image - equipment_image.get_height()//3
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Giga Meter':
                    equipX = x_vehicle_image + vehicle_image.get_width()//2 + equipment_image.get_width()*1.75 
                    equipY = y_vehicle_image 
                    screen.blit(equipment_image, (equipX, equipY))
                

                if equipment['name'] == 'Image Intensifier':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image + equipment_image.get_height()*3.25 # 
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Sonic Disruptor':
                    equipX = x_vehicle_image + equipment_image.get_width()*0.25
                    equipY = y_vehicle_image + equipment_image.get_height()*2.5
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Marshmallow Sensor':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image + equipment_image.get_height()*3
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Infrared Camera':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 + 35
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 3 - 12 # 
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Barometric Analyzer':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 2  + equipment_image.get_height()# 
                    screen.blit(equipment_image, (equipX, equipY))

                        

                if equipment['name'] == 'Cargo Expansion':
                    # equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    # equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 2  + equipment_image.get_height()# 
                    # screen.blit(equipment_image, (equipX, equipY))

                    ...

                if equipment['name'] == 'Muon Scrubber':
                    equipX = x_vehicle_image + vehicle_image.get_width()//2 - equipment_image.get_width()//2
                    equipY = y_vehicle_image + vehicle_image.get_height() - equipment_image.get_height()*2.20 # 
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Aerosol Slime Cleaner':
                    equipX = x_vehicle_image + vehicle_image.get_width() - equipment_image.get_width() - 10
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) - 20# 
                    screen.blit(equipment_image, (equipX, equipY))


                if equipment['name'] == 'Ghost Bait':
                    equipX = x_vehicle_image - 10 # LEFT SIDE REAR
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 1 - 20# 
                    screen.blit(equipment_image, (equipX, equipY))


                if equipment['name'] == '*Full Trap*':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 1 - 35 - (num_traps*5)# 
                    screen.blit(equipment_image, (equipX, equipY))
                    num_traps += 1

                if equipment['name'] == 'Ghost Trap':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 1 - 35 - (num_traps*5)# 
                    screen.blit(equipment_image, (equipX, equipY))
                    num_traps += 1

                

                if equipment['name'] == 'Portable Lazer Confinement':
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 1 - 10 # 
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Mobile Proton Charger':
                    equipX = x_vehicle_image + equipment_image.get_width()*1.2  # LEFT SIDE
                    equipY = y_vehicle_image + vehicle_image.get_height()//2.5 # 
                    screen.blit(equipment_image, (equipX, equipY))
                    

                if equipment['name'] == 'Remote Control Trap Vehicle':
                    equipX = x_vehicle_image + vehicle_image.get_width() - 20
                    equipY = y_vehicle_image + (vehicle_image.get_height() - equipment_image.get_height()) // 2# CENTERED Y
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Portable Shield Generator':
                    equipX = x_vehicle_image + vehicle_image.get_width() - equipment_image.get_width() -5
                    equipY = y_vehicle_image + vehicle_image.get_height() - equipment_image.get_height()*2.25# 
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Extendable Gunner Seat':
                    equipX = x_vehicle_image + vehicle_image.get_width() - equipment_image.get_width()//2.25
                    equipY = y_vehicle_image + vehicle_image.get_height() - equipment_image.get_height() - 70 # 
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Ghost Vacuum':
                    if vacuum_on: 
                        equipment_image = equipment_images.get("Ghost Vacuum On")
                    equipX = x_vehicle_image + (vehicle_image.get_width() - equipment_image.get_width()) // 2 # CENTERED X
                    equipY = y_vehicle_image + 20 
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'EMP Emitter':
                    equipX = x_vehicle_image + equipment_image.get_width()*1
                    equipY = y_vehicle_image + equipment_image.get_height()*1.75
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Ecto-Repellent Field Generator':
                    equipX = x_vehicle_image + vehicle_image.get_width()//2 - equipment_image.get_width()*1.4
                    equipY = y_vehicle_image + vehicle_image.get_height() - equipment_image.get_height()*2.8
                    screen.blit(equipment_image, (equipX, equipY))

                if equipment['name'] == 'Ecto-Fusion Fuel Generator':
                    equipX = x_vehicle_image + equipment_image.get_width()*1.2  # LEFT SIDE
                    equipY = y_vehicle_image + vehicle_image.get_height()//2.5 + equipment_image.get_height() # 
                    screen.blit(equipment_image, (equipX, equipY))




def display_car_in_garage():
    global player

    # if player_vehicle == None:
    #     player_vehicle = {"name": "Hearse", "cost": 4800, "speed":90, "capacity": 9}

    if player.vehicle is not None:
        # Assuming you have a dictionary mapping vehicle names to images
        # Get the image corresponding to the player's vehicle
        vehicle_image = vehicle_images.get(player.vehicle['name'].lower())  # Convert to lowercase for case-insensitivity

        if vehicle_image is not None:
            # Resize the vehicle image
            vehicle_image = pygame.transform.scale(vehicle_image, (vehicle_image.get_width() * 2, vehicle_image.get_height() * 2))

            # Calculate the position for the vehicle image (centered in the middle, slightly offset to the right)
            x_vehicle_image = (WIDTH - vehicle_image.get_width()) // 2 + 350  # Adjust the offset as needed
            y_vehicle_image = (HEIGHT - vehicle_image.get_height()) // 2  # Center vertically

            # Define a larger fill rectangle to create a margin around the image
            margin_size = 50
            fill_rect = pygame.Rect(
                x_vehicle_image - margin_size,
                y_vehicle_image - margin_size,
                vehicle_image.get_width() + 2 * margin_size,
                vehicle_image.get_height() + 2 * margin_size
            )

            # Clear the area around the vehicle image
            # screen.fill(BROWN, fill_rect)

            showCar(vehicle_image, x_vehicle_image, y_vehicle_image)
                            



    # Update the display
    # pygame.display.flip()




def display_shopping_credit_vehicle_header():
    global player
    global linePosition
    linePosition = TOP_LINE_POSITION

    if player.vehicle == None:
        player.vehicle = {"name": "Hearse", "cost": 4800, "speed": 90, "capacity": 9, "tank_size": 100}

    
    rendered_textA = FONT36.render("Credit: ", True, BLACK)
    screen.blit(rendered_textA, (WIDTH - 200, linePosition))

    rendered_textB = FONT36.render(" $" + str(player.cash_balance), True, WHITE)
    screen.blit(rendered_textB, (WIDTH - 200 + rendered_textA.get_width() , linePosition))
    linePosition += (rendered_textB.get_height() * 2)

    
    # rendered_text = font.render("--------------------------", True, BLACK)
    # screen.blit(rendered_text, (WIDTH - 300, linePosition))
    # linePosition += (font.get_height() * 2) - 30

    # Display player vehicle items on the right side
    rendered_text = FONT36.render(player.vehicle["name"], True, BLACK)
    screen.blit(rendered_text, (WIDTH - 300, linePosition))
    linePosition += (FONT36.get_height() * 2) - 30

    rendered_text = FONT36.render("--------------------------", True, BLACK)
    screen.blit(rendered_text, (WIDTH - 300, linePosition))
    linePosition += (FONT36.get_height() * 2) - 10

# function to display a list ofthe vehicle mounted equipment
def display_vehicle_equipment():
    global player
    global linePosition

    linePosition = 200
    # screen.fill(BROWN, (WIDTH - 300, linePosition, 300, HEIGHT - linePosition))
    rendered_textA = FONT36.render("Equipped: ", True, BLACK)
    screen.blit(rendered_textA, (WIDTH - 300, linePosition))

    display_two_color(f"{len(player.vehicle_items)}", f" / {player.vehicle['capacity']}", WIDTH - 300 + rendered_textA.get_width(), linePosition, firstColor=WHITE, secondColor=BLACK)

    # Count occurrences of each item
    item_counts = Counter(item["name"] for item in player.vehicle_items)

    for item_name, count in item_counts.items():
    # Display item name with count (if count is greater than 1)
        display_text = f"{item_name} x{count}" if count > 1 else item_name
        rendered_text = FONT24.render(display_text, True, BLACK)
        screen.blit(rendered_text, (WIDTH - 280, linePosition))
        linePosition += (rendered_text.get_height() * 2)


# function to display a list ofthe vehicle mounted equipment
def display_base():
    global player
    global linePosition



    linePosition = 200
    # screen.fill(BROWN, (WIDTH - 300, linePosition, 300, HEIGHT - linePosition))
    rendered_textA = FONT36.render("Equipped: ", True, BLACK)
    screen.blit(rendered_textA, (WIDTH - 300, linePosition))
    linePosition += (FONT36.get_height() * 2)
    
    for improvement in player.base:
        rendered_text = FONT24.render(improvement["name"], True, BLACK)
        screen.blit(rendered_text, (WIDTH - 280, linePosition))
        linePosition += (FONT24.get_height() * 2)


    

def display_base_add_():
    global player
    global linePosition



    linePosition = 200
    # screen.fill(BROWN, (WIDTH - 300, linePosition, 300, HEIGHT - linePosition))
    rendered_textA = FONT36.render("Equipped: ", True, BLACK)
    screen.blit(rendered_textA, (WIDTH - 300, linePosition))
    linePosition += (FONT36.get_height() * 2)
    
    last_item = player.base[-1]
    for improvement in player.base:
        if improvement == last_item:
            display_text_typewriter(improvement["name"], WIDTH - 280, linePosition, this_font=FONT24)
        else:
            rendered_text = FONT24.render(improvement["name"], True, BLACK)
            screen.blit(rendered_text, (WIDTH - 280, linePosition))
            linePosition += (FONT24.get_height() * 2)

    

def display_base_grid():
    global linePosition
    global player

    # Constants for grid layout
    grid_width = 4  # Number of columns
    grid_height = 5 # number of rows
    box_size = 100  # Size of each box
    margin = 20  # Margin between boxes

    # Calculate the starting position for the grid
    start_x = WIDTH // 2 + 0 # - (grid_width * (box_size + margin)) + margin
    start_y = TOP_LINE_POSITION + 70  # linePosition + margin

    # Fill the base grid area with a background color
    screen.fill(BLACK, (start_x - 20, start_y - 20, grid_width * (box_size + margin) + margin, (grid_height) * (box_size + margin) + margin))

    # Iterate through base improvements and display them in a grid
    for i, improvement in enumerate(player.base):
        col = i % grid_width
        row = i // grid_width

        # Calculate the position for each box
        box_x = start_x + col * (box_size + margin)
        box_y = start_y + row * (box_size + margin)

        # Draw the box for the improvement
        pygame.draw.rect(screen, improvement['color'], (box_x, box_y, box_size, box_size))  # Draw box

        # Display improvement name inside the box
        if improvement["name"] == "Vehicle Garage":
            if player.vehicle is not None:
                # Assuming you have a dictionary mapping vehicle names to images
                # Get the image corresponding to the player's vehicle
                vehicle_image = vehicle_images.get(player.vehicle['name'].lower())  # Convert to lowercase for case-insensitivity

                if vehicle_image is not None:
                    # Resize the vehicle image
                    wh_ratio = vehicle_image.get_width() / vehicle_image.get_height()
                    vehicle_image = pygame.transform.scale(vehicle_image, (box_size * wh_ratio , box_size))

                    # Calculate the position for the vehicle image (centered in the box)
                    x_vehicle_image = box_x + (box_size // 2) - (vehicle_image.get_width() // 2)
                    y_vehicle_image = box_y + (box_size // 2) - (vehicle_image.get_height() // 2)


                    # # Define a larger fill rectangle to create a margin around the image
                    # margin_size = 50
                    # fill_rect = pygame.Rect(
                    #     x_vehicle_image - margin_size,
                    #     y_vehicle_image - margin_size,
                    #     vehicle_image.get_width() + 2 * margin_size,
                    #     vehicle_image.get_height() + 2 * margin_size
                    # )

                    # # Clear the area around the vehicle image
                    # screen.fill(BROWN, fill_rect)

                    # Render and display the vehicle image
                    screen.blit(vehicle_image, (x_vehicle_image, y_vehicle_image))


        else:

            # Calculate text position
            text_x = box_x + (box_size // 2)
            text_y = box_y + (box_size // 2) - (FONT18.size(improvement["name"])[1] * len(split_text_into_lines(improvement["name"], box_size, FONT18)) // 2)

            # Display each line of the improvement name
            for line in split_text_into_lines(improvement["name"], box_size, FONT18):
                rendered_text = FONT18.render(line, True, BLACK)
                screen.blit(rendered_text, (text_x - rendered_text.get_width() // 2, text_y))
                text_y += rendered_text.get_height()

    # pygame.display.flip()  # Update the display


# function to display a list ofthe vehicle mounted equipment
def display_vehicle_equipment_add_equipment():
    global player
    global linePosition

    linePosition = 200
    screen.fill(BROWN, (WIDTH - 300, linePosition, 300, HEIGHT - linePosition))

    rendered_textA = FONT36.render("Equipped: ", True, BLACK)
    screen.blit(rendered_textA, (WIDTH - 300, linePosition))

    rendered_textB = FONT36.render(f"{len(player.vehicle_items)}", True, WHITE)
    screen.blit(rendered_textB, (WIDTH - 300 + rendered_textA.get_width(), linePosition))

    rendered_textC = FONT36.render(" / " + str(player.vehicle["capacity"]), True, BLACK)
    screen.blit(rendered_textC, (WIDTH - 300 + rendered_textA.get_width() + rendered_textB.get_width(), linePosition))

    linePosition += (rendered_textC.get_height() * 2)

    last_item_name = player.vehicle_items[-1]["name"]
    # Count occurrences of each item
    item_counts = Counter(item["name"] for item in player.vehicle_items)

    for item_name, count in item_counts.items():
        if item_name == last_item_name:
            display_text = f"{item_name} x{count}" if count > 1 else item_name
            display_text_typewriter(display_text, WIDTH - 280, linePosition,this_font=FONT24)
        else:
            # Display item name with count (if count is greater than 1)
            display_text = f"{item_name} x{count}" if count > 1 else item_name
            rendered_text = FONT24.render(display_text, True, BLACK)
            screen.blit(rendered_text, (WIDTH - 280, linePosition))
            linePosition += (rendered_text.get_height() * 2)


# function to display a list ofthe vehicle mounted equipment
def display_hired_busters():
    global player
    global linePosition

    roster = player.roster.sprites()
    linePosition = HEIGHT - HEIGHT//4
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height() // 2), (WIDTH - 30, linePosition - FONT36.get_height() // 2), 3)
    rendered_text = FONT36.render("Hired Staff:", True, BLACK)
    screen.blit(rendered_text, (0 + 50, linePosition))
    linePosition += rendered_text.get_height()*2

    for buster in roster:
        screen.blit(buster.images[0], (25, linePosition-10))
        rendered_text = FONT36.render(buster.name, True, BLACK)
        screen.blit(rendered_text, (0 + 80, linePosition))
        

        xPos = 250

        for trait, score in buster.traits.items():
            rendered_text = FONT36.render(str(score), True, WHITE)
            screen.blit(rendered_text, (xPos, linePosition))
            xPos += 110

        rendered_text = FONT36.render(buster.origin, True, WHITE)
        screen.blit(rendered_text, (xPos, linePosition))

        xPos += 280

        rendered_text = FONT36.render(buster.goal, True, WHITE)
        screen.blit(rendered_text, (xPos, linePosition))

        # xPos += 290

        # rendered_text = font.render("$ " + str(buster.hiring_cost), True, WHITE)
        # screen.blit(rendered_text, (xPos, linePosition))

        linePosition += (rendered_text.get_height() * 1.75)


# function to display a list ofthe vehicle mounted equipment
def display_hired_busters_add_buster():
    global player
    global linePosition

    roster = player.roster.sprites()
    linePosition = HEIGHT - HEIGHT//4
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height() // 2), (WIDTH - 30, linePosition - FONT36.get_height() // 2), 3)
    rendered_text = FONT36.render("Hired Staff:", True, BLACK)
    screen.blit(rendered_text, (0 + 50, linePosition))
    linePosition += rendered_text.get_height()*2

    last_buster = roster[-1]
    for buster in roster:
        if buster == last_buster:
            display_text_typewriter(buster.name, 0 + 80, linePosition)
        else:
            screen.blit(buster.images[0], (25, linePosition-10))
            rendered_text = FONT36.render(buster.name, True, BLACK)
            screen.blit(rendered_text, (0 + 80, linePosition))
            
            xPos = 250

            for trait, score in buster.traits.items():
                rendered_text = FONT36.render(str(score), True, WHITE)
                screen.blit(rendered_text, (xPos, linePosition))
                xPos += 110

            rendered_text = FONT36.render(buster.origin, True, WHITE)
            screen.blit(rendered_text, (xPos, linePosition))

            xPos += 280

            rendered_text = FONT36.render(buster.goal, True, WHITE)
            screen.blit(rendered_text, (xPos, linePosition))
            linePosition += (rendered_text.get_height() * 1.75)

        

def purchase_equipment(equipment_choices):
    global player
    global linePosition
    global shopping_equipment
    global game_mode
    global sell_mode
    global forklift

    linePosition = HEIGHT - 50
    # screen.fill(BROWN, (50, linePosition, WIDTH, HEIGHT)) #font.get_height() * 2))
    # Wait for any key press before proceeding
    purchase_text = "Press # to Purchase Equipment, Press R to Remove - E to Continue"
    prompt_color = BLACK
    if sell_mode: 
        purchase_text = "Press # to Remove Equipment, Press R to Cancel - E to Continue"
        prompt_color = RED
    
    selection = get_input(purchase_text, 50, linePosition, shopping=True, color=prompt_color) #_typewriter
    # Simulate equipment purchase (replace this with your actual logic)
    if selection == "s":
        sell_mode = not sell_mode
    elif selection == "e":
        shopping_equipment = False  # Update this based on your logic
    elif selection == "x":
        game_mode -= 2
        shopping_equipment = False  # Update this based on your logic

    elif selection == "0":
        # print("none")
        return False

    elif selection == "esc":
        shopping_equipment = False  # Update this based on your logic

    

    else:

        if sell_mode: # SELL MODE
            selected_equipment = int(selection)

            if equipment_choices[selected_equipment] in player.vehicle_items and equipment_choices[selected_equipment]['name'] != "Cargo Expansion":
                ...
                player.vehicle_items.remove(equipment_choices[selected_equipment])

                if equipment_choices[selected_equipment]['name'] == "Ecto-Fusion Fuel Generator":

                    player.vehicle["speed"] -= EXTRA_SPEED_FROM_GENERATOR
                    # print("remove generator" + str(player.vehicle["speed"]))

                sell_mode = not sell_mode
                return False

            else:
                ...
                # print("1")
                CLOCK_SOUND.play()
                
                return False
                        

        else: # PURCHASE MODE

            selected_equipment = int(selection)
            if (len(player.vehicle_items) < player.vehicle["capacity"]) or (equipment_choices[selected_equipment]['name'] == "Cargo Expansion"):
                #selected_equipment = int(selection)
                if selected_equipment <= len(equipment_choices):
                    if equipment_choices[selected_equipment] not in player.vehicle_items or equipment_choices[selected_equipment]['unique'] == False:  
                        equipment_cost = equipment_choices[selected_equipment]['cost']
                        # PRICE CHECK, CAN PLAYER AFFORD??
                        if player.cash_balance >= equipment_cost:
                            #player.cash_balance -= equipment_cost
                            

                            forklift.sprites()[0].load(equipment_choices[selected_equipment])
                            # player.vehicle_items.append(equipment_choices[selected_equipment])

                            if equipment_choices[selected_equipment]['name'] == "Cargo Expansion":
                                player.vehicle["capacity"] += EXTRA_CAPACITY_FROM_CARGO_EXPANSION

                            if equipment_choices[selected_equipment]['name'] == "Ecto-Fusion Fuel Generator":
                                player.vehicle["speed"] += EXTRA_SPEED_FROM_GENERATOR
                                # print("add generator" + str(player.vehicle["speed"]))


                            return True
                        else:
                            TRAP_NO_SOUND.play()
                            return False

                    else:
                        ...
                        # print("2")
                        CLOCK_SOUND.play()
                        return False
                else:
                    ...
                    # print("3")
                    CLOCK_SOUND.play()
                    return False
            else:
                ...
                # print("4")
                CLOCK_SOUND.play()
                return False


def purchase_improvement(improvement_choices):
    global player
    global linePosition
    global shopping_equipment
    global game_mode

    linePosition = HEIGHT - 50
    # screen.fill(BROWN, (50, linePosition, WIDTH, HEIGHT)) #font.get_height() * 2))
    # Wait for any key press before proceeding
    selection = get_input("Press # to Add Improvement  -   E to Continue", 50, linePosition, shopping=True) # _typewriter
    # Simulate equipment purchase (replace this with your actual logic)
    if selection == "s":
        ...
    elif selection == "e":
        shopping_equipment = False  # Update this based on your logic
    elif selection == "x":
        game_mode -= 2
        shopping_equipment = False  # Update this based on your logic

    # elif event.key == pygame.K_ESCAPE:
    #     shopping_equipment = False
    #     game_mode = 0

    elif selection == "esc":
        game_mode = -1
        shopping_equipment = False  # Update this based on your logic

    elif selection != "0" and int(selection) <= len(improvement_choices):
        if len(player.base) < 20:
            selected_improvement = int(selection)
            if improvement_choices[selected_improvement] not in player.base or improvement_choices[selected_improvement]['unique'] == False:  
                improvement_cost = improvement_choices[selected_improvement]['cost']
                # PRICE CHECK
                if player.cash_balance >= improvement_cost:
                    player.cash_balance -= improvement_cost
                    player.base.append(improvement_choices[selected_improvement])
                    FORK_SHORT_SOUND.play()
                    CASH_SOUND.play()
                    return True
                else:
                    TRAP_NO_SOUND.play()
                    return False
            else:
                ...
                CLOCK_SOUND.play()
                return False
        else:
            ...
            CLOCK_SOUND.play()
            return False

def display_text(text, x, y, this_font=FONT36, line_space=2, color=BLACK):
    global linePosition
    rendered_text = this_font.render(text, True, color)
    screen.blit(rendered_text, (x, y))
    # pygame.display.flip()
    linePosition += (rendered_text.get_height() * line_space) + 1

# Function to display text on the screen with a typewriter effect
def display_text_typewriter(text, x, y, this_font=FONT36, line_space=2, color=BLACK):
    global linePosition


    lines = text.split("\n")  # Split the text into lines


    

    for line in lines:
        rendered_text = ""
        for i in range(len(line) + 1):
            rendered_text = this_font.render(line[:i], True, color)  # GAME INFO & PROMPT TEXT 
            screen.blit(rendered_text, (x, linePosition))
            pygame.display.flip()
            pygame.time.delay(40)  # Adjust the delay for typing speed
            TYPE_SOUND.play()

        linePosition += (rendered_text.get_height() * line_space) + 1

    return rendered_text

# Function to display player's balance with dollar number in white
def display_two_color_typewriter(textA, textB, x, y, this_font=FONT36, firstColor=BLACK, secondColor=WHITE):
    global linePosition
    # balance_text = textA #f"Your Balance: $"#{balance}"


    

    for i in range(len(textA) + 1):
        rendered_text = this_font.render(textA[:i], True, firstColor)  # GAME INFO & PROMPT TEXT 
        screen.blit(rendered_text, (x, linePosition))
        pygame.display.flip()
        pygame.time.delay(40)  # Adjust the delay for typing speed
        TYPE_SOUND.play()


    rendered_text_static = this_font.render(textA, True, firstColor)
    rendered_text_variable = ""

    for i in range(len(str(textB)) + 1):
        rendered_text_variable = this_font.render(str(textB)[:i], True, secondColor)
        screen.blit(rendered_text_variable, (x + rendered_text_static.get_width(), linePosition))
        pygame.display.flip()
        pygame.time.delay(40)  # Adjust the delay for typing speed
        TYPE_SOUND.play()

    linePosition += (rendered_text_variable.get_height() * 2) + 1 

    return rendered_text_variable

def display_two_color(textA, textB, x, y, this_font=FONT36, firstColor=BLACK, secondColor=WHITE):
    global linePosition

    rendered_text_static = this_font.render(textA, True, firstColor)
    rendered_text_variable = this_font.render(str(textB), True, secondColor)

    screen.blit(rendered_text_static, (x, linePosition))
    screen.blit(rendered_text_variable, (x + rendered_text_static.get_width(), linePosition))

    linePosition += (rendered_text_variable.get_height() * 2) + 1

    # pygame.display.flip()
    # TYPE_SOUND.play()

    return rendered_text_variable



def get_input(prompt, x, y, this_font=FONT36, numeric_prompt=False, yes_no_prompt=False, key_continue=False, shopping=False, color=BLACK):
    global choosing_car
    global sell_mode
    global selected_index
    global running
    global starting


    input_text = ""
    display_text(prompt, x, y, this_font=this_font, color=color)

    # while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            choosing_car = False
            running = False
            starting = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                return "s"

            if key_continue:
                return

            if shopping:
                if event.unicode.lower() == "s" or event.unicode.lower() == "r":
                    return "s"
                elif event.unicode.lower() == "e":
                    return "e"
                elif event.key == pygame.K_LEFT:
                    return "x"
                elif event.key == pygame.K_RIGHT:
                    return "e"

                elif event.key == pygame.K_ESCAPE:
                    return "esc"

                if event.key == pygame.K_UP:
                    selected_index -= 1
                    return "0"

                elif event.key == pygame.K_DOWN:
                    selected_index += 1

                    return "0"

                elif event.unicode.isdigit():
                    input_text = event.unicode
                    return input_text

                elif event.key == pygame.K_RETURN:
                    return str(selected_index+1)

            if numeric_prompt or yes_no_prompt:
                if event.unicode.isdigit() or (yes_no_prompt and event.unicode.lower() in ('y', 'n')):
                    input_text = str(event.unicode)  # Ensures it's always a string
                    return input_text

            if event.key == pygame.K_RETURN:
                return input_text

            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]



            else:
                input_text += str(event.unicode)

            if not choosing_car:
                display_text(prompt + input_text, x, y, color=color)

    return "0"



# Function to get player input with typewriter effect
def get_input_typewriter(prompt, x, y, this_font=FONT36, numeric_prompt=False, yes_no_prompt=False, keyContinue=False, shopping=False, color=BLACK):
    global linePosition
    global choosing_car
    global sell_mode
    
    input_text = ""
    display_text_typewriter(prompt, x, y, this_font=this_font, color=color)
    
    while True:
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                TYPE_SOUND.play()

                # if event.key == pygame.K_RALT or event.key == pygame.K_LALT:
                #     return "s"


                if keyContinue:
                    return

                if shopping:

                    if event.unicode.lower() == "s":
                        return "s"

                    if event.unicode.lower() == "r":
                        return "s"

                    if event.unicode.lower() == "e":
                        return "e"



                    elif event.key == pygame.K_LEFT:
                        return "x"

                    elif event.key == pygame.K_RIGHT:
                        return "e"


                    elif event.unicode.isdigit():
                        input_text = event.unicode
                        # Display the digit on the same line as the prompt
                        prompt_rendered = FONT36.render(prompt, True, color)
                        input_rendered = FONT36.render(input_text, True, WHITE)
                        screen.blit(prompt_rendered, (x, y))
                        screen.blit(input_rendered, (x + prompt_rendered.get_width(), y))  # Position the input_text next to the prompt
                        pygame.display.flip()
                        return input_text
                elif numeric_prompt:
                    if event.unicode.isdigit():
                        input_text = event.unicode
                        # Display the digit on the same line as the prompt
                        prompt_rendered = FONT36.render(prompt, True, color)
                        input_rendered = FONT36.render(input_text, True, WHITE)
                        screen.blit(prompt_rendered, (x, y))
                        screen.blit(input_rendered, (x + prompt_rendered.get_width(), y))  # Position the input_text next to the prompt
                        pygame.display.flip()
                        return input_text
                elif yes_no_prompt:
                    if event.unicode.lower() in ('y', 'n'):
                        input_text = event.unicode.lower()
                        # Display 'y' or 'n' on the same line as the prompt
                        prompt_rendered = FONT36.render(prompt, True, color)
                        input_rendered = FONT36.render(input_text, True, WHITE)
                        screen.blit(prompt_rendered, (x, y))
                        screen.blit(input_rendered, (x + prompt_rendered.get_width(), y))  # Position the input_text next to the prompt
                        pygame.display.flip()
                        return input_text

                

                elif event.key == pygame.K_RETURN:
                    return input_text

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode


                if not choosing_car:
                    # Re-render the input_text on a new line without repeating the prompt
                    # screen.fill(BROWN, (x, y, WIDTH, font.get_height() * 2))
                    prompt_rendered = FONT36.render(prompt, True, color)
                    input_rendered = FONT36.render(input_text, True, WHITE)
                    screen.blit(prompt_rendered, (x, y))
                    screen.blit(input_rendered, (x + prompt_rendered.get_width(), y))  # Position the input_text next to the prompt
                    pygame.display.flip()


def start_loop():
    global linePosition
    global player
    global choosing_car
    global game_mode

    screen.fill(BROWN)
    linePosition = TOP_LINE_POSITION

    # Load and resize the image
    # image = pygame.image.load("your_image_path.png")
    image = pygame.transform.scale(GB_LOGO, (200, 200))

    # Calculate the position for the image 
    x_image = 75
    y_image = 5  # Adjust as needed for vertical positioning
    # Render and display the image
    screen.blit(image, (x_image, y_image))

    text = "Ghostbusters!"
    VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)
    # Calculate the position for the text (just below the image)
    x_text = (WIDTH - FONT36.size(text)[0]) // 2
    linePosition = FONT36.get_height()
    # Render and display the text
    # rendered_text = font.render(text, True, BLACK)
    # screen.blit(rendered_text, (x_text, linePosition))
    display_text_typewriter(text, x_text, linePosition)
    # linePosition += font.get_height() * 2

    # Welcome message
    welcome_message = "For Professional\nParanormal\nInvestigations\nand Eliminations."
    welcome_message = welcome_message.split("\n")
    offset = 0
    for line in welcome_message:
        display_text_typewriter(line, x_text + 150 + offset, linePosition, line_space=1)
        offset += 50
    linePosition += FONT36.get_height() * 2

    display_text_typewriter("- We're Ready to Believe You -", 50, linePosition)

    # Draw the line with gaps on both sides
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)

    linePosition += FONT36.get_height()

    

    # Get player name
    display_text_typewriter("To form a Ghostbusters franchise in your city, ", 50, linePosition)
    player.name = get_input_typewriter("please state your name: ", 50, linePosition)

    # Check if the player has an account
    has_account = get_input_typewriter("Do you have an account? (y/n): ", 50, linePosition, yes_no_prompt=True).lower()

    if has_account == "n":
        # Give $10,000 to the player
        player.cash_balance = NEW_GAME_CASH_ADVANCE
        display_text_typewriter(f"\nIn that case, welcome to your new business.\nAs a new franchise owner, the bank will advance you $ {NEW_GAME_CASH_ADVANCE} for equipment.\nUse it wisely...\nGood Luck...", 50, linePosition)
    else:
        # Get player balance if they have an account



        player.cash_balance = int(get_input_typewriter("Enter your account balance: $ ", 50, linePosition))
        
        display_text_typewriter(f"\nWelcome back...\n ",50, linePosition)


    display_two_color_typewriter("Your balance: $ ",player.cash_balance, 50, linePosition)
    # Wait for any key press before proceeding
    get_input_typewriter("Press Any Key to Continue ", 50, linePosition, keyContinue=True)
    
    


                
def purchase_car():
    global linePosition
    global player
    global choosing_car
    global selected_index

    # CHECK IF TESTING:
    if player.name == "" and player.cash_balance == 0:
        player.name = "Game Tester"
        player.cash_balance = 50000

    selected_index = 0

    # Clear the screen
    screen.fill(BROWN)
    # Draw the bars
    draw_bars(screen, game_mode)
    linePosition = TOP_LINE_POSITION

    display_ghostbuster_hq_text()
    display_text_typewriter(f"Ghostbusting Vehicle Selection:", 50, linePosition)
    
    # Draw the line with gaps on both sides
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
    linePosition += (FONT36.get_height() * 2)

    # Get player's choice of vehicle
    # vehicle_choices = {
    #     # 1: {"name": "Motorcycle", "cost": 1000, "speed": 120, "capacity": 3, "tank_size": 50},
    #     1: {"name": "Compact", "cost": 2000, "speed": 75, "capacity": 5, "tank_size": 60},
    #     2: {"name": "Hearse", "cost": 4800, "speed": 90, "capacity": 9, "tank_size": 100},
    #     3: {"name": "Wagon", "cost": 6000, "speed": 90, "capacity": 11, "tank_size": 120},
    #     4: {"name": "Utility-Truck", "cost": 9000, "speed": 90, "capacity": 12, "tank_size": 140},
    #     5: {"name": "High-Performance", "cost": 15000, "speed": 160, "capacity": 8, "tank_size": 130}
    # }

   # Display vehicle choices with cost
    for number, vehicle in VEHICLE_CHOICES.items():
        # display_two_color_typewriter(f"{number}.   {vehicle['name']}",f"   - ${vehicle['cost']}", 75, linePosition)
        if player.cash_balance >= vehicle['cost']:
            display_two_color(f"{number}.   {vehicle['name']}",f"   - ${vehicle['cost']}",75, linePosition)
        else:
            display_two_color(f"{number}.   {vehicle['name']}",f"   - ${vehicle['cost']}",75, linePosition, secondColor=RED)

    display_two_color_typewriter("Your balance: $ ",player.cash_balance, 50, linePosition)
    display_text_typewriter(f"Press (1-{len(VEHICLE_CHOICES)}) to purchase car. ", 50, linePosition)
    choosing_car = True
    lastPos = linePosition
    tooPricy = False

    while choosing_car:

        if selected_index > len(VEHICLE_CHOICES)-1: 
            selected_index = len(VEHICLE_CHOICES)-1

        if selected_index < 0:
            selected_index = 0


        # Clear the screen
        screen.fill(BROWN)
        # Draw the bars
        draw_bars(screen, game_mode)
        linePosition = TOP_LINE_POSITION

        display_ghostbuster_hq_text()
        display_text(f"Ghostbusting Vehicle Selection:", 50, linePosition)
        
        # Draw the line with gaps on both sides
        pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
        linePosition += (FONT36.get_height() * 2)

        

        # Display vehicle choices with cost
        for number, vehicle in VEHICLE_CHOICES.items():
            # display_two_color_typewriter(f"{number}.   {vehicle['name']}",f"   - ${vehicle['cost']}", 75, linePosition)
            if number-1 == selected_index:
                # print(number, selected_index)
                pygame.draw.rect(screen, WHITE, (40, linePosition-(FONT36.get_height()*0.25), WIDTH - 700, FONT36.get_height()*1.5), 2)  # Highlight the selected hire
            if player.cash_balance >= vehicle['cost']:
                display_two_color(f"{number}.   {vehicle['name']}",f"   - ${vehicle['cost']}",75, linePosition)
            else:
                display_two_color(f"{number}.   {vehicle['name']}",f"   - ${vehicle['cost']}",75, linePosition, secondColor=RED)

        display_two_color("Your balance: $ ",player.cash_balance, 50, linePosition)
        display_text(f"Press (1-{len(VEHICLE_CHOICES)}) to purchase car. ", 50, linePosition)
        choosing_car = True
        lastPos = linePosition

        linePosition = lastPos
        # Get player's choice
        selected_vehicle = get_input("", 50, linePosition, shopping=True, numeric_prompt=True) #_typewriter

        if selected_vehicle == "e": 
            if player.vehicle is not None:
                # IS CAR AFFORDABLE?
                if player.cash_balance >= player.vehicle['cost']:
                    player.cash_balance -= player.vehicle['cost']
                    player.fuel = player.vehicle['tank_size']
                    choosing_car = False
                else:
                    TRAP_NO_SOUND.play()
                    tooPricy = True



        elif selected_vehicle == "x":
            ...
            

        elif selected_vehicle.isdigit() and selected_vehicle != "0":
            selected_vehicle = int(selected_vehicle)
            if selected_vehicle <= len(VEHICLE_CHOICES) and selected_vehicle > 0: # prevent key error
                if player.vehicle != VEHICLE_CHOICES[selected_vehicle]:
                    player.vehicle = VEHICLE_CHOICES[selected_vehicle]
                    tooPricy = False
                CLOCK_SOUND.play()


        
        display_car_in_garage()


        # display_text_typewriter(f"You have chosen the {player.vehicle['name']} for $ {player.vehicle['cost']}", 50, linePosition)
        # display_text_typewriter(f"Carries {player.vehicle['capacity']} items of cargo", 50, linePosition)
        # display_text_typewriter(f"Top Speed {player.vehicle['speed']} MPH", 50, linePosition)
        if player.vehicle is not None:
            # linePosition = HEIGHT - (font.get_height()*5)
            display_text(f"You have chosen the {player.vehicle['name']} for $ {player.vehicle['cost']}", 50, linePosition)
            display_text(f"Carries {player.vehicle['capacity']} items of cargo", 50, linePosition)
            display_text(f"Top Speed {player.vehicle['speed']} MPH", 50, linePosition)

            # Wait for any key press before proceeding
            if tooPricy or (player.cash_balance < player.vehicle['cost']):
                display_text("You cannot afford this Vehicle, Please select another", 50, linePosition, color=RED)
            else:
                display_text("Press E to Confirm", 50, linePosition)



        display_credits_while()
        pygame.display.flip()


        

# Function to handle equipment shopping loop
def equipment_shopping_loop(mode):
    global linePosition
    global player
    global shopping_equipment
    global selected_index
    global forklift
    global equipment_sprites
    global equipment_choices

    equipment_sprites = pygame.sprite.Group()

    if len(forklift) == 0:
        lift = Forklift()
        forklift.add(lift)


    screen.fill(BROWN)

    # Draw the bars
    draw_bars(screen, game_mode)

    linePosition = TOP_LINE_POSITION

    menu_header_text = ""
    if mode == "monitor": 
        menu_header_text = "Monitoring Equipment:"
        equipment_choices = {
            1: {"name": "PK Energy Detector", "cost": 400, 'unique': True},
            2: {"name": "Image Intensifier", "cost": 800, 'unique': True},
            3: {"name": "Marshmallow Sensor", "cost": 800, 'unique': True},
            4: {"name": "Infrared Camera", "cost": 1200, 'unique': True},
            5: {"name": "Giga Meter", "cost": 1250, 'unique': True},
            6: {"name": "Barometric Analyzer", "cost": 1400, 'unique': True},
            7: {"name": "Cargo Expansion", "cost": 10000, 'unique': True}
        }

    elif mode == "capture": 
        menu_header_text = "Ghost Capture Equipment:"
        equipment_choices = {
            1: {"name": "Ghost Bait", "cost": 400, 'unique': True},
            2: {"name": "Ghost Trap", "cost": 600, 'unique': False},
            3: {"name": "Ghost Vacuum", "cost": 500, 'unique': True},
            4: {"name": "Remote Control Trap Vehicle", "cost": 2500, 'unique': True},
            5: {"name": "Extendable Gunner Seat", "cost": 2500, 'unique': True},
            6: {"name": "Mobile Proton Charger", "cost": 5000, 'unique': True},
            7: {"name": "Portable Lazer Confinement", "cost": 15000, 'unique': True}
        
        }

    elif mode == "defense": 
        menu_header_text = "Defense Equipment:"
        equipment_choices = {
            1: {"name": "Muon Scrubber", "cost": 1200, 'unique': True},
            2: {"name": "Aerosol Slime Cleaner", "cost": 3000, 'unique': True},
            3: {"name": "Portable Shield Generator", "cost": 4000, 'unique': True},
            4: {"name": "EMP Emitter", "cost": 5000, 'unique': True},
            5: {"name": "Ecto-Repellent Field Generator", "cost": 9000, 'unique': True},
            6: {"name": "Sonic Disruptor", "cost": 12000, 'unique': True},
            7: {"name": "Holographic Decoy", "cost": 15000, 'unique': True},
            8: {"name": "Ecto-Fusion Fuel Generator", "cost": 25000, 'unique': True}
        
        }

    for number, equipment in equipment_choices.items():
        item = Equipment_Sprite(equipment['name'],equipment['cost'],equipment['unique'])
        equipment_sprites.add(item)

    # Display the equipment menu
    
    display_ghostbuster_hq_text()
    display_text_typewriter(menu_header_text, 50, linePosition)

    # Draw the line with gaps on both sides
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
    linePosition += (FONT36.get_height() * 2)

    

    selected_index = 0  # Index of the currently selected
    fresh_purchase = False
    shopping_equipment = True
    while shopping_equipment:
        

        if selected_index > len(equipment_choices)-1: 
            selected_index = len(equipment_choices)-1

        if selected_index < 0: 
            selected_index = 0

        screen.fill(BROWN)
        # Draw the bars
        draw_bars(screen, game_mode)
        linePosition = TOP_LINE_POSITION

        display_ghostbuster_hq_text()
        display_text(menu_header_text, 50, linePosition)

        # Draw the line with gaps on both sides
        pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
        linePosition += (FONT36.get_height() * 2)


        # display_available_equip_list(equipment_choices)
        display_shopping_credit_vehicle_header()
        display_car_in_garage()

        update_available_equip_sprites()
        for item in equipment_sprites:
            if not player.has(item.name) or item.name == "Ghost Trap":
                screen.blit(item.image, (item.rect.x, item.rect.y))

        forklift.update()
        forklift.draw(screen)

        
        

        # display_credits_while()
        if fresh_purchase:
            # display_vehicle_equipment_add_equipment()
            display_vehicle_equipment()
        else:
            display_vehicle_equipment()

        fresh_purchase = purchase_equipment(equipment_choices)


        

        

        pygame.display.flip()



def update_available_equip_sprites():
    global linePosition
    global selected_index
    global forklift
    global player
    global equipment_sprites

    # Display equipment choices with cost
    number = 0
    for item in equipment_sprites.sprites():
        number += 1
        # display_two_color_typewriter(f"{number}.   {equipment['name']}", f"   - ${equipment['cost']}", 75, linePosition)

        rendered_textA = FONT36.render(f"{item.name}", True, BLACK)
        screen.blit(rendered_textA, (75, linePosition))
        boxstartY = linePosition
        
        # PRICE CHECK, CAN PLAYER AFFORD??
        if player.cash_balance >= item.cost:
            rendered_textB = FONT36.render(f"   - ${item.cost}", True, WHITE)
        else:
            rendered_textB = FONT36.render(f"   - ${item.cost}", True, RED)


        screen.blit(rendered_textB, (75 + rendered_textA.get_width() , linePosition))

        if (item.name == "Ghost Trap")  and not (player.has("Ghost Trap")):
            rendered_textC = FONT36.render(f"  - REQUIRED -", True, RED)
            screen.blit(rendered_textC, (75 + rendered_textA.get_width() + rendered_textB.get_width(), linePosition))

        equipment_image = None
        # Load and resize the equipment image

        # if equipment['name'] in equipment_images:
        #     equipment_image = equipment_images[equipment['name']]

        #     if equipment['name'] == "Muon Scrubber":
        #         equipment_image = pygame.transform.rotate(equipment_image,-90)

        # else:
        #     equipment_image = equipment_images['Portable Lazer Confinement'] # default image
            
        # equipment_image = pygame.transform.scale(equipment_image, (50, 50))
        # Calculate the position for the equipment image (right below the text)
        x_image = 120  # Adjust as needed for horizontal positioning
        linePosition += rendered_textB.get_height() # Adjust as needed for vertical spacing

        # Render and display the equipment image
        # if not player.has(equipment['name']) or equipment['name'] == "Ghost Trap":

            # screen.blit(equipment_image, (x_image, linePosition))



        if item == forklift.sprites()[0].target_sprite:
            if forklift.sprites()[0].loaded:
                item.rect.x = forklift.sprites()[0].rect.x + forklift.sprites()[0].image.get_width() - item.image.get_width()
                item.rect.y = forklift.sprites()[0].rect.bottom - item.image.get_height()

            else:
                item.rect.x = x_image
                item.rect.y = linePosition
        else:
            item.rect.x = x_image
            item.rect.y = linePosition

            

        linePosition += 60 #(equipment_image.get_height())

        if (number-1) == selected_index:
            pygame.draw.rect(screen, WHITE, (40, boxstartY-(FONT36.get_height()*0.25), WIDTH - 650, linePosition-boxstartY),2 ) # Highlight the selected hire

            if not forklift.sprites()[0].loading:
                forklift.sprites()[0].goto(40 + WIDTH - 850, boxstartY-(FONT36.get_height()*0.25))




# THIS DOESN"T SEEM TO BE USED!!!!! MAYBE FOR BASE IMPROVMENTS
def display_available_improvement_list(improvement_choices):
    global linePosition
    global selected_index
    # global forklift
    global player



    # Display equipment choices with cost
    for number, improvement in improvement_choices.items():
        # display_two_color_typewriter(f"{number}.   {equipment['name']}", f"   - ${equipment['cost']}", 75, linePosition)

        rendered_textA = FONT36.render(f"{number}.   {improvement['name']}", True, BLACK)
        screen.blit(rendered_textA, (75, linePosition))
        boxstartY = linePosition
        
        # PRICE CHECK, CAN PLAYER AFFORD??
        if player.cash_balance >= improvement['cost']:
            rendered_textB = FONT36.render(f"   - ${improvement['cost']}", True, WHITE)
        else:
            rendered_textB = FONT36.render(f"   - ${improvement['cost']}", True, RED)


        screen.blit(rendered_textB, (75 + rendered_textA.get_width() , linePosition))



        # equipment_image = None
        # Load and resize the equipment image

        # if equipment['name'] in equipment_images:
        #     equipment_image = equipment_images[equipment['name']]

        #     if equipment['name'] == "Muon Scrubber":
        #         equipment_image = pygame.transform.rotate(equipment_image,-90)

        # else:
        #     equipment_image = equipment_images['Portable Lazer Confinement'] # default image
            
        # # equipment_image = pygame.transform.scale(equipment_image, (50, 50))
        # # Calculate the position for the equipment image (right below the text)
        # x_image = 120  # Adjust as needed for horizontal positioning
        # linePosition += rendered_textB.get_height() # Adjust as needed for vertical spacing

        # # Render and display the equipment image
        # if not player.has(equipment['name']) or equipment['name'] == "Ghost Trap":


        #     screen.blit(equipment_image, (x_image, linePosition))

        linePosition += 60 #(equipment_image.get_height())

        if (number-1) == selected_index:
            pygame.draw.rect(screen, WHITE, (40, boxstartY-(FONT36.get_height()*0.25), WIDTH - 650, linePosition-boxstartY),2 ) # Highlight the selected hire

            # if not forklift.loading:
            #     forklift.sprites()[0].goto(40 + WIDTH - 850, boxstartY-(font.get_height()*0.25))



def research_allocation_loop():
    global linePosition
    global player
    global game_mode
    global starting


    COLUMN_WIDTH = 150
    COLUMN_MARGIN = 25


    # Initialize loop variables
    researching = True

    # Display the research allocation menu
    screen.fill(BROWN)
    # Draw the bars
    draw_bars(screen, game_mode)
    linePosition = TOP_LINE_POSITION
    display_ghostbuster_hq_text()
    display_text_typewriter("Research Allocation Menu", 50, linePosition)
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height() // 2), (WIDTH - 30, linePosition - FONT36.get_height() // 2), 3)
    linePosition += (FONT36.get_height() * 2)



    # Index of the currently selected column
    selected_index = 0

    while researching:
        # Clear the screen
        screen.fill(BROWN)
        # Draw the bars
        draw_bars(screen, game_mode)
        linePosition = TOP_LINE_POSITION

        if not PKE_CHANNEL.get_busy():
            PKE_CHANNEL.play(LAB_BUBBLES)



        # Display the research allocation menu
        display_ghostbuster_hq_text()
        display_text("Research Allocation Menu", 50, linePosition)
        pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height() // 2), (WIDTH - 30, linePosition - FONT36.get_height() // 2), 3)
        linePosition += (FONT36.get_height() * 2)

        display_credits_while()


        total_width = len(player.research_aspects) * (COLUMN_WIDTH + COLUMN_MARGIN) - COLUMN_MARGIN
        start_x = (WIDTH - total_width) // 2
        for i, aspect in enumerate(player.research_aspects):
            x = start_x + i * (COLUMN_WIDTH + COLUMN_MARGIN)
            color = WHITE if i == selected_index else BLUE
            pygame.draw.rect(screen, BLACK, (x+10, HEIGHT//4*3 - player.research_allocations[i]*4 +10, COLUMN_WIDTH, player.research_allocations[i]*4 -10))
            

            pygame.draw.rect(screen, color, (x, HEIGHT//4*3 - player.research_allocations[i]*4, COLUMN_WIDTH, player.research_allocations[i]*4))
            
            textcolor = BLACK if i == selected_index else WHITE
            # text = FONT24.render(aspect, True, textcolor)
            lines = aspect.split("\n")  # Split the text into lines
            text = FONT24.render(aspect, True, WHITE)
            text_rect = text.get_rect(center=(x + COLUMN_WIDTH // 2, HEIGHT//4*3))
            yPos = text_rect.y

            for line in lines:
                rendered_text = FONT24.render(line, True, textcolor)
                screen.blit(rendered_text, (x + 10, yPos))
                yPos += FONT36.get_height()


            totalAllocation = 0
            for allocation in player.research_allocations:
                totalAllocation += allocation
                # print(totalAllocation)

            thisPercent = player.research_allocations[i] / totalAllocation
            thisPercent = round(thisPercent*100)
            

            rendered_text = FONT24.render(str(thisPercent), True, textcolor)
            screen.blit(rendered_text, (x + 10, yPos))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Move selection with arrow keys
                if event.key == pygame.K_UP:
                    player.research_allocations[selected_index] = min(100, player.research_allocations[selected_index] + 10)
                    
                elif event.key == pygame.K_DOWN:
                    player.research_allocations[selected_index] = max(10, player.research_allocations[selected_index] - 10)
                    
                # Increase or decrease allocation with left and right arrow keys
                elif event.key == pygame.K_LEFT:
                    selected_index -= 1
                    if selected_index < 0:
                        researching = False
                        game_mode -= 2
                        PKE_CHANNEL.stop()
                    
                elif event.key == pygame.K_RIGHT:
                    selected_index += 1
                    if selected_index > len(player.research_aspects)-1:
                        researching = False
                        starting = False
                        PKE_CHANNEL.stop()

                # Press ESC to exit
                elif event.key == pygame.K_ESCAPE:
                    researching = False
                    PKE_CHANNEL.stop()
                    game_mode = -1

        # Update the display
        pygame.display.flip()
            
def hire_busters_loop():
    global linePosition
    global player
    global game_mode
    global running
    global starting


    screen.fill(BROWN)
    # Draw the bars
    draw_bars(screen, game_mode)

    linePosition = TOP_LINE_POSITION

    hiring_busters = True
    display_ghostbuster_hq_text()
    display_text_typewriter("Hire Ghostbusters:", 50, linePosition)
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height() // 2), (WIDTH - 30, linePosition - FONT36.get_height() // 2), 3)
    linePosition += (FONT36.get_height() * 2)


    # Repopulate the potential hires
    while len(for_hire_roster) < 8:
        new_name = random.choice(list_of_names)
        # Check if the name is unique among potential hires
        if new_name not in [buster.name for buster in for_hire_roster]:
            # Check if the name is unique among player's roster
            if new_name not in [buster.name for buster in player.roster]:
                # Create a new ghostbuster with the unique name
                buster = Ghostbuster(new_name)
                for_hire_roster.append(buster)


    selected_index = 0  # Index of the currently selected hire
    typeLast = False

    while hiring_busters:

        if selected_index > len(for_hire_roster): 
            selected_index = len(for_hire_roster)-1

        screen.fill(BROWN)

        # Draw the bars
        draw_bars(screen, game_mode)

        linePosition = TOP_LINE_POSITION
        display_ghostbuster_hq_text()
        display_text("Hire Ghostbusters:",50, linePosition)
        # Draw the line with gaps on both sides
        pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
        linePosition += (FONT36.get_height() * 2)
    


        display_text("                     |  Brains  |  Muscle  |  Moves  |  Cool  |            Origin                   |               Goal                  |  Hiring Cost  |", 50, linePosition)

        for index, buster in enumerate(for_hire_roster):
            xPos = 250
            yPos = linePosition + (index * (FONT36.get_height() * 2))
            if index == selected_index:
                pygame.draw.rect(screen, WHITE, (75, yPos-(FONT36.get_height()*0.25), WIDTH - 200, FONT36.get_height()*1.5), 2)  # Highlight the selected hire

            screen.blit(buster.images[0], (25, yPos-10))
            rendered_text = FONT36.render(buster.name, True, BLACK)
            screen.blit(rendered_text, (80, yPos))

            for trait, score in buster.traits.items():
                rendered_text = FONT36.render(str(score), True, WHITE)
                screen.blit(rendered_text, (xPos, yPos))
                xPos += 110

            rendered_text = FONT36.render(buster.origin, True, WHITE)
            screen.blit(rendered_text, (xPos, yPos))

            xPos += 280

            rendered_text = FONT36.render(buster.goal, True, WHITE)
            screen.blit(rendered_text, (xPos, yPos))

            xPos += 290

            rendered_text = FONT36.render("$ " + str(buster.hiring_cost), True, WHITE)
            screen.blit(rendered_text, (xPos, yPos))

        display_credits_while()

        
        if typeLast:
            display_hired_busters_add_buster()
        else:
            display_hired_busters()

        typeLast = False

        # Wait for key press to navigate and select hires
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                hiring_busters = False
                running = False

            if event.type == pygame.KEYDOWN:

                

                if event.key == pygame.K_UP:
                    selected_index = max(0, selected_index - 1)
                elif event.key == pygame.K_DOWN:
                    selected_index = min(len(for_hire_roster) - 1, selected_index + 1)
                elif event.key == pygame.K_RETURN:
                    if len(for_hire_roster) > 0:
                        if len(player.roster) < 4: # MAX NUMBER OF GHOSTBUSTERS
                            selected_buster = for_hire_roster.pop(selected_index)
                            player.cash_balance -= selected_buster.hiring_cost
                            player.roster.add(selected_buster)
                            typeLast = True
                            if selected_index >= len(for_hire_roster): 
                                selected_index = len(for_hire_roster)-1
                        else:
                            TRAP_NO_SOUND.play()


                elif event.key == pygame.K_e or pygame.K_RIGHT:
                    hiring_busters = False
                elif event.key == pygame.K_x or pygame.K_LEFT:
                    if running:
                        game_mode -= 2
                        hiring_busters = False

                elif event.key == pygame.K_ESCAPE:
                    if running == True:
                        hiring_busters = False
                        game_mode = -1

        pygame.display.flip()



def show_busters_loop():
    global linePosition
    global player
    global game_mode
    global running
    global sell_mode
    global selected_index


    screen.fill(BROWN)
    linePosition = TOP_LINE_POSITION

    # Draw the bars
    draw_bars(screen, game_mode)

    viewing_busters = True
    display_ghostbuster_hq_text()
    display_text_typewriter("Ghostbusters on Staff:", 50, linePosition)
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height() // 2), (WIDTH - 30, linePosition - FONT36.get_height() // 2), 3)
    linePosition += (FONT36.get_height() * 2)
    selected_index = 0  # Index of the currently selected hire
    selection = 0 

    while viewing_busters:
        # print('in loop')

        if selected_index > len(player.roster): 
            selected_index = len(player.roster)-1

        selection = 0 


        screen.fill(BROWN)
        # Draw the bars
        draw_bars(screen, game_mode)
        linePosition = TOP_LINE_POSITION
        display_ghostbuster_hq_text()
        display_text("Ghostbusters on Staff:", 50, linePosition)
        # Draw the line with gaps on both sides
        pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
        linePosition += (FONT36.get_height() * 2)

        display_text("                     |  Brains  |  Muscle  |  Moves  |  Cool  |            Origin                   |               Goal                  |  Status  |  Experience  |", 50, linePosition)
        
        buster_num = 0
        for index, buster in enumerate(player.roster.sprites()):
            buster_num += 1
            thisLinePos = linePosition
            if index == selected_index:
                pygame.draw.rect(screen, WHITE, (75, thisLinePos-(FONT36.get_height()*0.25), WIDTH - 200, FONT36.get_height()*1.5), 2)  # Highlight the selected hire

            screen.blit(buster.images[0], (25, linePosition-10))
            rendered_text = FONT36.render(buster.name, True, BLACK)
            screen.blit(rendered_text, (80, linePosition))

            xPos = 250
            linePosition = thisLinePos
            for trait, score in buster.traits.items():
                rendered_text = FONT36.render(str(score), True, WHITE)
                screen.blit(rendered_text, (xPos, linePosition))
                xPos += 110

            rendered_text = FONT36.render(buster.origin, True, WHITE)
            screen.blit(rendered_text, (xPos, linePosition))
            xPos += 280

            rendered_text = FONT36.render(buster.goal, True, WHITE)
            screen.blit(rendered_text, (xPos, linePosition))

        
            

            xPos += 270

            status = "Ready"
            status_color = GREEN
            if buster.slimed:
                status = "X Slimed X"
                status_color = RED
            elif buster.levelPoints > 0:
                status = "+ Level Up +"
                status_color = GREEN
                if buster.levelPoints > 1:
                    status = "++ Level Up ++"

            rendered_text = FONT36.render(status, True, status_color)
            screen.blit(rendered_text, (xPos, linePosition))

            xPos += 170

            rendered_text = FONT36.render(str(buster.experience), True, WHITE)
            screen.blit(rendered_text, (xPos, linePosition))

            linePosition += (rendered_text.get_height() * 2)

        display_credits_while()


        linePosition = HEIGHT - FONT36.get_height()*2
        xPos = 50
        purchase_text = "Select to Heal/Level Ghostbuster   - Press: (R) to Remove, (+) Change Outfit"
        prompt_color = BLACK
        if sell_mode: 
            purchase_text = "Press # to Fire Ghostbuster, Press: R to Cancel"
            prompt_color = RED

        rendered_text = FONT36.render(purchase_text, True, BLACK)
        screen.blit(rendered_text, (xPos, linePosition))

        # Wait for key press to navigate and select hires
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                viewing_busters = False
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = max(0, selected_index - 1)
                elif event.key == pygame.K_DOWN:
                    selected_index = min(len(player.roster) - 1, selected_index + 1)



                elif event.key == pygame.K_LEFT:
                    if running:
                        game_mode -= 2
                        viewing_busters = False
                elif event.key == pygame.K_RIGHT:
                    viewing_busters = False

                elif event.unicode.lower() == "s" or event.unicode.lower() == "r":
                    sell_mode = not sell_mode

                elif (event.key == pygame.K_PLUS) or (event.key == pygame.K_KP_PLUS):
                    
                    if len(player.roster) > 0:
                        selected_buster = player.roster.sprites().pop(selected_index)
                        if not sell_mode or selected_buster.slimed:
                            selected_buster.change_worn_outfit()


                elif event.key == pygame.K_RETURN:
                    if len(player.roster) > 0:
                        selected_buster = player.roster.sprites().pop(selected_index)
                        if not sell_mode:
                            if selected_buster.slimed:
                                player.cash_balance -= 1000
                                selected_buster.slimed = False
                                VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)
                                CASH_SOUND.play()

                            elif selected_buster.levelPoints > 0:
                                # trait_list = list(selected_buster.traits.keys())
                                # trait = random.choice(trait_list)
                                # selected_buster.traits[trait] += 1
                                # selected_buster.levelPoints -= 1
                                # VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)

                                selected_trait = display_trait_selection(screen, selected_buster.traits)
                                if selected_trait:
                                    selected_buster.traits[selected_trait] += 1  # Increase the selected trait by 1
                                    selected_buster.levelPoints -= 1
                                    VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)

                            else:
                                TRAP_NO_SOUND.play()
                        elif sell_mode:
                            selected_buster.kill()
                            CLOCK_SOUND.play()
                            sell_mode = False
                        else:
                            TRAP_NO_SOUND.play()

                elif event.key == pygame.K_ESCAPE:
                    viewing_busters = False
                    game_mode = -1

                elif event.unicode.isdigit():
                    input_text = event.unicode
                    if not sell_mode and int(input_text) <= len(player.roster.sprites()) and int(input_text) != 0:
                        selected_buster = player.roster.sprites().pop(int(input_text) - 1)
                        if selected_buster.slimed:
                            player.cash_balance -= 1000
                            selected_buster.slimed = False
                            VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)
                            CASH_SOUND.play()
                        else:
                            TRAP_NO_SOUND.play()
                    elif sell_mode:
                        selected_buster = player.roster.sprites().pop(int(selection) - 1)
                        selected_buster.kill()
                        CLOCK_SOUND.play()
                        sell_mode = False
                    else:
                        TRAP_NO_SOUND.play()

        pygame.display.flip()



    
def base_improvment_shopping_loop():
    global linePosition
    global player
    global shopping_equipment
    global selected_index


    screen.fill(BROWN)
    # Draw the bars
    draw_bars(screen, game_mode)

    linePosition = TOP_LINE_POSITION

    shopping_equipment = True
    fresh_purchase = False

    if len(player.base) == 0:
        spawn_fresh_base()

    
    display_ghostbuster_hq_text()
    display_text_typewriter(f"Base Improvements:", 50, linePosition)
    # Draw the line with gaps on both sides
    pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
    linePosition += (FONT36.get_height() * 2)

    # Get player's choice of monitoring equipment
    improvement_choices = {
        1: {"name": "Office", "cost": 200, 'unique': False, 'color': GREY},
        2: {"name": "Auto Mechanic Shop", "cost": 200, 'unique': True, 'color': GREY},
        3: {"name": "Vehicle Garage", "cost": 200, 'unique': True, 'color': WHITE},
        4: {"name": "Communications Center", "cost": 500, 'unique': True, 'color': GREY},
        5: {"name": "Computer Server / Archive", "cost": 1000, 'unique': True, 'color': BLUE},
        6: {"name": "Emergency Response Center", "cost": 1100, 'unique': True, 'color': BLUE},
        7: {"name": "Research Lab", "cost": 1200, 'unique': True, 'color': BLUE},
        8: {"name": "Training Facility", "cost": 1000, 'unique': True, 'color': GREEN},
        9: {"name": "Protection Grid / Containment System", "cost": 2000, 'unique': True, 'color': RED}
    
    }


    # display_available_equip_list(improvement_choices)
    # display_shopping_credit_vehicle_header()
    # display_car_in_garage()

    
    while shopping_equipment:

        if selected_index > len(improvement_choices)-1: 
            selected_index = len(improvement_choices)-1

        if selected_index < 0: 
            selected_index = 0


        screen.fill(BROWN)
        # Draw the bars
        draw_bars(screen, game_mode)
        linePosition = TOP_LINE_POSITION
        display_ghostbuster_hq_text()
        display_text(f"Base Improvements:", 50, linePosition)
        # Draw the line with gaps on both sides
        pygame.draw.line(screen, BLACK, (30, linePosition - FONT36.get_height()//2), (WIDTH - 30, linePosition - FONT36.get_height()//2), 3)
        linePosition += (FONT36.get_height() * 2)

        display_available_improvement_list(improvement_choices)


        display_base_grid()
        display_credits_while()
        if fresh_purchase:
            display_base_add_()
            fresh_purchase = False
            ...
        else:
            display_base()
            ...

            fresh_purchase = purchase_improvement(improvement_choices)
            
        pygame.display.flip()
            
# Split the improvement name into multiple lines based on the width of the box
def split_text_into_lines(text, max_width, this_font):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        test_line = current_line + " " + word
        if this_font.size(test_line)[0] <= (max_width *.95) :
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    return lines
    



        
    
def generate_map():
    global BUILDING_SIZE_X
    global BUILDING_SIZE_Y
    global STREET_SIZE
    global all_sprites
    global breadcrumbs
    global buildings
    global active_buildings
    global player
    global clock
    global mapGhosts
    global pk_energy
    global textShown
    global marshmallowed
    global end_game
    global gatekeeper
    global keymaster
    global mrStayPuft
    global game_over
    

    # Define constants
    GRID_WIDTH = 9#11
    GRID_HEIGHT = 6 #7
    STREET_SIZE = 48
    PLAYER_SIZE = 36

    marshmallowed = False
    end_game = False
    mrStayPuft = None
    game_over = False
    

    hq = None
    
    if player == None:
        player = Player()

    clock = pygame.time.Clock()

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    buildings = pygame.sprite.Group()
    active_buildings = pygame.sprite.Group()
    mapGhosts = pygame.sprite.Group()
    breadcrumbs = pygame.sprite.Group()
    textShown = pygame.sprite.Group()

    # Initialize PK energy reading
    pk_energy = 0000  # You can set the initial PK energy value
    last_pk_energy_increase_time = pygame.time.get_ticks()

    # Create buildings and add to sprite groups
    num_buildings = 0

    # Adjust building size to account for the extra street size
    BUILDING_SIZE_X = (WIDTH - (GRID_WIDTH + 1) * STREET_SIZE) // GRID_WIDTH
    BUILDING_SIZE_Y = (HEIGHT - (GRID_HEIGHT + 1) * STREET_SIZE) // GRID_HEIGHT

    # Calculate the starting position to center the grid
    start_x = STREET_SIZE
    start_y = STREET_SIZE


    # Place Buildings onto the city grid

    # hqX, hqY = 1, GRID_HEIGHT-2

    possible__hq_locations = [
    (1, GRID_HEIGHT - 2),          
    (1, 1),                        
    (GRID_WIDTH - 2, 1),           
    (GRID_WIDTH - 2, GRID_HEIGHT - 2)  
    ]

    # Randomly choose one of the locations
    hqX, hqY = random.choice(possible__hq_locations)

    if GRID_HEIGHT % 2 == 0: ZuulX, ZuulY = GRID_WIDTH // 2, GRID_HEIGHT // 2 - 1
    else: ZuulX, ZuulY = GRID_WIDTH // 2, GRID_HEIGHT // 2

    

    building_positions = [
        ("Gas", 0, 0),
        ("Gas", 0, 0),
        ("Park", 0, 0),
        ("Hotel", 0, 0),
        ("Library", 0, 0),
        ("Train", 0, 0),
        ("Museum", 0, 0),
        ("City Hall", 0, 0),
        ("Church", 0, 0),
        ("University", 0, 0),
        ("Hospital", 0, 0),
        ("Bank", 0, 0),
        ("Police", 0, 0),
    ]

    # Place custom buildings
    for i in range(len(building_positions)):
        while True:
            x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
            if (
                (x, y) not in [(hqX, hqY), (ZuulX, ZuulY)] and
                all((x, y) != (px, py) for _, px, py in building_positions[:i])
            ):
                building_positions[i] = (building_positions[i][0], x, y)
                break

    # Create and add buildings to sprite groups
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            building = Building(
                start_x + i * (BUILDING_SIZE_X + STREET_SIZE),
                start_y + j * (BUILDING_SIZE_Y + STREET_SIZE),
                BUILDING_SIZE_X,
                BUILDING_SIZE_Y,
            )

            if i == hqX and j == hqY:
                building.name = "HQ"

            elif i == ZuulX and j == ZuulY:
                building.name = "Zuul"

            else:
                for name, x, y in building_positions:
                    if i == x and j == y:
                        building.name = name

            # if building.name == "Park": # TEST 
            #     active_buildings.add(building)

            all_sprites.add(building)
            buildings.add(building)



    for building in buildings:
        if building.name == "HQ":
            # Create player and add to sprite groups
            player.mapSprite = Player_On_Map(building.rect.x + building.rect.width // 2, building.rect.bottom + 2 , PLAYER_SIZE)
            all_sprites.add(player.mapSprite)
            hq = building

        if building.name == "Zuul":
            keymaster = Keymaster(building.rect.x - 10 + building.rect.width // 2, building.rect.bottom + 2, building)
            mapGhosts.add(keymaster)
            all_sprites.add(keymaster)

            gatekeeper = Gatekeeper(building.rect.x + 10 + building.rect.width // 2, building.rect.bottom + 2, building)
            mapGhosts.add(gatekeeper)
            all_sprites.add(gatekeeper)

    return hq


def navigate_map():
    global BUILDING_SIZE_X
    global BUILDING_SIZE_Y
    global STREET_SIZE
    global all_sprites
    global buildings
    global active_buildings
    global player
    global mapGhosts
    global textShown
    global navigating
    global running
    global clock
    global pk_energy
    global trap_warning_timer
    global trap_warning_interval
    global trap_show_warning
    global marshmallowed
    global end_game
    global mrStayPuft
    global keymaster
    global gatekeeper
    global game_over
    global fee_card 


    # Player_On_Map # looking for me?? 

    target_building = None


    for building in buildings:
        
        
        if building.name == "Zuul":
            if not game_over: # GB1
                target_building = building
                building.target_building = True
            else:
                building.target_building = False
                


    last_pk_energy_increase_time = pygame.time.get_ticks()
    last_fined_time = pygame.time.get_ticks()

    # Warning text variables
    trap_warning_timer = 0
    trap_warning_interval = 10  # Adjust the flashing interval as needed
    trap_show_warning = False

    FORK_CHANNEL.stop()

    if not MUSIC.get_busy():
        if MUSIC_ON:
            MUSIC.play(THEME,loops=-1)
    else:
        MUSIC.unpause()
    
    MUSIC.unpause()

    # Game loop
    navigating = True
    while navigating:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                navigating = False
                running = False

        

        if not game_over:
            for building in buildings:
                if building.name == "Zuul":
                    target_building = building
                    building.target_building = True


        # Spawn a new ghost randomly with a chance of 1 in 100 per frame
        if not marshmallowed and not end_game:
            if random.randint(1, 100) == 1 and len(mapGhosts) <= 8:
                ghost = MapGhost(target_building)
                mapGhosts.add(ghost)
                all_sprites.add(ghost)

            if len(active_buildings) < NUMBER_OF_MAX_ACTIVE_BUILDINGS:
                if random.randint(1, 100) <= 1:
                    building = random.choice(buildings.sprites())
                    if (building.name not in ["HQ", "Gas", "Zuul"]) and not building.target_building and not (building.isSmashed):
                        active_buildings.add(building)

        if pk_energy >= ZUUL_END_GAME_PK_REQUIREMENT and not end_game and not game_over:
            end_game = True
            active_buildings.empty()


        if end_game and not marshmallowed and not game_over:

            if (gatekeeper is None) and (keymaster is None):
                # SPAWN THE STAY PUFT MARSHMALLOW MAN! 

                mrStayPuft = StayPuft(target_building)
                mapGhosts.add(mrStayPuft)
                all_sprites.add(mrStayPuft)
                marshmallowed = True
                if target_building.name == "Zuul": active_buildings.add(target_building)


        if game_over:
            for building in buildings:
        
                if building.name == "Zuul":
                    building.target_building = False

                        
                elif building.name == "Museum":
                    target_building = building
                    building.target_building = True




        # increase PK Level each other second
        current_time = pygame.time.get_ticks()
        time_elapsed_since_last_increase = current_time - last_pk_energy_increase_time


        if time_elapsed_since_last_increase >= 1000:  # Increase PK energy every 1000 milliseconds (1 second)
            pk_energy += 1
            last_pk_energy_increase_time = current_time


        # CREATE A RANDOM FINE, DRAINING INCOME
        time_elapsed_since_last_fine = current_time - last_fined_time
        if time_elapsed_since_last_fine >= 30000:
            if fee_card == None:
                last_fined_time = current_time
                if random.randint(0,100) > 50:
                    fee_card = generate_random_fine()


        # Update sprites
        all_sprites.update()



        # Draw everything
        screen.fill(STREET_GREY)
        all_sprites.draw(screen)

        
        draw_pk_meter()
        draw_credits()
        draw_fuel_meter()
        draw_proton_charge_meter(DARK_RED)
        draw_trap_warning()

        # Draw and manage the fee card
        if fee_card:
            fee_card.update()  # Updates the card's position and animation
        if fee_card:
            fee_card.draw(screen)

 


        pygame.display.flip()
        clock.tick(30)
    

def drive_to_destination(driving_time_to_destination, number_of_sucked_ghosts, give_fuel):
    # Initial car position
    global player
    global all_sprites
    global street_ghosts
    global BUILDING_MARGIN
    global clock
    global pk_energy
    global barrels
    global vacuum_on


    give_fuel_barrel = give_fuel


    BUILDING_MARGIN = 400

    siren_size = 30

    siren_logo = pygame.transform.scale(GB_LOGO, (siren_size, siren_size))
    siren_circle_color = BLUE  # Initial color
    siren_color_timer = 0

    # Create a blue circle surface
    siren_circle = pygame.Surface((siren_size, siren_size), pygame.SRCALPHA)
    pygame.draw.circle(siren_circle, siren_circle_color, (siren_size // 2, siren_size // 2), siren_size // 2)

    # Combine the blue circle and the centered Ghostbusters logo
    siren_image = pygame.Surface((siren_size, siren_size), pygame.SRCALPHA)
    siren_image.blit(siren_circle, (0, 0))
    siren_image.blit(siren_logo, ((siren_size - siren_logo.get_width()) // 2, (siren_size - siren_logo.get_height()) // 2))


    

    # Create sprite groups
    street_ghosts = pygame.sprite.Group()
    centerLine = pygame.sprite.Group()
    dash = Center_line_dash(0)
    centerLine.add(dash)
    dash = Center_line_dash(HEIGHT//3)
    centerLine.add(dash)
    dash = Center_line_dash((HEIGHT//3)*2)
    centerLine.add(dash)

    barrels = pygame.sprite.Group()


    numofcurbstones = 8
    gap = 6
    size = (HEIGHT-(numofcurbstones*gap)) // numofcurbstones 

    
    # print(numofcurbstones, gap)
    y = gap
    i = 0
    while i < numofcurbstones + 1:
        leftcurb = CurbStone(BUILDING_MARGIN, y, size)
        rightcurb = CurbStone(WIDTH-BUILDING_MARGIN, y, size)
        centerLine.add(leftcurb)
        centerLine.add(rightcurb)
        y += size + gap  
        i += 1
        # print(y)





    if player.vehicle is not None:
        # Assuming you have a dictionary mapping vehicle names to images
        # Get the image corresponding to the player's vehicle
        vehicle_image = vehicle_images.get(player.vehicle['name'].lower())  # Convert to lowercase for case-insensitivity

        if vehicle_image is not None:
            # Resize the vehicle image
            vehicle_image = pygame.transform.scale(vehicle_image, (vehicle_image.get_width() * 2, vehicle_image.get_height() * 2))


    car_x = WIDTH//2 + 30
    car_y = HEIGHT - vehicle_image.get_height() - 20

    # Street variables
    street_y = 0
    car_speed = player.vehicle["speed"] // CAR_SPEED_ON_MAP_FACTOR
    

    # Main game loop
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()  # Record the start time
    driving_duration = min(driving_time_to_destination,12)  # Set the driving duration in seconds, 14 is about 10 sirens
    driving_duration = max(3,driving_duration)  # Set the driving duration in seconds
    driving = True
    ghost_interval = 0
    ghost_spawn_time = 1
    fuel_interval = 0
    vacuum_on = False
    proton_charge_color = DARK_RED

    if number_of_sucked_ghosts > 0:
        ghost_interval = (driving_duration // (number_of_sucked_ghosts+1))
        # print("number_of_sucked_ghosts:" + str(number_of_sucked_ghosts))
        # print("driving_duration:" + str(driving_duration))
        # print("interval:" + str(ghost_interval))

    if give_fuel_barrel:
        fuel_interval = driving_duration // random.randint(2,4)

    ghost_spawn_time = ghost_interval - 1

    last_pk_energy_increase_time = pygame.time.get_ticks()

    while driving:

        # increase PK Level each other second
        current_time = pygame.time.get_ticks()
        time_elapsed_since_last_increase = current_time - last_pk_energy_increase_time

        if time_elapsed_since_last_increase >= 1000:  # Increase PK energy every 1000 milliseconds (1 second)
            pk_energy += 1
            last_pk_energy_increase_time = current_time

        if not SIREN.get_busy():
            SIREN.play(SIREN_SOUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        


        # Check if the driving duration has passed
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert to seconds
        if elapsed_time >= driving_duration:

            if car_x < WIDTH - vehicle_image.get_width() - BUILDING_MARGIN: ## PULL OVER TO SIDE OF ROAD
                vacuum_on = False
                PROTON_PACK_CHANNEL.stop()

                car_x += 5
                current_speed = 4
                if car_y < HEIGHT - vehicle_image.get_height(): 
                    car_y += 5
            else:

                # WHAT HAPPENS WHEN THE PLAYER REACHES DESTINATION??

                

                driving = False
                vacuum_on = False
                PROTON_PACK_CHANNEL.stop()

        else:
            
            if (number_of_sucked_ghosts > 0) and (elapsed_time >= ghost_spawn_time):
                #spawn a ghost that needs sucking
                # print("spawn ghost" + str(elapsed_time))
                street_ghost = Street_Ghost()
                street_ghosts.add(street_ghost)
                number_of_sucked_ghosts -= 1
                ghost_spawn_time += ghost_interval

            if give_fuel_barrel and (elapsed_time >= fuel_interval):
                fuel_barrel = FuelBarrel()
                barrels.add(fuel_barrel)
                give_fuel_barrel = False



            # Handle player input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and car_x > 0 + BUILDING_MARGIN + 20 :
                car_x -= 8
            if keys[pygame.K_RIGHT] and car_x < WIDTH - vehicle_image.get_width() - BUILDING_MARGIN:
                car_x += 8


            if keys[pygame.K_UP] and car_y > HEIGHT//4:
                car_y -= 8

            if keys[pygame.K_DOWN] and car_y < HEIGHT - vehicle_image.get_height():
                car_y += 8

            if keys[pygame.K_SPACE]:
                if fee_card:
                    fee_card.clear_card_manually()

            if keys[pygame.K_LCTRL]:
                if player.has("Ghost Vacuum"):
                    vacuum_on = True
                    player.proton_charge -= VACUUM_PROTON_CHARGE_PER_TICK
                    proton_charge_color = random.choice([RED, RED, DARK_RED, ORANGE, YELLOW, WHITE])
                
                    if not PROTON_PACK_CHANNEL.get_busy():
                        PROTON_PACK_CHANNEL.play(PROTON_FIRE_SOUND)
                else:
                    vacuum_on = False
                    PROTON_PACK_CHANNEL.stop()
                    proton_charge_color = DARK_RED

            else:
                vacuum_on = False
                PROTON_PACK_CHANNEL.stop()
                proton_charge_color = DARK_RED


            current_speed = max(14,((HEIGHT - car_y)/100)*car_speed)
            current_speed = min(24,current_speed)
            


        # Draw the street background
        screen.fill(STREET_GREY)

        screen.fill(BROWN,(0,0,BUILDING_MARGIN,HEIGHT))
        screen.fill(BROWN,(WIDTH-BUILDING_MARGIN,0,BUILDING_MARGIN,HEIGHT))

        centerLine.update(current_speed)
        centerLine.draw(screen)

        

        # Draw the Ghostbusters car
        showCar(vehicle_image, car_x, car_y)

        vacuum_center = [car_x + vehicle_image.get_width()//2, car_y + 30]

        # Change the color of the blue circle every few frames
        siren_color_timer += 1
        if siren_color_timer % 20 == 0:
            # Red color during every even frame
            if siren_color_timer % 60 == 0:
                siren_circle_color = RED
            elif siren_color_timer % 40 == 0:
                # White color during every 40th frame
                siren_circle_color = WHITE
            else:
                # Blue color during every odd frame
                siren_circle_color = TRUE_BLUE

        siren_circle = pygame.Surface((siren_size, siren_size), pygame.SRCALPHA)
        pygame.draw.circle(siren_circle, siren_circle_color, (siren_size // 2, siren_size // 2), siren_size // 2)

        siren_image = pygame.Surface((siren_size, siren_size), pygame.SRCALPHA)
        siren_image.blit(siren_circle, (0, 0))
        siren_image.blit(siren_logo, ((siren_size - siren_logo.get_width()) // 2, (siren_size - siren_logo.get_height()) // 2))


        # Draw the flashing circle and logo over the car
        screen.blit(siren_image, (car_x + vehicle_image.get_width() // 2 - siren_size // 2, car_y - 20 + vehicle_image.get_height()//2))


        street_ghosts.update(vacuum_center, vacuum_on)
        street_ghosts.draw(screen)

        barrels.update(vacuum_center)
        barrels.draw(screen)

        textShown.update()
        textShown.draw(screen)



        draw_pk_meter()
        draw_credits()
        draw_fuel_meter()
        draw_proton_charge_meter(proton_charge_color)
        draw_trap_warning()

        # Draw and manage the fee card
        if fee_card:
            #dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds
            fee_card.update()  # Updates the card's position and animation
        if fee_card:
            fee_card.draw(screen)
            # if fee_card.is_expired():
            #     fee_card = None  # Remove the card after the display time

        pygame.display.flip()
        clock.tick(60)  # Adjust the frame rate as needed


def climb_stairs_in_building(ghostbusters_entered_door): # ASCENDING THE ZUUL BUILDING
    global player
    global selected_ghostbuster
    global ghosts_at_building
    global ghostbusters_at_building
    global num_ghosts_busted
    global elapsed_time
    global floors_of_building
    global goo_in_building
    global floor_gap
    # global leavePackSoundOn
    global marshmallowed
    global end_game
    global game_over

    # global traps_at_building


    # Create sprite groups
    ghostbusters_at_building = pygame.sprite.Group()
    ghosts_at_building = pygame.sprite.Group()
    traps_at_building = pygame.sprite.Group()
    floors_of_building = pygame.sprite.Group()
    floor_level_sprites = pygame.sprite.Group()  # Create a sprite group for floor level sprites

    doors_in_building = pygame.sprite.Group()
    goo_in_building = pygame.sprite.Group()


    # Create Ghostbuster sprites

    roster = ghostbusters_entered_door.sprites() #player.roster.sprites()
    random.shuffle(roster) # randomize buster selection for each mission
    length_roster = len(roster)

    ghostbuster1 = None 
    ghostbuster2 = None
    ghostbuster3 = None
    ghostbuster4 = None

    for buster in roster:
        if ghostbuster1 == None:
            if not buster.slimed:
                ghostbuster1 = buster
                # ghostbuster1.set_for_building(BLUE, WIDTH - 120 - 150, HEIGHT - 110, has_trap=True)
                ghostbuster1.set_for_stairs(BLUE, WIDTH - 120 - 150, HEIGHT - 110)
                ghostbusters_at_building.add(ghostbuster1)
        elif ghostbuster2 == None:
                if not buster.slimed:
                    ghostbuster2 = buster
                    ghostbuster2.set_for_stairs(RED, WIDTH - 120 - 100, HEIGHT - 110)
                    ghostbusters_at_building.add(ghostbuster2)
        elif ghostbuster3 == None:
                if not buster.slimed:
                    ghostbuster3 = buster
                    ghostbuster3.set_for_stairs(YELLOW, WIDTH - 120 - 50, HEIGHT - 110)
                    ghostbusters_at_building.add(ghostbuster3)
        elif ghostbuster4 == None:
                if not buster.slimed:
                    ghostbuster4 = buster
                    ghostbuster4.set_for_stairs(YELLOW, WIDTH - 120 - 0, HEIGHT - 110)
                    ghostbusters_at_building.add(ghostbuster4)

    selected_ghostbuster = ghostbuster1


    floor_level_y = HEIGHT - 110 + ghostbuster1.image.get_height()
    num_of_floors = NUM_FOORS_IN_ZUUL_BUILDING -1 # always even before -1
    floor_gap = 208
    num_of_steps = 13
    step_height = floor_gap / num_of_steps
    stair_width = ((step_height * 11) // 7)*1.8
    first_floor = Floor_in_building(0,floor_level_y, WIDTH, step_height*2)
    floors_of_building.add(first_floor)

    door_image = random.choice([DOOR1_IMAGE, DOOR2_IMAGE])
    doorX = WIDTH - door_image.get_width() - 50
    doorY = floor_level_y - door_image.get_height()
    bottomDoor = Door(doorX,doorY,door_image)
    doors_in_building.add(bottomDoor)

    floor_level_y -= floor_gap
    level = 1



    while level <= num_of_floors:


        # ADD GHOSTS
        if level > 2:
            # Create Ghost sprite
            num_ghosts = random.choice([0,1,1])
            count = 0

            while count < num_ghosts:
                ghost_at_building = Ghost_at_building(inside=True, inside_level=floor_level_y)
                ghosts_at_building.add(ghost_at_building)
                count += 1

        # ADD THE TOP FLOOR EXIT DOOR
        if level == num_of_floors:
            door_image = random.choice([DOOR1_IMAGE, DOOR2_IMAGE])
            doorX = WIDTH - door_image.get_width() - 50
            doorY = floor_level_y - door_image.get_height()
            topDoor = Door(doorX,doorY,door_image)
            doors_in_building.add(topDoor)

            floor = Floor_in_building(0,floor_level_y - floor_gap - step_height*2  , WIDTH, step_height*2 , color=STREET_GREY)
            floors_of_building.add(floor)


        if (level % 2) == 0:
            # STAIR ON THE RIGHT
            floor = Floor_in_building(0,floor_level_y, WIDTH-WIDTH//3, step_height)
            floors_of_building.add(floor)

            # Create a sprite for dripping goo
            if level > 2 and (random.randint(0,100) <= 50):
                goo_sprite = Drip_of_goo(20,WIDTH-WIDTH//3,floor_level_y+step_height)  # Adjust position as needed
                goo_in_building.add(goo_sprite)

            floor_level_sprite = FloorLevelSprite(level+1, WIDTH-130, floor_level_y-50)  # Adjust the position as needed
            floor_level_sprites.add(floor_level_sprite)

            num_of_stairs = floor_gap // step_height - 1
            step_num = 1
            while step_num <= num_of_stairs:
                stair = Floor_in_building(WIDTH-WIDTH//3-stair_width+stair_width//2*step_num,floor_level_y+step_height*step_num,stair_width,step_height,color=STREET_GREY)
                floors_of_building.add(stair)
                step_num += 1



            floor = Floor_in_building(WIDTH-WIDTH//3+WIDTH//6,floor_level_y, WIDTH, step_height)
            floors_of_building.add(floor)

            # Create a sprite for dripping goo
            if level > 2 and (random.randint(0,100) <= 50):
                goo_sprite = Drip_of_goo(WIDTH-WIDTH//3+WIDTH//6+20,WIDTH-20,floor_level_y+step_height)  # Adjust position as needed
                goo_in_building.add(goo_sprite)

        else:
            # STAIR ON THE LEFT
            floor = Floor_in_building(0,floor_level_y, WIDTH//6, step_height)
            floors_of_building.add(floor)

            # Create a sprite for dripping goo
            if level > 2 and (random.randint(0,100) <= 50):
                goo_sprite = Drip_of_goo(20,WIDTH//6,floor_level_y+step_height)  # Adjust position as needed
                goo_in_building.add(goo_sprite)

            floor_level_sprite = FloorLevelSprite(level+1, 50, floor_level_y-50)  # Adjust the position as needed
            floor_level_sprites.add(floor_level_sprite)

            num_of_stairs = floor_gap // step_height - 1
            step_num = 1
            while step_num <= num_of_stairs:
                stair = Floor_in_building(WIDTH//3-stair_width//2*step_num,floor_level_y+step_height*step_num,stair_width,step_height,color=STREET_GREY)
                floors_of_building.add(stair)
                step_num += 1

            floor = Floor_in_building(WIDTH//3,floor_level_y, WIDTH, step_height)
            floors_of_building.add(floor)

            # Create a sprite for dripping goo
            if level > 2 and (random.randint(0,100) <= 50):
                goo_sprite = Drip_of_goo(WIDTH//3+20,WIDTH-20,floor_level_y+step_height)  # Adjust position as needed
                goo_in_building.add(goo_sprite)

        floor_level_y -= floor_gap
        level +=1


    ascent_started = False

    elapsed_time = 0
    clock = pygame.time.Clock()
    running = True
    start_time = pygame.time.get_ticks()  # Get the start time in milliseconds
    CHARGE_SOUND.play()
    playonce = False
    num_ghosts_busted = 0

    while running:



        # Move sprites upwards if above the 3rd floor
        if selected_ghostbuster.rect.y < 400:
            ascent_started = True

            # Calculate the offset to move sprites
            move_up_offset = selected_ghostbuster.speed * -1

            if selected_ghostbuster.rect.y < 0:
                move_up_offset = selected_ghostbuster.speed * -5

            # Move ghostbusters
            for buster in ghostbusters_at_building:
                buster.rect.y -= move_up_offset

            # Move ghosts
            for ghost in ghosts_at_building:
                ghost.rect.y -= move_up_offset
                ghost.orig_y -= move_up_offset

            # Move floors
            for floor in floors_of_building:
                floor.rect.y -= move_up_offset

            for goo in goo_in_building:
                goo.rect.y -= move_up_offset

            for door in doors_in_building:
                door.rect.y -= move_up_offset

            for sign in floor_level_sprites:
                sign.rect.y -= move_up_offset

            floor_level_y += move_up_offset

        elif ascent_started and selected_ghostbuster.rect.y > 600:
            # Calculate the offset to move sprites
            move_up_offset = selected_ghostbuster.speed * 1

            if selected_ghostbuster.rect.y > HEIGHT:
                move_up_offset = selected_ghostbuster.speed * 5

            # Move ghostbusters
            for buster in ghostbusters_at_building:
                buster.rect.y -= move_up_offset

            # Move ghosts
            for ghost in ghosts_at_building:
                ghost.rect.y -= move_up_offset
                ghost.orig_y -= move_up_offset

            # Move floors
            for floor in floors_of_building:
                floor.rect.y -= move_up_offset

            for goo in goo_in_building:
                goo.rect.y -= move_up_offset

            for door in doors_in_building:
                door.rect.y -= move_up_offset

            for sign in floor_level_sprites:
                sign.rect.y -= move_up_offset

            floor_level_y += move_up_offset
            



        elapsed_time = pygame.time.get_ticks() - start_time


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                PROTON_PACK_CHANNEL.stop()
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    available_ghostbusters = [ghostbuster1, ghostbuster2, ghostbuster3]

                    
                    # Filter out None values
                    available_ghostbusters = [ghostbuster for ghostbuster in available_ghostbusters if ghostbuster is not None]
                    
                    # THEN Filter out slimed
                    available_ghostbusters = [ghostbuster for ghostbuster in available_ghostbusters if not ghostbuster.slimed]
                    

                    if available_ghostbusters:
                        current_index = available_ghostbusters.index(selected_ghostbuster) if selected_ghostbuster in available_ghostbusters else -1
                        next_index = (current_index + 1) % len(available_ghostbusters)
                        selected_ghostbuster = available_ghostbusters[next_index]

                elif event.key == pygame.K_RETURN:
                #     # Drop the trap when Enter is pressed, should use no traps inside zuul building


                    if player.has("Aerosol Slime Cleaner"):
                        slimedBody = pygame.sprite.spritecollide(selected_ghostbuster, ghostbusters_at_building, False)
                        for body in slimedBody:
                            if (body != selected_ghostbuster) and body.slimed:
                                body.slimed = False
                                if selected_ghostbuster.last_left:
                                    body.rect.x = selected_ghostbuster.rect.right + 50
                                else:
                                    body.rect.x = selected_ghostbuster.rect.left - 50
                                VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)
                        

                elif event.key == (pygame.K_LCTRL or pygame.K_RCTRL):

                    if not selected_ghostbuster.proton_pack_on and not selected_ghostbuster.complete and not selected_ghostbuster.has_trap and not selected_ghostbuster.slimed:
                        selected_ghostbuster.proton_pack_on = True

                    elif selected_ghostbuster.proton_pack_on and not selected_ghostbuster.complete :
                        selected_ghostbuster.proton_pack_on = False
                        # leavePackSoundOn = False
                        # for buster in ghostbusters_at_building.sprites():
                        #     if buster.proton_pack_on:
                        #         leavePackSoundOn = True

                        # if not leavePackSoundOn:
                        #     PROTON_PACK_CHANNEL.stop()

                elif event.key == pygame.K_SPACE:
                    for trap in traps_at_building.sprites():
                        trap.toggle_trap()



        keys = pygame.key.get_pressed()


        # IF GHOSTBUSTERS REACH THE TOP LEVEL SAFELY:
        all_busters_climbed_safe = True
        num_safe_busters = 0 
        for buster in ghostbusters_at_building.sprites():

            if buster == selected_ghostbuster:
                ...
                # print(buster.climbed_height, num_of_floors*208)

            if buster.slimed:
                ...

            elif (buster.rect.x < 1380):
                # all_busters_climbed_safe = False
                # break
                ...
            elif (buster.climbed_height < num_of_floors*208): #num_of_floors == 22 - 1  is 4369  208 consider calculating based on #of levels instead of raw #
                # all_busters_climbed_safe = False
                # break
                ...
            else:
                num_safe_busters += 1

        if (num_safe_busters >= NUM_BUSTER_REQUIRED_FOR_ZUUL_ROOF): #all_busters_climbed_safe:
            MUSIC.pause()
            PKE_CHANNEL.stop()

            for buster in ghostbusters_at_building:
                buster.complete = True
                buster.proton_pack_on = False
                # PROTON_PACK_CHANNEL.stop()

            if not playonce:
                VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)
                playonce = True
                for buster in ghostbusters_at_building.sprites():
                    buster.gain_experience(random.randint(5,10) + 25)

            if VOICE_CHANNEL.get_busy() and playonce:
                ...
            elif (not VOICE_CHANNEL.get_busy()) and playonce:
                ## END OF PLOT ##
                running = False
                return True, num_ghosts_busted

        ### IF TOO MANY GHOSTBUSTERS ARE SLIMED:
        numOfGoodBusters = len(ghostbusters_at_building.sprites())  
        for buster in ghostbusters_at_building.sprites():
            if buster.slimed: numOfGoodBusters -= 1
            if numOfGoodBusters < 1 and not VOICE_CHANNEL.get_busy(): #  MINIMUM OF TWO REQUIRED FOR THE END GAME
                VOICE_CHANNEL.play(VOICE_LAUGH)
                running = False # EXIT WITH A MISSION FAILURE
                for buster in ghostbusters_at_building:
                    buster.complete = True
                    buster.proton_pack_on = False
                    # PROTON_PACK_CHANNEL.stop()
                return False, 0
                break



        # Update sprites
        # traps_at_building.update()
        ghostbusters_at_building.update(keys)
        ghosts_at_building.update()
        floors_of_building.update()
        goo_in_building.update()
        

        
        # Draw everything ############################################################
        screen.fill(BROWN)
        floors_of_building.draw(screen)
        screen.fill(STREET_GREY, (0,0, 40, HEIGHT)) # LEFT WALL
        screen.fill(STREET_GREY, (WIDTH-40,0, 40, HEIGHT)) # RIGHT WALL
        floor_level_sprites.draw(screen)
        doors_in_building.draw(screen)
        goo_in_building.draw(screen)
        
        ghostbusters_at_building.draw(screen)
        for buster in ghostbusters_at_building.sprites():
            buster.draw_slime_circle(screen)
            buster.display_name(screen)
            if buster.proton_pack_on:
                player.proton_charge -= PROTON_CHARGE_PER_TICK
                buster.draw_Proton_Stream()

        ghosts_at_building.draw(screen)
        pk_counter = 0
        for ghost in ghosts_at_building.sprites():
            ghost.display_pk_health(screen)
            ghost.draw_damage()
            pk_counter += ghost.pk_health


        # traps_at_building.draw(screen)

        
        # display_pk_time = elapsed_time // 100 # show as
        display_pk_time = pk_counter + (elapsed_time // 100)

        draw_pk_meter(reading=display_pk_time, silent=True)
        draw_proton_charge_meter()
        # #############################################################################

        # SOUNDS ######################################################

        # Check if any ghostbuster has their proton pack on
        any_proton_pack_on = any(buster.proton_pack_on for buster in ghostbusters_at_building.sprites())
        if any_proton_pack_on:
            if not PROTON_PACK_CHANNEL.get_busy():
                PROTON_PACK_CHANNEL.play(PROTON_FIRE_SOUND, loops=-1)  # Loop the sound continuously
        else:
            PROTON_PACK_CHANNEL.stop()

        # ##############################################################

        pygame.display.flip()
        clock.tick(60)

# #########################################################
def evade_staypuft_at_doorway():
    global player
    global selected_ghostbuster
    
    global ghostbusters_at_building






    testing = False

    success_exit = False

    # Create sprite groups
    ghostbusters_at_building = pygame.sprite.Group()

    ghostbusters_entered_door = pygame.sprite.Group()





    # Create Ghostbuster sprites

    roster = player.roster.sprites()
    random.shuffle(roster) # randomize buster selection for each mission
    length_roster = len(roster)

    ghostbuster1 = None 
    ghostbuster2 = None
    ghostbuster3 = None
    ghostbuster4 = None

    left_most_buster = None


    for buster in roster:
        if ghostbuster1 == None:
            if not buster.slimed:
                ghostbuster1 = buster
                ghostbuster1.set_for_building(BLUE, WIDTH - 120 - 150, HEIGHT - 110)
                ghostbuster1.evading_stay_puft = True
                ghostbusters_at_building.add(ghostbuster1)
        elif ghostbuster2 == None:
                if not buster.slimed:
                    ghostbuster2 = buster
                    ghostbuster2.set_for_building(RED, WIDTH - 120 - 100, HEIGHT - 110)
                    ghostbuster2.evading_stay_puft = True
                    ghostbusters_at_building.add(ghostbuster2)
        elif ghostbuster3 == None:
            if not buster.slimed:
                ghostbuster3 = buster
                ghostbuster3.set_for_building(YELLOW, WIDTH - 120 - 50, HEIGHT - 100)
                ghostbuster3.evading_stay_puft = True
                ghostbusters_at_building.add(ghostbuster3)
        elif ghostbuster4 == None:
            if not buster.slimed:
                ghostbuster4 = buster
                ghostbuster4.set_for_building(YELLOW, WIDTH - 120 - 0, HEIGHT - 100)
                ghostbuster4.evading_stay_puft = True
                ghostbusters_at_building.add(ghostbuster4)

    selected_ghostbuster = ghostbuster1




    # Create Ghost sprite
    # Create the Jumping Ghost
    jumping_staypuft = JumpingGhost(x=890, y=560, jump_radius=150, jump_speed=0.035)

    # Sprite group for drawing and updating
    jumping_staypuft_group = pygame.sprite.Group(jumping_staypuft)
    clock = pygame.time.Clock()

    running = True
    start_time = pygame.time.get_ticks()  # Get the start time in milliseconds

    CHARGE_SOUND.play()
    playonce = False

    left_most_buster = None
    left_selected = False
    left_most_buster_x = WIDTH

    
    vehicle_side_image = vehicle__side_images.get(player.vehicle['name'].lower())

    buildingX = 0
    buildingY = 0


    building_image = ZUUL_FACADE
    building_image = pygame.transform.scale(building_image, (WIDTH, HEIGHT))


    elapsed_time = 0 
    while running:
        screen.fill(BLACK)
        screen.blit(building_image, (buildingX, buildingY))

        # ---
        # draw the ectomobile:
        screen.blit(vehicle_side_image, (WIDTH - vehicle_side_image.get_width(), HEIGHT - 200))



        elapsed_time = pygame.time.get_ticks() - start_time



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                PROTON_PACK_CHANNEL.stop()
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    available_ghostbusters = [ghostbuster1, ghostbuster2, ghostbuster3, ghostbuster4]
                    
                    # Filter out None values
                    available_ghostbusters = [ghostbuster for ghostbuster in available_ghostbusters if ghostbuster is not None]
                    
                    if available_ghostbusters:
                        current_index = available_ghostbusters.index(selected_ghostbuster) if selected_ghostbuster in available_ghostbusters else -1
                        next_index = (current_index + 1) % len(available_ghostbusters)
                        selected_ghostbuster = available_ghostbusters[next_index]




        keys = pygame.key.get_pressed()


        # Update sprites

        ghostbusters_at_building.update(keys)
        jumping_staypuft_group.update()

        if len(ghostbusters_at_building.sprites()) <= 0:
            running = False

            return ghostbusters_entered_door

        numSlimed = 0
        for buster in ghostbusters_at_building:
            if buster.slimed:
                numSlimed += 1
        if numSlimed >= len(ghostbusters_at_building.sprites()):
            running = False
            return ghostbusters_entered_door





        # Ensure both sprites have a `radius` attribute for collide_circle
        jumping_staypuft.radius = 150  # Approximate radius of the ghost sprite
        for ghostbuster in ghostbusters_at_building:
            ghostbuster.radius = 50  # Approximate radius of the ghostbuster sprite

            # Use circle-based collision detection
            if pygame.sprite.collide_circle(jumping_staypuft, ghostbuster):
                if not ghostbuster.slimed:
                    print(f"Circle collision detected with Ghostbuster: {ghostbuster.name}")
                    ghostbuster.getSlimed()
                    available_ghostbusters = [ghostbuster1, ghostbuster2, ghostbuster3, ghostbuster4]
                    # Filter out None values
                    available_ghostbusters = [ghostbuster for ghostbuster in available_ghostbusters if ghostbuster is not None]
                    if available_ghostbusters:
                        current_index = available_ghostbusters.index(selected_ghostbuster) if selected_ghostbuster in available_ghostbusters else -1
                        next_index = (current_index + 1) % len(available_ghostbusters)
                        selected_ghostbuster = available_ghostbusters[next_index]




            # CHECK IF GHOSTBUSTER ENTERS DOORWAY
            elif ghostbuster.rect.x >= 800 and ghostbuster.rect.x <=900:
                if ghostbuster.rect.y <= 670:
                    if not ghostbuster.slimed:
                        print(ghostbuster.name, " entered door")
                        # entered door successfully
                        ghostbusters_entered_door.add(ghostbuster)
                        ghostbusters_at_building.remove(ghostbuster)
                        VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)

                        available_ghostbusters = [ghostbuster1, ghostbuster2, ghostbuster3, ghostbuster4]
                        # Filter out None values
                        available_ghostbusters = [ghostbuster for ghostbuster in available_ghostbusters if ghostbuster is not None]
                        if available_ghostbusters:
                            current_index = available_ghostbusters.index(selected_ghostbuster) if selected_ghostbuster in available_ghostbusters else -1
                            next_index = (current_index + 1) % len(available_ghostbusters)
                            selected_ghostbuster = available_ghostbusters[next_index]


            

        
        # Draw everything

        # print(selected_ghostbuster.rect.x, selected_ghostbuster.rect.y)
        
        ### GHOSTBUSTERS ###
        ghostbusters_at_building.draw(screen)
        for buster in ghostbusters_at_building.sprites():
            buster.display_name(screen)





        ### GHOSTS ###
        jumping_staypuft_group.draw(screen)

        
        # display_pk_time = elapsed_time // 100 # show as  
        # draw_pk_meter(reading=display_pk_time, alertLevel=alertLevel)
        # draw_proton_charge_meter(proton_charge_color)

        pygame.display.flip()
        clock.tick(60)



#################################################################################
def bust_ghost_at_building(building=None):
    global player
    global selected_ghostbuster
    global ghosts_at_building
    global ghostbusters_at_building
    global num_ghosts_busted
    global elapsed_time
    global left_most_buster
    global traps_at_building
    global ghosts_captured
            

    building = building

    

    testing = False

    success_exit = False

    # Create sprite groups
    ghostbusters_at_building = pygame.sprite.Group()
    ghosts_at_building = pygame.sprite.Group()
    traps_at_building = pygame.sprite.Group()
    doors_at_building = pygame.sprite.Group()

    ghosts_captured = pygame.sprite.Group() 

    # Create Ghostbuster sprites

    roster = player.roster.sprites()
    random.shuffle(roster) # randomize buster selection for each mission
    length_roster = len(roster)

    ghostbuster1 = None 
    ghostbuster2 = None
    ghostbuster3 = None

    left_most_buster = None

    sign_image = None
    signX = 0
    signY = 0

    for buster in roster:
        if ghostbuster1 == None:
            if not buster.slimed:
                ghostbuster1 = buster
                ghostbuster1.set_for_building(BLUE, WIDTH - 120 - 150, HEIGHT - 110, has_trap=True)
                ghostbusters_at_building.add(ghostbuster1)
        elif ghostbuster2 == None:
                if not buster.slimed:
                    ghostbuster2 = buster
                    ghostbuster2.set_for_building(RED, WIDTH - 120 - 100, HEIGHT - 110)
                    ghostbusters_at_building.add(ghostbuster2)
        # elif ghostbuster3 == None:
        #         if not buster.slimed:
        #             ghostbuster3 = buster
        #             ghostbuster3.set_for_building(YELLOW, WIDTH - 120 - 50, HEIGHT - 100)
        #             ghostbusters_at_building.add(ghostbuster3)

    selected_ghostbuster = ghostbuster1

    targeted_buster = random.choice(ghostbusters_at_building.sprites())

    # Create Ghost sprite
    num_ghosts = 1
    for buster in player.roster:
        if buster.level > 1: # ONLY ONE GHOST EARLY GAME
            num_ghosts = random.choice([1,1,1,2])
            break

    
    count = 0

    while count < num_ghosts:
        ghost_at_building = Ghost_at_building()
        ghosts_at_building.add(ghost_at_building)
        count += 1

    clock = pygame.time.Clock()

    running = True
    start_time = pygame.time.get_ticks()  # Get the start time in milliseconds

    CHARGE_SOUND.play()
    playonce = False
    num_ghosts_busted = 0
    left_most_buster = None
    left_selected = False
    left_most_buster_x = WIDTH

    
    vehicle_side_image = vehicle__side_images.get(player.vehicle['name'].lower())
    buildingX = 150
    buildingY = 20
    buildingWidth = WIDTH-150-150
    buildingHeight = (HEIGHT//3)*2 + 15
    building_image = None

    if random.randint(0,100) > 50:
        building_image = pygame.transform.scale(BRICKS_FACADE, (buildingWidth , buildingHeight))

    # if building.name == "HQ": # SPECIFIC BUILDING FACADE?
    #     building_image = pygame.transform.scale(HQ_FACADE, (buildingWidth , buildingHeight))


    building_color = random.choice([DARK_RED, DARK_GREY, BROWN, DARK_YELLOW, GREEN])

    if building.name == "Park":
        building_image = pygame.transform.scale(PARK_FACADE, (buildingWidth , buildingHeight))
    else:


        if building.name == "Hotel":
            door_image = DOOR3_IMAGE # REVOLVING DOORS
        elif building.name == "Police":
            sign_image = pygame.transform.scale(POLICE, (50, 50))
            door_image = DOOR4_IMAGE# DOOR WITH COLUMNS
            signX = buildingX + buildingWidth//2 - sign_image.get_width()//2
            signY = ((HEIGHT//3)*2 + 40) - door_image.get_height() - sign_image.get_height()*0.75
            

        elif building.name == "Church":
            sign_image = pygame.transform.scale(CROSS, (50, 50))
            door_image = DOOR4_IMAGE# DOOR WITH COLUMNS
            signX = buildingX + buildingWidth//2 - sign_image.get_width()//2
            signY = ((HEIGHT//3)*2 + 40) - door_image.get_height() - sign_image.get_height()*0.75
            

        elif building.name == "Hospital":
            sign_image = pygame.transform.scale(REDCROSS, (50, 50))
            door_image = random.choice([DOOR1_IMAGE, DOOR2_IMAGE, DOOR3_IMAGE, DOOR4_IMAGE,DOOR5_IMAGE])
            signX = buildingX + buildingWidth//2 - sign_image.get_width()//2
            signY = ((HEIGHT//3)*2 + 40) - door_image.get_height() - sign_image.get_height()*0.75
            
        else:
            door_image = random.choice([DOOR1_IMAGE, DOOR2_IMAGE, DOOR3_IMAGE, DOOR4_IMAGE,DOOR5_IMAGE])


        doorX = (WIDTH//2) - (door_image.get_width()//2)
        doorY = ((HEIGHT//3)*2 + 40) - door_image.get_height()
        
        door = Door(doorX,doorY,door_image)
        doors_at_building.add(door)


        # Load the window image
        window_image = random.choice(WINDOW_IMAGE_LIST)  # Replace WINDOW1_IMAGE with your image loading code

        # Get the dimensions of the window image
        window_width = window_image.get_width()
        window_height = window_image.get_height()

        # Calculate the number of windows that can fit within the available space
        available_space = WIDTH - 150 - 150 - 150 - 150 # Available space for windows
        num_windows = random.randint(3,7)
        num_rows = random.randint(1,2)

        has_side_window = bool(random.getrandbits(1))
        side_window_image = None
        if has_side_window: 
            side_window_image = random.choice([WINDOW1_IMAGE, WINDOW2_IMAGE, WINDOW3_IMAGE, WINDOW4_IMAGE, WINDOW5_IMAGE])  


        # Calculate the actual spacing between windows
        window_spacing = (available_space - num_windows * window_width) // (num_windows - 1)

        # Calculate the starting position for the first window
        start_x = 150 + 150 + (available_space - num_windows * window_width - (num_windows - 1) * window_spacing) // 2

    ghost_escaping = False
    streams_crossed_death =  False
    elapsed_time = 0 
    success =  False
    while running:

        # draw the background 
        # screen.fill(BLACK)
        # screen.fill(SKY_BLUE, (0,0, WIDTH, HEIGHT//5))
        screen.fill(SKY_BLUE) # BACKGROUND
        screen.fill(STREET_GREY, (0,(HEIGHT//3)*2 + 5, WIDTH, HEIGHT//3)) # SIDEWALK & BEHIND BUILDINGS
        screen.fill(GREY, (0,70, 125, (HEIGHT//3)*2 - 15 - 20)) # LEFT NEIGHBOR BUILDING
        screen.fill(GREY, (WIDTH-125,70, 125, (HEIGHT//3)*2 - 15 - 20)) # RIGHT NEIGHBOR BUILDING
        screen.fill(building_color, (buildingX,buildingY, buildingWidth, buildingHeight)) # BUILDING ITSELF

        leftGapCoords = [(125,70), (buildingX,70+15), (buildingX,buildingY+buildingHeight-15), (125,buildingY+buildingHeight)]
        pygame.draw.polygon(screen, BLACK, leftGapCoords ) # LEFT SHADOW GAP

        rightGapCoords = [(buildingX+buildingWidth,70+15), (WIDTH-125,70), (WIDTH-125,buildingY+buildingHeight), (buildingX+buildingWidth,buildingY+buildingHeight-15)]
        pygame.draw.polygon(screen, BLACK, rightGapCoords ) # RIGHT SHADOW GAP

        if building_image is not None:
            screen.blit(building_image, (buildingX, buildingY))

        if not building.name == "Park":

            window_y = 20 + window_height
            # Iterate over each window position and blit the images
            for row in range(num_rows):
                for i in range(num_windows):
                    window_x = start_x + (window_width + window_spacing) * i
                    screen.blit(window_image, (window_x, window_y))
                window_y += window_height*2
            if has_side_window:
                screen.blit(side_window_image, (doorX + door.image.get_width()+ side_window_image.get_width()*2, doorY - side_window_image.get_height()*0.5))


        screen.fill(DARK_GREY, (0, HEIGHT - 175, WIDTH, 10))

        # ---
        # draw the ectomobile:
        screen.blit(vehicle_side_image, (WIDTH - vehicle_side_image.get_width(), HEIGHT - 200))



        elapsed_time = pygame.time.get_ticks() - start_time



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                PROTON_PACK_CHANNEL.stop()
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    available_ghostbusters = [ghostbuster1, ghostbuster2, ghostbuster3]
                    
                    # Filter out None values
                    available_ghostbusters = [ghostbuster for ghostbuster in available_ghostbusters if ghostbuster is not None]
                    
                    if available_ghostbusters:
                        current_index = available_ghostbusters.index(selected_ghostbuster) if selected_ghostbuster in available_ghostbusters else -1
                        next_index = (current_index + 1) % len(available_ghostbusters)
                        if not selected_ghostbuster.complete:
                            selected_ghostbuster = available_ghostbusters[next_index]

                elif event.key == pygame.K_RETURN:

                    if not selected_ghostbuster.complete:
                        # Drop the trap when Enter is pressed
                        if selected_ghostbuster.has_trap or selected_ghostbuster.has_full_trap:
                            trap = selected_ghostbuster.drop_trap()
                            selected_ghostbuster.has_trap = False
                            selected_ghostbuster.has_full_trap = False
                            traps_at_building.add(trap)

                        elif not selected_ghostbuster.has_trap:
                            trap_here = pygame.sprite.spritecollide(selected_ghostbuster,traps_at_building,False)
                            if trap_here:
                                if trap_here[0].opened or (trap_here[0].light_size > 0):
                                    # can't pick up open trap
                                    ...
                                else:
                                    if trap_here[0].full:
                                        selected_ghostbuster.has_full_trap = True
                                        trap_here[0].kill()
                                    else:
                                        selected_ghostbuster.has_trap = True
                                        trap_here[0].kill()

                        

                elif event.key == (pygame.K_LCTRL or pygame.K_RCTRL):
                    if not selected_ghostbuster.complete:

                        if not selected_ghostbuster.proton_pack_on and not selected_ghostbuster.has_trap:
                            selected_ghostbuster.proton_pack_on = True

                        elif selected_ghostbuster.proton_pack_on:
                            selected_ghostbuster.proton_pack_on = False
                            # leavePackSoundOn = False
                            # for buster in ghostbusters_at_building.sprites():
                            #     if buster.proton_pack_on:
                            #         leavePackSoundOn = True
                            #         break


                            # if not leavePackSoundOn and PROTON_PACK_CHANNEL.get_busy():
                            #     PROTON_PACK_CHANNEL.stop()

                elif event.key == pygame.K_SPACE:
                    if not selected_ghostbuster.complete:
                        for trap in traps_at_building.sprites():
                            trap.toggle_trap()



        keys = pygame.key.get_pressed()

        
        

        allLeft = True
        if len(ghosts_at_building.sprites()) == 0:
            PKE_CHANNEL.stop()
            elapsed_time = 0

            if not playonce:
                VOICE_CHANNEL.play(VOICE_GHOSTBUSTERS)
                playonce = True
                success = True
                for buster in ghostbusters_at_building.sprites():
                    buster.complete = True
                    buster.gain_experience(random.randint(0,5) + 5)



            if playonce:
                
                #SUCCESS

                if not VOICE_CHANNEL.get_busy():
                    MUSIC.unpause()

                if len(ghostbusters_at_building.sprites()) == 0:
                    if not ghost_escaping:
                        return num_ghosts_busted, ghosts_captured

                else:
                    ghostbusters_group = ghostbusters_at_building.sprites()
                    traps_group = traps_at_building.sprites()
                    # left_most_buster_x = WIDTH
                    
                    if left_most_buster is None:

                        # while True:
                        #     left_most_buster = random.choice(ghostbusters_group)
                        #     if left_most_buster.slimed:
                        #         ...
                        #     else:
                        #         break


                        for buster in ghostbusters_group:
                            if buster.slimed:
                                ...
                            elif buster.rect.x < left_most_buster_x:
                                left_most_buster = buster
                                left_most_buster_x = buster.rect.x


                    if left_most_buster is not None:
                        # print(left_most_buster.name)

                        if not left_most_buster.has_full_trap:

                            if left_most_buster.rect.bottom < traps_group[0].rect.bottom:
                                left_most_buster.rect.y += left_most_buster.speed*1.5
                            elif left_most_buster.rect.bottom > traps_group[0].rect.bottom:
                                left_most_buster.rect.y -= left_most_buster.speed*1.5

                            if left_most_buster.rect.x < traps_group[0].rect.x:
                                left_most_buster.rect.x += left_most_buster.speed*1.5
                                left_most_buster.last_left = False
                            elif left_most_buster.rect.x > traps_group[0].rect.x:
                                left_most_buster.rect.x -= left_most_buster.speed*1.5
                                left_most_buster.last_left = True

                            if abs(left_most_buster.rect.bottom - traps_group[0].rect.bottom) <= left_most_buster.speed:
                                if abs(left_most_buster.rect.x - traps_group[0].rect.x) <= left_most_buster.speed:
                                    traps_at_building.remove(traps_group[0])
                                    left_most_buster.has_full_trap = True

                        if left_most_buster.has_full_trap:

                            for buster in ghostbusters_group:
                                buster.last_left = False
                                if buster.rect.y < HEIGHT - buster.image.get_height()*2:
                                    buster.rect.y += buster.speed*1.5

                                if buster.rect.x <= WIDTH:
                                    buster.rect.x += buster.speed*2

                                if buster.rect.x >= WIDTH:
                                    ghostbusters_at_building.remove(buster)
                                    # print("removed!")

                            

        else:
            for buster in ghostbusters_at_building.sprites():
                buster.complete = False

        # Update sprites
        traps_at_building.update()
        ghostbusters_at_building.update(keys)
        ghosts_at_building.update()

        # if len(ghostbusters_at_building.sprites()) <= 0:
        #     if not ghost_escaping:
        #         running = False
        #         return num_ghosts_busted, ghosts_captured


        # IF ALL BUSTERS SLIMED... EXIT. MOSTLY LIKE WHEN STREAMS CROSSED
        if not success and not ghost_escaping: 
            numSlimed = 0
            for buster in ghostbusters_at_building:
                if buster.slimed:
                    numSlimed += 1
            if numSlimed >= len(ghostbusters_at_building.sprites()) and not streams_crossed_death:
                PKE_CHANNEL.stop()
                # PROTON_PACK_CHANNEL.stop()
                MUSIC.pause()
                VOICE_CHANNEL.play(VOICE_YELL)
                streams_crossed_death = True
                print("streams_crossed_death!!!!")
                # return num_ghosts_busted, ghosts_captured


        # Check if 1 minute has passed    
        # print(elapsed_time)
        alertLevel = "very low"
        if elapsed_time >= GHOST_ESCAPE_TIME - GHOST_ESCAPE_TIME//4:
            alertLevel = "high"
                
        elif elapsed_time >= GHOST_ESCAPE_TIME//2:
            alertLevel = "med"
                
        elif elapsed_time >= GHOST_ESCAPE_TIME//4:
            alertLevel = "low"

        elif elapsed_time < GHOST_ESCAPE_TIME//4:
            alertLevel = "very low"

        # buster gets slimed  as time has elapsed!!
        if (elapsed_time >= GHOST_ESCAPE_TIME) and not testing:  # 1 minute = 60,000 milliseconds
            elapsed_time = GHOST_ESCAPE_TIME # stop counting 
            for this_ghost in ghosts_at_building.sprites():
                if not this_ghost.trapped:
                    this_ghost.escaped = True
                    MUSIC.pause()
                    PKE_CHANNEL.stop()

                for buster in ghostbusters_at_building:
                    buster.proton_pack_on = False
                    # PROTON_PACK_CHANNEL.stop()

            
            if not playonce and not streams_crossed_death:
                ghost_escaping = True
                buster_x = targeted_buster.rect.x + targeted_buster.image.get_width()//2
                buster_y = targeted_buster.rect.y + targeted_buster.image.get_height()//2
                # Move the ghost towards the ghostbuster
            
                vector = pygame.Vector2(buster_x - this_ghost.rect.centerx, buster_y - this_ghost.rect.centery)
                vector.normalize_ip()
                this_ghost.rect.move_ip(15 * vector.x, 15 * vector.y)

                
                distX = abs(this_ghost.rect.centerx - buster_x)
                distY = abs(this_ghost.rect.centery - buster_y)

                dist = math.hypot(distX,distY)


                if pygame.sprite.spritecollide(this_ghost, ghostbusters_at_building, False):
                    if dist < 20:
                        ghost_escaping = True
                        targeted_buster.getSlimed()
                        playonce = True

            if VOICE_CHANNEL.get_busy() and playonce:
                
                ...
            elif (not VOICE_CHANNEL.get_busy()) and playonce:
                ghost_escaping = True
                randomX = random.randint(0,WIDTH)
                vector = pygame.Vector2(randomX - this_ghost.rect.centerx, -100 - this_ghost.rect.centery)
                vector.normalize_ip()
                this_ghost.rect.move_ip(15 * vector.x, 15 * vector.y)

                if this_ghost.rect.y < 0: # GHOST ESCAPES
                    this_ghost.kill()
                    return num_ghosts_busted, ghosts_captured


        if streams_crossed_death and not playonce:
            if VOICE_CHANNEL.get_busy():
                ...
            else:
                MUSIC.unpause()
                return num_ghosts_busted, ghosts_captured
            

        
        # Draw everything

        doors_at_building.draw(screen)
        if sign_image is not None:
            # screen.fill(WHITE,(signX-1, signY-1,sign_image.get_width()+2,sign_image.get_height()+2))
            pygame.draw.rect(screen, BLACK, pygame.Rect(signX-2, signY-2,sign_image.get_width()+4,sign_image.get_height()+4),  0, 3)
            pygame.draw.rect(screen, OFF_WHITE, pygame.Rect(signX-1, signY-1,sign_image.get_width()+2,sign_image.get_height()+2),  0, 3)
            screen.blit(sign_image, (signX, signY))

        ### TRAPS AND TRAP EFFECTS ### 
        for trap in traps_at_building.sprites():
            trap.draw_light_column()
        traps_at_building.draw(screen)

        proton_charge_color = DARK_RED
        
        ### GHOSTBUSTERS ###
        ghostbusters_at_building.draw(screen)
        for buster in ghostbusters_at_building.sprites():
            buster.display_name(screen)
            if buster.proton_pack_on:
                player.proton_charge -= PROTON_CHARGE_PER_TICK
                buster.draw_Proton_Stream()
                proton_charge_color = random.choice([RED, RED, DARK_RED, ORANGE, YELLOW, WHITE])


            if buster.has_trap or buster.has_full_trap:
                show_trap_image = buster.trap_image
                if buster.has_full_trap: show_trap_image = buster.full_trap_image
                if buster.last_left: # facing left
                    screen.blit(show_trap_image, (buster.rect.x - buster.trap_image.get_width() + 5, buster.rect.y + buster.size//3))
                else: # facing right
                    screen.blit(show_trap_image, (buster.rect.x + buster.image.get_width() - 5, buster.rect.y + buster.size//3))

            

        ### GHOSTS ###
        ghosts_at_building.draw(screen)
        for ghost in ghosts_at_building:
            ghost.draw_damage()
            ghost.display_pk_health(screen)
        
        display_pk_time = elapsed_time // 100 # show as  
        draw_pk_meter(reading=display_pk_time, alertLevel=alertLevel)
        draw_proton_charge_meter(proton_charge_color)


        # SOUNDS ######################################################

        # Check if any ghostbuster has their proton pack on
        any_proton_pack_on = any(buster.proton_pack_on for buster in ghostbusters_at_building.sprites())
        if any_proton_pack_on:
            if not PROTON_PACK_CHANNEL.get_busy():
                PROTON_PACK_CHANNEL.play(PROTON_FIRE_SOUND, loops=-1)  # Loop the sound continuously
        else:
            PROTON_PACK_CHANNEL.stop()

        # ##############################################################




        pygame.display.flip()
        clock.tick(60)


def enterOrExit_building(building=None, enter=True, exit=False):
    global player
    global selected_ghostbuster
    global ghostbusters_at_building
    global ghosts_at_building


    building = building

    if building is None:
        ...
    enter  =  enter
    if exit == True:
        FORK_CHANNEL.stop()
        enter = False
        if not MUSIC.get_busy():
            if MUSIC_ON:
                MUSIC.play(THEME,loops=-1)
        else:
            MUSIC.unpause()
    if enter == True:
        MUSIC.pause()
        

    # Create sprite groups
    ghostbusters_at_building = pygame.sprite.Group()
    ghosts_at_building = pygame.sprite.Group()

    doors_at_building = pygame.sprite.Group()

    clock = pygame.time.Clock()

    running = True
    start_time = pygame.time.get_ticks()  # Get the start time in milliseconds

    
    vehicle_side_image = vehicle__side_images.get(player.vehicle['name'].lower())
    buildingX = 150
    buildingY = 20
    buildingWidth = WIDTH-150-150
    buildingHeight = (HEIGHT//3)*2 + 15
    building_image = None

    num_windows = random.randint(3,7)
    num_rows = random.randint(1,2)

    sign_image = None
    signX = 0
    signY = 0

    
    building_color = random.choice([DARK_RED, DARK_GREY, BROWN, DARK_YELLOW])

    if building is not None:
        if building.name == "Hotel":
            door_image = DOOR3_IMAGE # REVOLVING DOORS
            # Load the window image
            window_image = random.choice(WINDOW_IMAGE_LIST)  # Replace WINDOW1_IMAGE with your image loading code


        elif (building.name == "HQ"): # SPECIFIC BUILDING FACADE?
            door_image = DOOR_HQ_IMAGE
            building_color = DARK_RED
            window_image = WINDOW4_IMAGE
            buildingX = 150 + 40
            buildingWidth = WIDTH-150-150 - 80
            num_windows = 4
            num_rows = 2
            building_image = pygame.transform.scale(BRICKS_FACADE, (buildingWidth , buildingHeight))

            sign_image = pygame.transform.scale(GB_LOGO, (50, 50))
            signX = buildingX + buildingWidth//2 - sign_image.get_width()//2
            signY = ((HEIGHT//3)*2 + 40) - door_image.get_height() - sign_image.get_height()*0.75

        else:
            door_image = random.choice(DOOR_IMAGE_LIST)
            # Load the window image
            window_image = random.choice(WINDOW_IMAGE_LIST)  # Replace WINDOW1_IMAGE with your image loading code
    
    elif building is None: # SPECIFIC BUILDING FACADE?
        door_image = random.choice(DOOR_IMAGE_LIST)
        # Load the window image
        window_image = random.choice(WINDOW_IMAGE_LIST)  # Replace WINDOW1_IMAGE with your image loading code


    doorX = (WIDTH//2) - (door_image.get_width()//2)
    doorY = ((HEIGHT//3)*2 + 40) - door_image.get_height()
    
    door = Door(doorX,doorY,door_image)
    doors_at_building.add(door)



    # Get the dimensions of the window image
    window_width = window_image.get_width()
    window_height = window_image.get_height()

    # Calculate the number of windows that can fit within the available space
    available_space = WIDTH - 150 - 150 - 150 - 150 # Available space for windows
    

    # Calculate the actual spacing between windows
    window_spacing = (available_space - num_windows * window_width) // (num_windows - 1)

    # Calculate the starting position for the first window
    start_x = 150 + 150 + (available_space - num_windows * window_width - (num_windows - 1) * window_spacing) // 2


    # Create Ghostbuster sprites

    roster = player.roster.sprites()
    random.shuffle(roster) # randomize buster selection for each mission
    length_roster = len(roster)

    ghostbuster1 = None 
    ghostbuster2 = None
    ghostbuster3 = None
    ghostbuster4 = None

    selected_ghostbuster = None

    for buster in roster:
        if ghostbuster1 == None:
            if not buster.slimed:
                ghostbuster1 = buster
                if enter:
                    ghostbuster1.set_for_building(BLUE, WIDTH - 120 - 150, HEIGHT - 110)
                else:
                    ghostbuster1.set_for_building(BLUE, door.rect.x + door.image.get_width()//2, door.rect.bottom - ghostbuster1.image.get_height())
                ghostbusters_at_building.add(ghostbuster1)
        elif ghostbuster2 == None:
                if not buster.slimed:
                    ghostbuster2 = buster
                    if enter:
                        ghostbuster2.set_for_building(RED, WIDTH - 120 - 100, HEIGHT - 110)
                    else:
                        ghostbuster2.set_for_building(RED, door.rect.x + door.image.get_width()//2 + ghostbuster2.image.get_width(), door.rect.bottom - ghostbuster2.image.get_height())
                    ghostbusters_at_building.add(ghostbuster2)
        elif ghostbuster3 == None:
                if not buster.slimed:
                    ghostbuster3 = buster
                    if enter:
                        ghostbuster3.set_for_building(YELLOW, WIDTH - 120 - 50, HEIGHT - 100)
                    else:
                        ghostbuster3.set_for_building(YELLOW, door.rect.x + door.image.get_width()//2 + ghostbuster3.image.get_width()*2, door.rect.bottom - ghostbuster3.image.get_height())
                    ghostbusters_at_building.add(ghostbuster3)
        elif ghostbuster4 == None:
                if not buster.slimed:
                    ghostbuster4 = buster
                    if enter:
                        ghostbuster4.set_for_building(PURPLE, WIDTH - 120, HEIGHT - 100)
                    else:
                        ghostbuster4.set_for_building(PURPLE, door.rect.x + door.image.get_width()//2 + ghostbuster4.image.get_width()*3, door.rect.bottom - ghostbuster4.image.get_height())
                    ghostbusters_at_building.add(ghostbuster4)


    while running:

        # draw the background 
        # screen.fill(BLACK)
        screen.fill(SKY_BLUE)
        # screen.fill(SKY_BLUE, (0,0, WIDTH, HEIGHT//5))
        screen.fill(STREET_GREY, (0,(HEIGHT//3)*2 + 5, WIDTH, HEIGHT//3)) # SIDEWALK & BEHIND BUILDINGS
        screen.fill(GREY, (0,45, 125+20, (HEIGHT//3)*2 - 25))
        screen.fill(GREY, (WIDTH-125-20,45, 125+20, (HEIGHT//3)*2 - 25))
        
        

        screen.fill(building_color, (buildingX,buildingY, buildingWidth, buildingHeight))

        if building_image is not None:
            screen.blit(building_image, (buildingX, buildingY))

        leftGapCoords = [(125+20,45), (buildingX,45+15), (buildingX,buildingY+buildingHeight-15), (125+20,buildingY+buildingHeight)]
        pygame.draw.polygon(screen, BLACK, leftGapCoords ) # LEFT SHADOW GAP

        rightGapCoords = [(buildingX+buildingWidth,45+15), (WIDTH-125-20,45), (WIDTH-125-20,buildingY+buildingHeight-15), (buildingX+buildingWidth,buildingY+buildingHeight)]
        pygame.draw.polygon(screen, BLACK, rightGapCoords ) # RIGHT SHADOW GAP

        window_y = 20 + window_height
        # Iterate over each window position and blit the images
        for row in range(num_rows):
            for i in range(num_windows):
                window_x = start_x + (window_width + window_spacing) * i
                screen.blit(window_image, (window_x, window_y))
            window_y += window_height*2


        screen.fill(DARK_GREY, (0, HEIGHT - 175, WIDTH, 10))

        # ---
        # draw the ectomobile:
        screen.blit(vehicle_side_image, (WIDTH - vehicle_side_image.get_width(), HEIGHT - 200))



        elapsed_time = pygame.time.get_ticks() - start_time


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                PROTON_PACK_CHANNEL.stop()
                return

            if event.type == pygame.KEYDOWN:
                ...


        keys = pygame.key.get_pressed()

        doors = doors_at_building.sprites()
        entrance = doors[0]

        if enter:
            for buster in ghostbusters_at_building.sprites():
                buster.complete = True
                buster.last_left = True
                if buster.rect.bottom > entrance.rect.bottom - 10:
                    buster.rect.y -= buster.speed*1.50
                if buster.rect.x > entrance.rect.x + entrance.image.get_width()//2:
                    buster.rect.x -= buster.speed*1.50
                else:
                    ghostbusters_at_building.remove(buster)
        else: # exit
            for buster in ghostbusters_at_building.sprites():
                buster.complete = True
                buster.last_left = False
                
                if buster.rect.y < HEIGHT - buster.image.get_height()*3:
                                    
                    if buster.rect.left > (entrance.rect.right - buster.image.get_width()):
                        buster.rect.y += buster.speed*1.50
                    else:
                        ...
                        # buster.rect.y += buster.speed*1


                if buster.rect.x < WIDTH:
                    buster.rect.x += buster.speed*1.50

                else:
                    ghostbusters_at_building.remove(buster)    
                    
                


                

                            


        # Update sprites

        ghostbusters_at_building.update(keys)



        
        # Draw everything

        doors_at_building.draw(screen)

        if sign_image is not None:
            # screen.fill(WHITE,(signX-1, signY-1,sign_image.get_width()+2,sign_image.get_height()+2))
            pygame.draw.rect(screen, BLACK, pygame.Rect(signX-2, signY-2,sign_image.get_width()+4,sign_image.get_height()+4),  0, 3)
            pygame.draw.rect(screen, OFF_WHITE, pygame.Rect(signX-1, signY-1,sign_image.get_width()+2,sign_image.get_height()+2),  0, 3)
            screen.blit(sign_image, (signX, signY))
        
        ### GHOSTBUSTERS ###
        ghostbusters_at_building.draw(screen)
        for buster in ghostbusters_at_building.sprites():
            buster.display_name(screen)

        if len(ghostbusters_at_building.sprites()) == 0:
            running = False
            return

        pygame.display.flip()
        clock.tick(60)

def generate_random_fine():


    fee_text = []

    # Randomly select a fine
    random_fine = random.choice(CITY_FINE_TYPES)
    description = random_fine["name"]
    fee = int(random_fine["amount"]) * -1


    fee_text.append(f"{description} - $ {str(fee)}")

    below_building = None
    
    
    if player.mapSprite.rect.centerx >= WIDTH//2:
        fee_card = IndexCard(fee, fee_text, below_building, (10, CARD_ORIGIN_Y), slide_direction="left")
    else:
        fee_card = IndexCard(fee, fee_text, below_building, (WIDTH - CARD_WIDTH - 10, CARD_ORIGIN_Y), slide_direction="right")


    player.cash_balance += fee
    CASH_SOUND.play()
    VOICE_CHANNEL.play(VOICE_LAUGH)


    return fee_card

def display_trait_selection(screen, buster_traits):
    """
    Displays a trait selection window where the player can choose a trait to upgrade.

    Args:
        screen: The pygame display surface.
        buster_traits (dict): A dictionary of the Ghostbuster's traits.

    Returns:
        str: The selected trait key.
    """

    # Define window size
    window_width, window_height = 500, 200  # Adjust as needed
    
    
    # Calculate the position to center the window
    window_x = (WIDTH - window_width) // 2
    window_y = (HEIGHT - window_height) // 2
    



    selected_index = 0  # Start with the first trait selected
    trait_keys = list(buster_traits.keys())  # Extract trait names as a list

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    selected_index = (selected_index + 1) % len(trait_keys)
                elif event.key == pygame.K_LEFT:
                    selected_index = (selected_index - 1) % len(trait_keys)
                elif event.key == pygame.K_RETURN:
                    return trait_keys[selected_index]
        
        # Draw the centered window
        pygame.draw.rect(screen, STREET_GREY, (window_x, window_y, window_width, window_height)) # Background
        pygame.draw.rect(screen, BLACK, (window_x, window_y, window_width, window_height), 2)  # Border
        
        # Render the prompt
        prompt_text = FONT36.render("Choose a trait to upgrade:", True, BLACK)
        prompt_x = window_x + (window_width - prompt_text.get_width()) // 2
        screen.blit(prompt_text, (prompt_x, window_y + 20))

        # Display traits left-to-right, centered horizontally
        spacing = 120  # Horizontal spacing between traits
        total_width = len(trait_keys) * spacing  # Total width of all traits combined
        start_x = 10 + window_x + (window_width - total_width) // 2  # Start X position for traits (centered)
        y_position = window_y + 100  # Fixed Y position for all traits

        for i, trait in enumerate(trait_keys):
            color = GREEN if i == selected_index else BLACK
            trait_text = FONT36.render(f"{trait}: {buster_traits[trait]}", True, color)
            trait_x = start_x + i * spacing
            screen.blit(trait_text, (trait_x, y_position))
        
        pygame.display.flip()




# Function to start the game and get player information
def start_game():
    global game_mode
    global starting
    global player
    global forklift
    global traps_at_building
    global vacuum_on
    global fee_card 

    player = Player() # create a new player

    forklift = pygame.sprite.Group()
    traps_at_building = pygame.sprite.Group()

    game_mode =  0

    if START_GAME == 1:
        game_mode =  1


    starting = True

    vacuum_on = False

    # Initialize fee_card as None
    fee_card = None

    while starting:

        if game_mode == 0:
            start_loop()
            game_mode += 1
        elif game_mode == 1:
            purchase_car()

            if START_GAME == 1:
                player.vehicle_items.append({"name": "Ghost Bait", "cost": 400, 'unique': True})
                player.vehicle_items.append({"name": "Ghost Trap", "cost": 600, 'unique': False})
                player.vehicle_items.append({"name": "Ghost Vacuum", "cost": 500, 'unique': True})
                player.vehicle_items.append({"name": "Portable Lazer Confinement", "cost": 15000, 'unique': True})
                player.vehicle_items.append({"name": "PK Energy Detector", "cost": 400, 'unique': True})


            game_mode += 1
        elif game_mode == 2:
            hire_busters_loop()
            game_mode += 1
        elif game_mode == 3:
            equipment_shopping_loop("monitor")
            game_mode += 1
        elif game_mode == 4:
            equipment_shopping_loop("capture")
            game_mode += 1
        elif game_mode == 5:
            equipment_shopping_loop("defense")
            game_mode += 1
        elif game_mode == 6:
            # base_improvment_shopping_loop()
            game_mode += 1
        elif game_mode == 7:
            # research_allocation_loop()
            ...
            starting = False
            
        

def run_game():
    global game_mode
    global running
    game_mode = 0
    hq = generate_map()

    running = True
    while running:
        
        MUSIC.pause()
        if game_mode == 0:

            enterOrExit_building(building=hq, enter=False,exit=True)
            navigate_map()
            game_mode += 2

        elif game_mode == 1:
            hire_busters_loop()
            game_mode += 1

        elif game_mode == 2:
            show_busters_loop()
            game_mode += 1

        elif game_mode == 3:
            equipment_shopping_loop("monitor")
            game_mode += 1

        elif game_mode == 4:
            equipment_shopping_loop("capture")
            game_mode += 1

        elif game_mode == 5:
            equipment_shopping_loop("defense")
            game_mode += 1

        elif game_mode == 6:
            base_improvment_shopping_loop()
            game_mode += 1

        elif game_mode == 7:
            research_allocation_loop()
            game_mode += 1

        elif game_mode == 8:
            game_mode = 0


# Run the game
start_game()
run_game()


# Wait for a moment before closing the game window
pygame.time.delay(1000)
# Quit pygame
pygame.quit()
sys.exit()
