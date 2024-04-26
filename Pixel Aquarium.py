import pygame
import sys
import random
import pickle
import time

pygame.init()
window = pygame.display.set_mode((1080, 600))
clock = pygame.time.Clock()
font = pygame.font.Font('font/Pixeltype.ttf',40)
background = pygame.image.load('backgrounds/l_aquarium.png').convert_alpha()
background = pygame.transform.scale(background, (1080, 600)).convert_alpha()
s_background = pygame.image.load('backgrounds/aquarium.png').convert_alpha()
s_background = pygame.transform.scale(s_background, (1080, 600)).convert_alpha()
watermark = pygame.image.load('backgrounds/watermark.png').convert_alpha()
v_background = pygame.image.load('backgrounds/vill_back.png').convert_alpha()
v_background = pygame.transform.scale(v_background, (1080, 600)).convert_alpha()
v_back1 = pygame.image.load('backgrounds/vill_back_1.png').convert_alpha()
v_back1 = pygame.transform.scale(v_back1, (1080, 600)).convert_alpha()
v_back2 = pygame.image.load('backgrounds/vill_back_2.png').convert_alpha()
v_back2 = pygame.transform.scale(v_back2, (1080, 600)).convert_alpha()
v_back3 = pygame.image.load('backgrounds/vill_back_3.png').convert_alpha()
v_back3 = pygame.transform.scale(v_back3, (1080, 600)).convert_alpha()
v_back4 = pygame.image.load('backgrounds/vill_back_4.png').convert_alpha()
v_back4 = pygame.transform.scale(v_back4, (1080, 600)).convert_alpha()
shop_background = pygame.image.load('backgrounds/shop_back.png').convert_alpha()
shop_background = pygame.transform.scale(shop_background, (1080, 600)).convert_alpha()
con_background = pygame.image.load('backgrounds/under_construction.png').convert_alpha()
con_background = pygame.transform.scale(con_background, (1080, 600)).convert_alpha()
lake_background = pygame.image.load('backgrounds/lake_back.png').convert_alpha()
lake_background = pygame.transform.scale(lake_background, (1080, 600)).convert_alpha()
lake_back1= pygame.image.load('backgrounds/lake_back_1.png').convert_alpha()
lake_back1 = pygame.transform.scale(lake_back1, (1080, 600)).convert_alpha()
fishing_lake_back = pygame.image.load('backgrounds/fishing_lake_back.png').convert_alpha()
fishing_lake_back = pygame.transform.scale(fishing_lake_back, (1080, 600)).convert_alpha()
sea_fishing_back = pygame.image.load('backgrounds/sea_fishing_back.png').convert_alpha()
fishmarket_back = pygame.image.load('backgrounds/market_back.png').convert_alpha()
trophy_back = pygame.image.load('backgrounds/trophy_back.png').convert_alpha()
achieve_back = pygame.image.load('backgrounds/achievement_back.png').convert_alpha()
trophy_cover = pygame.image.load('buttons/trophy_cover.png').convert_alpha()
trophy_cover_q = pygame.image.load('buttons/trophy_cover_q.png').convert_alpha()
sea_back = pygame.image.load('backgrounds/sea_back.png').convert_alpha()
sea_back = pygame.transform.scale(sea_back, (1080, 600)).convert_alpha()
sea_back1 = pygame.image.load('backgrounds/sea_back_1.png').convert_alpha()
sea_back1 = pygame.transform.scale(sea_back1, (1080, 600)).convert_alpha()
sea_cover = pygame.image.load('buttons/sea_cover.png').convert_alpha()
sea_cover = pygame.transform.scale(sea_cover, (320, 209)).convert_alpha()
title = pygame.image.load('buttons/title.png').convert_alpha()
start = pygame.image.load('buttons/start.png').convert_alpha()
start_coll = pygame.image.load('buttons/start_coll.png').convert_alpha()
load_coll = pygame.image.load('buttons/load_coll.png').convert_alpha()
quit_coll = pygame.image.load('buttons/quit_coll.png').convert_alpha()
load = pygame.image.load('buttons/load.png').convert_alpha()
quit = pygame.image.load('buttons/quit.png').convert_alpha()
cash = pygame.image.load('buttons/cash.png').convert_alpha()
check = pygame.image.load('buttons/check.png').convert_alpha()
buy_alert = pygame.image.load('buttons/buy_alert.png').convert_alpha()
not_enough = pygame.image.load('buttons/not_enough.png').convert_alpha()
to_menu = pygame.image.load('buttons/to_menu.png').convert_alpha()
mini_house = pygame.image.load('scenery/mini_house.png').convert_alpha()
mini_house = pygame.transform.scale(mini_house, (85, 85)).convert_alpha()
pin_plant = pygame.image.load('scenery/pin_plant.png').convert_alpha()
pur_plant = pygame.image.load('scenery/pur_plant.png').convert_alpha()
grn_plant = pygame.image.load('scenery/grn_plant.png').convert_alpha()
grn_plant = pygame.transform.scale(grn_plant, (110, 142)).convert_alpha()
skeleton = pygame.image.load('scenery/skeleton.png').convert_alpha()
skeleton = pygame.transform.scale(skeleton, (100, 45)).convert_alpha()
grass = pygame.image.load('scenery/grass.png').convert_alpha()
grass = pygame.transform.scale(grass, (76, 75)).convert_alpha()
bl_coral = pygame.image.load('scenery/bl_coral.png').convert_alpha()
bl_coral = pygame.transform.scale(bl_coral, (85, 85)).convert_alpha()
metal = pygame.image.load('scenery/metal.png').convert_alpha()
metal = pygame.transform.scale(metal, (75, 90)).convert_alpha()
lizard = pygame.image.load('scenery/lizard.png').convert_alpha()
lizard = pygame.transform.scale(lizard, (50, 50)).convert_alpha()
statue = pygame.image.load('scenery/statue.png').convert_alpha()
flamingo = pygame.image.load('scenery/flamingo.png').convert_alpha()
flamingo = pygame.transform.scale(flamingo, (90, 140)).convert_alpha()
vulcano = pygame.image.load('scenery/vulcano.png').convert_alpha()
cash = pygame.transform.scale(cash, (65, 60)).convert_alpha()
cash1 = pygame.transform.scale(cash, (50, 46)).convert_alpha()
door = pygame.image.load('buttons/door.png').convert_alpha()
door = pygame.transform.scale(door, (110, 110)).convert_alpha()
door_coll = pygame.image.load('buttons/door_coll.png').convert_alpha()
door_coll = pygame.transform.scale(door_coll, (110, 110)).convert_alpha()
fishes_button = pygame.image.load('buttons/fishes_button.png').convert_alpha()
fishes_button_coll = pygame.image.load('buttons/fishes_button_coll.png').convert_alpha()
scenery_button = pygame.image.load('buttons/scenery_button.png').convert_alpha()
scenery_button_coll = pygame.image.load('buttons/scenery_button_coll.png').convert_alpha()
equipment_button = pygame.image.load('buttons/equipment_button.png').convert_alpha()
equipment_button_coll = pygame.image.load('buttons/equipment_button_coll.png').convert_alpha()
scenery2_button = pygame.image.load('buttons/scenery2_button.png').convert_alpha()
scenery2_button_coll = pygame.image.load('buttons/scenery2_button_coll.png').convert_alpha()
fish_button = pygame.image.load('buttons/fish_button.png').convert_alpha()
fish_button_coll = pygame.image.load('buttons/fish_button_coll.png').convert_alpha()
cancel = pygame.image.load('buttons/cancel.png').convert_alpha()
cancel_coll = pygame.image.load('buttons/cancel_coll.png').convert_alpha()
blocked_info = pygame.image.load('buttons/blocked_info.png').convert_alpha()
blocked_cover = pygame.image.load('buttons/blocked_cover.png').convert_alpha()
border_shop = pygame.image.load('buttons/border_shop.png').convert_alpha()
border_shop = pygame.transform.scale(border_shop, (350, 110)).convert_alpha()
mini_button = pygame.image.load('buttons/mini_button.png').convert_alpha()
coral_button = pygame.image.load('scenery_buttons/coral_button.png').convert_alpha()
flamingo_button = pygame.image.load('scenery_buttons/flamingo_button.png').convert_alpha()
grass_button = pygame.image.load('scenery_buttons/grass_button.png').convert_alpha()
grn_plant_button = pygame.image.load('scenery_buttons/grn_plant_button.png').convert_alpha()
house_button = pygame.image.load('scenery_buttons/house_button.png').convert_alpha()
lizard_button = pygame.image.load('scenery_buttons/lizard_button.png').convert_alpha()
metal_button = pygame.image.load('scenery_buttons/metal_button.png').convert_alpha()
pin_plant_button = pygame.image.load('scenery_buttons/pin_plant_button.png').convert_alpha()
pur_plant_button = pygame.image.load('scenery_buttons/pur_plant_button.png').convert_alpha()
skeleton_button = pygame.image.load('scenery_buttons/skeleton_button.png').convert_alpha()
statue_button = pygame.image.load('scenery_buttons/statue_button.png').convert_alpha()
vulcano_button = pygame.image.load('scenery_buttons/vulcano_button.png').convert_alpha()
owned_item = pygame.image.load('scenery_buttons/owned_item.png').convert_alpha()
in_item = pygame.image.load('scenery_buttons/in_item.png').convert_alpha()
shop_aquarium = pygame.image.load('buttons/shop_aquarium.png').convert_alpha()
padlock = pygame.image.load('buttons/padlock.png').convert_alpha()
padlock = pygame.transform.scale(padlock, (50, 50)).convert_alpha()
rod_panel= pygame.image.load('buttons/rod_panel.png').convert_alpha()
rod_cover = pygame.image.load('buttons/rod_cover.png').convert_alpha()
info_button = pygame.image.load('buttons/info_button.png').convert_alpha()
info_button = pygame.transform.scale(info_button, (60, 60)).convert_alpha()
info_button_coll = pygame.image.load('buttons/info_button_coll.png').convert_alpha()
info_button_coll = pygame.transform.scale(info_button_coll, (60, 60)).convert_alpha()
save_button = pygame.image.load('buttons/save_button.png').convert_alpha()
save_button_coll = pygame.image.load('buttons/save_button_coll.png').convert_alpha()
back_button = pygame.image.load('buttons/back_button.png').convert_alpha()
back_button_coll = pygame.image.load('buttons/back_button_coll.png').convert_alpha()
fishes_info = pygame.image.load('buttons/fishes_info.png').convert_alpha()
fishes_info_cover = pygame.image.load('buttons/fishes_info_cover.png').convert_alpha()
fishing_info = pygame.image.load('buttons/fishing_info.png').convert_alpha()
fishing_info_cover = pygame.image.load('buttons/fishing_info_cover.png').convert_alpha()
boat = pygame.image.load('equipment/boat.png').convert_alpha()
start_fishing = pygame.image.load('buttons/start_fishing.png').convert_alpha()
start_fishing_coll = pygame.image.load('buttons/start_fishing_coll.png').convert_alpha()
start_fishing_coll = pygame.transform.scale(start_fishing_coll, (326, 50)).convert_alpha()
start1 = pygame.image.load('buttons/start1.png').convert_alpha()
start_fishing = pygame.transform.scale(start_fishing, (326, 50)).convert_alpha()
start1_coll = pygame.image.load('buttons/start1_coll.png').convert_alpha()
cancel_1 = pygame.image.load('buttons/cancel_1.png').convert_alpha()
saved_game = pygame.image.load('buttons/saved_game.png').convert_alpha()
#---------------------------------------------shop_fishes
fightfish = pygame.image.load('shop_fishes/fightfish.png').convert_alpha()
clownfish = pygame.image.load('shop_fishes/clownfish.png').convert_alpha()
starfish = pygame.image.load('shop_fishes/starfish.png').convert_alpha()
jelly = pygame.image.load('shop_fishes/jelly.png').convert_alpha()
lionfish = pygame.image.load('shop_fishes/lionfish.png').convert_alpha()
tang = pygame.image.load('shop_fishes/tang.png').convert_alpha()
ray = pygame.image.load('shop_fishes/ray.png').convert_alpha()
octopus = pygame.image.load('shop_fishes/octopus.png').convert_alpha()
seahorse = pygame.image.load('shop_fishes/seahorse.png').convert_alpha()
#-----------------------------------------------------rodes
bamboo_rod = pygame.image.load('equipment/bamboo_rod.png').convert_alpha()
bamboo_rod = pygame.transform.scale(bamboo_rod, (120, 120)).convert_alpha()
wooden_rod = pygame.image.load('equipment/wooden_rod.png').convert_alpha()
wooden_rod = pygame.transform.scale(wooden_rod, (120, 120)).convert_alpha()
iron_rod = pygame.image.load('equipment/iron_rod.png').convert_alpha()
iron_rod = pygame.transform.scale(iron_rod, (120, 120)).convert_alpha()
carbon_rod = pygame.image.load('equipment/carbon_rod.png').convert_alpha()
carbon_rod = pygame.transform.scale(carbon_rod, (120, 120)).convert_alpha()
golden_rod = pygame.image.load('equipment/golden_rod.png').convert_alpha()
golden_rod = pygame.transform.scale(golden_rod, (120, 120)).convert_alpha()
#------------------------------------------------------------------lake_fishes
blue_fish = pygame.image.load('lake_fishes/blue_fish.png').convert_alpha()
pike = pygame.image.load('lake_fishes/pike.png').convert_alpha()
fat_fish = pygame.image.load('lake_fishes/fat_fish.png').convert_alpha()
frog = pygame.image.load('lake_fishes/frog.png').convert_alpha()
koi_fish = pygame.image.load('lake_fishes/koi_fish.png').convert_alpha()
piranha = pygame.image.load('lake_fishes/piranha.png').convert_alpha()
snail = pygame.image.load('lake_fishes/snail.png').convert_alpha()
sturgeon = pygame.image.load('lake_fishes/sturgeon.png').convert_alpha()
#----------------------------------------------------------------------------sea_fishes
prawn = pygame.image.load('sea_fishes/prawn.png').convert_alpha()
tiger_fish = pygame.image.load('sea_fishes/tiger_fish.png').convert_alpha()
crab = pygame.image.load('sea_fishes/crab.png').convert_alpha()
sword_fish = pygame.image.load('sea_fishes/sword_fish.png').convert_alpha()
turtle = pygame.image.load('sea_fishes/turtle.png').convert_alpha()
shark = pygame.image.load('sea_fishes/shark.png').convert_alpha()
light_fish = pygame.image.load('sea_fishes/light_fish.png').convert_alpha()
nautilus = pygame.image.load('sea_fishes/nautilus.png').convert_alpha()
zombie_fish = pygame.image.load('sea_fishes/zombie_fish.png').convert_alpha()
#------------------------------------------------------------fishes buttons
blue_button = pygame.image.load('fish_buttons/blue_button.png').convert_alpha()
clown_button = pygame.image.load('fish_buttons/clown_button.png').convert_alpha()
crab_button = pygame.image.load('fish_buttons/crab_button.png').convert_alpha()
fat_button = pygame.image.load('fish_buttons/fat_button.png').convert_alpha()
fight_button = pygame.image.load('fish_buttons/fight_button.png').convert_alpha()
frog_button = pygame.image.load('fish_buttons/frog_button.png').convert_alpha()
jelly_button = pygame.image.load('fish_buttons/jelly_button.png').convert_alpha()
koi_button = pygame.image.load('fish_buttons/koi_button.png').convert_alpha()
light_button = pygame.image.load('fish_buttons/light_button.png').convert_alpha()
lion_button = pygame.image.load('fish_buttons/lion_button.png').convert_alpha()
nautilus_button = pygame.image.load('fish_buttons/nautilus_button.png').convert_alpha()
octopus_button = pygame.image.load('fish_buttons/octopus_button.png').convert_alpha()
pike_button = pygame.image.load('fish_buttons/pike_button.png').convert_alpha()
piranha_button = pygame.image.load('fish_buttons/piranha_button.png').convert_alpha()
prawn_button = pygame.image.load('fish_buttons/prawn_button.png').convert_alpha()
ray_button = pygame.image.load('fish_buttons/ray_button.png').convert_alpha()
seahorse_button = pygame.image.load('fish_buttons/seahorse_button.png').convert_alpha()
shark_button = pygame.image.load('fish_buttons/shark_button.png').convert_alpha()
snail_button = pygame.image.load('fish_buttons/snail_button.png').convert_alpha()
star_button = pygame.image.load('fish_buttons/star_button.png').convert_alpha()
sturgeon_button = pygame.image.load('fish_buttons/sturgeon_button.png').convert_alpha()
sword_button = pygame.image.load('fish_buttons/sword_button.png').convert_alpha()
tang_button = pygame.image.load('fish_buttons/tang_button.png').convert_alpha()
tiger_button = pygame.image.load('fish_buttons/tiger_button.png').convert_alpha()
turtle_button = pygame.image.load('fish_buttons/turtle_button.png').convert_alpha()
zombie_button = pygame.image.load('fish_buttons/zombie_button.png').convert_alpha()
#-------------------------------------------------------------------
pond1 = pygame.image.load('pond_fishing/pond1.jpg').convert_alpha()
pond1 = pygame.transform.scale(pond1, (414, 600)).convert_alpha()
to_backpack = pygame.image.load('buttons/to_backpack.png').convert_alpha()
release = pygame.image.load('buttons/release.png').convert_alpha()
backpack = pygame.image.load('buttons/backpack.png').convert_alpha()
backpack = pygame.transform.scale(backpack, (140, 140)).convert_alpha()
sea1 = pygame.image.load('sea_fishing/sea1.png').convert_alpha()
fish_frame = pygame.image.load('buttons/fish_frame.png').convert_alpha()
fish_frame_coll = pygame.image.load('buttons/fish_frame_coll.png').convert_alpha()
plus = pygame.image.load('buttons/plus.png').convert_alpha()
minus = pygame.image.load('buttons/minus.png').convert_alpha()
empty_backpack = pygame.image.load('buttons/empty_backpack.png').convert_alpha()
full_backpack = pygame.image.load('buttons/full_backpack.png').convert_alpha()
locked = pygame.image.load('buttons/locked.png').convert_alpha()
achievement_button = pygame.image.load('buttons/achievement_button.png').convert_alpha()
achievement_button_coll = pygame.image.load('buttons/achievement_button_coll.png').convert_alpha()
zero_fishes = pygame.image.load('buttons/zero_fishes.png').convert_alpha()
trophy_button = pygame.image.load('buttons/trophy_button.png').convert_alpha()
trophy_button_coll = pygame.image.load('buttons/trophy_button_coll.png').convert_alpha()
gift_button = pygame.image.load('buttons/gift_button.png').convert_alpha()
locked_gift = pygame.image.load('buttons/locked_gift.png').convert_alpha()
gift_alert1 = pygame.image.load('buttons/gift_alert.png').convert_alpha()
received_gift = pygame.image.load('buttons/received_gift.png').convert_alpha()
trophy_img = pygame.image.load('buttons/trophy.png').convert_alpha()
trophy_square = pygame.image.load('buttons/trophy_back.png').convert_alpha()
s_trophy = pygame.image.load('buttons/s_trophy.png').convert_alpha()
b_trophy = pygame.image.load('buttons/b_trophy.png').convert_alpha()
mode = 0
start_game = 0

def home(event):
    global mode, start_game,money,pin_plant,vulcano,pur_plant,grn_plant,statue,in_sum,aqua_slots,trophy_owned
    global grass_owned,bl_coral_owned,flamingo_owned,grn_plant_owned,lizard_owned,metal_owned,mini_house_owned,pin_plant_owned,pur_plant_owned,skeleton_owned,statue_owned,vulcano_owned
    global grass_in,pur_plant_in,bl_coral_in,metal_in,pin_plant_in,lizard_in,grn_plant_in,skeleton_in,mini_house_in,statue_in,flamingo_in,vulcano_in
    global fightfish_owned,clownfish_owned,starfish_owned,jelly_owned,lionfish_owned,tang_owned,ray_owned,octopus_owned,seahorse_owned
    global fightfish_amount,clownfish_amount,starfish_amount,jelly_amount,lionfish_amount,tang_amount,ray_amount,octopus_amount,seahorse_amount
    global fightfish_in,clownfish_in,starfish_in,jelly_in,lionfish_in,tang_in,ray_in,octopus_in,seahorse_in
    global wooden_owned, iron_owned, carbon_owned, golden_owned, boat_owned,backpack_slots
    global blue_fish_owned,pike_owned,fat_fish_owned,snail_owned,frog_owned,koi_fish_owned,sturgeon_owned,piranha_owned
    global blue_fish_amount,pike_amount,fat_fish_amount,snail_amount,frog_amount,koi_fish_amount,sturgeon_amount,piranha_amount
    global prawn_owned,tiger_fish_owned,crab_owned,sword_fish_owned,turtle_owned,shark_owned,light_fish_owned,zombie_fish_owned,nautilus_owned
    global prawn_amount,tiger_fish_amount,crab_amount,sword_fish_amount,turtle_amount,shark_amount,light_fish_amount,zombie_fish_amount,nautilus_amount
    global blue_fish_in,pike_in,fat_fish_in,snail_in,frog_in,koi_in,sturgeon_in,piranha_in,prawn_in,tiger_in,crab_in,sword_in,turtle_in,shark_in,light_in,nautilus_in,zombie_in
    global gift_1_received,gift_2_received,gift_3_received,gift_4_received,gift_5_received,catched,decorations,fish_bought,total_money
    pin_plant = pygame.transform.scale(pin_plant, (130, 260))
    grn_plant = pygame.transform.scale(grn_plant, (162, 248))
    vulcano = pygame.transform.scale(vulcano, (180, 160))
    pur_plant = pygame.transform.scale(pur_plant, (44, 218))
    pur_plant = pygame.transform.scale(pur_plant, (44, 218))
    statue = pygame.transform.scale(statue, (74, 140))
    active = False
    active1 = False
    back_active = False
    blue_get_dir = clown_get_dir = crab_get_dir = fat_get_dir = fight_get_dir = frog_get_dir = jelly_get_dir = koi_get_dir = light_get_dir = lion_get_dir = nautilus_get_dir = octopus_get_dir = pike_get_dir = piranha_get_dir = prawn_get_dir = ray_get_dir = seahorse_get_dir = shark_get_dir = snail_get_dir = star_get_dir = sturgeon_get_dir = sword_get_dir = tang_get_dir = tiger_get_dir = turtle_get_dir = zombie_get_dir = False
    if mode == 1 and start_game == 1:
        money = 100
        start_game = 0
        #-------------------scenery owned
        grass_owned = False
        bl_coral_owned = False
        flamingo_owned = False
        grn_plant_owned = False
        lizard_owned = False
        metal_owned = False
        mini_house_owned = False
        pin_plant_owned = False
        pur_plant_owned = False
        skeleton_owned = False
        statue_owned = False
        vulcano_owned = False
        grass_in = False
        pur_plant_in = False
        bl_coral_in = False
        metal_in = False
        pin_plant_in = False
        lizard_in = False
        grn_plant_in = False
        skeleton_in = False
        mini_house_in = False
        statue_in = False
        flamingo_in = False
        vulcano_in = False
        #--------------------shop fishes owned
        fightfish_owned = False
        clownfish_owned = False
        starfish_owned = False
        jelly_owned = False
        lionfish_owned = False
        tang_owned = False
        ray_owned = False
        octopus_owned = False
        seahorse_owned = False
        #----------------------shop fishes amount
        fightfish_amount = 0
        clownfish_amount = 0
        starfish_amount = 0
        jelly_amount = 0
        lionfish_amount = 0
        tang_amount = 0
        ray_amount = 0
        octopus_amount = 0
        seahorse_amount = 0
        #-------------------shop fishes in
        fightfish_in = False
        clownfish_in = False
        starfish_in = False
        jelly_in = False
        lionfish_in = False
        tang_in = False
        ray_in = False
        octopus_in = False
        seahorse_in = False
        #------------------rods owned
        wooden_owned = False
        iron_owned = False
        carbon_owned = False
        golden_owned = False
        boat_owned = False
        #------------------
        backpack_slots = 0
        aqua_slots = 0
        #-------------------lake fishes
        blue_fish_owned = False
        pike_owned = False
        fat_fish_owned = False
        snail_owned = False
        frog_owned = False
        koi_fish_owned = False
        sturgeon_owned = False
        piranha_owned = False
        #----------------------lake fishes amount
        blue_fish_amount = 0
        pike_amount = 0
        fat_fish_amount = 0
        snail_amount = 0
        frog_amount = 0
        koi_fish_amount = 0
        sturgeon_amount = 0
        piranha_amount = 0
        #-----------------sea fishes
        prawn_owned = False
        tiger_fish_owned = False
        crab_owned = False
        sword_fish_owned = False
        turtle_owned = False
        shark_owned = False
        light_fish_owned = False
        nautilus_owned = False
        zombie_fish_owned = False
        #-----------------------sea fishes amount
        prawn_amount = 0
        tiger_fish_amount = 0
        crab_amount = 0
        sword_fish_amount = 0
        turtle_amount = 0
        shark_amount = 0
        light_fish_amount = 0
        zombie_fish_amount = 0
        nautilus_amount = 0
        #-----------------------------
        in_sum = 0
        catched = 0
        decorations = 0
        fish_bought = 0
        total_money = 0
        #------------------------wild fishes in
        blue_fish_in = False
        pike_in = False
        fat_fish_in = False
        snail_in = False
        frog_in = False
        koi_in = False
        sturgeon_in = False
        piranha_in = False
        prawn_in = False
        tiger_in = False
        crab_in = False
        sword_in = False
        turtle_in = False
        shark_in = False
        light_in = False
        nautilus_in = False
        zombie_in = False
        #-----------------------------------
        gift_1_received = False
        gift_2_received = False
        gift_3_received = False
        gift_4_received = False
        gift_5_received = False
        #----------------------------
        trophy_owned = False
    elif mode != 1 and start_game == 1:
        with open("zapis.pkl", "rb") as f:
            money = pickle.load(f)
            grass_owned = pickle.load(f)
            bl_coral_owned = pickle.load(f)
            flamingo_owned = pickle.load(f)
            grn_plant_owned = pickle.load(f)
            lizard_owned = pickle.load(f)
            metal_owned = pickle.load(f)
            mini_house_owned = pickle.load(f)
            pin_plant_owned = pickle.load(f)
            pur_plant_owned = pickle.load(f)
            skeleton_owned = pickle.load(f)
            statue_owned = pickle.load(f)
            vulcano_owned = pickle.load(f)
            grass_in = pickle.load(f)
            pur_plant_in = pickle.load(f)
            bl_coral_in = pickle.load(f)
            metal_in = pickle.load(f)
            pin_plant_in = pickle.load(f)
            lizard_in = pickle.load(f)
            grn_plant_in = pickle.load(f)
            skeleton_in = pickle.load(f)
            mini_house_in = pickle.load(f)
            statue_in = pickle.load(f)
            flamingo_in = pickle.load(f)
            vulcano_in = pickle.load(f)
            fightfish_owned = pickle.load(f)
            clownfish_owned = pickle.load(f)
            starfish_owned = pickle.load(f)
            jelly_owned = pickle.load(f)
            lionfish_owned = pickle.load(f)
            tang_owned = pickle.load(f)
            ray_owned = pickle.load(f)
            octopus_owned = pickle.load(f)
            seahorse_owned = pickle.load(f)
            fightfish_amount = pickle.load(f)
            clownfish_amount = pickle.load(f)
            starfish_amount = pickle.load(f)
            jelly_amount = pickle.load(f)
            lionfish_amount = pickle.load(f)
            tang_amount = pickle.load(f)
            ray_amount = pickle.load(f)
            octopus_amount = pickle.load(f)
            seahorse_amount = pickle.load(f)
            fightfish_in = pickle.load(f)
            clownfish_in = pickle.load(f)
            starfish_in = pickle.load(f)
            jelly_in = pickle.load(f)
            lionfish_in = pickle.load(f)
            tang_in = pickle.load(f)
            ray_in = pickle.load(f)
            octopus_in = pickle.load(f)
            seahorse_in = pickle.load(f)
            wooden_owned = pickle.load(f)
            iron_owned = pickle.load(f)
            carbon_owned = pickle.load(f)
            golden_owned = pickle.load(f)
            boat_owned = pickle.load(f)
            backpack_slots = pickle.load(f)
            aqua_slots = pickle.load(f)
            blue_fish_owned = pickle.load(f)
            pike_owned = pickle.load(f)
            fat_fish_owned = pickle.load(f)
            snail_owned = pickle.load(f)
            frog_owned = pickle.load(f)
            koi_fish_owned = pickle.load(f)
            sturgeon_owned = pickle.load(f)
            piranha_owned = pickle.load(f)
            blue_fish_amount = pickle.load(f)
            pike_amount = pickle.load(f)
            fat_fish_amount = pickle.load(f)
            snail_amount = pickle.load(f)
            frog_amount = pickle.load(f)
            koi_fish_amount = pickle.load(f)
            sturgeon_amount = pickle.load(f)
            piranha_amount = pickle.load(f)
            prawn_owned = pickle.load(f)
            tiger_fish_owned = pickle.load(f)
            crab_owned = pickle.load(f)
            sword_fish_owned = pickle.load(f)
            turtle_owned = pickle.load(f)
            shark_owned = pickle.load(f)
            light_fish_owned = pickle.load(f)
            nautilus_owned = pickle.load(f)
            zombie_fish_owned = pickle.load(f)
            prawn_amount = pickle.load(f)
            tiger_fish_amount = pickle.load(f)
            crab_amount = pickle.load(f)
            sword_fish_amount = pickle.load(f)
            turtle_amount = pickle.load(f)
            shark_amount = pickle.load(f)
            light_fish_amount = pickle.load(f)
            zombie_fish_amount = pickle.load(f)
            nautilus_amount = pickle.load(f)
            in_sum = pickle.load(f)
            catched = pickle.load(f)
            decorations = pickle.load(f)
            fish_bought = pickle.load(f)
            total_money = pickle.load(f)
            blue_fish_in = pickle.load(f)
            pike_in = pickle.load(f)
            fat_fish_in = pickle.load(f)
            snail_in = pickle.load(f)
            frog_in = pickle.load(f)
            koi_in = pickle.load(f)
            sturgeon_in = pickle.load(f)
            piranha_in = pickle.load(f)
            prawn_in = pickle.load(f)
            tiger_in = pickle.load(f)
            crab_in = pickle.load(f)
            sword_in = pickle.load(f)
            turtle_in = pickle.load(f)
            shark_in = pickle.load(f)
            light_in = pickle.load(f)
            nautilus_in = pickle.load(f)
            zombie_in = pickle.load(f)
            gift_1_received = pickle.load(f)
            gift_2_received = pickle.load(f)
            gift_3_received = pickle.load(f)
            gift_4_received = pickle.load(f)
            gift_5_received = pickle.load(f)
            trophy_owned = pickle.load(f)
            start_game = 0
    else:
        pass  # !!! tutaj gra bedzie wczytywala ekwipunek ze zmiennych globalnych, gdy "to nie bedzie pierwsza wizyta w home gracza (gdy nie bedzie to wizyta po ekranie startowym)" 
    image_list = []
    for i in range(1, 32):
        filename = f"bubb_animation/bubb_{i}.png"
        img = pygame.image.load(filename)
        image_list.append(img)

    current_image_index = 0
    display_time = 90
    last_display_time = pygame.time.get_ticks()
    x = random.randint(400, 800)
    y = 290
    image_list_v = []
    for i in range(1, 47):
        filename_v = f"vulcano_animation/bubb_{i}.png"
        filename_v = pygame.image.load(filename_v)
        filename_v = pygame.transform.scale(filename_v, (36, 282))
        image_list_v.append(filename_v)

    current_image_index_v = 0
    display_time_v = 50
    saved_vis = False
    loop = False
    last_display_time_v = pygame.time.get_ticks()
    clownfish1 = pygame.transform.scale(clownfish,(67,63))
    seahorse1 = pygame.transform.scale(seahorse,(56,80))
    tang1 = pygame.transform.scale(tang,(90,63))
    jelly1 = pygame.transform.rotate(jelly,270)
    run = True
    while run:
        window.blit(background, (0, 0))
        window.blit(cash,(920,10))
        scenery_rect = scenery2_button.get_rect()
        scenery_rect.topleft = (290,520)
        back_rect = back_button.get_rect()
        back_rect.topleft = (10,520)
        if scenery_rect.collidepoint(pygame.mouse.get_pos()) and back_active==False:
                window.blit(scenery2_button_coll,(290,520))
        else:
                window.blit(scenery2_button,(290,520))
        if back_rect.collidepoint(pygame.mouse.get_pos()) and back_active==False:
                window.blit(back_button_coll,(10,520))
        else:
                window.blit(back_button,(10,520))
        fishes_rect = fish_button.get_rect()
        fishes_rect.topleft = (200,520)
        if fishes_rect.collidepoint(pygame.mouse.get_pos()) and back_active==False:
                window.blit(fish_button_coll,(200,520))
        else:
                window.blit(fish_button,(200,520))
        outdoor_rect = door.get_rect()
        outdoor_rect.topleft = (960, 480)
        trophy_rect = trophy_button.get_rect()
        trophy_rect.topleft = (720,520)
        achievement_rect = achievement_button.get_rect()
        achievement_rect.topleft = (810,520)
        money_amount = font.render(str(money),True,(255,255,255))
        window.blit(money_amount,(983,31))    
        #----------------------------------------
        if shark_in == True:
            if shark_get_dir==False:
                shark_x = random.randint(320, 710)
                shark_y = random.randint(175, 315)
                shark_direction_x = random.choice([-1, 1])
                shark_direction_y = random.choice([-1, 1])
                shark_touch=0
                shark_speed = random.uniform(0.4, 0.7)
                shark_get_dir=True
            else:
                pass
            shark_a,shark_x,shark_y,shark_direction_x,shark_direction_y,shark_touch,shark_speed = swim(shark,shark_x,shark_y,shark_direction_x,shark_direction_y,shark_touch,shark_speed)
            window.blit(shark_a,(shark_x,shark_y))
        if sword_in == True:
            if sword_get_dir==False:
                sword_x = random.randint(320, 710)
                sword_y = random.randint(175, 315)
                sword_direction_x = random.choice([-1, 1])
                sword_direction_y = random.choice([-1, 1])
                sword_touch=0
                sword_speed = random.uniform(0.4, 0.7)
                sword_get_dir=True
            else:
                pass
            sword_a,sword_x,sword_y,sword_direction_x,sword_direction_y,sword_touch,sword_speed = swim(sword_fish,sword_x,sword_y,sword_direction_x,sword_direction_y,sword_touch,sword_speed)
            window.blit(sword_a,(sword_x,sword_y))
        if piranha_in == True:
            if piranha_get_dir==False:
                piranha_x = random.randint(320, 710)
                piranha_y = random.randint(175, 315)
                piranha_direction_x = random.choice([-1, 1])
                piranha_direction_y = random.choice([-1, 1])
                piranha_touch=0
                piranha_speed = random.uniform(0.4, 0.7)
                piranha_get_dir=True
            else:
                pass
            piranha_a,piranha_x,piranha_y,piranha_direction_x,piranha_direction_y,piranha_touch,piranha_speed = swim(piranha,piranha_x,piranha_y,piranha_direction_x,piranha_direction_y,piranha_touch,piranha_speed)
            window.blit(piranha_a,(piranha_x,piranha_y))
        if sturgeon_in == True:
            if sturgeon_get_dir==False:
                sturgeon_x = random.randint(320, 710)
                sturgeon_y = random.randint(175, 315)
                sturgeon_direction_x = random.choice([-1, 1])
                sturgeon_direction_y = random.choice([-1, 1])
                sturgeon_touch=0
                sturgeon_speed = random.uniform(0.4, 0.7)
                sturgeon_get_dir=True
            else:
                pass
            sturgeon_a,sturgeon_x,sturgeon_y,sturgeon_direction_x,sturgeon_direction_y,sturgeon_touch,sturgeon_speed = swim(sturgeon,sturgeon_x,sturgeon_y,sturgeon_direction_x,sturgeon_direction_y,sturgeon_touch,sturgeon_speed)
            window.blit(sturgeon_a,(sturgeon_x,sturgeon_y))
        if zombie_in == True:
            if zombie_get_dir==False:
                zombie_x = random.randint(320, 710)
                zombie_y = random.randint(175, 315)
                zombie_direction_x = random.choice([-1, 1])
                zombie_direction_y = random.choice([-1, 1])
                zombie_touch=0
                zombie_speed = random.uniform(0.4, 0.7)
                zombie_get_dir=True
            else:
                pass
            zombie_a,zombie_x,zombie_y,zombie_direction_x,zombie_direction_y,zombie_touch,zombie_speed = swim(zombie_fish,zombie_x,zombie_y,zombie_direction_x,zombie_direction_y,zombie_touch,zombie_speed)
            window.blit(zombie_a,(zombie_x,zombie_y))
        if light_in == True:
            if light_get_dir==False:
                light_x = random.randint(320, 710)
                light_y = random.randint(175, 315)
                light_direction_x = random.choice([-1, 1])
                light_direction_y = random.choice([-1, 1])
                light_touch=0
                light_speed = random.uniform(0.4, 0.7)
                light_get_dir=True
            else:
                pass
            light_a,light_x,light_y,light_direction_x,light_direction_y,light_touch,light_speed = swim(light_fish,light_x,light_y,light_direction_x,light_direction_y,light_touch,light_speed)
            window.blit(light_a,(light_x,light_y))
        if octopus_in == True:
            if octopus_get_dir==False:
                octopus_x = random.randint(320, 710)
                octopus_y = random.randint(175, 315)
                octopus_direction_x = random.choice([-1, 1])
                octopus_direction_y = random.choice([-1, 1])
                octopus_touch=0
                octopus_speed = random.uniform(0.4, 0.7)
                octopus_get_dir=True
            else:
                pass
            octopus_a,octopus_x,octopus_y,octopus_direction_x,octopus_direction_y,octopus_touch,octopus_speed = swim(octopus,octopus_x,octopus_y,octopus_direction_x,octopus_direction_y,octopus_touch,octopus_speed)
            window.blit(octopus_a,(octopus_x,octopus_y))
        if lionfish_in == True:
            if lion_get_dir==False:
                lion_x = random.randint(320, 710)
                lion_y = random.randint(175, 315)
                lion_direction_x = random.choice([-1, 1])
                lion_direction_y = random.choice([-1, 1])
                lion_touch=0
                lion_speed = random.uniform(0.4, 0.7)
                lion_get_dir=True
            else:
                pass
            lion_a,lion_x,lion_y,lion_direction_x,lion_direction_y,lion_touch,lion_speed = swim(lionfish,lion_x,lion_y,lion_direction_x,lion_direction_y,lion_touch,lion_speed)
            window.blit(lion_a,(lion_x,lion_y))
        if fat_fish_in == True:
            if fat_get_dir==False:
                fat_x = random.randint(320, 710)
                fat_y = random.randint(175, 315)
                fat_direction_x = random.choice([-1, 1])
                fat_direction_y = random.choice([-1, 1])
                fat_touch=0
                fat_speed = random.uniform(0.4, 0.7)
                fat_get_dir=True
            else:
                pass
            fat_a,fat_x,fat_y,fat_direction_x,fat_direction_y,fat_touch,fat_speed = swim(fat_fish,fat_x,fat_y,fat_direction_x,fat_direction_y,fat_touch,fat_speed)
            window.blit(fat_a,(fat_x,fat_y))
        #----------------------------------------
        if vulcano_in == True:
            window.blit(image_list_v[current_image_index_v], (680,15))
            current_time_v = pygame.time.get_ticks()
            if current_time_v - last_display_time_v >= display_time_v:
                current_image_index_v = (current_image_index_v + 1) % len(image_list_v)
                last_display_time_v= current_time_v
        #---------------------scenery in aquarium
        if vulcano_in == True:
            window.blit(vulcano, (611, 260))
        if flamingo_in == True:
            window.blit(flamingo, (350, 281))  
        if statue_in == True:
            window.blit(statue, (426, 281))    
        if grn_plant_in == True:
            window.blit(grn_plant, (214, 174))
        if mini_house_in == True:
            window.blit(mini_house, (530, 347))
        #-------------------------------------------------------
        if blue_fish_in == True:
            if blue_get_dir==False:
                blue_x = random.randint(320, 710)
                blue_y = random.randint(175, 315)
                blue_direction_x = random.choice([-1, 1])
                blue_direction_y = random.choice([-1, 1])
                blue_touch=0
                blue_speed = random.uniform(0.4, 0.7)
                blue_get_dir=True
            else:
                pass
            blue_fish_a,blue_x,blue_y,blue_direction_x,blue_direction_y,blue_touch,blue_speed = swim(blue_fish,blue_x,blue_y,blue_direction_x,blue_direction_y,blue_touch,blue_speed)
            window.blit(blue_fish_a,(blue_x,blue_y))
        if clownfish_in == True:
            if clown_get_dir==False:
                clown_x = random.randint(320, 710)
                clown_y = random.randint(175, 315)
                clown_direction_x = random.choice([-1, 1])
                clown_direction_y = random.choice([-1, 1])
                clown_touch=0
                clown_speed = random.uniform(0.4, 0.7)
                clown_get_dir=True
            else:
                pass
            clown_a,clown_x,clown_y,clown_direction_x,clown_direction_y,clown_touch,clown_speed = swim(clownfish1,clown_x,clown_y,clown_direction_x,clown_direction_y,clown_touch,clown_speed)
            window.blit(clown_a,(clown_x,clown_y))
        if fightfish_in == True:
            if fight_get_dir==False:
                fight_x = random.randint(320, 710)
                fight_y = random.randint(175, 315)
                fight_direction_x = random.choice([-1, 1])
                fight_direction_y = random.choice([-1, 1])
                fight_touch=0
                fight_speed = random.uniform(0.4, 0.7)
                fight_get_dir=True
            else:
                pass
            fight_a,fight_x,fight_y,fight_direction_x,fight_direction_y,fight_touch,fight_speed = swim(fightfish,fight_x,fight_y,fight_direction_x,fight_direction_y,fight_touch,fight_speed)
            window.blit(fight_a,(fight_x,fight_y))
        if frog_in == True:
            if frog_get_dir==False:
                frog_x = random.randint(320, 710)
                frog_y = random.randint(175, 315)
                frog_direction_x = random.choice([-1, 1])
                frog_direction_y = random.choice([-1, 1])
                frog_touch=0
                frog_speed = random.uniform(0.4, 0.7)
                frog_get_dir=True
            else:
                pass
            frog_a,frog_x,frog_y,frog_direction_x,frog_direction_y,frog_touch,frog_speed = swim(frog,frog_x,frog_y,frog_direction_x,frog_direction_y,frog_touch,frog_speed)
            window.blit(frog_a,(frog_x,frog_y))
        if koi_in == True:
            if koi_get_dir==False:
                koi_x = random.randint(320, 710)
                koi_y = random.randint(175, 315)
                koi_direction_x = random.choice([-1, 1])
                koi_direction_y = random.choice([-1, 1])
                koi_touch=0
                koi_speed = random.uniform(0.4, 0.7)
                koi_get_dir=True
            else:
                pass
            koi_a,koi_x,koi_y,koi_direction_x,koi_direction_y,koi_touch,koi_speed = swim(koi_fish,koi_x,koi_y,koi_direction_x,koi_direction_y,koi_touch,koi_speed)
            window.blit(koi_a,(koi_x,koi_y))
        if nautilus_in == True:
            if nautilus_get_dir==False:
                nautilus_x = random.randint(320, 710)
                nautilus_y = random.randint(175, 315)
                nautilus_direction_x = random.choice([-1, 1])
                nautilus_direction_y = random.choice([-1, 1])
                nautilus_touch=0
                nautilus_speed = random.uniform(0.4, 0.7)
                nautilus_get_dir=True
            else:
                pass
            nautilus_a,nautilus_x,nautilus_y,nautilus_direction_x,nautilus_direction_y,nautilus_touch,nautilus_speed = swim(nautilus,nautilus_x,nautilus_y,nautilus_direction_x,nautilus_direction_y,nautilus_touch,nautilus_speed)
            window.blit(nautilus_a,(nautilus_x,nautilus_y))
        if pike_in == True:
            if pike_get_dir==False:
                pike_x = random.randint(320, 710)
                pike_y = random.randint(175, 315)
                pike_direction_x = random.choice([-1, 1])
                pike_direction_y = random.choice([-1, 1])
                pike_touch=0
                pike_speed = random.uniform(0.4, 0.7)
                pike_get_dir=True
            else:
                pass
            pike_a,pike_x,pike_y,pike_direction_x,pike_direction_y,pike_touch,pike_speed = swim(pike,pike_x,pike_y,pike_direction_x,pike_direction_y,pike_touch,pike_speed)
            window.blit(pike_a,(pike_x,pike_y))
        if ray_in == True:
            if ray_get_dir==False:
                ray_x = random.randint(320, 710)
                ray_y = random.randint(175, 315)
                ray_direction_x = random.choice([-1, 1])
                ray_direction_y = random.choice([-1, 1])
                ray_touch=0
                ray_speed = random.uniform(0.4, 0.7)
                ray_get_dir=True
            else:
                pass
            ray_a,ray_x,ray_y,ray_direction_x,ray_direction_y,ray_touch,ray_speed = swim(ray,ray_x,ray_y,ray_direction_x,ray_direction_y,ray_touch,ray_speed)
            window.blit(ray_a,(ray_x,ray_y))
        if seahorse_in == True:
            if seahorse_get_dir==False:
                seahorse_x = random.randint(320, 710)
                seahorse_y = random.randint(175, 315)
                seahorse_direction_x = random.choice([-1, 1])
                seahorse_direction_y = random.choice([-1, 1])
                seahorse_touch=0
                seahorse_speed = random.uniform(0.4, 0.7)
                seahorse_get_dir=True
            else:
                pass
            seahorse_a,seahorse_x,seahorse_y,seahorse_direction_x,seahorse_direction_y,seahorse_touch,seahorse_speed = swim(seahorse1,seahorse_x,seahorse_y,seahorse_direction_x,seahorse_direction_y,seahorse_touch,seahorse_speed)
            window.blit(seahorse_a,(seahorse_x,seahorse_y))
        if tang_in == True:
            if tang_get_dir==False:
                tang_x = random.randint(320, 710)
                tang_y = random.randint(175, 315)
                tang_direction_x = random.choice([-1, 1])
                tang_direction_y = random.choice([-1, 1])
                tang_touch=0
                tang_speed = random.uniform(0.4, 0.7)
                tang_get_dir=True
            else:
                pass
            tang_a,tang_x,tang_y,tang_direction_x,tang_direction_y,tang_touch,tang_speed = swim(tang1,tang_x,tang_y,tang_direction_x,tang_direction_y,tang_touch,tang_speed)
            window.blit(tang_a,(tang_x,tang_y))
        if prawn_in == True:
            if prawn_get_dir==False:
                prawn_x = random.randint(320, 710)
                prawn_y = random.randint(175, 315)
                prawn_direction_x = random.choice([-1, 1])
                prawn_direction_y = random.choice([-1, 1])
                prawn_touch=0
                prawn_speed = random.uniform(0.4, 0.7)
                prawn_get_dir=True
            else:
                pass
            prawn_a,prawn_x,prawn_y,prawn_direction_x,prawn_direction_y,prawn_touch,prawn_speed = swim(prawn,prawn_x,prawn_y,prawn_direction_x,prawn_direction_y,prawn_touch,prawn_speed)
            window.blit(prawn_a,(prawn_x,prawn_y))
        if turtle_in == True:
            if turtle_get_dir==False:
                turtle_x = random.randint(320, 710)
                turtle_y = random.randint(175, 315)
                turtle_direction_x = random.choice([-1, 1])
                turtle_direction_y = random.choice([-1, 1])
                turtle_touch=0
                turtle_speed = random.uniform(0.4, 0.7)
                turtle_get_dir=True
            else:
                pass
            turtle_a,turtle_x,turtle_y,turtle_direction_x,turtle_direction_y,turtle_touch,turtle_speed = swim(turtle,turtle_x,turtle_y,turtle_direction_x,turtle_direction_y,turtle_touch,turtle_speed)
            window.blit(turtle_a,(turtle_x,turtle_y))
        if jelly_in == True:
            if jelly_get_dir==False:
                jelly_x = random.randint(320, 710)
                jelly_y = random.randint(175, 315)
                jelly_direction_x = random.choice([-1, 1])
                jelly_direction_y = random.choice([-1, 1])
                jelly_touch=0
                jelly_speed = random.uniform(0.4, 0.7)
                jelly_get_dir=True
            else:
                pass
            jelly_a,jelly_x,jelly_y,jelly_direction_x,jelly_direction_y,jelly_touch,jelly_speed = swim(jelly1,jelly_x,jelly_y,jelly_direction_x,jelly_direction_y,jelly_touch,jelly_speed)
            window.blit(jelly_a,(jelly_x,jelly_y))
        if tiger_in == True:
            if tiger_get_dir==False:
                tiger_x = random.randint(320, 710)
                tiger_y = random.randint(175, 315)
                tiger_direction_x = random.choice([-1, 1])
                tiger_direction_y = random.choice([-1, 1])
                tiger_touch=0
                tiger_speed = random.uniform(0.4, 0.7)
                tiger_get_dir=True
            else:
                pass
            tiger_a,tiger_x,tiger_y,tiger_direction_x,tiger_direction_y,tiger_touch,tiger_speed = swim(tiger_fish,tiger_x,tiger_y,tiger_direction_x,tiger_direction_y,tiger_touch,tiger_speed)
            window.blit(tiger_a,(tiger_x,tiger_y))
        #-----------------------------------------------------
        if grass_in == True:
            window.blit(grass, (388, 344))
        if pur_plant_in == True:
            window.blit(pur_plant, (490, 210))
        if bl_coral_in == True:
            window.blit(bl_coral, (220, 340))
        if metal_in == True:
            window.blit(metal, (290, 335))
        if pin_plant_in == True:
            window.blit(pin_plant, (740, 170))
        #-------------------------------------------------------
        window.blit(image_list[current_image_index], (x, y))
        current_time = pygame.time.get_ticks()
        if current_time - last_display_time >= display_time:
            current_image_index = (current_image_index + 1) % len(image_list)
            last_display_time = current_time
            if current_image_index==30:
                x = random.randint(200, 800) 
        #-------------------------------------------------------
        if crab_in == True:
            if crab_get_dir==False:
                crab_x = 250
                crab_y = 370
                crab_direction_x = random.choice([-1, 1])
                crab_direction_y = random.choice([-1, 1])
                crab_touch=0
                crab_get_dir=True
            else:
                pass
            crab_a,crab_x,crab_y,crab_direction_x,crab_direction_y,crab_touch = swim_crab(crab,crab_x,crab_y,crab_direction_x,crab_direction_y,crab_touch)
            window.blit(crab,(crab_x,crab_y))
        if skeleton_in == True:
            window.blit(skeleton, (708, 391))
        if snail_in == True:
            if snail_get_dir==False:
                snail_x = random.randint(320, 710)
                snail_y = random.randint(175, 315)
                snail_direction_x = random.choice([-1, 1])
                snail_direction_y = random.choice([-1, 1])
                snail_touch=0
                snail_get_dir=True
            else:
                pass
            snail_a,snail_x,snail_y,snail_direction_x,snail_direction_y,snail_touch = swim_snail(snail,snail_x,snail_y,snail_direction_x,snail_direction_y,snail_touch)
            window.blit(snail_a,(snail_x,snail_y))
        if starfish_in == True:
            if star_get_dir==False:
                star_x = random.randint(320, 710)
                star_y = random.randint(175, 315)
                star_get_dir=True
            window.blit(starfish,(star_x,star_y))
        #------------------------------------------------------
        if lizard_in == True:
            window.blit(lizard, (820, 155))
        if trophy_owned == True:
            window.blit(trophy_img,(210,384))
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if back_rect.collidepoint(mouse_pos) and back_active==False:
                    back_active = True
                if outdoor_rect.collidepoint(mouse_pos) and back_active==False:
                    village(event)
                if scenery_rect.collidepoint(mouse_pos) and back_active==False:
                   active = active_scenery(event)
                   if active is not None:
                        if active==True:
                            active=False
                if fishes_rect.collidepoint(mouse_pos) and back_active==False:
                    active1 = active_fishes(event)
                    if active1 is not None:
                        if active1==True:
                            active1=False
                if trophy_rect.collidepoint(mouse_pos) and back_active==False:
                    trophy(event)
                if achievement_rect.collidepoint(mouse_pos) and back_active==False:
                    achievement(event)
                if save_rect.collidepoint(mouse_pos) and back_active==False:
                    saved_vis = True
                    with open("zapis.pkl","wb") as f:
                        pickle.dump(money,f)
                        pickle.dump(grass_owned,f)
                        pickle.dump(bl_coral_owned,f)
                        pickle.dump(flamingo_owned,f)
                        pickle.dump(grn_plant_owned,f)
                        pickle.dump(lizard_owned,f)
                        pickle.dump(metal_owned,f)
                        pickle.dump(mini_house_owned,f)
                        pickle.dump(pin_plant_owned,f)
                        pickle.dump(pur_plant_owned,f)
                        pickle.dump(skeleton_owned,f)
                        pickle.dump(statue_owned,f)
                        pickle.dump(vulcano_owned,f)
                        pickle.dump(grass_in,f)
                        pickle.dump(pur_plant_in,f)
                        pickle.dump(bl_coral_in,f)
                        pickle.dump(metal_in,f)
                        pickle.dump(pin_plant_in,f)
                        pickle.dump(lizard_in,f)
                        pickle.dump(grn_plant_in,f)
                        pickle.dump(skeleton_in,f)
                        pickle.dump(mini_house_in,f)
                        pickle.dump(statue_in,f)
                        pickle.dump(flamingo_in,f)
                        pickle.dump(vulcano_in,f)
                        pickle.dump(fightfish_owned,f)
                        pickle.dump(clownfish_owned,f)
                        pickle.dump(starfish_owned,f)
                        pickle.dump(jelly_owned,f)
                        pickle.dump(lionfish_owned,f)
                        pickle.dump(tang_owned,f)
                        pickle.dump(ray_owned,f)
                        pickle.dump(octopus_owned,f)
                        pickle.dump(seahorse_owned,f)
                        pickle.dump(fightfish_amount,f)
                        pickle.dump(clownfish_amount,f)
                        pickle.dump(starfish_amount,f)
                        pickle.dump(jelly_amount,f)
                        pickle.dump(lionfish_amount,f)
                        pickle.dump(tang_amount,f)
                        pickle.dump(ray_amount,f)
                        pickle.dump(octopus_amount,f)
                        pickle.dump(seahorse_amount,f)
                        pickle.dump(fightfish_in,f)
                        pickle.dump(clownfish_in,f)
                        pickle.dump(starfish_in,f)
                        pickle.dump(jelly_in,f)
                        pickle.dump(lionfish_in,f)
                        pickle.dump(tang_in,f)
                        pickle.dump(ray_in,f)
                        pickle.dump(octopus_in,f)
                        pickle.dump(seahorse_in,f)
                        pickle.dump(wooden_owned,f)
                        pickle.dump(iron_owned,f)
                        pickle.dump(carbon_owned,f)
                        pickle.dump(golden_owned,f)
                        pickle.dump(boat_owned,f)
                        pickle.dump(backpack_slots,f)
                        pickle.dump(aqua_slots,f)
                        pickle.dump(blue_fish_owned,f)
                        pickle.dump(pike_owned,f)
                        pickle.dump(fat_fish_owned,f)
                        pickle.dump(snail_owned,f)
                        pickle.dump(frog_owned,f)
                        pickle.dump(koi_fish_owned,f)
                        pickle.dump(sturgeon_owned,f)
                        pickle.dump(piranha_owned,f)
                        pickle.dump(blue_fish_amount,f)
                        pickle.dump(pike_amount,f)
                        pickle.dump(fat_fish_amount,f)
                        pickle.dump(snail_amount,f)
                        pickle.dump(frog_amount,f)
                        pickle.dump(koi_fish_amount,f)
                        pickle.dump(sturgeon_amount,f)
                        pickle.dump(piranha_amount,f)
                        pickle.dump(prawn_owned,f)
                        pickle.dump(tiger_fish_owned,f)
                        pickle.dump(crab_owned,f)
                        pickle.dump(sword_fish_owned,f)
                        pickle.dump(turtle_owned,f)
                        pickle.dump(shark_owned,f)
                        pickle.dump(light_fish_owned,f)
                        pickle.dump(nautilus_owned,f)
                        pickle.dump(zombie_fish_owned,f)
                        pickle.dump(prawn_amount,f)
                        pickle.dump(tiger_fish_amount,f)
                        pickle.dump(crab_amount,f)
                        pickle.dump(sword_fish_amount,f)
                        pickle.dump(turtle_amount,f)
                        pickle.dump(shark_amount,f)
                        pickle.dump(light_fish_amount,f)
                        pickle.dump(zombie_fish_amount,f)
                        pickle.dump(nautilus_amount,f)
                        pickle.dump(in_sum,f)
                        pickle.dump(catched,f)
                        pickle.dump(decorations,f)
                        pickle.dump(fish_bought,f)
                        pickle.dump(total_money,f)
                        pickle.dump(blue_fish_in,f)
                        pickle.dump(pike_in,f)
                        pickle.dump(fat_fish_in,f)
                        pickle.dump(snail_in,f)
                        pickle.dump(frog_in,f)
                        pickle.dump(koi_in,f)
                        pickle.dump(sturgeon_in,f)
                        pickle.dump(piranha_in,f)
                        pickle.dump(prawn_in,f)
                        pickle.dump(tiger_in,f)
                        pickle.dump(crab_in,f)
                        pickle.dump(sword_in,f)
                        pickle.dump(turtle_in,f)
                        pickle.dump(shark_in,f)
                        pickle.dump(light_in,f)
                        pickle.dump(nautilus_in,f)
                        pickle.dump(zombie_in,f)
                        pickle.dump(gift_1_received,f)
                        pickle.dump(gift_2_received,f)
                        pickle.dump(gift_3_received,f)
                        pickle.dump(gift_4_received,f)
                        pickle.dump(gift_5_received,f)
                        pickle.dump(trophy_owned,f)
        if outdoor_rect.collidepoint(pygame.mouse.get_pos()) and back_active==False:
                window.blit(door_coll,(960,480))
        else:
                window.blit(door,(960,480))
        if achievement_rect.collidepoint(pygame.mouse.get_pos()) and back_active==False:
                window.blit(achievement_button_coll,(810,520))
        else:
                window.blit(achievement_button,(810,520))
        if trophy_rect.collidepoint(pygame.mouse.get_pos()) and back_active==False:
                window.blit(trophy_button_coll,(720,520))
        else:
                window.blit(trophy_button,(720,520))
        money_amount = font.render(str(money),True,(0,0,0))
        mouse_pos = pygame.mouse.get_pos()
        save_rect = save_button.get_rect()
        save_rect.topleft = (10,435)
        if save_rect.collidepoint(pygame.mouse.get_pos()) and back_active==False:
                window.blit(save_button_coll,(10,435))
        else:
                window.blit(save_button,(10,435))
        if saved_vis == True:
            window.blit(saved_game,(164,250))
            start_time = pygame.time.get_ticks()
            if loop == False:
                vis_time = start_time
                loop = True
            if start_time > vis_time+1900:
                saved_vis = False
                loop = False
        else:
            start_time = 0
        if back_active==True:
            yes = pygame.Rect(314, 350, 60, 60)
            no = pygame.Rect(706, 350, 60, 60)
            window.blit(to_menu,(300,120))
            if yes.collidepoint(mouse_pos)and event.type == pygame.MOUSEBUTTONUP:
                back_active=True
                main()
            elif no.collidepoint(mouse_pos)and event.type == pygame.MOUSEBUTTONUP:
                back_active=False
        pygame.display.update()
        clock.tick(60)
def active_scenery(event):
    global grass_in,pur_plant_in,bl_coral_in,metal_in,pin_plant_in,lizard_in,grn_plant_in,skeleton_in,mini_house_in,statue_in,flamingo_in,vulcano_in
    cancel_rect = cancel.get_rect()
    cancel_rect.topleft = (504, 515)
    run = True
    window.blit(con_background, (0, 0))
    window.blit(grass_button, (40, 130))
    if grass_owned == True:
        pass
    else:
        window.blit(locked, (40,130))
    if grass_in == True:
        window.blit(in_item,(40,130))
    window.blit(pur_plant_button, (90, 130))
    if pur_plant_owned == True:
        pass
    else:
        window.blit(locked, (90,130))
    if pur_plant_in == True:
        window.blit(in_item,(90,130))
    window.blit(coral_button, (40, 180))
    if bl_coral_owned == True:
        pass
    else:
        window.blit(locked, (40,180))
    if bl_coral_in == True:
        window.blit(in_item,(40,180))
    window.blit(metal_button, (90, 180))
    if metal_owned == True:
        pass
    else:
        window.blit(locked, (90,180))
    if metal_in == True:
        window.blit(in_item,(90,180))
    window.blit(pin_plant_button, (40, 230))
    if pin_plant_owned == True:
        pass
    else:
        window.blit(locked, (40,230))
    if pin_plant_in == True:
        window.blit(in_item,(40,230))
    window.blit(lizard_button, (90, 230))
    if lizard_owned == True:
        pass
    else:
        window.blit(locked, (90,230))
    if lizard_in == True:
        window.blit(in_item,(90,230))
    window.blit(grn_plant_button, (40, 280))
    if grn_plant_owned == True:
        pass
    else:
        window.blit(locked, (40,280))
    if grn_plant_in == True:
        window.blit(in_item,(40,280))
    window.blit(skeleton_button, (90, 280))
    if skeleton_owned == True:
        pass
    else:
        window.blit(locked, (90,280))
    if skeleton_in == True:
        window.blit(in_item,(90,280))
    window.blit(house_button, (40, 330))
    if mini_house_owned == True:
        pass
    else:
        window.blit(locked, (40,330))
    if mini_house_in == True:
        window.blit(in_item,(40,330))
    window.blit(statue_button, (90, 330))
    if statue_owned == True:
        pass
    else:
        window.blit(locked, (90,330))
    if statue_in == True:
        window.blit(in_item,(90,330))
    window.blit(flamingo_button, (40, 380))
    if flamingo_owned == True:
        pass
    else:
        window.blit(locked, (40,380))
    if flamingo_in == True:
        window.blit(in_item,(40,380))
    window.blit(vulcano_button, (90, 380))
    if vulcano_owned == True:
        pass
    else:
        window.blit(locked, (90,380))
    if vulcano_in == True:
        window.blit(in_item,(90,380))
    grass_button_rect = grass_button.get_rect()
    grass_button_rect.topleft = (40, 130)
    pur_plant_button_rect = pur_plant_button.get_rect()
    pur_plant_button_rect.topleft = (90, 130)
    coral_button_rect = coral_button.get_rect()
    coral_button_rect.topleft = (40, 180)
    metal_button_rect = metal_button.get_rect()
    metal_button_rect.topleft = (90, 180)
    pin_plant_button_rect = pin_plant_button.get_rect()
    pin_plant_button_rect.topleft = (40, 230)
    lizard_button_rect = lizard_button.get_rect()
    lizard_button_rect.topleft = (90, 230)
    grn_plant_button_rect = grn_plant_button.get_rect()
    grn_plant_button_rect.topleft = (40, 280)
    skeleton_button_rect = skeleton_button.get_rect()
    skeleton_button_rect.topleft = (90, 280)
    mini_button_rect = mini_button.get_rect()
    mini_button_rect.topleft = (40, 330)
    statue_button_rect = statue_button.get_rect()
    statue_button_rect.topleft = (90, 330)
    flamingo_button_rect = flamingo_button.get_rect()
    flamingo_button_rect.topleft = (40, 380)
    vulcano_button_rect = vulcano_button.get_rect()
    vulcano_button_rect.topleft = (90, 380)
    while run:
        if cancel_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(cancel_coll,(504, 515))
        else:
                window.blit(cancel,(504, 515))
        for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if cancel_rect.collidepoint(mouse_pos):
                        return False
                    elif grass_button_rect.collidepoint(mouse_pos) and grass_owned==True:
                        if grass_in == False:
                            window.blit(in_item,(40,130))
                            grass_in = True
                        else:
                            grass_in = False
                            window.blit(grass_button, (40, 130))
                    elif pur_plant_button_rect.collidepoint(mouse_pos) and pur_plant_owned==True:
                        if pur_plant_in == False:
                            window.blit(in_item,(90,130))
                            pur_plant_in = True
                        else:
                            pur_plant_in = False
                            window.blit(pur_plant_button, (90, 130))
                    elif coral_button_rect.collidepoint(mouse_pos) and bl_coral_owned==True:
                        if bl_coral_in == False:
                            window.blit(in_item,(40,180))
                            bl_coral_in = True
                        else:
                            bl_coral_in = False
                            window.blit(coral_button, (40, 180))
                    elif metal_button_rect.collidepoint(mouse_pos) and metal_owned==True:
                        if metal_in == False:
                            window.blit(in_item,(90,180))
                            metal_in = True
                        else:
                            metal_in = False
                            window.blit(metal_button, (90, 180))
                    elif pin_plant_button_rect.collidepoint(mouse_pos) and pin_plant_owned==True:
                        if pin_plant_in == False:
                            window.blit(in_item,(40,230))
                            pin_plant_in = True
                        else:
                            pin_plant_in = False
                            window.blit(pin_plant_button, (40, 230))
                    elif lizard_button_rect.collidepoint(mouse_pos) and lizard_owned==True:
                        if lizard_in == False:
                            window.blit(in_item,(90,230))
                            lizard_in = True
                        else:
                            lizard_in = False
                            window.blit(lizard_button, (90, 230))
                    elif grn_plant_button_rect.collidepoint(mouse_pos) and grn_plant_owned==True:
                        if grn_plant_in == False:
                            window.blit(in_item,(40,280))
                            grn_plant_in = True
                        else:
                            grn_plant_in = False
                            window.blit(grn_plant_button, (40, 280))
                    elif skeleton_button_rect.collidepoint(mouse_pos) and skeleton_owned==True:
                        if skeleton_in == False:
                            window.blit(in_item,(90,280))
                            skeleton_in = True
                        else:
                            skeleton_in = False
                            window.blit(skeleton_button, (90, 280))
                    elif mini_button_rect.collidepoint(mouse_pos) and mini_house_owned==True:
                        if mini_house_in == False:
                            window.blit(in_item,(40,330))
                            mini_house_in = True
                        else:
                            mini_house_in = False
                            window.blit(house_button, (40, 330))
                    elif statue_button_rect.collidepoint(mouse_pos) and statue_owned==True:
                        if statue_in == False:
                            window.blit(in_item,(90,330))
                            statue_in = True
                        else:
                            statue_in = False
                            window.blit(statue_button, (90, 330))
                    elif flamingo_button_rect.collidepoint(mouse_pos) and flamingo_owned==True:
                        if flamingo_in == False:
                            window.blit(in_item,(40,380))
                            flamingo_in = True
                        else:
                            flamingo_in = False
                            window.blit(flamingo_button, (40, 380))
                    elif vulcano_button_rect.collidepoint(mouse_pos) and vulcano_owned==True:
                        if vulcano_in == False:
                            window.blit(in_item,(90,380))
                            vulcano_in = True
                        else:
                            vulcano_in = False
                            window.blit(vulcano_button, (90, 380))                 
        pygame.display.update()
def active_fishes(event):
    global blue_fish_in,pike_in,fat_fish_in,snail_in,frog_in,koi_in,sturgeon_in,piranha_in,prawn_in,tiger_in,crab_in,sword_in,turtle_in,shark_in,light_in,nautilus_in,zombie_in
    global fightfish_in,clownfish_in,starfish_in,jelly_in,lionfish_in,tang_in,ray_in,octopus_in,seahorse_in,in_sum,backpack_slots,aqua_slots
    global blue_fish_in,pike_in,fat_fish_in,snail_in,frog_in,koi_in,sturgeon_in,piranha_in,prawn_in,tiger_in,crab_in,sword_in,turtle_in,shark_in,light_in,nautilus_in,zombie_in
    global blue_fish_amount,pike_amount,fat_fish_amount,snail_amount,frog_amount,koi_fish_amount,sturgeon_amount,piranha_amount
    global prawn_amount,tiger_fish_amount,crab_amount,sword_fish_amount,turtle_amount,shark_amount,light_fish_amount,zombie_fish_amount,nautilus_amount
    global fightfish_amount,clownfish_amount,starfish_amount,jelly_amount,lionfish_amount,tang_amount,ray_amount,octopus_amount,seahorse_amount
    cancel_rect = cancel.get_rect()
    cancel_rect.topleft = (504, 515)
    a_point = 0
    run = True
    points = [(40,55),(90,55),(40,105),(90,105),(40,155),(90,155),(40,205),(90,205),(40,255),(90,255),(40,305),(90,305),(40,355),(90,355),(40,405),(90,405),(40,455),(90,455),(40,505),(90,505),(40,555),(90,555),(40,605),(90,605),(40,655),(90,655)]
    window.blit(con_background, (0, 0))
    if blue_fish_amount>= 1 or (blue_fish_amount==0 and blue_fish_in==True):
        blue_x = points[a_point][0]
        blue_y = points[a_point][1]
        a_point+=1
        window.blit(blue_button,(blue_x,blue_y))
        blue_rect = blue_button.get_rect()
        blue_rect.topleft = (blue_x,blue_y)
        if blue_fish_in == True:
            window.blit(in_item,(blue_x,blue_y))
    if pike_amount>= 1 or (pike_amount==0 and pike_in==True):
        pike_x = points[a_point][0]
        pike_y = points[a_point][1]
        a_point+=1
        window.blit(pike_button,(pike_x,pike_y))
        pike_rect = pike_button.get_rect()
        pike_rect.topleft = (pike_x,pike_y)
        if pike_in == True:
            window.blit(in_item,(pike_x,pike_y))
    if fat_fish_amount>= 1 or (fat_fish_amount==0 and fat_fish_in==True):
        fat_x = points[a_point][0]
        fat_y = points[a_point][1]
        a_point+=1
        window.blit(fat_button,(fat_x,fat_y))
        fat_rect = fat_button.get_rect()
        fat_rect.topleft = (fat_x,fat_y)
        if fat_fish_in == True:
            window.blit(in_item,(fat_x,fat_y))
    if snail_amount>= 1 or (snail_amount==0 and snail_in==True):
        snail_x = points[a_point][0]
        snail_y = points[a_point][1]
        a_point+=1
        window.blit(snail_button,(snail_x,snail_y))
        snail_rect = snail_button.get_rect()
        snail_rect.topleft = (snail_x,snail_y)
        if snail_in == True:
            window.blit(in_item,(snail_x,snail_y))
    if frog_amount>= 1 or (frog_amount==0 and frog_in==True):
        frog_x = points[a_point][0]
        frog_y = points[a_point][1]
        a_point+=1
        window.blit(frog_button,(frog_x,frog_y))
        frog_rect = frog_button.get_rect()
        frog_rect.topleft = (frog_x,frog_y)
        if frog_in == True:
            window.blit(in_item,(frog_x,frog_y))
    if koi_fish_amount>= 1 or (koi_fish_amount==0 and koi_in==True):
        koi_x = points[a_point][0]
        koi_y = points[a_point][1]
        a_point+=1
        window.blit(koi_button,(koi_x,koi_y))
        koi_rect = koi_button.get_rect()
        koi_rect.topleft = (koi_x,koi_y)
        if koi_in == True:
            window.blit(in_item,(koi_x,koi_y))
    if sturgeon_amount>= 1 or (sturgeon_amount==0 and sturgeon_in==True):
        sturgeon_x = points[a_point][0]
        sturgeon_y = points[a_point][1]
        a_point+=1
        window.blit(sturgeon_button,(sturgeon_x,sturgeon_y))
        sturgeon_rect = sturgeon_button.get_rect()
        sturgeon_rect.topleft = (sturgeon_x,sturgeon_y)
        if sturgeon_in == True:
            window.blit(in_item,(sturgeon_x,sturgeon_y))
    if piranha_amount>= 1 or (piranha_amount==0 and piranha_in==True):
        piranha_x = points[a_point][0]
        piranha_y = points[a_point][1]
        a_point+=1
        window.blit(piranha_button,(piranha_x,piranha_y))
        piranha_rect = piranha_button.get_rect()
        piranha_rect.topleft = (piranha_x,piranha_y)
        if piranha_in == True:
            window.blit(in_item,(piranha_x,piranha_y))
    if prawn_amount>= 1 or (prawn_amount==0 and prawn_in==True):
        prawn_x = points[a_point][0]
        prawn_y = points[a_point][1]
        a_point+=1
        window.blit(prawn_button,(prawn_x,prawn_y))
        prawn_rect = prawn_button.get_rect()
        prawn_rect.topleft = (prawn_x,prawn_y)
        if prawn_in == True:
            window.blit(in_item,(prawn_x,prawn_y))
    if tiger_fish_amount>= 1 or (tiger_fish_amount==0 and tiger_in==True):
        tiger_x = points[a_point][0]
        tiger_y = points[a_point][1]
        a_point+=1
        window.blit(tiger_button,(tiger_x,tiger_y))
        tiger_rect = tiger_button.get_rect()
        tiger_rect.topleft = (tiger_x,tiger_y)
        if tiger_in == True:
            window.blit(in_item,(tiger_x,tiger_y))
    if crab_amount>= 1 or (crab_amount==0 and crab_in==True):
        crab_x = points[a_point][0]
        crab_y = points[a_point][1]
        a_point+=1
        window.blit(crab_button,(crab_x,crab_y))
        crab_rect = crab_button.get_rect()
        crab_rect.topleft = (crab_x,crab_y)
        if crab_in == True:
            window.blit(in_item,(crab_x,crab_y))
    if sword_fish_amount>= 1 or (sword_fish_amount==0 and sword_in==True):
        sword_x = points[a_point][0]
        sword_y = points[a_point][1]
        a_point+=1
        window.blit(sword_button,(sword_x,sword_y))
        sword_rect = sword_button.get_rect()
        sword_rect.topleft = (sword_x,sword_y)
        if sword_in == True:
            window.blit(in_item,(sword_x,sword_y))
    if turtle_amount>= 1 or (turtle_amount==0 and turtle_in==True):
        turtle_x = points[a_point][0]
        turtle_y = points[a_point][1]
        a_point+=1
        window.blit(turtle_button,(turtle_x,turtle_y))
        turtle_rect = turtle_button.get_rect()
        turtle_rect.topleft = (turtle_x,turtle_y)
        if turtle_in == True:
            window.blit(in_item,(turtle_x,turtle_y))
    if shark_amount>= 1 or (shark_amount==0 and shark_in==True):
        shark_x = points[a_point][0]
        shark_y = points[a_point][1]
        a_point+=1
        window.blit(shark_button,(shark_x,shark_y))
        shark_rect = shark_button.get_rect()
        shark_rect.topleft = (shark_x,shark_y)
        if shark_in == True:
            window.blit(in_item,(shark_x,shark_y))
    if light_fish_amount>= 1 or (light_fish_amount==0 and light_in==True):
        light_x = points[a_point][0]
        light_y = points[a_point][1]
        a_point+=1
        window.blit(light_button,(light_x,light_y))
        light_rect = light_button.get_rect()
        light_rect.topleft = (light_x,light_y)
        if light_in == True:
            window.blit(in_item,(light_x,light_y))
    if nautilus_amount>= 1 or (nautilus_amount==0 and nautilus_in==True):
        nautilus_x = points[a_point][0]
        nautilus_y = points[a_point][1]
        a_point+=1
        window.blit(nautilus_button,(nautilus_x,nautilus_y))
        nautilus_rect = nautilus_button.get_rect()
        nautilus_rect.topleft = (nautilus_x,nautilus_y)
        if nautilus_in == True:
            window.blit(in_item,(nautilus_x,nautilus_y))
    if zombie_fish_amount>= 1 or (zombie_fish_amount==0 and zombie_in==True):
        zombie_x = points[a_point][0]
        zombie_y = points[a_point][1]
        a_point+=1
        window.blit(zombie_button,(zombie_x,zombie_y))
        zombie_rect = zombie_button.get_rect()
        zombie_rect.topleft = (zombie_x,zombie_y)
        if zombie_in == True:
            window.blit(in_item,(zombie_x,zombie_y))
    if fightfish_amount>= 1 or (fightfish_amount==0 and fightfish_in==True):
        fight_x = points[a_point][0]
        fight_y = points[a_point][1]
        a_point+=1
        window.blit(fight_button,(fight_x,fight_y))
        fight_rect = fight_button.get_rect()
        fight_rect.topleft = (fight_x,fight_y)
        if fightfish_in == True:
            window.blit(in_item,(fight_x,fight_y))
    if clownfish_amount>= 1 or (clownfish_amount==0 and clownfish_in==True):
        clown_x = points[a_point][0]
        clown_y = points[a_point][1]
        a_point+=1
        window.blit(clown_button,(clown_x,clown_y))
        clown_rect = clown_button.get_rect()
        clown_rect.topleft = (clown_x,clown_y)
        if clownfish_in == True:
            window.blit(in_item,(clown_x,clown_y))
    if starfish_amount>= 1 or (starfish_amount==0 and starfish_in==True):
        star_x = points[a_point][0]
        star_y = points[a_point][1]
        a_point+=1
        window.blit(star_button,(star_x,star_y))
        star_rect = star_button.get_rect()
        star_rect.topleft = (star_x,star_y)
        if starfish_in == True:
            window.blit(in_item,(star_x,star_y))
    if jelly_amount>= 1 or (jelly_amount==0 and jelly_in==True):
        jelly_x = points[a_point][0]
        jelly_y = points[a_point][1]
        a_point+=1
        window.blit(jelly_button,(jelly_x,jelly_y))
        jelly_rect = jelly_button.get_rect()
        jelly_rect.topleft = (jelly_x,jelly_y)
        if jelly_in == True:
            window.blit(in_item,(jelly_x,jelly_y))
    if lionfish_amount>= 1 or (lionfish_amount==0 and lionfish_in==True):
        lion_x = points[a_point][0]
        lion_y = points[a_point][1]
        a_point+=1
        window.blit(lion_button,(lion_x,lion_y))
        lion_rect = lion_button.get_rect()
        lion_rect.topleft = (lion_x,lion_y)
        if lionfish_in == True:
            window.blit(in_item,(lion_x,lion_y))
    if tang_amount>= 1 or (tang_amount==0 and tang_in==True):
        tang_x = points[a_point][0]
        tang_y = points[a_point][1]
        a_point+=1
        window.blit(tang_button,(tang_x,tang_y))
        tang_rect = tang_button.get_rect()
        tang_rect.topleft = (tang_x,tang_y)
        if tang_in == True:
            window.blit(in_item,(tang_x,tang_y))
    if ray_amount>= 1 or (ray_amount==0 and ray_in==True):
        ray_x = points[a_point][0]
        ray_y = points[a_point][1]
        a_point+=1
        window.blit(ray_button,(ray_x,ray_y))
        ray_rect = ray_button.get_rect()
        ray_rect.topleft = (ray_x,ray_y)
        if ray_in == True:
            window.blit(in_item,(ray_x,ray_y))
    if octopus_amount>= 1 or (octopus_amount==0 and octopus_in==True):
        octopus_x = points[a_point][0]
        octopus_y = points[a_point][1]
        a_point+=1
        window.blit(octopus_button,(octopus_x,octopus_y))
        octopus_rect = octopus_button.get_rect()
        octopus_rect.topleft = (octopus_x,octopus_y)
        if octopus_in == True:
            window.blit(in_item,(octopus_x,octopus_y))
    if seahorse_amount>= 1 or (seahorse_amount==0 and seahorse_in==True):
        seahorse_x = points[a_point][0]
        seahorse_y = points[a_point][1]
        a_point+=1
        window.blit(seahorse_button,(seahorse_x,seahorse_y))
        seahorse_rect = seahorse_button.get_rect()
        seahorse_rect.topleft = (seahorse_x,seahorse_y)
        if seahorse_in == True:
            window.blit(in_item,(seahorse_x,seahorse_y))
    if backpack_slots ==0 and blue_fish_in == False and pike_in== False and fat_fish_in== False and snail_in== False and frog_in== False and koi_in== False and sturgeon_in== False and piranha_in== False and prawn_in== False and tiger_in== False and crab_in== False and sword_in== False and turtle_in== False and shark_in== False and light_in== False and nautilus_in== False and zombie_in== False and fightfish_in== False and clownfish_in== False and starfish_in== False and jelly_in== False and lionfish_in== False and tang_in== False and ray_in== False and octopus_in== False and seahorse_in== False:
        window.blit(zero_fishes,(20,140))
    while run:
        if cancel_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(cancel_coll,(504, 515))
        else:
                window.blit(cancel,(504, 515))
        for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if cancel_rect.collidepoint(mouse_pos):
                        return False
                    if blue_fish_amount>0 or blue_fish_in==True:
                        if blue_rect.collidepoint(mouse_pos) and blue_fish_in==False and blue_fish_amount>0 and aqua_slots<10:
                            blue_fish_in=True
                            in_sum+=1
                            window.blit(in_item,(blue_x,blue_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            blue_fish_amount-=1
                        elif blue_rect.collidepoint(mouse_pos) and blue_fish_in==True and backpack_slots <20:
                            blue_fish_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(blue_button,(blue_x,blue_y))
                            backpack_slots+=1
                            blue_fish_amount+=1
                    if pike_amount>0 or pike_in==True:
                        if pike_rect.collidepoint(mouse_pos) and pike_in==False and pike_amount>0 and aqua_slots<10:
                            pike_in=True
                            in_sum+=1
                            window.blit(in_item,(pike_x,pike_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            pike_amount-=1
                        elif pike_rect.collidepoint(mouse_pos) and pike_in==True and backpack_slots <20:
                            pike_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(pike_button,(pike_x,pike_y))
                            backpack_slots+=1
                            pike_amount+=1
                    if fat_fish_amount>0 or fat_fish_in==True:
                        if fat_rect.collidepoint(mouse_pos) and fat_fish_in==False and fat_fish_amount>0 and aqua_slots<10:
                            fat_fish_in=True
                            in_sum+=1
                            window.blit(in_item,(fat_x,fat_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            fat_fish_amount-=1
                        elif fat_rect.collidepoint(mouse_pos) and fat_fish_in==True and backpack_slots <20:
                            fat_fish_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(fat_button,(fat_x,fat_y))
                            backpack_slots+=1
                            fat_fish_amount+=1
                    if snail_amount>0 or snail_in==True:
                        if snail_rect.collidepoint(mouse_pos) and snail_in==False and snail_amount>0 and aqua_slots<10:
                            snail_in=True
                            in_sum+=1
                            window.blit(in_item,(snail_x,snail_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            snail_amount-=1
                        elif snail_rect.collidepoint(mouse_pos) and snail_in==True and backpack_slots <20:
                            snail_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(snail_button,(snail_x,snail_y))
                            backpack_slots+=1
                            snail_amount+=1
                    if frog_amount>0 or frog_in==True:
                        if frog_rect.collidepoint(mouse_pos) and frog_in==False and frog_amount>0 and aqua_slots<10:
                            frog_in=True
                            in_sum+=1
                            window.blit(in_item,(frog_x,frog_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            frog_amount-=1
                        elif frog_rect.collidepoint(mouse_pos) and frog_in==True:
                            frog_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(frog_button,(frog_x,frog_y))
                            backpack_slots+=1
                            frog_amount+=1
                    if koi_fish_amount>0 or koi_in==True:
                        if koi_rect.collidepoint(mouse_pos) and koi_in==False and koi_fish_amount>0 and aqua_slots<10:
                            koi_in=True
                            in_sum+=1
                            window.blit(in_item,(koi_x,koi_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            koi_fish_amount-=1
                        elif koi_rect.collidepoint(mouse_pos) and koi_in==True:
                            koi_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(koi_button,(koi_x,koi_y))
                            backpack_slots+=1
                            koi_fish_amount+=1
                    if sturgeon_amount>0 or sturgeon_in==True:
                        if sturgeon_rect.collidepoint(mouse_pos) and sturgeon_in==False and sturgeon_amount>0 and aqua_slots<10:
                            sturgeon_in=True
                            in_sum+=1
                            window.blit(in_item,(sturgeon_x,sturgeon_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            sturgeon_amount-=1
                        elif sturgeon_rect.collidepoint(mouse_pos) and sturgeon_in==True:
                            sturgeon_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(sturgeon_button,(sturgeon_x,sturgeon_y))
                            backpack_slots+=1
                            sturgeon_amount+=1
                    if piranha_amount>0 or piranha_in==True:
                        if piranha_rect.collidepoint(mouse_pos) and piranha_in==False and piranha_amount>0 and aqua_slots<10:
                            piranha_in=True
                            in_sum+=1
                            window.blit(in_item,(piranha_x,piranha_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            piranha_amount-=1
                        elif piranha_rect.collidepoint(mouse_pos) and piranha_in==True:
                            piranha_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(piranha_button,(piranha_x,piranha_y))
                            backpack_slots+=1
                            piranha_amount+=1
                    if prawn_amount>0 or prawn_in==True:
                        if prawn_rect.collidepoint(mouse_pos) and prawn_in==False and prawn_amount>0 and aqua_slots<10:
                            prawn_in=True
                            in_sum+=1
                            window.blit(in_item,(prawn_x,prawn_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            prawn_amount-=1
                        elif prawn_rect.collidepoint(mouse_pos) and prawn_in==True:
                            prawn_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(prawn_button,(prawn_x,prawn_y))
                            backpack_slots+=1
                            prawn_amount+=1
                    if tiger_fish_amount>0 or tiger_in==True:
                        if tiger_rect.collidepoint(mouse_pos) and tiger_in==False and tiger_fish_amount>0 and aqua_slots<10:
                            tiger_in=True
                            in_sum+=1
                            window.blit(in_item,(tiger_x,tiger_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            tiger_fish_amount-=1
                        elif tiger_rect.collidepoint(mouse_pos) and tiger_in==True:
                            tiger_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(tiger_button,(tiger_x,tiger_y))
                            backpack_slots+=1
                            tiger_fish_amount+=1
                    if crab_amount>0 or crab_in==True:
                        if crab_rect.collidepoint(mouse_pos) and crab_in==False and crab_amount>0 and aqua_slots<10:
                            crab_in=True
                            in_sum+=1
                            window.blit(in_item,(crab_x,crab_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            crab_amount-=1
                        elif crab_rect.collidepoint(mouse_pos) and crab_in==True:
                            crab_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(crab_button,(crab_x,crab_y))
                            backpack_slots+=1
                            crab_amount+=1
                    if sword_fish_amount>0 or sword_in==True:
                        if sword_rect.collidepoint(mouse_pos) and sword_in==False and sword_fish_amount>0 and aqua_slots<10:
                            sword_in=True
                            in_sum+=1
                            window.blit(in_item,(sword_x,sword_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            sword_fish_amount-=1
                        elif sword_rect.collidepoint(mouse_pos) and sword_in==True:
                            sword_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(sword_button,(sword_x,sword_y))
                            backpack_slots+=1
                            sword_fish_amount+=1
                    if turtle_amount>0 or turtle_in==True:
                        if turtle_rect.collidepoint(mouse_pos) and turtle_in==False and turtle_amount>0 and aqua_slots<10:
                            turtle_in=True
                            in_sum+=1
                            window.blit(in_item,(turtle_x,turtle_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            turtle_amount-=1
                        elif turtle_rect.collidepoint(mouse_pos) and turtle_in==True:
                            turtle_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(turtle_button,(turtle_x,turtle_y))
                            backpack_slots+=1
                            turtle_amount+=1
                    if shark_amount>0 or shark_in==True:
                        if shark_rect.collidepoint(mouse_pos) and shark_in==False and shark_amount>0 and aqua_slots<10:
                            shark_in=True
                            in_sum+=1
                            window.blit(in_item,(shark_x,shark_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            shark_amount-=1
                        elif shark_rect.collidepoint(mouse_pos) and shark_in==True:
                            shark_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(shark_button,(shark_x,shark_y))
                            backpack_slots+=1
                            shark_amount+=1
                    if light_fish_amount>0 or light_in==True:
                        if light_rect.collidepoint(mouse_pos) and light_in==False and light_fish_amount>0 and aqua_slots<10:
                            light_in=True
                            in_sum+=1
                            window.blit(in_item,(light_x,light_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            light_fish_amount-=1
                        elif light_rect.collidepoint(mouse_pos) and light_in==True:
                            light_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(light_button,(light_x,light_y))
                            backpack_slots+=1
                            light_fish_amount+=1
                    if nautilus_amount>0 or nautilus_in==True:
                        if nautilus_rect.collidepoint(mouse_pos) and nautilus_in==False and nautilus_amount>0 and aqua_slots<10:
                            nautilus_in=True
                            in_sum+=1
                            window.blit(in_item,(nautilus_x,nautilus_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            nautilus_amount-=1
                        elif nautilus_rect.collidepoint(mouse_pos) and nautilus_in==True:
                            nautilus_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(nautilus_button,(nautilus_x,nautilus_y))
                            backpack_slots+=1
                            nautilus_amount+=1
                    if zombie_fish_amount>0 or zombie_in==True:
                        if zombie_rect.collidepoint(mouse_pos) and zombie_in==False and zombie_fish_amount>0 and aqua_slots<10:
                            zombie_in=True
                            in_sum+=1
                            window.blit(in_item,(zombie_x,zombie_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            zombie_fish_amount-=1
                        elif zombie_rect.collidepoint(mouse_pos) and zombie_in==True:
                            zombie_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(zombie_button,(zombie_x,zombie_y))
                            backpack_slots+=1
                            zombie_fish_amount+=1
                    if fightfish_amount>0 or fightfish_in==True:
                        if fight_rect.collidepoint(mouse_pos) and fightfish_in==False and fightfish_amount>0 and aqua_slots<10:
                            fightfish_in=True
                            in_sum+=1
                            window.blit(in_item,(fight_x,fight_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            fightfish_amount-=1
                        elif fight_rect.collidepoint(mouse_pos) and fightfish_in==True:
                            fightfish_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(fight_button,(fight_x,fight_y))
                            backpack_slots+=1
                            fightfish_amount+=1
                    if clownfish_amount>0 or clownfish_in==True:
                        if clown_rect.collidepoint(mouse_pos) and clownfish_in==False and clownfish_amount>0 and aqua_slots<10:
                            clownfish_in=True
                            in_sum+=1
                            window.blit(in_item,(clown_x,clown_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            clownfish_amount-=1
                        elif clown_rect.collidepoint(mouse_pos) and clownfish_in==True:
                            clownfish_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(clown_button,(clown_x,clown_y))
                            backpack_slots+=1
                            clownfish_amount+=1
                    if starfish_amount>0 or starfish_in==True:
                        if star_rect.collidepoint(mouse_pos) and starfish_in==False and starfish_amount>0 and aqua_slots<10:
                            starfish_in=True
                            in_sum+=1
                            window.blit(in_item,(star_x,star_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            starfish_amount-=1
                        elif star_rect.collidepoint(mouse_pos) and starfish_in==True:
                            starfish_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(star_button,(star_x,star_y))
                            backpack_slots+=1
                            starfish_amount+=1
                    if jelly_amount>0 or jelly_in==True:
                        if jelly_rect.collidepoint(mouse_pos) and jelly_in==False and jelly_amount>0 and aqua_slots<10:
                            jelly_in=True
                            in_sum+=1
                            window.blit(in_item,(jelly_x,jelly_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            jelly_amount-=1
                        elif jelly_rect.collidepoint(mouse_pos) and jelly_in==True:
                            jelly_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(jelly_button,(jelly_x,jelly_y))
                            backpack_slots+=1
                            jelly_amount+=1
                    if lionfish_amount>0 or lionfish_in==True:
                        if lion_rect.collidepoint(mouse_pos) and lionfish_in==False and lionfish_amount>0 and aqua_slots<10:
                            lionfish_in=True
                            in_sum+=1
                            window.blit(in_item,(lion_x,lion_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            lionfish_amount-=1
                        elif lion_rect.collidepoint(mouse_pos) and lionfish_in==True:
                            lionfish_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(lion_button,(lion_x,lion_y))
                            backpack_slots+=1
                            lionfish_amount+=1
                    if tang_amount>0 or tang_in==True:
                        if tang_rect.collidepoint(mouse_pos) and tang_in==False and tang_amount>0 and aqua_slots<10:
                            tang_in=True
                            in_sum+=1
                            window.blit(in_item,(tang_x,tang_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            tang_amount-=1
                        elif tang_rect.collidepoint(mouse_pos) and tang_in==True:
                            tang_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(tang_button,(tang_x,tang_y))
                            backpack_slots+=1
                            tang_amount+=1
                    if ray_amount>0 or ray_in==True:
                        if ray_rect.collidepoint(mouse_pos) and ray_in==False and ray_amount>0 and aqua_slots<10:
                            ray_in=True
                            in_sum+=1
                            window.blit(in_item,(ray_x,ray_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            ray_amount-=1
                        elif ray_rect.collidepoint(mouse_pos) and ray_in==True:
                            ray_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(ray_button,(ray_x,ray_y))
                            backpack_slots+=1
                            ray_amount+=1
                    if octopus_amount>0 or octopus_in==True:
                        if octopus_rect.collidepoint(mouse_pos) and octopus_in==False and octopus_amount>0 and aqua_slots<10:
                            octopus_in=True
                            in_sum+=1
                            window.blit(in_item,(octopus_x,octopus_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            octopus_amount-=1
                        elif octopus_rect.collidepoint(mouse_pos) and octopus_in==True:
                            octopus_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(octopus_button,(octopus_x,octopus_y))
                            backpack_slots+=1
                            octopus_amount+=1
                    if seahorse_amount>0 or seahorse_in==True:
                        if seahorse_rect.collidepoint(mouse_pos) and seahorse_in==False and seahorse_amount>0 and aqua_slots<10:
                            seahorse_in=True
                            in_sum+=1
                            window.blit(in_item,(seahorse_x,seahorse_y))
                            backpack_slots-=1
                            aqua_slots+=1
                            seahorse_amount-=1
                        elif seahorse_rect.collidepoint(mouse_pos) and seahorse_in==True:
                            seahorse_in=False
                            in_sum-=1
                            aqua_slots-=1
                            window.blit(seahorse_button,(seahorse_x,seahorse_y))
                            backpack_slots+=1
                            seahorse_amount+=1
                                      
        pygame.display.update()
def trophy(event):
    global gift_1_received,gift_2_received,gift_3_received,gift_4_received,gift_5_received
    cancel_rect = cancel.get_rect()
    cancel_rect.topleft = (945, 515)
    gift1_rect = gift_button.get_rect()
    gift1_rect.topleft = (915,97)
    gift2_rect = gift_button.get_rect()
    gift2_rect.topleft = (915,194)
    gift3_rect = gift_button.get_rect()
    gift3_rect.topleft = (915,291)
    gift4_rect = gift_button.get_rect()
    gift4_rect.topleft = (915,388)
    gift5_rect = gift_button.get_rect()
    gift5_rect.topleft = (625,485)
    window.blit(trophy_back,(0,0))
    if blue_fish_owned==True:
        window.blit(trophy_cover,(97,75))
        window.blit(blue_fish,(140,80))
    if pike_owned==True:
        window.blit(trophy_cover,(287,75))
        window.blit(pike,(321,82))
    if fat_fish_owned==True:
        window.blit(trophy_cover,(477,75))
        window.blit(fat_fish,(518,79))
    if snail_owned==True:
        window.blit(trophy_cover,(667,75))
        window.blit(snail,(714,79))
    if blue_fish_owned==True and pike_owned==True and fat_fish_owned == True and snail_owned == True and gift_1_received==False:
        window.blit(gift_button,(915,97))
    elif gift_1_received==False:
        window.blit(locked_gift,(915,97))
    else:
        window.blit(received_gift,(915,97))
    if frog_owned==True:
        window.blit(trophy_cover,(97,173))
        window.blit(frog,(132,175))
    if koi_fish_owned==True:
        window.blit(trophy_cover,(287,173))
        window.blit(koi_fish,(327,183))
    if sturgeon_owned==True:
        window.blit(trophy_cover,(477,173))
        window.blit(sturgeon,(518,180))
    if piranha_owned==True:
        window.blit(trophy_cover,(667,173))
        window.blit(piranha,(709,179))
    if frog_owned==True and koi_fish_owned==True and sturgeon_owned == True and piranha_owned == True and gift_2_received==False:
        window.blit(gift_button,(915,194))
    elif gift_2_received==False:
        window.blit(locked_gift,(915,194))
    else:
        window.blit(received_gift,(915,194)) 
    if prawn_owned==True:
        window.blit(trophy_cover,(97,271))
        window.blit(prawn,(150,280))
    if tiger_fish_owned==True:
        window.blit(trophy_cover,(287,271))
        window.blit(tiger_fish,(338,278))
    if crab_owned==True:
        window.blit(trophy_cover,(477,271))
        window.blit(crab,(525,273))
    if sword_fish_owned==True:
        window.blit(trophy_cover,(667,271))
        window.blit(sword_fish,(691,283))
    if prawn_owned==True and tiger_fish_owned==True and crab_owned == True and sword_fish_owned == True and gift_3_received==False:
        window.blit(gift_button,(915,291))
    elif gift_3_received==False:
        window.blit(locked_gift,(915,291))
    else:
        window.blit(received_gift,(915,291))
    if turtle_owned==True:
        window.blit(trophy_cover,(97,369))
        window.blit(turtle,(137,379))
    if shark_owned==True:
        window.blit(trophy_cover,(287,369))
        window.blit(shark,(319,380))
    if light_fish_owned==True:
        window.blit(trophy_cover,(477,369))
        window.blit(light_fish,(524,371))
    if nautilus_owned==True:
        window.blit(trophy_cover,(667,369))
        window.blit(nautilus,(713,373))
    if turtle_owned==True and shark_owned==True and nautilus_owned == True and light_fish_owned == True and gift_4_received==False:
        window.blit(gift_button,(915,388))
    elif gift_4_received==False:
        window.blit(locked_gift,(915,388))
    else:
        window.blit(received_gift,(915,388))
    if zombie_fish_owned==True:
        window.blit(trophy_cover,(381,467))
        window.blit(zombie_fish,(426,477))
    if zombie_fish_owned==True and gift_5_received==False:
        window.blit(gift_button,(625,485))
    elif gift_5_received==False:
        window.blit(locked_gift,(625,485))
    else:
        window.blit(received_gift,(625,485))
    run = True
    while run:
        if cancel_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(cancel_coll,(945,515))
        else:
                window.blit(cancel,(945,515))
        for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if cancel_rect.collidepoint(mouse_pos):
                        home(event)
                    if gift1_rect.collidepoint(mouse_pos) and blue_fish_owned==True and pike_owned==True and fat_fish_owned == True and snail_owned == True and gift_1_received==False:
                        gift_type = 1
                        gift_alert(event,gift_type)
                    if gift2_rect.collidepoint(mouse_pos) and frog_owned==True and koi_fish_owned==True and piranha_owned == True and sturgeon_owned == True and gift_2_received==False:
                        gift_type = 2
                        gift_alert(event,gift_type)
                    if gift3_rect.collidepoint(mouse_pos) and prawn_owned==True and tiger_fish_owned==True and crab_owned == True and sword_fish_owned == True and gift_3_received==False:
                        gift_type = 3
                        gift_alert(event,gift_type)
                    if gift4_rect.collidepoint(mouse_pos) and turtle_owned==True and light_fish_owned==True and shark_owned == True and nautilus_owned == True and gift_4_received==False:
                        gift_type = 4
                        gift_alert(event,gift_type)
                    if gift5_rect.collidepoint(mouse_pos) and zombie_fish_owned == True and gift_5_received==False:
                        gift_type = 5
                        gift_alert(event,gift_type)
                         
        pygame.display.update()
def achievement(event):
    global catched,decorations,fish_bought,total_money
    cancel_rect = cancel.get_rect()
    cancel_rect.topleft = (945, 515)
    gift1_rect = gift_button.get_rect()
    gift1_rect.topleft = (915,97)
    gift2_rect = gift_button.get_rect()
    gift2_rect.topleft = (915,194)
    gift3_rect = gift_button.get_rect()
    gift3_rect.topleft = (915,291)
    gift4_rect = gift_button.get_rect()
    gift4_rect.topleft = (915,388)
    gift5_rect = gift_button.get_rect()
    gift5_rect.topleft = (625,485)
    window.blit(achieve_back,(0,0))
    if catched<1000:
        pygame.draw.rect(window, (80,80,80), (500, 100, 300, 30))
    if decorations<12:
        pygame.draw.rect(window, (80,80,80), (500, 197, 300, 30))
    if fish_bought<9:
        pygame.draw.rect(window, (80,80,80), (500, 294, 300, 30))
    if total_money<100000:
        pygame.draw.rect(window, (80,80,80), (500, 392, 300, 30))
    achieve_task1 = font.render("Catch", True, (255, 255, 255))
    achieve_task2 = font.render("Buy", True, (255, 255, 255))
    achieve_task3 = font.render("Earn", True, (255, 255, 255))
    if catched<10:
        window.blit(achieve_task1,(120,107))
        achieve_task1f = font.render("10 fish                               "+str(catched)+"/10", True, (255, 255, 255))
        filled = catched*30
        pygame.draw.rect(window, (12,165,0), (500, 100, filled, 30))
    elif catched<100 and catched>=10:
        window.blit(achieve_task1,(120,107))
        achieve_task1f = font.render("100 fish                      "+str(catched)+"/100", True, (255, 255, 255))
        filled = catched*3
        pygame.draw.rect(window, (12,165,0), (500, 100, filled, 30))
        window.blit(trophy_square,(894,75))
        window.blit(b_trophy,(900,81))
    elif catched<1000 and catched>=100:
        window.blit(achieve_task1,(120,107))
        achieve_task1f = font.render("1000 fish             "+str(catched)+"/1000", True, (255, 255, 255))
        filled = catched*0.3
        pygame.draw.rect(window, (12,165,0), (500, 100, filled, 30))
        window.blit(trophy_square,(894,75))
        window.blit(s_trophy,(900,81))
    elif catched>=1000:
        achieve_task1f = font.render("                              Fish catched: "+str(catched), True, (255, 255, 255))
        window.blit(trophy_square,(894,75))
        window.blit(trophy_img,(900,81))
    window.blit(achieve_task1f,(200,107))
    if decorations<4:
        window.blit(achieve_task2,(120,204))
        achieve_task2f = font.render("4 decorations                    "+str(decorations)+"/4", True, (255, 255, 255))
        filled = decorations*75
        pygame.draw.rect(window, (12,165,0), (500, 197, filled, 30))
    elif decorations<8 and decorations>=4:
        window.blit(achieve_task2,(120,204))
        achieve_task2f = font.render("8 decorations                    "+str(decorations)+"/8", True, (255, 255, 255))
        filled = decorations*37.5
        pygame.draw.rect(window, (12,165,0), (500, 197, filled, 30))
        window.blit(trophy_square,(894,173))
        window.blit(b_trophy,(900,179))
    elif decorations<12 and decorations>=8:
        window.blit(achieve_task2,(120,204))
        achieve_task2f = font.render("12 decorations               "+str(decorations)+"/12", True, (255, 255, 255))
        filled = decorations*25
        pygame.draw.rect(window, (12,165,0), (500, 197, filled, 30))
        window.blit(trophy_square,(894,173))
        window.blit(s_trophy,(900,179))
    elif decorations>=12:
        achieve_task2f = font.render("                                 All decorations bought", True, (255, 255, 255))
        window.blit(trophy_square,(894,173))
        window.blit(trophy_img,(900,179))
    window.blit(achieve_task2f,(172,204))
    if fish_bought<3:
        window.blit(achieve_task2,(120,301))
        achieve_task3f = font.render("3 species of fish             "+str(fish_bought)+"/3", True, (255, 255, 255))
        filled = fish_bought*100
        pygame.draw.rect(window, (12,165,0), (500, 294, filled, 30))
    elif fish_bought<6 and fish_bought>=3:
        window.blit(achieve_task2,(120,301))
        achieve_task3f = font.render("6 species of fish             "+str(fish_bought)+"/6", True, (255, 255, 255))
        filled = fish_bought*50
        pygame.draw.rect(window, (12,165,0), (500, 294, filled, 30))
        window.blit(trophy_square,(894,271))
        window.blit(b_trophy,(900,277))
    elif fish_bought<9 and fish_bought>=6:
        window.blit(achieve_task2,(120,301))
        achieve_task3f = font.render("9 species of fish             "+str(fish_bought)+"/9", True, (255, 255, 255))
        filled = fish_bought*33.5
        pygame.draw.rect(window, (12,165,0), (500, 294, filled, 30))
        window.blit(trophy_square,(894,271))
        window.blit(s_trophy,(900,277))
    elif fish_bought>=9:
        achieve_task3f = font.render("                              All species of fish bought", True, (255, 255, 255))
        window.blit(trophy_square,(894,271))
        window.blit(trophy_img,(900,277))
    window.blit(achieve_task3f,(175,301))
    if total_money < 1000:
        window.blit(achieve_task3,(120,400))
        achieve_task4f = font.render("$1000                              "+str(total_money)+"/1K", True, (255, 255, 255))
        filled = total_money*0.3
        pygame.draw.rect(window, (12,165,0), (500, 392, filled, 30))
    elif total_money>=1000 and total_money < 10000: 
        window.blit(achieve_task3,(120,400))  
        achieve_task4f = font.render("$10000                    "+str(total_money)+"/10K", True, (255, 255, 255))
        filled = total_money*0.03
        pygame.draw.rect(window, (12,165,0), (500, 392, filled, 30))
        window.blit(trophy_square,(894,369))
        window.blit(b_trophy,(900,375))
    elif total_money>=10000 and total_money < 100000:
        window.blit(achieve_task3,(120,400))  
        achieve_task4f = font.render("$100K                 "+str(total_money)+"/100K", True, (255, 255, 255))
        filled = total_money*0.003
        pygame.draw.rect(window, (12,165,0), (500, 392, filled, 30))
        window.blit(trophy_square,(894,369))
        window.blit(s_trophy,(900,375))
    elif total_money>=100000:
        achieve_task4f = font.render("                          Money earned: $"+str(total_money), True, (255, 255, 255))
        window.blit(trophy_square,(894,369))
        window.blit(trophy_img,(900,375))
    if total_money < 1000:     
        window.blit(achieve_task4f,(188,400))
    else:
        window.blit(achieve_task4f,(188,400))
    run = True
    while run:
        if cancel_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(cancel_coll,(945,515))
        else:
                window.blit(cancel,(945,515))
        for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if cancel_rect.collidepoint(mouse_pos):
                        home(event)
        pygame.display.update()
def gift_alert(event,gift_type):
    global gift_1_received,gift_2_received,gift_3_received,gift_4_received,gift_5_received,grass_owned,clownfish_owned,clownfish_amount,backpack_slots,metal_owned,jelly_amount,jelly_owned,trophy_owned,money
    cancel_1_rect = cancel_1.get_rect()
    cancel_1_rect.topleft = (515,340)
    window.blit(trophy_back,(0,0))
    if blue_fish_owned==True:
        window.blit(trophy_cover,(97,75))
        window.blit(blue_fish,(140,80))
    if pike_owned==True:
        window.blit(trophy_cover,(287,75))
        window.blit(pike,(321,82))
    if fat_fish_owned==True:
        window.blit(trophy_cover,(477,75))
        window.blit(fat_fish,(518,79))
    if snail_owned==True:
        window.blit(trophy_cover,(667,75))
        window.blit(snail,(714,79))
    if blue_fish_owned==True and pike_owned==True and fat_fish_owned == True and snail_owned == True and gift_1_received==False:
        window.blit(gift_button,(915,97))
    elif gift_1_received==False:
        window.blit(locked_gift,(915,97))
    else:
        window.blit(received_gift,(915,97))
    if frog_owned==True:
        window.blit(trophy_cover,(97,173))
        window.blit(frog,(132,175))
    if koi_fish_owned==True:
        window.blit(trophy_cover,(287,173))
        window.blit(koi_fish,(327,183))
    if sturgeon_owned==True:
        window.blit(trophy_cover,(477,173))
        window.blit(sturgeon,(518,180))
    if piranha_owned==True:
        window.blit(trophy_cover,(667,173))
        window.blit(piranha,(709,179))
    if frog_owned==True and koi_fish_owned==True and sturgeon_owned == True and piranha_owned == True and gift_2_received==False:
        window.blit(gift_button,(915,194))
    elif gift_2_received==False:
        window.blit(locked_gift,(915,194))
    else:
        window.blit(received_gift,(915,194)) 
    if prawn_owned==True:
        window.blit(trophy_cover,(97,271))
        window.blit(prawn,(150,280))
    if tiger_fish_owned==True:
        window.blit(trophy_cover,(287,271))
        window.blit(tiger_fish,(338,278))
    if crab_owned==True:
        window.blit(trophy_cover,(477,271))
        window.blit(crab,(525,273))
    if sword_fish_owned==True:
        window.blit(trophy_cover,(667,271))
        window.blit(sword_fish,(691,283))
    if prawn_owned==True and tiger_fish_owned==True and crab_owned == True and sword_fish_owned == True and gift_3_received==False:
        window.blit(gift_button,(915,291))
    elif gift_3_received==False:
        window.blit(locked_gift,(915,291))
    else:
        window.blit(received_gift,(915,291))
    if turtle_owned==True:
        window.blit(trophy_cover,(97,369))
        window.blit(turtle,(137,379))
    if shark_owned==True:
        window.blit(trophy_cover,(287,369))
        window.blit(shark,(319,380))
    if light_fish_owned==True:
        window.blit(trophy_cover,(477,369))
        window.blit(light_fish,(524,371))
    if nautilus_owned==True:
        window.blit(trophy_cover,(667,369))
        window.blit(nautilus,(713,373))
    if turtle_owned==True and shark_owned==True and nautilus_owned == True and light_fish_owned == True and gift_4_received==False:
        window.blit(gift_button,(915,388))
    elif gift_4_received==False:
        window.blit(locked_gift,(915,388))
    else:
        window.blit(received_gift,(915,388))
    if zombie_fish_owned==True:
        window.blit(trophy_cover,(381,467))
        window.blit(zombie_fish,(426,477))
    if zombie_fish_owned==True and gift_5_received==False:
        window.blit(gift_button,(625,485))
    elif gift_5_received==False:
        window.blit(locked_gift,(625,485))
    else:
        window.blit(received_gift,(625,485))
    window.blit(gift_alert1,(300,110))
    window.blit(cancel_1,(515,340))
    if gift_type==1 and grass_owned==False:
        gift_1_received = True
        grass_owned=True
        window.blit(grass,(500,230))
    elif gift_type==1 and grass_owned==True:
        gift_1_received = True
        window.blit(cash,(480,245))
        price = font.render("100",True,(0,0,0))
        window.blit(price,(545,265))
        money+=100
    if gift_type==2 and clownfish_amount==0 and backpack_slots<20 and clownfish_in==False:
        gift_2_received = True
        clownfish_owned=True
        clownfish_amount +=1
        backpack_slots+=1
        window.blit(clownfish,(506,238))
    elif gift_type==2 and clownfish_amount>0 or backpack_slots>=20:
        gift_2_received = True
        window.blit(cash,(480,245))
        price = font.render("600",True,(0,0,0))
        window.blit(price,(545,265))
        money+=600
    elif gift_type==2 and clownfish_in==True:
        gift_2_received = True
        window.blit(cash,(480,245))
        price = font.render("600",True,(0,0,0))
        window.blit(price,(545,265))
        money+=600
    if gift_type==3 and metal_owned==False:
        gift_3_received = True
        metal_owned=True
        window.blit(metal,(503,236))
    elif gift_type==3 and metal_owned==True:
        gift_3_received = True
        window.blit(cash,(480,245))
        price = font.render("450",True,(0,0,0))
        window.blit(price,(545,265))
        money+=450
    if gift_type==4 and jelly_amount==0 and backpack_slots<20 and jelly_in==False:
        gift_4_received = True
        jelly_owned=True
        jelly_amount +=1
        backpack_slots+=1
        window.blit(jelly,(509,238))
    elif gift_type==4 and jelly_amount>0 or backpack_slots>=20:
        gift_4_received = True
        window.blit(cash,(480,245))
        price = font.render("1500",True,(0,0,0))
        window.blit(price,(545,265))
        money+=1500
    elif gift_type==4 and jelly_in==True:
        gift_4_received = True
        window.blit(cash,(480,245))
        price = font.render("1500",True,(0,0,0))
        window.blit(price,(545,265))
        money+=1500
    if gift_type==5 and trophy_owned==False:
        gift_5_received = True
        trophy_owned=True
        window.blit(trophy_img,(503,236))
    run = True
    while run:
        for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if cancel_1_rect.collidepoint(mouse_pos):
                        trophy(event)
                         
        pygame.display.update()
    
def village(event):
    run = True
    image_list_f = []
    for i in range(1, 12):
        filename = f"react_animation/react_{i}.png"
        img = pygame.image.load(filename).convert_alpha()
        image_list_f.append(img)
    current_image_index = 0
    display_time = 44
    display_time1 = 65
    display_time2 = 120
    last_display_time = pygame.time.get_ticks()
    last_display_time1 = pygame.time.get_ticks()
    last_display_time2 = pygame.time.get_ticks()
    last_display_time3 = pygame.time.get_ticks()
    last_display_time4 = pygame.time.get_ticks()
    image_list_b = []
    image_list_2 = []
    image_list_3 = []
    image_list_4 = []
    count = 0
    a_stop = False
    for i in range(1, 65):
        filename1 = f"bird_fly/bird_{i}.png"
        img1 = pygame.image.load(filename1).convert_alpha()
        filename1 = pygame.transform.scale(img1, (704, 125)).convert_alpha()
        image_list_b.append(filename1)
    current_image_index1 = 0
    current_image_index2 = 0
    current_image_index3 = 0
    current_image_index4 = 0
    for i in range(1, 19):
        filename2 = f"fire_animation/fire_{i}.png"
        img2 = pygame.image.load(filename2).convert_alpha()
        filename2 = pygame.transform.scale(img2, (16, 24)).convert_alpha()
        image_list_2.append(filename2)
    for i in range(1, 5):
        filename3 = f"bird_animation/bird1_{i}.png"
        img3 = pygame.image.load(filename3).convert_alpha()
        image_list_3.append(img3)
    for i in range(1, 22):
        filename4 = f"fire_animation_2/fire_{i}.png"
        img4 = pygame.image.load(filename4).convert_alpha()
        filename4 = pygame.transform.scale(img4, (15, 18)).convert_alpha()
        image_list_4.append(filename4)
    window.blit(v_background,(0,0))
    stop = False
    back_home = pygame.Rect(190, 230, 150, 80)
    to_shop = pygame.Rect(745, 270, 140, 85)
    to_lake = pygame.Rect(130, 490, 210, 80)
    to_market = pygame.Rect(400, 420, 280, 75)
    while run:
        window.blit(image_list_b[current_image_index1], (0, -1))
        window.blit(image_list_2[current_image_index2], (533, 341))
        window.blit(image_list_3[current_image_index3], (944, 225))
        window.blit(image_list_4[current_image_index4], (114, 458))
        current_time1 = pygame.time.get_ticks()
        current_time2 = pygame.time.get_ticks()
        current_time3 = pygame.time.get_ticks()
        current_time4 = pygame.time.get_ticks()
        if current_time1 - last_display_time1 >= display_time1:
            current_image_index1 = (current_image_index1 + 1) % len(image_list_b)
            last_display_time1 = current_time1
        if current_image_index1 == 63 and count<36:
            current_image_index1 = 59
            count+=1
        elif count==36:
            count=0
            current_image_index1 = 0
        if current_time2 - last_display_time2 >= display_time2:
            current_image_index2 = (current_image_index2 + 1) % len(image_list_2)
            last_display_time2 = current_time2
        if current_image_index2== 19:
            current_image_index2 = 1
        if current_time3 - last_display_time3 >= 1200 and a_stop==False:
            current_image_index3 = (current_image_index3 + 1) % len(image_list_3)
            last_display_time3 = current_time3
        if current_time4 - last_display_time4 >= 120:
            current_image_index4 = (current_image_index4 + 1) % len(image_list_4)
            last_display_time4 = current_time4
        if current_image_index4== 22:
            current_image_index4 = 1
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if back_home.collidepoint(pygame.mouse.get_pos()):
            a_stop=True
            window.blit(image_list_f[current_image_index], (70, 120))
            current_time = pygame.time.get_ticks()
            if current_time - last_display_time >= display_time and stop== False:
                window.blit(v_back1,(0,0))
                window.blit(image_list_3[current_image_index3], (944, 225))
                current_image_index = (current_image_index + 1) % len(image_list_f)
                last_display_time = current_time
            if current_image_index == 10:
                stop = True
        elif to_shop.collidepoint(pygame.mouse.get_pos()):
            a_stop=True
            window.blit(image_list_f[current_image_index], (620, 195))
            current_time = pygame.time.get_ticks()
            if current_time - last_display_time >= display_time and stop== False:
                window.blit(v_back2,(0,0))
                window.blit(image_list_3[current_image_index3], (944, 225))
                current_image_index = (current_image_index + 1) % len(image_list_f)
                last_display_time = current_time
            if current_image_index == 10:
                stop = True
        elif to_lake.collidepoint(pygame.mouse.get_pos()):
            a_stop=True
            window.blit(image_list_f[current_image_index], (70, 395))
            current_time = pygame.time.get_ticks()
            if current_time - last_display_time >= display_time and stop== False:
                window.blit(v_back4,(0,0))
                window.blit(image_list_3[current_image_index3], (944, 225))
                current_image_index = (current_image_index + 1) % len(image_list_f)
                last_display_time = current_time
            if current_image_index == 10:
                stop = True
        elif to_market.collidepoint(pygame.mouse.get_pos()):
            a_stop=True
            window.blit(image_list_f[current_image_index], (350, 315))
            current_time = pygame.time.get_ticks()
            if current_time - last_display_time >= display_time and stop== False:
                window.blit(v_back3,(0,0))
                window.blit(image_list_3[current_image_index3], (944, 225))
                current_image_index = (current_image_index + 1) % len(image_list_f)
                last_display_time = current_time
            if current_image_index == 10:
                stop = True     
        else:
            a_stop=False
            current_image_index = 0
            window.blit(v_background,(0,0))
            window.blit(image_list_b[current_image_index1], (0, -1))
            window.blit(image_list_2[current_image_index2], (533, 341))
            window.blit(image_list_3[current_image_index3], (944, 225))
            window.blit(image_list_4[current_image_index4], (114, 458))
            stop = False
        if back_home.collidepoint(mouse_pos):
            home(event)
        if to_shop.collidepoint(mouse_pos):
            shop(event)
        if to_lake.collidepoint(mouse_pos):
            lake(event)
        if to_market.collidepoint(mouse_pos):
            fishmarket(event)
        pygame.display.update()
    
def shop(event):
    global money,shop_aquarium,jelly,lionfish,backpack_slots,fish_bought
    global fightfish_owned,clownfish_owned,starfish_owned,jelly_owned,lionfish_owned,tang_owned,ray_owned,octopus_owned,seahorse_owned
    fightfish_buying=clownfish_buying=starfish_buying=jelly_buying=lionfish_buying=tang_buying=ray_buying=octopus_buying=seahorse_buying=False
    global fightfish_amount,clownfish_amount,starfish_amount,jelly_amount,lionfish_amount,tang_amount,ray_amount,octopus_amount,seahorse_amount
    shop_aquarium = pygame.transform.scale(shop_aquarium, (150, 150)).convert_alpha()
    jelly1 = pygame.transform.scale(jelly, (60, 66)).convert_alpha()
    lionfish1 = pygame.transform.scale(lionfish, (80, 70)).convert_alpha()
    tang1 = pygame.transform.scale(tang, (85, 60)).convert_alpha()
    octopus1 = pygame.transform.scale(octopus, (83, 56)).convert_alpha()
    seahorse1 = pygame.transform.scale(seahorse, (43, 74)).convert_alpha()
    run = True
    start_time = pygame.time.get_ticks()
    buying = True
    can_exit = True
    outdoor_rect = door.get_rect()
    outdoor_rect.topleft = (10, 480)
    scenery_rect = scenery_button.get_rect()
    scenery_rect.topleft = (65,195)
    equipment_rect = equipment_button.get_rect()
    equipment_rect.topleft = (0,355)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        if elapsed_time >= 600:
            buying = False
        window.blit(shop_background, (0, 0))
        if outdoor_rect.collidepoint(pygame.mouse.get_pos()) and can_exit == True:
                window.blit(door_coll,(10,480))
        else:
                window.blit(door,(10,480))
        window.blit(fishes_button_coll,(90,55))
        if scenery_rect.collidepoint(pygame.mouse.get_pos()) and can_exit== True:
                window.blit(scenery_button_coll,(65,195))
        else:
                window.blit(scenery_button,(65,195))
        if equipment_rect.collidepoint(pygame.mouse.get_pos()) and can_exit== True:
                window.blit(equipment_button_coll,(0,355))
        else:
                window.blit(equipment_button,(0,355))
        window.blit(border_shop,(-120,0))
        window.blit(cash,(40,0))
        #-----------------------------------------aquariums
        if fightfish_amount == 0 and fightfish_in==False:
            window.blit(shop_aquarium,(490,95))
            window.blit(fightfish,(523,130))
            fightfish_price = 300
            fightfish_price_s = font.render("      300",True,(255,255,255))
            window.blit(fightfish_price_s,(535,80))
            window.blit(cash1,(518,65))
        else:
            window.blit(check,(540,150))
        if clownfish_amount == 0 and clownfish_in==False:
            window.blit(shop_aquarium,(640,95))
            window.blit(clownfish,(680,140))
            clownfish_price = 580
            clownfish_price_s = font.render("      580",True,(255,255,255))
            window.blit(clownfish_price_s,(685,80))
            window.blit(cash1,(667,65))
        else:
            window.blit(check,(685,150))
        if starfish_amount == 0 and starfish_in==False:
            window.blit(shop_aquarium,(790,95))
            window.blit(starfish,(832,136))
            starfish_price = 950
            starfish_price_s = font.render("     950",True,(255,255,255))
            window.blit(starfish_price_s,(835,80))
            window.blit(cash1,(813,65))
        else:
            window.blit(check,(835,150))
        if jelly_amount == 0 and jelly_in==False:
            window.blit(shop_aquarium,(490,282))
            window.blit(jelly1,(536,325))
            jelly_price = 1500
            jelly_price_s = font.render("     1500",True,(255,255,255))
            window.blit(jelly_price_s,(530,270))
            window.blit(cash1,(507,255))
        else:
            window.blit(check,(540,335))
        if lionfish_amount == 0 and lionfish_in==False:
            window.blit(shop_aquarium,(640,282))
            window.blit(lionfish1,(674,320))
            lionfish_price = 2700
            lionfish_price_s = font.render("     2700",True,(255,255,255))
            window.blit(lionfish_price_s,(680,270))
            window.blit(cash1,(657,255))
        else:
            window.blit(check,(685,335))
        if tang_amount == 0 and tang_in==False:
            window.blit(shop_aquarium,(790,282))
            window.blit(tang1,(820,328))
            tang_price = 4200
            tang_price_s = font.render("     4200",True,(255,255,255))
            window.blit(tang_price_s,(830,270))
            window.blit(cash1,(807,255))
        else:
            window.blit(check,(835,335))
        if ray_amount == 0 and ray_in==False:
            window.blit(shop_aquarium,(490,468))
            window.blit(ray,(518,500))
            ray_price = 8000
            ray_price_s = font.render("     8000",True,(255,255,255))
            window.blit(ray_price_s,(530,455))
            window.blit(cash1,(507,440))
        else:
            window.blit(check,(540,520))
        if octopus_amount == 0 and octopus_in==False:
            window.blit(shop_aquarium,(640,468))
            window.blit(octopus1,(676,505))
            octopus_price = 15000
            octopus_price_s = font.render("      15000",True,(255,255,255))
            window.blit(octopus_price_s,(672,455))
            window.blit(cash1,(654,440))
        else:
            window.blit(check,(685,520))
        if seahorse_amount == 0 and seahorse_in==False:
            window.blit(shop_aquarium,(790,468))
            window.blit(seahorse1,(844,504))
            seahorse_price = 30000
            seahorse_price_s = font.render("     30000",True,(255,255,255))
            window.blit(seahorse_price_s,(821,455))
            window.blit(cash1,(799,440))
        else:
            window.blit(check,(835,520))
        #-----------------------------------------
        money_amount = font.render(str(money),True,(0,0,0))
        window.blit(money_amount,(105,21))
        fightfish_rect = shop_aquarium.get_rect()
        fightfish_rect.topleft = (490,95)
        clownfish_rect = shop_aquarium.get_rect()
        clownfish_rect.topleft = (640,95)
        starfish_rect = shop_aquarium.get_rect()
        starfish_rect.topleft = (790,95)
        jelly_rect = shop_aquarium.get_rect()
        jelly_rect.topleft = (490,282)
        lionfish_rect = shop_aquarium.get_rect()
        lionfish_rect.topleft = (640,282)
        tang_rect = shop_aquarium.get_rect()
        tang_rect.topleft = (790,282)
        ray_rect = shop_aquarium.get_rect()
        ray_rect.topleft = (490,468)
        octopus_rect = shop_aquarium.get_rect()
        octopus_rect.topleft = (640,468)
        seahorse_rect = shop_aquarium.get_rect()
        seahorse_rect.topleft = (790,468)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if outdoor_rect.collidepoint(mouse_pos) and can_exit == True:
                village(event)
            elif scenery_rect.collidepoint(mouse_pos) and buying == False and can_exit == True:
                shop_scenery(event)
            elif equipment_rect.collidepoint(mouse_pos) and buying == False and can_exit == True:
                shop_equipment(event)
            elif fightfish_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and fightfish_amount == 0 and fightfish_in==False:
                fightfish_buying = True
                price = fightfish_price
            elif clownfish_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and clownfish_amount == 0 and clownfish_in==False:
                clownfish_buying = True
                price = clownfish_price
            elif starfish_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and starfish_amount == 0 and starfish_in==False:
                starfish_buying = True
                price = starfish_price
            elif jelly_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and jelly_amount == 0 and jelly_in==False:
                jelly_buying = True
                price = jelly_price
            elif lionfish_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and lionfish_amount == 0 and lionfish_in==False:
                lionfish_buying = True
                price = lionfish_price
            elif tang_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and tang_amount == 0 and tang_in==False:
                tang_buying = True
                price = tang_price
            elif ray_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and ray_amount == 0 and ray_in==False:
                ray_buying = True
                price = ray_price
            elif octopus_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and octopus_amount == 0 and octopus_in==False:
                octopus_buying = True
                price = octopus_price
            elif seahorse_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and seahorse_amount == 0 and seahorse_in==False:
                seahorse_buying = True
                price = seahorse_price
        if fightfish_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if fightfish_owned==False:
                        fish_bought+=1
                    fightfish_owned = True
                    fightfish_amount = 1
                    fightfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    fightfish_owned = False
                    fightfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if clownfish_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if clownfish_owned==False:
                        fish_bought+=1
                    clownfish_owned = True
                    clownfish_amount = 1
                    clownfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    clownfish_owned = False
                    clownfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if starfish_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if starfish_owned==False:
                        fish_bought+=1
                    starfish_owned = True
                    starfish_amount = 1
                    starfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    starfish_owned = False
                    starfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if jelly_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if jelly_owned==False:
                        fish_bought+=1
                    jelly_owned = True
                    jelly_amount = 1
                    jelly_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    jelly_owned = False
                    jelly_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if lionfish_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if lionfish_owned==False:
                        fish_bought+=1
                    lionfish_owned = True
                    lionfish_amount = 1
                    lionfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    lionfish_owned = False
                    lionfish_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if tang_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if tang_owned==False:
                        fish_bought+=1
                    tang_owned = True
                    tang_amount = 1
                    tang_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    tang_owned = False
                    tang_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if ray_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if ray_owned==False:
                        fish_bought+=1
                    ray_owned = True
                    ray_amount = 1
                    ray_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    ray_owned = False
                    ray_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if octopus_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if octopus_owned==False:
                        fish_bought+=1
                    octopus_owned = True
                    octopus_amount = 1
                    octopus_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    octopus_owned = False
                    octopus_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if seahorse_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function_f(event,price)
            if purchased is not None:
                if purchased==True:
                    if seahorse_owned==False:
                        fish_bought+=1
                    seahorse_owned = True
                    seahorse_amount = 1
                    seahorse_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased==False:
                    seahorse_owned = False
                    seahorse_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        pygame.display.update()

def shop_scenery(event):
    global money,vulcano,statue,grn_plant,decorations
    global grass_owned,bl_coral_owned,flamingo_owned,grn_plant_owned,lizard_owned,metal_owned,mini_house_owned,pin_plant_owned,pur_plant_owned,skeleton_owned,statue_owned,vulcano_owned
    grass_buying = bl_coral_buying = flamingo_buying = grn_plant_buying = lizard_buying = metal_buying = mini_house_buying = pin_plant_buying = pur_plant_buying = skeleton_buying = statue_buying = vulcano_buying = False
    vulcano_shop = pygame.transform.scale(vulcano, (119, 108))
    pin_plant_shop = pygame.transform.scale(pin_plant, (50, 100))
    pur_plant_shop = pygame.transform.scale(pur_plant, (24, 109))
    grn_plant_shop = pygame.transform.scale(grn_plant, (81, 124))
    statue = pygame.transform.scale(statue, (70, 120))
    buying = False
    run = True
    outdoor_rect = door.get_rect()
    outdoor_rect.topleft = (10, 480)
    fishes_rect = fishes_button.get_rect()
    fishes_rect.topleft = (90,55)
    equipment_rect = equipment_button.get_rect()
    equipment_rect.topleft = (0,355)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.blit(shop_background, (0, 0))
        if outdoor_rect.collidepoint(pygame.mouse.get_pos()) and buying == False:
                window.blit(door_coll,(10,480))
        else:
                window.blit(door,(10,480))
        if fishes_rect.collidepoint(pygame.mouse.get_pos()) and buying == False:
                window.blit(fishes_button_coll,(90,55))
        else:
                window.blit(fishes_button,(90,55))
        window.blit(scenery_button_coll,(65,195))
        if equipment_rect.collidepoint(pygame.mouse.get_pos()) and buying == False:
                window.blit(equipment_button_coll,(0,355))
        else:
                window.blit(equipment_button,(0,355))
        window.blit(border_shop,(-120,0))
        window.blit(cash,(40,0))
        if grass_owned==False:
            window.blit(grass,(490,142))
            grass_price_s = font.render("       100",True,(255,255,255))
            window.blit(grass_price_s,(490,60))
            window.blit(cash1,(477,45))
        else:
            window.blit(check,(500,141))
        grass_price = 100
        if pur_plant_owned == False:
            window.blit(pur_plant_shop,(630,107))
            pur_price_s = font.render("       180",True,(255,255,255))
            window.blit(pur_price_s,(610,60))
            window.blit(cash1,(597,45))
        else:
            window.blit(check,(610,141))
        pur_price = 180
        if bl_coral_owned == False:
            window.blit(bl_coral,(720,130))
            bl_price_s = font.render("        300",True,(255,255,255))
            window.blit(bl_price_s,(720,60))
            window.blit(cash1,(713,45))
        else:
            window.blit(check,(720,141))
        bl_price = 300
        if metal_owned == False:
            window.blit(metal,(840,125))
            metal_price_s = font.render("     450",True,(255,255,255))
            window.blit(metal_price_s,(850,60))
            window.blit(cash1,(827,45))
        else:
            window.blit(check,(840,141))
        metal_price = 450
        if pin_plant_owned == False:
            window.blit(pin_plant_shop,(500,303))
            pin_price_s = font.render("       600",True,(255,255,255))
            window.blit(pin_price_s,(490,260))
            window.blit(cash1,(477,245))
        else:
            window.blit(check,(500,340))
        pin_price = 600
        if lizard_owned == False:
            window.blit(lizard,(610,355))
            lizard_price_s = font.render("       820",True,(255,255,255))
            window.blit(lizard_price_s,(600,260))
            window.blit(cash1,(587,245))
        else:
            window.blit(check,(610,340))
        lizard_price = 820
        if grn_plant_owned == False:
            window.blit(grn_plant_shop,(705,280))
            grn_price_s = font.render("      1100",True,(255,255,255))
            window.blit(grn_price_s,(710,260))
            window.blit(cash1,(692,245))
        else:
            window.blit(check,(720,340))
        grn_price = 1100
        if skeleton_owned == False:
            window.blit(skeleton,(835,369))
            skeleton_price_s = font.render("       1500",True,(255,255,255))
            window.blit(skeleton_price_s,(840,260))
            window.blit(cash1,(827,245))
        else:
            window.blit(check,(835,340))
        skeleton_price = 1500
        if mini_house_owned == False:
            window.blit(mini_house,(490,503))
            mini_price_s = font.render("       2000",True,(255,255,255))
            window.blit(mini_price_s,(490,450))
            window.blit(cash1,(477,435))
        else:
            window.blit(check,(505,520))
        mini_price = 2000
        if statue_owned == False:
            window.blit(statue,(605,474))
            statue_price_s = font.render("       3800",True,(255,255,255))
            window.blit(statue_price_s,(600,450))
            window.blit(cash1,(588,435))
        else:
            window.blit(check,(605,520))
        statue_price = 3800
        if flamingo_owned == False:
            window.blit(flamingo,(705,453))
            flamingo_price_s = font.render("       6200",True,(255,255,255))
            window.blit(flamingo_price_s,(710,450))
            window.blit(cash1,(698,435))
        else:
            window.blit(check,(715,520))
        flamingo_price = 6200
        if vulcano_owned == False:
            window.blit(vulcano_shop,(820,480))
            vulcano_price_s = font.render("       10000",True,(255,255,255))
            window.blit(vulcano_price_s,(830,450))
            window.blit(cash1,(817,435))
        else:
            window.blit(check,(830,520))
        vulcano_price = 10000
        money_amount =font.render(str(money),True,(0,0,0))
        window.blit(money_amount,(105,21))
        outdoor_rect = door.get_rect()
        outdoor_rect.topleft = (10, 480)
        #------------------------------------------------------------------ Items collides
        grass_rect = grass.get_rect()
        grass_rect.topleft = (490,142)
        pur_plant_rect = pur_plant_shop.get_rect()
        pur_plant_rect.topleft = (630,107)
        bl_coral_rect = bl_coral.get_rect()
        bl_coral_rect.topleft = (720,130)
        metal_rect = metal.get_rect()
        metal_rect.topleft = (840,125)
        pin_plant_rect = pin_plant_shop.get_rect()
        pin_plant_rect.topleft = (500,303)
        lizard_rect = lizard.get_rect()
        lizard_rect.topleft = (610,355)
        grn_plant_rect = grn_plant_shop.get_rect()
        grn_plant_rect.topleft = (705,261)
        skeleton_rect = skeleton.get_rect()
        skeleton_rect.topleft = (835,369)
        mini_house_rect = mini_house.get_rect()
        mini_house_rect.topleft = (490,503)
        statue_rect = statue.get_rect()
        statue_rect.topleft = (605,474)
        flamingo_rect = flamingo.get_rect()
        flamingo_rect.topleft = (705,453)
        vulcano_rect = vulcano.get_rect()
        vulcano_rect.topleft = (820,480)
        fishes_rect = fishes_button.get_rect()
        fishes_rect.topleft = (90,55)
        equipment_rect = equipment_button.get_rect()
        equipment_rect.topleft = (0,355)
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if outdoor_rect.collidepoint(mouse_pos) and buying == False:
                village(event)
            elif equipment_rect.collidepoint(mouse_pos) and buying == False:
                shop_equipment(event)
            elif grass_rect.collidepoint(mouse_pos) and buying == False and grass_owned == False:
                grass_buying = True
                price = grass_price
            elif pur_plant_rect.collidepoint(mouse_pos) and buying == False and pur_plant_owned == False:
                pur_plant_buying = True
                price = pur_price
            elif bl_coral_rect.collidepoint(mouse_pos) and buying == False and bl_coral_owned == False:
                bl_coral_buying = True
                price = bl_price
            elif metal_rect.collidepoint(mouse_pos) and buying == False and metal_owned == False:
                metal_buying = True
                price = metal_price
            elif pin_plant_rect.collidepoint(mouse_pos) and buying == False and pin_plant_owned == False:
                pin_plant_buying = True
                price = pin_price
            elif lizard_rect.collidepoint(mouse_pos) and buying == False and lizard_owned == False:
                lizard_buying = True
                price = lizard_price
            elif grn_plant_rect.collidepoint(mouse_pos) and buying == False and grn_plant_owned == False:
                grn_plant_buying = True
                price = grn_price
            elif skeleton_rect.collidepoint(mouse_pos) and buying == False and skeleton_owned == False:
                skeleton_buying = True
                price = skeleton_price
            elif mini_house_rect.collidepoint(mouse_pos) and buying == False and mini_house_owned == False:
                mini_house_buying = True
                price = mini_price
            elif statue_rect.collidepoint(mouse_pos) and buying == False and statue_owned == False:
                statue_buying = True
                price = statue_price
            elif flamingo_rect.collidepoint(mouse_pos) and buying == False and flamingo_owned == False:
                flamingo_buying = True
                price = flamingo_price
            elif vulcano_rect.collidepoint(mouse_pos) and buying == False and vulcano_owned == False:
                vulcano_buying = True
                price = vulcano_price
            elif fishes_rect.collidepoint(mouse_pos):
                shop(event)
        if grass_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    grass_owned = True
                    grass_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    grass_owned = False
                    grass_buying = False
                    purchased = None
                    buying = False
        if pur_plant_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    pur_plant_owned = True
                    pur_plant_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    pur_plant_owned = False
                    pur_plant_buying = False
                    purchased = None
                    buying = False
        if bl_coral_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    bl_coral_owned = True
                    bl_coral_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    bl_coral_owned = False
                    bl_coral_buying = False
                    purchased = None
                    buying = False
        if metal_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    metal_owned = True
                    metal_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    metal_owned = False
                    metal_buying = False
                    purchased = None
                    buying = False
        if pin_plant_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    pin_plant_owned = True
                    pin_plant_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    pin_plant_owned = False
                    pin_plant_buying = False
                    purchased = None
                    buying = False
        if lizard_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    lizard_owned = True
                    lizard_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    lizard_owned = False
                    lizard_buying = False
                    purchased = None
                    buying = False
        if grn_plant_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    grn_plant_owned = True
                    grn_plant_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    grn_plant_owned = False
                    grn_plant_buying = False
                    purchased = None
                    buying = False
        if skeleton_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    skeleton_owned = True
                    skeleton_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    skeleton_owned = False
                    skeleton_buying = False
                    purchased = None
                    buying = False
        if mini_house_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    mini_house_owned = True
                    mini_house_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    mini_house_owned = False
                    mini_house_buying = False
                    purchased = None
                    buying = False
        if statue_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    statue_owned = True
                    statue_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    statue_owned = False
                    statue_buying = False
                    purchased = None
                    buying = False
        if flamingo_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    flamingo_owned = True
                    flamingo_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    flamingo_owned = False
                    flamingo_buying = False
                    purchased = None
                    buying = False
        if vulcano_buying == True:
            buying = True
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    vulcano_owned = True
                    vulcano_buying = False
                    purchased = None
                    buying = False
                    decorations+=1
                elif purchased==False:
                    vulcano_owned = False
                    vulcano_buying = False
                    purchased = None
                    buying = False
        pygame.display.update()
def shop_equipment(event):
    global money
    global wooden_owned, iron_owned, carbon_owned, golden_owned,boat_owned
    can_exit = True
    buying = False
    run = True
    wooden_buying = iron_buying = carbon_buying = golden_buying = boat_buying = False
    outdoor_rect = door.get_rect()
    outdoor_rect.topleft = (10, 480)
    scenery_rect = scenery_button.get_rect()
    scenery_rect.topleft = (65,195)
    fishes_rect = fishes_button.get_rect()
    fishes_rect.topleft = (90,55)
    wooden_rect = wooden_rod.get_rect()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.blit(shop_background, (0, 0))
        if outdoor_rect.collidepoint(pygame.mouse.get_pos()) and buying == False:
                window.blit(door_coll,(10,480))
        else:
                window.blit(door,(10,480))
        if fishes_rect.collidepoint(pygame.mouse.get_pos()) and buying == False:
                window.blit(fishes_button_coll,(90,55))
        else:
                window.blit(fishes_button,(90,55))
        if scenery_rect.collidepoint(pygame.mouse.get_pos()) and buying == False:
                window.blit(scenery_button_coll,(65,195))
        else:
                window.blit(scenery_button,(65,195))
        window.blit(equipment_button_coll,(0,355))
        window.blit(border_shop,(-120,0))
        window.blit(cash,(40,0))
        boat1 = pygame.transform.scale(boat, (165, 96)).convert_alpha()
        if wooden_owned == False:
            window.blit(wooden_rod,(550,105))
            wooden_price = 400
            wooden_price_s = font.render("      400",True,(255,255,255))
            window.blit(wooden_price_s,(575,80))
            window.blit(cash1,(557,65))
        else:
            window.blit(check,(590,140))
        if iron_owned == False:
            window.blit(iron_rod,(760,105))
        else:
            window.blit(check,(790,140))
        if wooden_owned == False:
            window.blit(padlock,(795,145))
        elif iron_owned == False and wooden_owned==True:
            iron_price = 2000
            iron_price_s = font.render("      2000",True,(255,255,255))
            window.blit(iron_price_s,(780,80))
            window.blit(cash1,(762,65))
        if carbon_owned == False:
            window.blit(carbon_rod,(550,290))
        else:
            window.blit(check,(590,330))
        if iron_owned == False:
            window.blit(padlock,(585,330))
        elif carbon_owned == False and iron_owned==True:
            carbon_price = 7000
            carbon_price_s = font.render("     7000",True,(255,255,255))
            window.blit(carbon_price_s,(575,265))
            window.blit(cash1,(553,250))
        if golden_owned == False:
            window.blit(golden_rod,(760,290))
        else:
            window.blit(check,(800,330))
        if carbon_owned == False:
            window.blit(padlock,(795,330))
        elif golden_owned == False and carbon_owned==True:
            golden_price = 16000
            golden_price_s = font.render("     16000",True,(255,255,255))
            window.blit(golden_price_s,(780,265))
            window.blit(cash1,(757,250))
        if boat_owned  == False:
            window.blit(boat1,(640,490))
            boat_price = 2500
            boat_price_s = font.render("      2500",True,(255,255,255))
            window.blit(cash1,(657,445))
            window.blit(boat_price_s,(675,460))
        else:
            window.blit(check,(680,500))
        money_amount = font.render(str(money),True,(0,0,0))
        window.blit(money_amount,(105,21))
        scenery_rect = scenery_button.get_rect()
        scenery_rect.topleft = (65,195)
        fishes_rect = fishes_button.get_rect()
        fishes_rect.topleft = (90,55)
        wooden_rect = wooden_rod.get_rect()
        wooden_rect.topleft = (550,105)
        iron_rect = iron_rod.get_rect()
        iron_rect.topleft = (760,105)
        carbon_rect = carbon_rod.get_rect()
        carbon_rect.topleft = (550,290)
        golden_rect = golden_rod.get_rect()
        golden_rect.topleft = (760,290)
        boat_rect = boat.get_rect()
        boat_rect.topleft = (640,490)
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if outdoor_rect.collidepoint(mouse_pos) and can_exit == True:
                village(event)
            elif scenery_rect.collidepoint(mouse_pos) and buying == False and can_exit == True:
                shop_scenery(event)
            elif fishes_rect.collidepoint(mouse_pos) and buying == False and can_exit == True:
                shop(event)
            elif wooden_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and wooden_owned == False:
                wooden_buying = True
                price = wooden_price
            elif iron_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and wooden_owned == True and iron_owned == False:
                iron_buying = True
                price = iron_price
            elif carbon_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and iron_owned == True and carbon_owned == False:
                carbon_buying = True
                price = carbon_price
            elif golden_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and carbon_owned == True and golden_owned == False:
                golden_buying = True
                price = golden_price
            elif boat_rect.collidepoint(mouse_pos) and buying == False and can_exit == True and boat_owned == False:
                boat_buying = True
                price = boat_price
        if wooden_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    wooden_owned = True
                    wooden_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased == False:
                    wooden_owned = False
                    wooden_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if iron_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    iron_owned = True
                    iron_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased == False:
                    iron_owned = False
                    iron_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if carbon_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    carbon_owned = True
                    carbon_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased == False:
                    carbon_owned = False
                    carbon_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if golden_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    golden_owned = True
                    golden_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased == False:
                    golden_owned = False
                    golden_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        if boat_buying == True:
            buying = True
            can_exit = False
            purchased = buy_function(event,price)
            if purchased is not None:
                if purchased==True:
                    boat_owned = True
                    boat_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
                elif purchased == False:
                    boat_owned = False
                    boat_buying = False
                    purchased = None
                    buying = False
                    can_exit = True
        pygame.display.update()
def buy_function(event,price):
    global money
    window.blit(buy_alert,(300,120))
    not_enough_rect = not_enough.get_rect()
    not_enough_rect.topleft = (300,120)
    price_s = font.render(str(price),True,(0,0,0))
    window.blit(price_s,(532,312))
    mouse_pos = pygame.mouse.get_pos()
    yes = pygame.Rect(314, 350, 60, 60)
    no = pygame.Rect(706, 350, 60, 60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if yes.collidepoint(mouse_pos) and money >= price:
                    money -= price
                    purchased = True
                    return purchased
                elif yes.collidepoint(mouse_pos) and money < price:
                    window.blit(not_enough,(300,180))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    purchased = False
                    return purchased
                elif no.collidepoint(mouse_pos) :
                    purchased = False
                    return purchased
            pygame.display.update()
    return None
def buy_function_f(event,price):
    global money,backpack_slots
    window.blit(buy_alert,(300,120))
    not_enough_rect = not_enough.get_rect()
    not_enough_rect.topleft = (300,120)
    price_s = font.render(str(price),True,(0,0,0))
    window.blit(price_s,(532,312))
    mouse_pos = pygame.mouse.get_pos()
    yes = pygame.Rect(314, 350, 60, 60)
    no = pygame.Rect(706, 350, 60, 60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if yes.collidepoint(mouse_pos) and money >= price and backpack_slots<20:
                    money -= price
                    purchased = True
                    backpack_slots +=1
                    return purchased
                elif yes.collidepoint(mouse_pos) and money >= price and backpack_slots>=20:
                    window.blit(full_backpack,(300,180))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    purchased = False
                    return purchased
                elif yes.collidepoint(mouse_pos) and money < price:
                    window.blit(not_enough,(300,180))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    purchased = False
                    return purchased
                elif no.collidepoint(mouse_pos) :
                    purchased = False
                    return purchased
            pygame.display.update()
    return None  
def lake(event):
    current_image_index = 0
    image_list = []
    display_time = 86
    last_display_time = pygame.time.get_ticks()
    for i in range(1, 52):
        filename = f"ducks_animation/ducks_{i}.png"
        img = pygame.image.load(filename).convert_alpha()
        filename = pygame.transform.scale(img, (111, 50)).convert_alpha()
        image_list.append(filename)
    bamboo_rod1 = pygame.transform.scale(bamboo_rod, (100, 100)).convert_alpha()
    bamboo_rod2 = pygame.transform.scale(bamboo_rod, (45, 45)).convert_alpha()
    wooden_rod1 = pygame.transform.scale(wooden_rod, (100, 100)).convert_alpha()
    wooden_rod2 = pygame.transform.scale(wooden_rod, (45, 45)).convert_alpha()
    iron_rod1 = pygame.transform.scale(iron_rod, (100, 100)).convert_alpha()
    iron_rod2 = pygame.transform.scale(iron_rod, (45, 45)).convert_alpha()
    carbon_rod1 = pygame.transform.scale(carbon_rod, (100, 100)).convert_alpha()
    golden_rod1 = pygame.transform.scale(golden_rod, (100, 100)).convert_alpha()
    window.blit(lake_background, (0, 0))
    if blue_fish_owned == False or pike_owned == False or fat_fish_owned == False or snail_owned == False or frog_owned==False or koi_fish_owned == False or sturgeon_owned == False or piranha_owned == False or boat_owned == False :
        window.blit(padlock, (236, 109))
    window.blit(rod_panel,(0,460))
    current_rod = font.render("Current fishing rod",True,(255,255,255))
    window.blit(current_rod,(10,480))
    run = True
    outdoor_rect = door.get_rect()
    outdoor_rect.topleft = (960, 480)
    padlock_rect = padlock.get_rect()
    padlock_rect.topleft = (236, 109)
    info_rect = info_button.get_rect()
    info_rect.topleft = (310,510)
    start_rect = start_fishing.get_rect()
    start_rect.topleft = (360,290)
    to_sea = pygame.Rect(70, 105, 175, 60)
    if wooden_owned == False:
        window.blit(bamboo_rod1,(75,500))
    elif wooden_owned == True and iron_owned == False:
        window.blit(wooden_rod1,(75,500))
    elif iron_owned == True and carbon_owned == False:
        window.blit(iron_rod1,(75,500))
    elif carbon_owned == True and golden_owned == False:
        window.blit(carbon_rod1,(75,500))
    elif golden_owned == True:
        window.blit(golden_rod1,(75,500))
    while run:
        window.blit(image_list[current_image_index], (380, 338))
        current_time = pygame.time.get_ticks()
        if current_time - last_display_time >= display_time:
            current_image_index = (current_image_index + 1) % len(image_list)
            last_display_time = current_time
        if to_sea.collidepoint(pygame.mouse.get_pos()) and blue_fish_owned == True and pike_owned == True and fat_fish_owned == True and snail_owned == True and frog_owned==True and koi_fish_owned == True and sturgeon_owned == True and piranha_owned == True and boat_owned == True:
            window.blit(lake_back1,(0,0))  
            window.blit(rod_panel,(0,460))
            window.blit(current_rod,(10,480))
            window.blit(image_list[current_image_index], (380, 338))
            if wooden_owned == False:
                window.blit(bamboo_rod1,(75,500))
            elif wooden_owned == True and iron_owned == False:
                window.blit(wooden_rod1,(75,500))
            elif iron_owned == True and carbon_owned == False:
                window.blit(iron_rod1,(75,500))
            elif carbon_owned == True and golden_owned == False:
                window.blit(carbon_rod1,(75,500))
            elif golden_owned == True:
                window.blit(golden_rod1,(75,500))
        elif blue_fish_owned == True and pike_owned == True and fat_fish_owned == True and snail_owned == True and frog_owned==True and koi_fish_owned == True and sturgeon_owned == True and piranha_owned == True and boat_owned == True:
            window.blit(lake_background,(0,0))  
            window.blit(rod_panel,(0,460))
            window.blit(current_rod,(10,480))
            window.blit(image_list[current_image_index], (380, 338))
            if wooden_owned == False:
                window.blit(bamboo_rod1,(75,500))
            elif wooden_owned == True and iron_owned == False:
                window.blit(wooden_rod1,(75,500))
            elif iron_owned == True and carbon_owned == False:
                window.blit(iron_rod1,(75,500))
            elif carbon_owned == True and golden_owned == False:
                window.blit(carbon_rod1,(75,500))
            elif golden_owned == True:
                window.blit(golden_rod1,(75,500))
            if info_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(fishes_info,(400,419))
                window.blit(bamboo_rod2,(410,430))
                bamboo_info = font.render("Common fishes", True, (44, 150, 72))
                window.blit(bamboo_info, (490, 442))
                window.blit(wooden_rod2,(410,485))
                wooden_info = font.render("Rare fishes", True, (64, 92, 184))
                window.blit(wooden_info,(500,497))
                window.blit(iron_rod2,(410,540))
                iron_info = font.render("Super rare fishes", True, (109, 56, 194))
                window.blit(iron_info,(467,551))
            else:
                window.blit(fishes_info_cover,(401,411))
        if info_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(info_button_coll,(310,510))
        else:
                window.blit(info_button,(310,510))
        if outdoor_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(door_coll,(960,480))
        else:
                window.blit(door,(960,480))
        if start_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(start_fishing_coll,(360,290))
        else:
                window.blit(start_fishing,(360,290))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if padlock_rect.collidepoint(pygame.mouse.get_pos()) and (blue_fish_owned == False or pike_owned == False or fat_fish_owned == False or snail_owned == False or frog_owned==False or koi_fish_owned == False or sturgeon_owned == False or piranha_owned == False or boat_owned == False ):
                padlock_info = font.render("Blocked", True, (255, 0, 0))
                padlock_info2 = font.render("To unlock the sea,", True, (255, 255, 255))
                padlock_info3 = font.render("you must catch all", True, (255, 255, 255))
                padlock_info4 = font.render("spacies of fish from", True, (255, 255, 255))
                padlock_info5 = font.render("the lake and buy a boat.", True, (255, 255, 255))
                window.blit(blocked_info,(300,20))
                window.blit(padlock_info, (420, 55))
                window.blit(padlock_info2, (360, 85))
                window.blit(padlock_info3, (360, 115))
                window.blit(padlock_info4, (342, 145))
                window.blit(padlock_info5, (325, 175))
            else:
                window.blit(blocked_cover,(282,1))
            if info_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(fishes_info,(400,419))
                window.blit(bamboo_rod2,(410,430))
                bamboo_info = font.render("Common fishes", True, (44, 150, 72))
                window.blit(bamboo_info, (490, 442))
                window.blit(wooden_rod2,(410,485))
                wooden_info = font.render("Rare fishes", True, (64, 92, 184))
                window.blit(wooden_info,(500,497))
                window.blit(iron_rod2,(410,540))
                iron_info = font.render("Super rare fishes", True, (109, 56, 194))
                window.blit(iron_info,(467,551))
            else:
                window.blit(fishes_info_cover,(401,411))
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if outdoor_rect.collidepoint(mouse_pos):
                    village(event)
                if start_rect.collidepoint(mouse_pos):
                    lake_fishing(event)
                if to_sea.collidepoint(mouse_pos) and blue_fish_owned == True and pike_owned == True and fat_fish_owned == True and snail_owned == True and frog_owned==True and koi_fish_owned == True and sturgeon_owned == True and piranha_owned == True and boat_owned == True:
                    sea(event)
        pygame.display.update()
def lake_fishing(event):
    global backpack_slots,catched
    global blue_fish_owned,pike_owned,fat_fish_owned,snail_owned,frog_owned,koi_fish_owned,sturgeon_owned,piranha_owned
    global blue_fish_amount,pike_amount,fat_fish_amount,snail_amount,frog_amount,koi_fish_amount,sturgeon_amount,piranha_amount
    image_list_f = []
    image_list_e = []
    filename = f"buttons/excl1.png"
    img = pygame.image.load(filename)
    image_list_e.append(img)
    filename = f"buttons/excl2.png"
    img = pygame.image.load(filename)
    image_list_e.append(img)
    for i in range(1, 18):
        filename = f"pond_fishing/pond{i}.jpg"
        img = pygame.image.load(filename)
        img = pygame.transform.scale(img, (414, 600)).convert_alpha()
        image_list_f.append(img)
    current_image_index = 0
    current_image_index_e = 0
    display_time = 90
    display_time_e = 600
    last_display_time = last_display_time_e = pygame.time.get_ticks()
    run = True
    fishing = False
    window.blit(fishing_lake_back,(0,0))
    window.blit(pond1,(400,0))
    window.blit(fishing_info,(860,-127))
    window.blit(backpack, (850, -20))
    backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
    window.blit(backpack_info, (985, 43))
    door_rect = door.get_rect()
    door_rect.topleft = (960, 480)
    info_rect = info_button.get_rect()
    info_rect.topleft = (20,20)
    start1_rect = start1.get_rect()
    start1_rect.topleft = (420, 250)
    cancel_rect = cancel_1.get_rect()
    cancel_rect.topleft = (485,275)
    to_backpack_rect = to_backpack.get_rect()
    to_backpack_rect.topleft = (377,275)
    release_rect = release.get_rect()
    release_rect.topleft = (590,275)
    info_count = 0
    catching = False
    no_catching = False
    backpack_code = 0 
    while run:
        if info_rect.collidepoint(pygame.mouse.get_pos()) and fishing == False and catching == False and no_catching == False:
                window.blit(info_button_coll,(20,20))
        elif fishing == False and catching == False and no_catching == False:
                window.blit(info_button,(20,20))
        if door_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(door_coll,(960,480))
        else:
                window.blit(door,(960,480))
        if start1_rect.collidepoint(pygame.mouse.get_pos()) and fishing == False and catching == False and no_catching == False:
                window.blit(start1_coll,(420, 250))
        elif fishing == False and catching == False and no_catching == False:
                window.blit(start1,(420, 250))
        if fishing == True:
            if info_count == 1 and no_catching==False:
                start_w = pygame.time.get_ticks()
                window.blit(fishing_lake_back,(0,0))
                window.blit(door, (960, 480))
                info_count = 0
            window.blit(image_list_f[current_image_index], (400, 0))
            current_time = pygame.time.get_ticks()
            if current_time - last_display_time >= display_time:
                current_image_index = (current_image_index + 1) % len(image_list_f)
                last_display_time = current_time
                if current_image_index == 16:
                    current_image_index = 12
                    display_time = 350
            time_w = random.randint(7000, 20000)
            time_s = time_w + 2000
            elapsed_time = current_time-start_w
            if elapsed_time >= time_w:
                window.blit(image_list_e[current_image_index_e], (440, 60))
                current_time_e = pygame.time.get_ticks()
                if current_time_e - last_display_time_e >= display_time_e:
                    current_image_index_e = (current_image_index_e + 1) % len(image_list_e)
                    last_display_time_e = current_time_e
                if elapsed_time>= time_w and elapsed_time < time_s:
                    catching = True
                elif elapsed_time>time_s:
                    fishing = False
                    no_catching = True
                    if no_catching == True:
                        info_count =1
                        window.blit(fishing_lake_back,(0,0))
                        window.blit(pond1,(400,0))
                        window.blit(door, (960, 480))
                        window.blit(start1, (420, 250))
                        window.blit(fishes_info,(360,160))
                        window.blit(cancel_1,(485,275))
                        no_catch_info = font.render("You failed. Try again :(", True, (255, 255, 255))
                        window.blit(no_catch_info, (377,220))
                    display_time = 90
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if info_rect.collidepoint(pygame.mouse.get_pos()) and fishing == False and no_catching==False and catching==False:
                window.blit(fishing_info,(90,5))
                fishing_info1 = font.render("Press START to begin fishing.", True, (255, 255, 255))
                fishing_info2 = font.render("Wait a moment and then press", True, (255, 255, 255))
                fishing_info3 = font.render("the SPACEBAR when you see", True, (255, 255, 255))
                fishing_info4 = font.render("the '!' sign next to the float.", True, (255, 255, 255))
                window.blit(fishing_info1, (130, 65))
                window.blit(fishing_info2, (130, 95))
                window.blit(fishing_info3, (135, 125))
                window.blit(fishing_info4, (145, 155))
                info_count = 0
            elif fishing == False and info_count == 0:
                info_count += 1
                window.blit(fishing_lake_back,(0,0))
                window.blit(pond1,(400,0))
                window.blit(door, (960, 480))
                window.blit(info_button,(20,20))
                window.blit(start1, (420, 250))
                window.blit(fishing_info,(860,-127))
                window.blit(backpack, (850, -20))
                backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                window.blit(backpack_info, (985, 43))
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if door_rect.collidepoint(mouse_pos):
                    lake(event)
                elif start1_rect.collidepoint(mouse_pos) and (catching == False and no_catching == False and fishing == False):
                    display_time = 90
                    current_image_index=0
                    fishing = True
                if no_catching == True:
                    if cancel_rect.collidepoint(mouse_pos):
                        no_catching = False
                        fishing = False
                        catching = False
                        window.blit(fishing_lake_back,(0,0))
                        window.blit(pond1,(400,0))
                        window.blit(door, (960, 480))
                        window.blit(info_button,(20,20))
                        window.blit(start1, (420, 250))
                        window.blit(fishing_info,(860,-127))
                        window.blit(backpack, (850, -20))
                        backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                        window.blit(backpack_info, (985, 43))
                if catching == True:
                    catched+=1
                    if to_backpack_rect.collidepoint(mouse_pos) and backpack_slots<20:
                        no_catching = False
                        fishing = False
                        catching = False
                        backpack_slots+=1
                        if backpack_code==1:
                            blue_fish_owned = True
                            blue_fish_amount +=1
                        elif backpack_code==2:
                            pike_owned = True
                            pike_amount +=1
                        elif backpack_code==3:
                            fat_fish_owned = True
                            fat_fish_amount +=1
                        elif backpack_code==4:
                            snail_owned = True
                            snail_amount +=1
                        elif backpack_code==5:
                            frog_owned = True
                            frog_amount +=1
                        elif backpack_code==6:
                            koi_fish_owned = True
                            koi_fish_amount +=1
                        elif backpack_code==7:
                            sturgeon_owned = True
                            sturgeon_amount +=1
                        elif backpack_code==8:
                            piranha_owned = True
                            piranha_amount +=1
                        window.blit(fishing_lake_back,(0,0))
                        window.blit(pond1,(400,0))
                        window.blit(door, (960, 480))
                        window.blit(info_button,(20,20))
                        window.blit(start1, (420, 250))
                        window.blit(fishing_info,(860,-127))
                        window.blit(backpack, (850, -20))
                        backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                        window.blit(backpack_info, (985, 43))
                    elif release_rect.collidepoint(mouse_pos):
                        no_catching = False
                        fishing = False
                        catching = False
                        window.blit(fishing_lake_back,(0,0))
                        window.blit(pond1,(400,0))
                        window.blit(door, (960, 480))
                        window.blit(info_button,(20,20))
                        window.blit(start1, (420, 250))
                        window.blit(fishing_info,(860,-127))
                        window.blit(backpack, (850, -20))
                        backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                        window.blit(backpack_info, (985, 43))
                    elif to_backpack_rect.collidepoint(pygame.mouse.get_pos()) and backpack_slots>=20:
                        backpack_full = font.render("Your backpack is full!", True, (255, 0,0))
                        window.blit(backpack_full, (385, 350))
            if catching == True:
                if keys[pygame.K_SPACE] and fishing == True:
                    fishing = False
                    info_count =1
                    window.blit(fishing_lake_back,(0,0))
                    window.blit(pond1,(400,0))
                    window.blit(door, (960, 480))
                    window.blit(fishing_info,(860,-127))
                    window.blit(backpack, (850, -20))
                    backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                    window.blit(backpack_info, (985, 43))
                    window.blit(start1, (420, 250))
                    window.blit(fishes_info,(360,160))
                    window.blit(to_backpack,(377,275))
                    window.blit(release,(590,275))
                    caught_info = font.render("You caught", True, (255, 255, 255))
                    rand_num = random.random()
                    if wooden_owned == False:
                        window.blit(caught_info,(444,176))
                        if rand_num<0.96:
                            window.blit(blue_fish,(470,200))
                            backpack_code = 1
                        elif rand_num<0.99:
                            window.blit(pike,(460,200))
                            backpack_code = 2
                        else:
                            window.blit(fat_fish,(470,200))
                            backpack_code = 3
                    elif wooden_owned == True and iron_owned == False:
                        window.blit(caught_info,(444,176))
                        if rand_num<0.91:
                            window.blit(blue_fish,(470,200))
                            backpack_code = 1
                        elif rand_num<0.96:
                            window.blit(pike,(460,200))
                            backpack_code = 2
                        elif rand_num<0.98:
                            window.blit(fat_fish,(470,200))
                            backpack_code = 3
                        elif rand_num<0.995:
                            window.blit(snail,(470,200))
                            backpack_code = 4
                        else:
                            window.blit(frog,(470,200))
                            backpack_code = 5
                    else:
                        window.blit(caught_info,(444,176))
                        if rand_num<0.83:
                            window.blit(blue_fish,(470,200))
                            backpack_code = 1
                        elif rand_num<0.90:
                            window.blit(pike,(460,200))
                            backpack_code = 2
                        elif rand_num<0.95:
                            window.blit(fat_fish,(470,200))
                            backpack_code = 3
                        elif rand_num<0.98:
                            window.blit(snail,(470,200))
                            backpack_code = 4
                        elif rand_num<0.99:
                            window.blit(frog,(470,200))
                            backpack_code = 5
                        elif rand_num<0.995:
                            window.blit(koi_fish,(470,200))
                            backpack_code = 6
                        elif rand_num<0.998:
                            window.blit(sturgeon,(470,200))
                            backpack_code = 7
                        else:
                            window.blit(piranha,(470,200))
                            backpack_code = 8    
                        
            if keys[pygame.K_SPACE] and fishing == True and elapsed_time < time_w:
                fishing = False
                info_count =1
                window.blit(fishing_lake_back,(0,0))
                window.blit(pond1,(400,0))
                window.blit(door, (960, 480))
                window.blit(start1, (420, 250))
                window.blit(fishes_info,(360,160))
                window.blit(cancel_1,(485,275))
                no_catch_info = font.render("You failed. Try again :(", True, (255, 255, 255))
                window.blit(no_catch_info, (375,220))
                display_time = 90
                catching = False
                no_catching = True
                        
                    
        pygame.display.update()
def sea(event):
    iron_rod1 = pygame.transform.scale(iron_rod, (100, 100)).convert_alpha()
    iron_rod2 = pygame.transform.scale(iron_rod, (45, 45)).convert_alpha()
    carbon_rod1 = pygame.transform.scale(carbon_rod, (100, 100)).convert_alpha()
    carbon_rod2 = pygame.transform.scale(carbon_rod, (45, 45)).convert_alpha()
    golden_rod1 = pygame.transform.scale(golden_rod, (100, 100)).convert_alpha()
    golden_rod2 = pygame.transform.scale(golden_rod, (45, 45)).convert_alpha()
    window.blit(sea_back, (0, 0))
    window.blit(rod_panel,(0,460))
    window.blit(info_button,(310,510))
    window.blit(start_fishing,(360,290))
    current_image_index = 107
    count = 1350
    image_list = []
    display_time = 62
    last_display_time = pygame.time.get_ticks()
    for i in range(1, 109):
        filename = f"shark_animation/shark_{i}.png"
        img = pygame.image.load(filename).convert_alpha()
        image_list.append(img)
    if iron_owned == True and carbon_owned == False:
        window.blit(iron_rod1,(75,500))
    elif carbon_owned == True and golden_owned == False:
        window.blit(carbon_rod1,(75,500))
    elif golden_owned == True:
        window.blit(golden_rod1,(75,500))
    current_rod = font.render("Current fishing rod",True,(255,255,255))
    window.blit(current_rod,(10,480))
    run = True
    outdoor_rect = door.get_rect()
    outdoor_rect.topleft = (960, 480)
    info_rect = info_button.get_rect()
    info_rect.topleft = (310,510)
    start_rect = start_fishing.get_rect()
    start_rect.topleft = (360,290)
    to_lake = pygame.Rect(865, 85, 205, 50)
    while run:
        current_time = pygame.time.get_ticks()
        if current_time - last_display_time >= display_time and current_image_index != 107:
            current_image_index = (current_image_index + 1) % len(image_list)
            last_display_time = current_time
        if current_image_index == 107:
            count +=0.1
        if count > 1500:
            current_image_index = 0
            count = 0
        if to_lake.collidepoint(pygame.mouse.get_pos()):
            window.blit(sea_back1, (0, 0))
            window.blit(rod_panel,(0,460))
            window.blit(info_button,(310,510))
            window.blit(start_fishing,(360,290))
            window.blit(image_list[current_image_index], (0, 392))
            if iron_owned == True and carbon_owned == False:
                window.blit(iron_rod1,(75,500))
            elif carbon_owned == True and golden_owned == False:
                window.blit(carbon_rod1,(75,500))
            elif golden_owned == True:
                window.blit(golden_rod1,(75,500))
            current_rod = font.render("Current fishing rod",True,(255,255,255))
            window.blit(current_rod,(10,480))
        else:
            window.blit(sea_back, (0, 0))
            window.blit(rod_panel,(0,460))
            window.blit(info_button,(310,510))
            window.blit(start_fishing,(360,290))
            window.blit(image_list[current_image_index], (0, 392))
            if iron_owned == True and carbon_owned == False:
                window.blit(iron_rod1,(75,500))
            elif carbon_owned == True and golden_owned == False:
                window.blit(carbon_rod1,(75,500))
            elif golden_owned == True:
                window.blit(golden_rod1,(75,500))
            current_rod = font.render("Current fishing rod",True,(255,255,255))
            window.blit(current_rod,(10,480))
            if info_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(fishes_info,(400,419))
                window.blit(iron_rod2,(410,430))
                bamboo_info = font.render("Common fishes", True, (44, 150, 72))
                window.blit(bamboo_info, (490, 442))
                window.blit(carbon_rod2,(410,485))
                wooden_info = font.render("Rare fishes", True, (64, 92, 184))
                window.blit(wooden_info,(500,497))
                window.blit(golden_rod2,(410,540))
                iron_info = font.render("Super rare fishes", True, (109, 56, 194))
                window.blit(iron_info,(467,551))
            else:
                window.blit(sea_cover,(397,391))
        if info_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(info_button_coll,(310,510))
        else:
                window.blit(info_button,(310,510))
        if outdoor_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(door_coll,(960,480))
        else:
                window.blit(door,(960,480))
        if start_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(start_fishing_coll,(360,290))
        else:
                window.blit(start_fishing,(360,290))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if info_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(fishes_info,(400,419))
                window.blit(iron_rod2,(410,430))
                bamboo_info = font.render("Common fishes", True, (44, 150, 72))
                window.blit(bamboo_info, (490, 442))
                window.blit(carbon_rod2,(410,485))
                wooden_info = font.render("Rare fishes", True, (64, 92, 184))
                window.blit(wooden_info,(500,497))
                window.blit(golden_rod2,(410,540))
                iron_info = font.render("Super rare fishes", True, (109, 56, 194))
                window.blit(iron_info,(467,551))
            else:
                window.blit(sea_cover,(397,391))
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if outdoor_rect.collidepoint(mouse_pos):
                    village(event)
                elif start_rect.collidepoint(mouse_pos):
                    sea_fishing(event)
                elif to_lake.collidepoint(mouse_pos):
                    lake(event)
        pygame.display.update()
def sea_fishing(event):
    global backpack_slots,catched
    global prawn_owned,tiger_fish_owned,crab_owned,sword_fish_owned,turtle_owned,shark_owned,light_fish_owned,zombie_fish_owned,nautilus_owned
    global prawn_amount,tiger_fish_amount,crab_amount,sword_fish_amount,turtle_amount,shark_amount,light_fish_amount,zombie_fish_amount,nautilus_amount
    image_list_f = []
    image_list_e = []
    filename = f"buttons/excl1.png"
    img = pygame.image.load(filename)
    image_list_e.append(img)
    filename = f"buttons/excl2.png"
    img = pygame.image.load(filename)
    image_list_e.append(img)
    for i in range(1, 22):
        filename = f"sea_fishing/sea{i}.png"
        img = pygame.image.load(filename)
        image_list_f.append(img)
    current_image_index = 0
    current_image_index_e = 0
    display_time = 90
    display_time_e = 600
    last_display_time = last_display_time_e = pygame.time.get_ticks()
    run = True
    fishing = False
    window.blit(sea_fishing_back,(0,0))
    window.blit(sea1,(330,0))
    window.blit(info_button,(20,20))
    window.blit(start1, (420, 250))
    window.blit(fishing_info,(860,-127))
    window.blit(backpack, (850, -20))
    backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
    window.blit(backpack_info, (985, 43))
    door_rect = door.get_rect()
    door_rect.topleft = (960, 480)
    info_rect = info_button.get_rect()
    info_rect.topleft = (20,20)
    start1_rect = start1.get_rect()
    start1_rect.topleft = (420, 250)
    cancel_rect = cancel_1.get_rect()
    cancel_rect.topleft = (485,275)
    to_backpack_rect = to_backpack.get_rect()
    to_backpack_rect.topleft = (377,275)
    release_rect = release.get_rect()
    release_rect.topleft = (590,275)
    info_count = 0
    catching = False
    no_catching = False
    backpack_code = 0
    
    while run:
        if info_rect.collidepoint(pygame.mouse.get_pos()) and fishing == False and catching == False and no_catching == False:
                window.blit(info_button_coll,(20,20))
        elif fishing == False and catching == False and no_catching == False:
                window.blit(info_button,(20,20))
        if door_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(door_coll,(960,480))
        else:
                window.blit(door,(960,480))
        if start1_rect.collidepoint(pygame.mouse.get_pos()) and fishing == False and catching == False and no_catching == False:
                window.blit(start1_coll,(420, 250))
        elif fishing == False and catching == False and no_catching == False:
                window.blit(start1,(420, 250))
        if fishing == True:
            if info_count == 1 and no_catching==False:
                start_w = pygame.time.get_ticks()
                window.blit(sea_fishing_back,(0,0))
                window.blit(door, (960, 480))
                info_count = 0
            window.blit(image_list_f[current_image_index], (330, 0))
            current_time = pygame.time.get_ticks()
            if current_time - last_display_time >= display_time:
                current_image_index = (current_image_index + 1) % len(image_list_f)
                last_display_time = current_time
                if current_image_index == 20:
                    current_image_index = 15
                    display_time = 350
            time_w = random.randint(7000, 20000)
            time_s = time_w + 2000
            elapsed_time = current_time-start_w
            if elapsed_time >= time_w:
                window.blit(image_list_e[current_image_index_e], (530, 2))
                current_time_e = pygame.time.get_ticks()
                if current_time_e - last_display_time_e >= display_time_e:
                    current_image_index_e = (current_image_index_e + 1) % len(image_list_e)
                    last_display_time_e = current_time_e
                if elapsed_time>= time_w and elapsed_time < time_s:
                    catching = True
                elif elapsed_time>time_s:
                    fishing = False
                    no_catching = True
                    if no_catching == True:
                        info_count =1
                        window.blit(sea_fishing_back,(0,0))
                        window.blit(sea1,(330,0))
                        window.blit(door, (960, 480))
                        window.blit(start1, (420, 250))
                        window.blit(fishes_info,(360,160))
                        window.blit(cancel_1,(485,275))
                        no_catch_info = font.render("You failed. Try again :(", True, (255, 255, 255))
                        window.blit(no_catch_info, (377,220))
                    display_time = 90
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if info_rect.collidepoint(pygame.mouse.get_pos()) and fishing == False and no_catching==False and catching==False:
                window.blit(fishing_info,(90,5))
                fishing_info1 = font.render("Press START to begin fishing.", True, (255, 255, 255))
                fishing_info2 = font.render("Wait a moment and then press", True, (255, 255, 255))
                fishing_info3 = font.render("the SPACEBAR when you see", True, (255, 255, 255))
                fishing_info4 = font.render("the '!' sign next to the float.", True, (255, 255, 255))
                window.blit(fishing_info1, (130, 65))
                window.blit(fishing_info2, (130, 95))
                window.blit(fishing_info3, (135, 125))
                window.blit(fishing_info4, (145, 155))
                info_count = 0
            elif fishing == False and info_count == 0:
                info_count += 1
                window.blit(sea_fishing_back,(0,0))
                window.blit(sea1,(330,0))
                window.blit(door, (960, 480))
                window.blit(info_button,(20,20))
                window.blit(start1, (420, 250))
                window.blit(fishing_info,(860,-127))
                window.blit(backpack, (850, -20))
                backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                window.blit(backpack_info, (985, 43))
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if door_rect.collidepoint(mouse_pos):
                    sea(event)
                elif start1_rect.collidepoint(mouse_pos) and (catching == False and no_catching == False and fishing == False):
                    display_time = 90
                    current_image_index=0
                    fishing = True
                if no_catching == True:
                    if cancel_rect.collidepoint(mouse_pos):
                        no_catching = False
                        fishing = False
                        catching = False
                        window.blit(sea_fishing_back,(0,0))
                        window.blit(sea1,(330,0))
                        window.blit(door, (960, 480))
                        window.blit(info_button,(20,20))
                        window.blit(start1, (420, 250))
                        window.blit(fishing_info,(860,-127))
                        window.blit(backpack, (850, -20))
                        backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                        window.blit(backpack_info, (985, 43))
                if catching == True:
                    catched+=1
                    if to_backpack_rect.collidepoint(mouse_pos) and backpack_slots<20:
                        no_catching = False
                        fishing = False
                        catching = False
                        backpack_slots+=1
                        if backpack_code==1:
                            prawn_owned = True
                            prawn_amount +=1
                        elif backpack_code==2:
                            tiger_fish_owned = True
                            tiger_fish_amount +=1
                        elif backpack_code==3:
                            crab_owned = True
                            crab_amount +=1
                        elif backpack_code==4:
                            sword_fish_owned = True
                            sword_fish_amount +=1
                        elif backpack_code==5:
                            turtle_owned = True
                            turtle_amount +=1
                        elif backpack_code==6:
                            shark_owned = True
                            shark_amount +=1
                        elif backpack_code==7:
                            light_fish_owned = True
                            light_fish_amount +=1
                        elif backpack_code==8:
                            nautilus_owned = True
                            nautilus_amount +=1
                        elif backpack_code==9:
                            zombie_fish_owned = True
                            zombie_fish_amount +=1
                        window.blit(sea_fishing_back,(0,0))
                        window.blit(sea1,(330,0))
                        window.blit(door, (960, 480))
                        window.blit(info_button,(20,20))
                        window.blit(start1, (420, 250))
                        window.blit(fishing_info,(860,-127))
                        window.blit(backpack, (850, -20))
                        backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                        window.blit(backpack_info, (985, 43))
                    elif release_rect.collidepoint(mouse_pos):
                        no_catching = False
                        fishing = False
                        catching = False
                        window.blit(sea_fishing_back,(0,0))
                        window.blit(sea1,(330,0))
                        window.blit(door, (960, 480))
                        window.blit(info_button,(20,20))
                        window.blit(start1, (420, 250))
                        window.blit(fishing_info,(860,-127))
                        window.blit(backpack, (850, -20))
                        backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                        window.blit(backpack_info, (985, 43))
                    elif to_backpack_rect.collidepoint(pygame.mouse.get_pos()) and backpack_slots>=20:
                        backpack_full = font.render("Your backpack is full!", True, (255, 0,0))
                        window.blit(backpack_full, (385, 350))
            if catching == True:
                if keys[pygame.K_SPACE] and fishing == True:
                    fishing = False
                    info_count =1
                    window.blit(sea_fishing_back,(0,0))
                    window.blit(sea1,(330,0))
                    window.blit(door, (960, 480))
                    window.blit(fishing_info,(860,-127))
                    window.blit(backpack, (850, -20))
                    backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
                    window.blit(backpack_info, (985, 43))
                    window.blit(start1, (420, 250))
                    window.blit(fishes_info,(360,160))
                    window.blit(to_backpack,(377,275))
                    window.blit(release,(590,275))
                    caught_info = font.render("You caught", True, (255, 255, 255))
                    rand_num = random.random()
                    if carbon_owned == False:
                        window.blit(caught_info,(444,176))
                        if rand_num<0.96:
                            window.blit(prawn,(470,200))
                            backpack_code = 1
                        elif rand_num<0.99:
                            window.blit(tiger_fish,(475,200))
                            backpack_code = 2
                        else:
                            window.blit(crab,(470,200))
                            backpack_code = 3
                    elif carbon_owned == True and golden_owned == False:
                        window.blit(caught_info,(444,176))
                        if rand_num<0.855:
                            window.blit(prawn,(470,200))
                            backpack_code = 1
                        elif rand_num<0.92:
                            window.blit(tiger_fish,(475,200))
                            backpack_code = 2
                        elif rand_num<0.96:
                            window.blit(crab,(470,200))
                            backpack_code = 3
                        elif rand_num<0.985:
                            window.blit(sword_fish,(455,200))
                            backpack_code = 4
                        elif rand_num<0.995:
                            window.blit(turtle,(470,200))
                            backpack_code = 5
                        else:
                            window.blit(shark,(458,200))
                            backpack_code = 6
                    elif golden_owned == True:
                        window.blit(caught_info,(444,176))
                        if rand_num<0.695:
                            window.blit(prawn,(470,200))
                            backpack_code = 1
                        elif rand_num<0.815:
                            window.blit(tiger_fish,(475,200))
                            backpack_code = 2
                        elif rand_num<0.895:
                            window.blit(crab,(470,200))
                            backpack_code = 3
                        elif rand_num<0.945:
                            window.blit(sword_fish,(455,200))
                            backpack_code = 4
                        elif rand_num<0.975:
                            window.blit(turtle,(470,200))
                            backpack_code = 5
                        elif rand_num<0.99:
                            window.blit(shark,(458,200))
                            backpack_code = 6
                        elif rand_num<0.995:
                            window.blit(light_fish,(470,200))
                            backpack_code = 7
                        elif rand_num<0.998:
                            window.blit(nautilus,(470,200))
                            backpack_code = 8
                        else:
                            window.blit(zombie_fish,(470,200))
                            backpack_code = 9    
                        
            if keys[pygame.K_SPACE] and fishing == True and elapsed_time < time_w:
                fishing = False
                info_count =1
                window.blit(sea_fishing_back,(0,0))
                window.blit(sea1,(330,0))
                window.blit(door, (960, 480))
                window.blit(start1, (420, 250))
                window.blit(fishes_info,(360,160))
                window.blit(cancel_1,(485,275))
                no_catch_info = font.render("You failed. Try again :(", True, (255, 255, 255))
                window.blit(no_catch_info, (375,220))
                display_time = 90
                catching = False
                no_catching = True
                        
                    
        pygame.display.update()  
def fishmarket(event):
    global blue_fish_in,pike_in,fat_fish_in,snail_in,frog_in,koi_in,sturgeon_in,piranha_in,prawn_in,tiger_in,crab_in,sword_in,turtle_in,shark_in,light_in,nautilus_in,zombie_in
    global blue_fish_amount,pike_amount,fat_fish_amount,snail_amount,frog_amount,koi_fish_amount,sturgeon_amount,piranha_amount
    global prawn_amount,tiger_fish_amount,crab_amount,sword_fish_amount,turtle_amount,shark_amount,light_fish_amount,zombie_fish_amount,nautilus_amount
    global fightfish_amount,clownfish_amount,starfish_amount,jelly_amount,lionfish_amount,tang_amount,ray_amount,octopus_amount,seahorse_amount
    global fightfish_in,clownfish_in,starfish_in,jelly_in,lionfish_in,tang_in,ray_in,octopus_in,seahorse_in
    global money,backpack_slots,in_sum,total_money
    seahorse1 = pygame.transform.scale(seahorse, (67, 90)).convert_alpha()
    blue_fish_show = 0
    pike_show = 0
    fat_fish_show = 0
    snail_show = 0
    frog_show = 0
    koi_show = 0
    sturgeon_show = 0
    piranha_show = 0
    prawn_show = 0
    tiger_show = 0
    crab_show = 0
    sword_show = 0
    turtle_show = 0
    shark_show = 0
    light_show = 0
    nautilus_show = 0
    zombie_show = 0
    fight_show = 0
    clown_show = 0
    star_show = 0
    jelly_show = 0
    lion_show = 0
    tang_show = 0
    ray_show = 0
    octopus_show = 0
    seahorse_show = 0
    points = [(140,100),(270,100),(400,100),(530,100),(660,100),(790,100),(140,200),(270,200),(400,200),(530,200),(660,200),(790,200),(140,300),(270,300),(400,300),(530,300),(660,300),(790,300),(140,400),(270,400),(400,400),(530,400),(660,400),(790,400),(140,500),(270,500),(400,500)]
    a_point = 0
    buying = False
    blue_buying = False
    pike_buying = False
    fat_buying = False
    snail_buying = False
    frog_buying = False
    koi_buying = False
    sturgeon_buying = False
    piranha_buying = False
    prawn_buying = False
    tiger_buying = False
    crab_buying = False
    sword_buying = False
    turtle_buying = False
    shark_buying = False
    light_buying = False
    nautilus_buying = False
    zombie_buying = False
    fight_buying = False
    clown_buying = False
    star_buying = False
    jelly_buying = False
    lion_buying = False
    tang_buying = False
    ray_buying = False
    octopus_buying = False
    seahorse_buying = False
    amount = 1
    run = True
    function_f = False
    result = False
    result_x = False
    mouse_pos = pygame.mouse.get_pos()
    outdoor_rect = door.get_rect()
    outdoor_rect.topleft = (10, 480)
    blue_rect = blue_fish.get_rect()
    pike_rect = pike.get_rect()
    fat_rect = fat_fish.get_rect()
    snail_rect = snail.get_rect()
    frog_rect = frog.get_rect()
    koi_rect = koi_fish.get_rect()
    sturgeon_rect = sturgeon.get_rect()
    piranha_rect = piranha.get_rect()
    prawn_rect = prawn.get_rect()
    tiger_rect = tiger_fish.get_rect()
    crab_rect = crab.get_rect()
    sword_rect = sword_fish.get_rect()
    turtle_rect = turtle.get_rect()
    shark_rect = shark.get_rect()
    light_rect = light_fish.get_rect()
    nautilus_rect = nautilus.get_rect()
    zombie_rect = zombie_fish.get_rect()
    fight_rect = fightfish.get_rect()
    clown_rect = clownfish.get_rect()
    star_rect = starfish.get_rect()
    jelly_rect = jelly.get_rect()
    lion_rect = lionfish.get_rect()
    tang_rect = tang.get_rect()
    ray_rect = ray.get_rect()
    octopus_rect = octopus.get_rect()
    seahorse_rect = seahorse.get_rect()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        window.blit(fishmarket_back, (0, 0))
        if outdoor_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(door_coll,(10,480))
        else:
                window.blit(door,(10,480))
        window.blit(border_shop,(-120,0))
        window.blit(cash,(40,0))
        window.blit(backpack, (790, 475))
        backpack_info = font.render(str(backpack_slots)+"/20", True, (255, 255, 255))
        window.blit(backpack_info, (918, 538))
        if prawn_amount==tiger_fish_amount==crab_amount==sword_fish_amount==turtle_amount==shark_amount==light_fish_amount==zombie_fish_amount==nautilus_amount==blue_fish_amount==pike_amount==fat_fish_amount==snail_amount==frog_amount==koi_fish_amount==sturgeon_amount==piranha_amount==fightfish_amount==clownfish_amount==starfish_amount==jelly_amount==lionfish_amount==tang_amount==ray_amount==octopus_amount==seahorse_amount==0 or prawn_amount+tiger_fish_amount+crab_amount+sword_fish_amount+turtle_amount+shark_amount+light_fish_amount+zombie_fish_amount+nautilus_amount+blue_fish_amount+pike_amount+fat_fish_amount+snail_amount+frog_amount+koi_fish_amount+sturgeon_amount+piranha_amount+fightfish_amount+clownfish_amount+starfish_amount+jelly_amount+lionfish_amount+tang_amount+ray_amount+octopus_amount+seahorse_amount== 0:
            window.blit(empty_backpack,(250,100))
        outdoor_rect = door.get_rect()
        outdoor_rect.topleft = (10, 480)
        minus_rect = minus.get_rect()
        minus_rect.topleft = (550,450)
        plus_rect = plus.get_rect()
        plus_rect.topleft = (410,450)
        check_rect = check.get_rect()
        check_rect.topleft = (320,533)
        cancel_rect = cancel_1.get_rect()
        cancel_rect.topleft = (650,537)
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if outdoor_rect.collidepoint(mouse_pos):
                village(event)
            if plus_rect.collidepoint(mouse_pos) and function_f == False and buying == True:
                start_time = pygame.time.get_ticks()
                if amount<amount_c:
                    amount +=1
                function_f = True
            elif plus_rect.collidepoint(mouse_pos) and buying == True:
                amount += 0
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - start_time
                if elapsed_time >= 300:
                    function_f = False   
            if minus_rect.collidepoint(mouse_pos) and function_f == False and buying == True:
                start_time = pygame.time.get_ticks()
                if amount>1:
                    amount -=1
                function_f = True
            elif minus_rect.collidepoint(mouse_pos) and buying == True:
                amount -= 0
                current_time = pygame.time.get_ticks()
                elapsed_time = current_time - start_time
                if elapsed_time >= 300:
                    function_f = False
            if cancel_rect.collidepoint(mouse_pos) and buying == True:
                result_x = True
            if check_rect.collidepoint(mouse_pos) and buying == True:
                result = True
                backpack_slots-=amount    

        if (blue_fish_amount>0) or (blue_fish_amount>1 and blue_fish_in == True):
            if blue_fish_show ==0:
                blue_x = points[a_point][0]
                blue_y = points[a_point][1]
                a_point +=1
                blue_fish_show = 1
            window.blit(fish_frame,(blue_x,blue_y))
            window.blit(blue_fish,(blue_x+16,blue_y+10))
            blue_a = font.render("x"+str(blue_fish_amount),True,(255,255,255))
            window.blit(blue_a,(blue_x+13,blue_y+5))
            blue_rect.topleft = (blue_x+16,blue_y+10)
            if blue_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                blue_buying = True
            if buying == True and blue_buying == True:
                amount_c = blue_fish_amount
                blue_price = 4
                price = blue_price
                
            if result == True and blue_buying == True:
                blue_fish_amount -= amount
                money += amount*blue_price
                total_money += amount*blue_price
                result = blue_buying = buying = False
                amount = 1
            if result_x == True and blue_buying == True:
                amount = 1
                buying = blue_buying = result_x = False
        if blue_rect.collidepoint(pygame.mouse.get_pos()) or blue_buying==True:
            window.blit(fish_frame_coll,(blue_x,blue_y))
        if (pike_amount>0) or (pike_amount>1 and pike_in == True):
            if pike_show ==0:
                pike_x = points[a_point][0]
                pike_y = points[a_point][1]
                a_point +=1
                pike_show = 1
            window.blit(fish_frame,(pike_x,pike_y))
            window.blit(pike,(pike_x+12,pike_y+10))
            pike_a = font.render("x"+str(pike_amount),True,(255,255,255))
            window.blit(pike_a,(pike_x+13,pike_y+5))
            pike_rect.topleft = (pike_x+12,pike_y+10)
            if pike_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                pike_buying = True
            if buying == True and pike_buying == True:
                amount_c = pike_amount
                pike_price = 12
                price = pike_price
            if result == True and pike_buying == True:
                pike_amount -= amount
                money += amount*pike_price
                total_money += amount*pike_price
                result = pike_buying = buying = False
                amount = 1
            if result_x == True and pike_buying == True:
                amount = 1
                buying = pike_buying = result_x = False
        if pike_rect.collidepoint(pygame.mouse.get_pos()) or pike_buying==True:
            window.blit(fish_frame_coll,(pike_x,pike_y))
        if (fat_fish_amount>0) or (fat_fish_amount>1 and fat_fish_in == True):
            if fat_fish_show ==0:
                fat_x = points[a_point][0]
                fat_y = points[a_point][1]
                a_point +=1
                fat_fish_show = 1
            window.blit(fish_frame,(fat_x,fat_y))
            window.blit(fat_fish,(fat_x+16,fat_y+10))
            fat_a = font.render("x"+str(fat_fish_amount),True,(255,255,255))
            window.blit(fat_a,(fat_x+13,fat_y+5))
            fat_rect.topleft = (fat_x+16,fat_y+10)
            if fat_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                fat_buying = True
            if buying == True and fat_buying == True:
                amount_c = fat_fish_amount
                fat_price = 25
                price = fat_price
            if result == True and fat_buying == True:
                fat_fish_amount -= amount
                money += amount*fat_price
                total_money += amount*fat_price
                result = fat_buying = buying = False
                amount = 1
            if result_x == True and fat_buying == True:
                amount = 1
                buying = fat_buying = result_x = False
        if fat_rect.collidepoint(pygame.mouse.get_pos()) or fat_buying==True:
            window.blit(fish_frame_coll,(fat_x,fat_y))
        if (snail_amount>0) or (snail_amount>1 and snail_in == True):
            if snail_show ==0:
                snail_x = points[a_point][0]
                snail_y = points[a_point][1]
                a_point +=1
                snail_show = 1
            window.blit(fish_frame,(snail_x,snail_y))
            window.blit(snail,(snail_x+16,snail_y+10))
            snail_a = font.render("x"+str(snail_amount),True,(255,255,255))
            window.blit(snail_a,(snail_x+13,snail_y+5))
            snail_rect.topleft = (snail_x+16,snail_y+10)
            if snail_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                snail_buying = True
            if buying == True and snail_buying == True:
                amount_c = snail_amount
                snail_price = 45
                price = snail_price
            if result == True and snail_buying == True:
                snail_amount -= amount
                money += amount*snail_price
                total_money += amount*snail_price
                result = snail_buying = buying = False
                amount = 1
            if result_x == True and snail_buying == True:
                amount = 1
                buying = snail_buying = result_x = False
        if snail_rect.collidepoint(pygame.mouse.get_pos()) or snail_buying==True:
            window.blit(fish_frame_coll,(snail_x,snail_y))
        if (frog_amount>0) or (frog_amount>1 and frog_in == True):
            if frog_show ==0:
                frog_x = points[a_point][0]
                frog_y = points[a_point][1]
                a_point +=1
                frog_show = 1
            window.blit(fish_frame,(frog_x,frog_y))
            window.blit(frog,(frog_x+11,frog_y+10))
            frog_a = font.render("x"+str(frog_amount),True,(255,255,255))
            window.blit(frog_a,(frog_x+13,frog_y+5))
            frog_rect.topleft = (frog_x+11,frog_y+10)
            if frog_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                frog_buying = True
            if buying == True and frog_buying == True:
                amount_c = frog_amount
                frog_price = 100
                price = frog_price
            if result == True and frog_buying == True:
                frog_amount -= amount
                money += amount*frog_price
                total_money += amount*frog_price
                result = frog_buying = buying = False
                amount = 1
            if result_x == True and frog_buying == True:
                amount = 1
                buying = frog_buying = result_x = False
        if frog_rect.collidepoint(pygame.mouse.get_pos()) or frog_buying==True:
            window.blit(fish_frame_coll,(frog_x,frog_y))
        if (koi_fish_amount>0) or (koi_fish_amount>1 and koi_in == True):
            if koi_show ==0:
                koi_x = points[a_point][0]
                koi_y = points[a_point][1]
                a_point +=1
                koi_show = 1
            window.blit(fish_frame,(koi_x,koi_y))
            window.blit(koi_fish,(koi_x+16,koi_y+17))
            koi_a = font.render("x"+str(koi_fish_amount),True,(255,255,255))
            window.blit(koi_a,(koi_x+13,koi_y+5))
            koi_rect.topleft = (koi_x+16,koi_y+17)
            if koi_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                koi_buying = True
            if buying == True and koi_buying == True:
                amount_c = koi_fish_amount
                koi_price = 185
                price = koi_price
            if result == True and koi_buying == True:
                koi_fish_amount -= amount
                money += amount*koi_price
                total_money += amount*koi_price
                result = koi_buying = buying = False
                amount = 1
            if result_x == True and koi_buying == True:
                amount = 1
                buying = koi_buying = result_x = False
        if koi_rect.collidepoint(pygame.mouse.get_pos()) or koi_buying==True:
            window.blit(fish_frame_coll,(koi_x,koi_y))
        if (sturgeon_amount>0) or (sturgeon_amount>1 and sturgeon_in == True):
            if sturgeon_show ==0:
                sturgeon_x = points[a_point][0]
                sturgeon_y = points[a_point][1]
                a_point +=1
                sturgeon_show = 1
            window.blit(fish_frame,(sturgeon_x,sturgeon_y))
            window.blit(sturgeon,(sturgeon_x+16,sturgeon_y+10))
            sturgeon_a = font.render("x"+str(sturgeon_amount),True,(255,255,255))
            window.blit(sturgeon_a,(sturgeon_x+13,sturgeon_y+5))
            sturgeon_rect.topleft = (sturgeon_x+16,sturgeon_y+10)
            if sturgeon_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                sturgeon_buying = True
            if buying == True and sturgeon_buying == True:
                amount_c = sturgeon_amount
                sturgeon_price = 300
                price = sturgeon_price
            if result == True and sturgeon_buying == True:
                sturgeon_amount -= amount
                money += amount*sturgeon_price
                total_money += amount*sturgeon_price
                result = sturgeon_buying = buying = False
                amount = 1
            if result_x == True and sturgeon_buying == True:
                amount = 1
                buying = sturgeon_buying = result_x = False
        if sturgeon_rect.collidepoint(pygame.mouse.get_pos()) or sturgeon_buying==True:
            window.blit(fish_frame_coll,(sturgeon_x,sturgeon_y))
        if (piranha_amount>0) or (piranha_amount>1 and piranha_in == True):
            if piranha_show ==0:
                piranha_x = points[a_point][0]
                piranha_y = points[a_point][1]
                a_point +=1
                piranha_show = 1
            window.blit(fish_frame,(piranha_x,piranha_y))
            window.blit(piranha,(piranha_x+16,piranha_y+10))
            piranha_a = font.render("x"+str(piranha_amount),True,(255,255,255))
            window.blit(piranha_a,(piranha_x+13,piranha_y+5))
            piranha_rect.topleft = (piranha_x+16,piranha_y+10)
            if piranha_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                piranha_buying = True
            if buying == True and piranha_buying == True:
                amount_c = piranha_amount
                piranha_price = 500
                price = piranha_price
            if result == True and piranha_buying == True:
                piranha_amount -= amount
                money += amount*piranha_price
                total_money += amount*piranha_price
                result = piranha_buying = buying = False
                amount = 1
            if result_x == True and piranha_buying == True:
                amount = 1
                buying = piranha_buying = result_x = False
        if piranha_rect.collidepoint(pygame.mouse.get_pos()) or piranha_buying==True:
            window.blit(fish_frame_coll,(piranha_x,piranha_y))
        if (prawn_amount>0) or (prawn_amount>1 and prawn_in == True):
            if prawn_show ==0:
                prawn_x = points[a_point][0]
                prawn_y = points[a_point][1]
                a_point +=1
                prawn_show = 1
            window.blit(fish_frame,(prawn_x,prawn_y))
            window.blit(prawn,(prawn_x+23,prawn_y+10))
            prawn_a = font.render("x"+str(prawn_amount),True,(255,255,255))
            window.blit(prawn_a,(prawn_x+13,prawn_y+5))
            prawn_rect.topleft = (prawn_x+23,prawn_y+10)
            if prawn_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                prawn_buying = True
            if buying == True and prawn_buying == True:
                amount_c = prawn_amount
                prawn_price = 20
                price = prawn_price
            if result == True and prawn_buying == True:
                prawn_amount -= amount
                money += amount*prawn_price
                total_money += amount*prawn_price
                result = prawn_buying = buying = False
                amount = 1
            if result_x == True and prawn_buying == True:
                amount = 1
                buying = prawn_buying = result_x = False
        if prawn_rect.collidepoint(pygame.mouse.get_pos()) or prawn_buying==True:
            window.blit(fish_frame_coll,(prawn_x,prawn_y))
        if (tiger_fish_amount>0) or (tiger_fish_amount>1 and tiger_in == True):
            if tiger_show ==0:
                tiger_x = points[a_point][0]
                tiger_y = points[a_point][1]
                a_point +=1
                tiger_show = 1
            window.blit(fish_frame,(tiger_x,tiger_y))
            window.blit(tiger_fish,(tiger_x+23,tiger_y+10))
            tiger_a = font.render("x"+str(tiger_fish_amount),True,(255,255,255))
            window.blit(tiger_a,(tiger_x+13,tiger_y+5))
            tiger_rect.topleft = (tiger_x+23,tiger_y+10)
            if tiger_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                tiger_buying = True
            if buying == True and tiger_buying == True:
                amount_c = tiger_fish_amount
                tiger_price = 70
                price = tiger_price
            if result == True and tiger_buying == True:
                tiger_fish_amount -= amount
                money += amount*tiger_price
                total_money += amount*tiger_price
                result = tiger_buying = buying = False
                amount = 1
            if result_x == True and tiger_buying == True:
                amount = 1
                buying = tiger_buying = result_x = False
        if tiger_rect.collidepoint(pygame.mouse.get_pos()) or tiger_buying==True:
            window.blit(fish_frame_coll,(tiger_x,tiger_y))
        if (crab_amount>0) or (crab_amount>1 and crab_in == True):
            if crab_show ==0:
                crab_x = points[a_point][0]
                crab_y = points[a_point][1]
                a_point +=1
                crab_show = 1
            window.blit(fish_frame,(crab_x,crab_y))
            window.blit(crab,(crab_x+23,crab_y+10))
            crab_a = font.render("x"+str(crab_amount),True,(255,255,255))
            window.blit(crab_a,(crab_x+13,crab_y+5))
            crab_rect.topleft = (crab_x+23,crab_y+10)
            if crab_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                crab_buying = True
            if buying == True and crab_buying == True:
                amount_c = crab_amount
                crab_price = 125
                price = crab_price
            if result == True and crab_buying == True:
                crab_amount -= amount
                money += amount*crab_price
                total_money += amount*crab_price
                result = crab_buying = buying = False
                amount = 1
            if result_x == True and crab_buying == True:
                amount = 1
                buying = crab_buying = result_x = False
        if crab_rect.collidepoint(pygame.mouse.get_pos()) or crab_buying==True:
            window.blit(fish_frame_coll,(crab_x,crab_y))
        if (sword_fish_amount>0) or (sword_fish_amount>1 and sword_in == True):
            if sword_show ==0:
                sword_x = points[a_point][0]
                sword_y = points[a_point][1]
                a_point +=1
                sword_show = 1
            window.blit(fish_frame,(sword_x,sword_y))
            window.blit(sword_fish,(sword_x-1,sword_y+14))
            sword_a = font.render("x"+str(sword_fish_amount),True,(255,255,255))
            window.blit(sword_a,(sword_x+13,sword_y+5))
            sword_rect.topleft = (sword_x-1,sword_y+14)
            if sword_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                sword_buying = True
            if buying == True and sword_buying == True:
                amount_c = sword_fish_amount
                sword_price = 220
                price = sword_price
            if result == True and sword_buying == True:
                sword_fish_amount -= amount
                money += amount*sword_price
                total_money += amount*sword_price
                result = sword_buying = buying = False
                amount = 1
            if result_x == True and sword_buying == True:
                amount = 1
                buying = sword_buying = result_x = False
        if sword_rect.collidepoint(pygame.mouse.get_pos()) or sword_buying==True:
            window.blit(fish_frame_coll,(sword_x,sword_y))
        if (turtle_amount>0) or (turtle_amount>1 and turtle_in == True):
            if turtle_show ==0:
                turtle_x = points[a_point][0]
                turtle_y = points[a_point][1]
                a_point +=1
                turtle_show = 1
            window.blit(fish_frame,(turtle_x,turtle_y))
            window.blit(turtle,(turtle_x+16,turtle_y+15))
            turtle_a = font.render("x"+str(turtle_amount),True,(255,255,255))
            window.blit(turtle_a,(turtle_x+13,turtle_y+5))
            turtle_rect.topleft = (turtle_x+16,turtle_y+15)
            if turtle_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                turtle_buying = True
            if buying == True and turtle_buying == True:
                amount_c = turtle_amount
                turtle_price = 400
                price = turtle_price
            if result == True and turtle_buying == True:
                turtle_amount -= amount
                money += amount*turtle_price
                total_money += amount*turtle_price
                result = turtle_buying = buying = False
                amount = 1
            if result_x == True and turtle_buying == True:
                amount = 1
                buying = turtle_buying = result_x = False
        if turtle_rect.collidepoint(pygame.mouse.get_pos()) or turtle_buying==True:
            window.blit(fish_frame_coll,(turtle_x,turtle_y))
        if (shark_amount>0) or (shark_amount>1 and shark_in == True):
            if shark_show ==0:
                shark_x = points[a_point][0]
                shark_y = points[a_point][1]
                a_point +=1
                shark_show = 1
            window.blit(fish_frame,(shark_x,shark_y))
            window.blit(shark,(shark_x+8,shark_y+17))
            shark_a = font.render("x"+str(shark_amount),True,(255,255,255))
            window.blit(shark_a,(shark_x+13,shark_y+5))
            shark_rect.topleft = (shark_x+8,shark_y+17)
            if shark_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                shark_buying = True
            if buying == True and shark_buying == True:
                amount_c = shark_amount
                shark_price = 650
                price = shark_price
            if result == True and shark_buying == True:
                shark_amount -= amount
                money += amount*shark_price
                total_money += amount*shark_price
                result = shark_buying = buying = False
                amount = 1
            if result_x == True and shark_buying == True:
                amount = 1
                buying = shark_buying = result_x = False
        if shark_rect.collidepoint(pygame.mouse.get_pos()) or shark_buying==True:
            window.blit(fish_frame_coll,(shark_x,shark_y))
        if (light_fish_amount>0) or (light_fish_amount>1 and light_in == True):
            if light_show ==0:
                light_x = points[a_point][0]
                light_y = points[a_point][1]
                a_point +=1
                light_show = 1
            window.blit(fish_frame,(light_x,light_y))
            window.blit(light_fish,(light_x+21,light_y+8))
            light_a = font.render("x"+str(light_fish_amount),True,(255,255,255))
            window.blit(light_a,(light_x+13,light_y+5))
            light_rect.topleft = (light_x+21,light_y+8)
            if light_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                light_buying = True
            if buying == True and light_buying == True:
                amount_c = light_fish_amount
                light_price = 900
                price = light_price
            if result == True and light_buying == True:
                light_fish_amount -= amount
                money += amount*light_price
                total_money += amount*light_price
                result = light_buying = buying = False
                amount = 1
            if result_x == True and light_buying == True:
                amount = 1
                buying = light_buying = result_x = False
        if light_rect.collidepoint(pygame.mouse.get_pos()) or light_buying==True:
            window.blit(fish_frame_coll,(light_x,light_y))
        if (nautilus_amount>0) or (nautilus_amount>1 and nautilus_in == True):
            if nautilus_show ==0:
                nautilus_x = points[a_point][0]
                nautilus_y = points[a_point][1]
                a_point +=1
                nautilus_show = 1
            window.blit(fish_frame,(nautilus_x,nautilus_y))
            window.blit(nautilus,(nautilus_x+21,nautilus_y+10))
            nautilus_a = font.render("x"+str(nautilus_amount),True,(255,255,255))
            window.blit(nautilus_a,(nautilus_x+13,nautilus_y+5))
            nautilus_rect.topleft = (nautilus_x+21,nautilus_y+10)
            if nautilus_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                nautilus_buying = True
            if buying == True and nautilus_buying == True:
                amount_c = nautilus_amount
                nautilus_price = 1200
                price = nautilus_price
            if result == True and nautilus_buying == True:
                nautilus_amount -= amount
                money += amount*nautilus_price
                total_money += amount*nautilus_price
                result = nautilus_buying = buying = False
                amount = 1
            if result_x == True and nautilus_buying == True:
                amount = 1
                buying = nautilus_buying = result_x = False
        if nautilus_rect.collidepoint(pygame.mouse.get_pos()) or nautilus_buying==True:
            window.blit(fish_frame_coll,(nautilus_x,nautilus_y))
        if (zombie_fish_amount>0) or (zombie_fish_amount>1 and zombie_in == True):
            if zombie_show ==0:
                zombie_x = points[a_point][0]
                zombie_y = points[a_point][1]
                a_point +=1
                zombie_show = 1
            window.blit(fish_frame,(zombie_x,zombie_y))
            window.blit(zombie_fish,(zombie_x+19,zombie_y+14))
            zombie_a = font.render("x"+str(zombie_fish_amount),True,(255,255,255))
            window.blit(zombie_a,(zombie_x+13,zombie_y+5))
            zombie_rect.topleft = (zombie_x+19,zombie_y+14)
            if zombie_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                zombie_buying = True
            if buying == True and zombie_buying == True:
                amount_c = zombie_fish_amount
                zombie_price = 1600
                price = zombie_price
            if result == True and zombie_buying == True:
                zombie_fish_amount -= amount
                money += amount*zombie_price
                total_money += amount*zombie_price
                result = zombie_buying = buying = False
                amount = 1
            if result_x == True and zombie_buying == True:
                amount = 1
                buying = zombie_buying = result_x = False
        if zombie_rect.collidepoint(pygame.mouse.get_pos()) or zombie_buying==True:
            window.blit(fish_frame_coll,(zombie_x,zombie_y))
        if (fightfish_amount>0) or (fightfish_amount>1 and fightfish_in == True):
            if fight_show ==0:
                fight_x = points[a_point][0]
                fight_y = points[a_point][1]
                a_point +=1
                fight_show = 1
            window.blit(fish_frame,(fight_x,fight_y))
            window.blit(fightfish,(fight_x+19,fight_y+14))
            fight_a = font.render("x"+str(fightfish_amount),True,(255,255,255))
            window.blit(fight_a,(fight_x+13,fight_y+5))
            fight_rect.topleft = (fight_x+19,fight_y+14)
            if fight_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                fight_buying = True
            if buying == True and fight_buying == True:
                amount_c = fightfish_amount
                fight_price = 200
                price = fight_price
            if result == True and fight_buying == True:
                fightfish_amount -= amount
                money += amount*fight_price
                total_money += amount*fight_price
                result = fight_buying = buying = False
                amount = 1
            if result_x == True and fight_buying == True:
                amount = 1
                buying = fight_buying = result_x = False
        if fight_rect.collidepoint(pygame.mouse.get_pos()) or fight_buying==True:
            window.blit(fish_frame_coll,(fight_x,fight_y))
        if (clownfish_amount>0) or (clownfish_amount>1 and clownfish_in == True):
            if clown_show ==0:
                clown_x = points[a_point][0]
                clown_y = points[a_point][1]
                a_point +=1
                clown_show = 1
            window.blit(fish_frame,(clown_x,clown_y))
            window.blit(clownfish,(clown_x+25,clown_y+16))
            clown_a = font.render("x"+str(clownfish_amount),True,(255,255,255))
            window.blit(clown_a,(clown_x+13,clown_y+5))
            clown_rect.topleft = (clown_x+19,clown_y+14)
            if clown_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                clown_buying = True
            if buying == True and clown_buying == True:
                amount_c = clownfish_amount
                clown_price = 400
                price = clown_price
            if result == True and clown_buying == True:
                clownfish_amount -= amount
                money += amount*clown_price
                total_money += amount*clown_price
                result = clown_buying = buying = False
                amount = 1
            if result_x == True and clown_buying == True:
                amount = 1
                buying = clown_buying = result_x = False
        if clown_rect.collidepoint(pygame.mouse.get_pos()) or clown_buying==True:
            window.blit(fish_frame_coll,(clown_x,clown_y))
        if (starfish_amount>0) or (starfish_amount>1 and starfish_in == True):
            if star_show ==0:
                star_x = points[a_point][0]
                star_y = points[a_point][1]
                a_point +=1
                star_show = 1
            window.blit(fish_frame,(star_x,star_y))
            window.blit(starfish,(star_x+29,star_y+15))
            star_a = font.render("x"+str(starfish_amount),True,(255,255,255))
            window.blit(star_a,(star_x+13,star_y+5))
            star_rect.topleft = (star_x+19,star_y+14)
            if star_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                star_buying = True
            if buying == True and star_buying == True:
                amount_c = starfish_amount
                star_price = 700
                price = star_price
            if result == True and star_buying == True:
                starfish_amount -= amount
                money += amount*star_price
                total_money += amount*star_price
                result = star_buying = buying = False
                amount = 1
            if result_x == True and star_buying == True:
                amount = 1
                buying = star_buying = result_x = False
        if star_rect.collidepoint(pygame.mouse.get_pos()) or star_buying==True:
            window.blit(fish_frame_coll,(star_x,star_y))
        if (jelly_amount>0) or (jelly_amount>1 and jelly_in == True):
            if jelly_show ==0:
                jelly_x = points[a_point][0]
                jelly_y = points[a_point][1]
                a_point +=1
                jelly_show = 1
            window.blit(fish_frame,(jelly_x,jelly_y))
            window.blit(jelly,(jelly_x+29,jelly_y+10))
            jelly_a = font.render("x"+str(jelly_amount),True,(255,255,255))
            window.blit(jelly_a,(jelly_x+13,jelly_y+5))
            jelly_rect.topleft = (jelly_x+19,jelly_y+14)
            if jelly_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                jelly_buying = True
            if buying == True and jelly_buying == True:
                amount_c = jelly_amount
                jelly_price = 1000
                price = jelly_price
            if result == True and jelly_buying == True:
                jelly_amount -= amount
                money += amount*jelly_price
                total_money += amount*jelly_price
                result = jelly_buying = buying = False
                amount = 1
            if result_x == True and jelly_buying == True:
                amount = 1
                buying = jelly_buying = result_x = False
        if jelly_rect.collidepoint(pygame.mouse.get_pos()) or jelly_buying==True:
            window.blit(fish_frame_coll,(jelly_x,jelly_y))
        if (lionfish_amount>0) or (lionfish_amount>1 and lionfish_in == True):
            if lion_show ==0:
                lion_x = points[a_point][0]
                lion_y = points[a_point][1]
                a_point +=1
                lion_show = 1
            window.blit(fish_frame,(lion_x,lion_y))
            window.blit(lionfish,(lion_x+15,lion_y+9))
            lion_a = font.render("x"+str(lionfish_amount),True,(255,255,255))
            window.blit(lion_a,(lion_x+13,lion_y+5))
            lion_rect.topleft = (lion_x+19,lion_y+14)
            if lion_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                lion_buying = True
            if buying == True and lion_buying == True:
                amount_c = lionfish_amount
                lion_price = 1800
                price = lion_price
            if result == True and lion_buying == True:
                lionfish_amount -= amount
                money += amount*lion_price
                total_money += amount*lion_price
                result = lion_buying = buying = False
                amount = 1
            if result_x == True and lion_buying == True:
                amount = 1
                buying = lion_buying = result_x = False
        if lion_rect.collidepoint(pygame.mouse.get_pos()) or lion_buying==True:
            window.blit(fish_frame_coll,(lion_x,lion_y))
        if (tang_amount>0) or (tang_amount>1 and tang_in == True):
            if tang_show ==0:
                tang_x = points[a_point][0]
                tang_y = points[a_point][1]
                a_point +=1
                tang_show = 1
            window.blit(fish_frame,(tang_x,tang_y))
            window.blit(tang,(tang_x+10,tang_y+14))
            tang_a = font.render("x"+str(tang_amount),True,(255,255,255))
            window.blit(tang_a,(tang_x+13,tang_y+5))
            tang_rect.topleft = (tang_x+19,tang_y+14)
            if tang_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                tang_buying = True
            if buying == True and tang_buying == True:
                amount_c = tang_amount
                tang_price = 2800
                price = tang_price
            if result == True and tang_buying == True:
                tang_amount -= amount
                money += amount*tang_price
                total_money += amount*tang_price
                result = tang_buying = buying = False
                amount = 1
            if result_x == True and tang_buying == True:
                amount = 1
                buying = tang_buying = result_x = False
        if tang_rect.collidepoint(pygame.mouse.get_pos()) or tang_buying==True:
            window.blit(fish_frame_coll,(tang_x,tang_y))
        if (ray_amount>0) or (ray_amount>1 and ray_in == True):
            if ray_show ==0:
                ray_x = points[a_point][0]
                ray_y = points[a_point][1]
                a_point +=1
                ray_show = 1
            window.blit(fish_frame,(ray_x,ray_y))
            window.blit(ray,(ray_x+14,ray_y+10))
            ray_a = font.render("x"+str(ray_amount),True,(255,255,255))
            window.blit(ray_a,(ray_x+13,ray_y+5))
            ray_rect.topleft = (ray_x+19,ray_y+14)
            if ray_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                ray_buying = True
            if buying == True and ray_buying == True:
                amount_c = ray_amount
                ray_price = 5200
                price = ray_price
            if result == True and ray_buying == True:
                ray_amount -= amount
                money += amount*ray_price
                total_money += amount*ray_price
                result = ray_buying = buying = False
                amount = 1
            if result_x == True and ray_buying == True:
                amount = 1
                buying = ray_buying = result_x = False
        if ray_rect.collidepoint(pygame.mouse.get_pos()) or ray_buying==True:
            window.blit(fish_frame_coll,(ray_x,ray_y))
        if (octopus_amount>0) or (octopus_amount>1 and octopus_in == True):
            if octopus_show ==0:
                octopus_x = points[a_point][0]
                octopus_y = points[a_point][1]
                a_point +=1
                octopus_show = 1
            window.blit(fish_frame,(octopus_x,octopus_y))
            window.blit(octopus,(octopus_x+14,octopus_y+10))
            octopus_a = font.render("x"+str(octopus_amount),True,(255,255,255))
            window.blit(octopus_a,(octopus_x+13,octopus_y+5))
            octopus_rect.topleft = (octopus_x+19,octopus_y+14)
            if octopus_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                octopus_buying = True
            if buying == True and octopus_buying == True:
                amount_c = octopus_amount
                octopus_price = 10000
                price = octopus_price
            if result == True and octopus_buying == True:
                octopus_amount -= amount
                money += amount*octopus_price
                total_money += amount*octopus_price
                result = octopus_buying = buying = False
                amount = 1
            if result_x == True and octopus_buying == True:
                amount = 1
                buying = octopus_buying = result_x = False
        if octopus_rect.collidepoint(pygame.mouse.get_pos()) or octopus_buying==True:
            window.blit(fish_frame_coll,(octopus_x,octopus_y))
        if (seahorse_amount>0) or (seahorse_amount>1 and seahorse_in == True):
            if seahorse_show ==0:
                seahorse_x = points[a_point][0]
                seahorse_y = points[a_point][1]
                a_point +=1
                seahorse_show = 1
            window.blit(fish_frame,(seahorse_x,seahorse_y))
            window.blit(seahorse1,(seahorse_x+31,seahorse_y))
            seahorse_a = font.render("x"+str(seahorse_amount),True,(255,255,255))
            window.blit(seahorse_a,(seahorse_x+13,seahorse_y+5))
            seahorse_rect.topleft = (seahorse_x+19,seahorse_y+14)
            if seahorse_rect.collidepoint(mouse_pos) and buying==False:
                buying = True
                seahorse_buying = True
            if buying == True and seahorse_buying == True:
                amount_c = seahorse_amount
                seahorse_price = 20000
                price = seahorse_price
            if result == True and seahorse_buying == True:
                seahorse_amount -= amount
                money += amount*seahorse_price
                total_money += amount*seahorse_price
                result = seahorse_buying = buying = False
                amount = 1
            if result_x == True and seahorse_buying == True:
                amount = 1
                buying = seahorse_buying = result_x = False
        if seahorse_rect.collidepoint(pygame.mouse.get_pos()) or seahorse_buying==True:
            window.blit(fish_frame_coll,(seahorse_x,seahorse_y))
        if buying == True:
            window.blit(fishing_info,(300,400))
            window.blit(check,(320,533))
            window.blit(cancel_1,(650,537))
            sale = font.render("Sale",True,(255,255,255))
            amount_s = font.render(str(amount),True,(255,255,255))
            window.blit(plus,(410,450))
            window.blit(minus,(550,450))
            window.blit(amount_s,(505,470))
            window.blit(sale,(485,425))
            window.blit(cash,(440,530))
            sum_s = font.render(str(amount*price),True,(255,255,255))
            window.blit(sum_s,(515,552))
        money_amount = font.render(str(money),True,(0,0,0))
        window.blit(money_amount,(105,21))
        pygame.display.update()


def swim(graphic,object_x,object_y,direction_x,direction_y,touch,object_speed):
    object_width = 40
    object_height = 25
    rand_num = random.random()
    object_x += direction_x * object_speed
    if touch % 2 == 0:
        object_y += 0
    else:
        object_y += direction_y * object_speed

    # Obrot grafiki w zaleznosci od kierunku
    if (direction_x == 1 and direction_y ==-1 and touch%2==0) or (direction_x == 1 and direction_y ==1 and touch%2==0) : #>
        rotated_graphic = pygame.transform.rotate(graphic, 0)
    elif direction_x == 1 and direction_y ==-1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 45)  
    elif direction_x == 1 and direction_y ==1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 315)
    elif (direction_x == -1 and direction_y ==1 and touch%2==0) or (direction_x == -1 and direction_y ==-1 and touch%2==0) :
        rotated_graphic = pygame.transform.rotate(graphic, 0)
        rotated_graphic = pygame.transform.flip(rotated_graphic,True, False)
    elif direction_x == -1 and direction_y ==1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 315)
        rotated_graphic = pygame.transform.flip(rotated_graphic,True, False)
    elif direction_x == -1 and direction_y ==-1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 45)
        rotated_graphic = pygame.transform.flip(rotated_graphic,True, False)

    # Odbijanie od krawędzi ekranu
    if object_x <= 206:
        direction_x = 1
        if rand_num<=0.5:
            touch += 1
    if object_x >= 795 - object_width:
        direction_x = -1
        if rand_num<=0.5:
            touch += 1
    if object_y <= 145 or object_y >= 345 - object_height:
        direction_y *= -1
    return[rotated_graphic,object_x,object_y,direction_x,direction_y,touch,object_speed]
    
def swim_snail(graphic,object_x,object_y,direction_x,direction_y,touch):
    object_width = 40
    object_height = 25
    object_speed = 0.02
    
    object_x += direction_x * object_speed
    if touch % 2 == 0:
        object_y += 0
    else:
        object_y += direction_y * object_speed

    # Obrot grafiki w zaleznosci od kierunku
    if (direction_x == 1 and direction_y ==-1 and touch%2==0) or (direction_x == 1 and direction_y ==1 and touch%2==0) : #>
        rotated_graphic = pygame.transform.rotate(graphic, 0)
    elif direction_x == 1 and direction_y ==-1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 45)  
    elif direction_x == 1 and direction_y ==1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 315)
    elif (direction_x == -1 and direction_y ==1 and touch%2==0) or (direction_x == -1 and direction_y ==-1 and touch%2==0) :
        rotated_graphic = pygame.transform.rotate(graphic, 0)
        rotated_graphic = pygame.transform.flip(rotated_graphic,True, False)
    elif direction_x == -1 and direction_y ==1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 315)
        rotated_graphic = pygame.transform.flip(rotated_graphic,True, False)
    elif direction_x == -1 and direction_y ==-1 and touch%2!=0:
        rotated_graphic = pygame.transform.rotate(graphic, 45)
        rotated_graphic = pygame.transform.flip(rotated_graphic,True, False)

    # Odbijanie od krawędzi ekranu
    if object_x <= 206 or object_x >= 795 - object_width:
        direction_x *= -1
        touch += 1
    if object_y <= 145 or object_y >= 345 - object_height:
        direction_y *= -1
    return[rotated_graphic,object_x,object_y,direction_x,direction_y,touch]

def swim_crab(graphic,object_x,object_y,direction_x,direction_y,touch):
    object_width = 40
    object_speed = 0.3
    
    object_x += direction_x * object_speed
    


    # Odbijanie od krawędzi ekranu
    if object_x <= 210 or object_x >= 800 - object_width:
        direction_x *= -1
        touch += 1
    if object_x >320 and object_x <350 and direction_x==1:
        object_y-=0.08
    if object_x >420 and object_x <505 and direction_x==1:
        object_y+=0.06
    if object_x >550 and object_x <607 and direction_x==1:
        object_y-=0.07
    if object_x >690 and object_x <740 and direction_x==1:
        object_y+=0.06
    if object_x >320 and object_x <350 and direction_x==-1:
        object_y+=0.08
    if object_x >420 and object_x <505 and direction_x==-1:
        object_y-=0.06
    if object_x >550 and object_x <607 and direction_x==-1:
        object_y+=0.07
    if object_x >690 and object_x <740 and direction_x==-1:
        object_y-=0.06
        

    return[graphic,object_x,object_y,direction_x,direction_y,touch]
def main():
    global mode, start_game, money
    run = True
    quit_rect = quit.get_rect()
    quit_rect.topleft = (720, 380)
    start_rect = start.get_rect()
    start_rect.topleft = (120, 380)
    load_rect = load.get_rect()
    load_rect.topleft = (420, 380)
    window.blit(s_background, (0, 0))
    window.blit(title, (100, 100))
    window.blit(load, (420, 380))
    window.blit(start, (120, 380))
    window.blit(quit, (720, 380))
    window.blit(watermark,(980,2))
    version = font.render("v.1.0", True, (0, 0, 0))
    window.blit(version,(5,5))
    pygame.display.set_caption("Pixel Aquarium")
    pygame.display.set_icon(pygame.image.load('buttons/icon.png'))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if start_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(start_coll,(120,380))
            else:
                window.blit(start,(120,380))
            if load_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(load_coll,(420,380))
            else:
                window.blit(load,(420,380))
            if quit_rect.collidepoint(pygame.mouse.get_pos()):
                window.blit(quit_coll,(720,380))
            else:
                window.blit(quit,(720,380))
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                elif start_rect.collidepoint(mouse_pos):
                    mode = 1
                    start_game = 1
                    home(event)
                elif load_rect.collidepoint(mouse_pos):
                    mode = 0
                    start_game = 1
                    home(event)
        pygame.display.update()

if __name__ == "__main__":
    main()
