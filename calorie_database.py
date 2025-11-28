# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 01:23:51 2025

@author: Deepika
"""

# calorie_database.py
"""
Mapping from Food-101 class labels to approximate calories.
You can expand this over time.
"""

# calorie_database.py
"""
Calorie lookup table for all 101 Food-101 classes.

Values are *approximate* kcal for a typical restaurant-style serving.
You can tweak numbers later if you want them closer to a specific source.
"""

FOOD_CALORIES = {
    "apple_pie": {
        "display_name": "Apple Pie",
        "calories_per_serving": 300,
        "serving_description": "1 slice (~125 g)"
    },
    "baby_back_ribs": {
        "display_name": "Baby Back Ribs",
        "calories_per_serving": 450,
        "serving_description": "1 serving ribs (~200 g)"
    },
    "baklava": {
        "display_name": "Baklava",
        "calories_per_serving": 330,
        "serving_description": "1 piece (~80 g)"
    },
    "beef_carpaccio": {
        "display_name": "Beef Carpaccio",
        "calories_per_serving": 220,
        "serving_description": "1 plate (~120 g)"
    },
    "beef_tartare": {
        "display_name": "Beef Tartare",
        "calories_per_serving": 250,
        "serving_description": "1 serving (~150 g)"
    },
    "beet_salad": {
        "display_name": "Beet Salad",
        "calories_per_serving": 160,
        "serving_description": "1 bowl (~150 g)"
    },
    "beignets": {
        "display_name": "Beignets",
        "calories_per_serving": 260,
        "serving_description": "3 small pieces (~75 g)"
    },
    "bibimbap": {
        "display_name": "Bibimbap",
        "calories_per_serving": 550,
        "serving_description": "1 bowl (~400 g)"
    },
    "bread_pudding": {
        "display_name": "Bread Pudding",
        "calories_per_serving": 350,
        "serving_description": "1 square (~150 g)"
    },
    "breakfast_burrito": {
        "display_name": "Breakfast Burrito",
        "calories_per_serving": 500,
        "serving_description": "1 burrito (~250 g)"
    },
    "bruschetta": {
        "display_name": "Bruschetta",
        "calories_per_serving": 180,
        "serving_description": "2 pieces (~80 g)"
    },
    "caesar_salad": {
        "display_name": "Caesar Salad",
        "calories_per_serving": 220,
        "serving_description": "1 bowl (~180 g)"
    },
    "cannoli": {
        "display_name": "Cannoli",
        "calories_per_serving": 220,
        "serving_description": "1 piece (~75 g)"
    },
    "caprese_salad": {
        "display_name": "Caprese Salad",
        "calories_per_serving": 200,
        "serving_description": "1 plate (~180 g)"
    },
    "carrot_cake": {
        "display_name": "Carrot Cake",
        "calories_per_serving": 330,
        "serving_description": "1 slice (~120 g)"
    },
    "ceviche": {
        "display_name": "Ceviche",
        "calories_per_serving": 180,
        "serving_description": "1 bowl (~180 g)"
    },
    "cheesecake": {
        "display_name": "Cheesecake",
        "calories_per_serving": 350,
        "serving_description": "1 slice (~125 g)"
    },
    "cheese_plate": {
        "display_name": "Cheese Plate",
        "calories_per_serving": 400,
        "serving_description": "Assorted cheeses (~150 g)"
    },
    "chicken_curry": {
        "display_name": "Chicken Curry",
        "calories_per_serving": 350,
        "serving_description": "1 serving (~200 g, curry only)"
    },
    "chicken_quesadilla": {
        "display_name": "Chicken Quesadilla",
        "calories_per_serving": 450,
        "serving_description": "1 quesadilla (~220 g)"
    },
    "chicken_wings": {
        "display_name": "Chicken Wings",
        "calories_per_serving": 430,
        "serving_description": "6 wings (~180 g)"
    },
    "chocolate_cake": {
        "display_name": "Chocolate Cake",
        "calories_per_serving": 360,
        "serving_description": "1 slice (~125 g)"
    },
    "chocolate_mousse": {
        "display_name": "Chocolate Mousse",
        "calories_per_serving": 310,
        "serving_description": "1 cup (~150 g)"
    },
    "churros": {
        "display_name": "Churros",
        "calories_per_serving": 280,
        "serving_description": "3 pieces (~90 g)"
    },
    "clam_chowder": {
        "display_name": "Clam Chowder",
        "calories_per_serving": 250,
        "serving_description": "1 bowl (~300 ml)"
    },
    "club_sandwich": {
        "display_name": "Club Sandwich",
        "calories_per_serving": 500,
        "serving_description": "1 sandwich (~250 g)"
    },
    "crab_cakes": {
        "display_name": "Crab Cakes",
        "calories_per_serving": 300,
        "serving_description": "2 cakes (~150 g)"
    },
    "creme_brulee": {
        "display_name": "Crème Brûlée",
        "calories_per_serving": 250,
        "serving_description": "1 ramekin (~120 g)"
    },
    "croque_madame": {
        "display_name": "Croque Madame",
        "calories_per_serving": 550,
        "serving_description": "1 sandwich (~250 g)"
    },
    "cup_cakes": {
        "display_name": "Cupcakes",
        "calories_per_serving": 180,
        "serving_description": "1 cupcake (~60 g)"
    },
    "deviled_eggs": {
        "display_name": "Deviled Eggs",
        "calories_per_serving": 130,
        "serving_description": "2 halves (1 egg)"
    },
    "donuts": {
        "display_name": "Donuts",
        "calories_per_serving": 260,
        "serving_description": "1 donut (~75 g)"
    },
    "dumplings": {
        "display_name": "Dumplings",
        "calories_per_serving": 220,
        "serving_description": "6 dumplings (~150 g)"
    },
    "edamame": {
        "display_name": "Edamame",
        "calories_per_serving": 190,
        "serving_description": "1 bowl (~150 g, with pods)"
    },
    "eggs_benedict": {
        "display_name": "Eggs Benedict",
        "calories_per_serving": 500,
        "serving_description": "2 halves (~220 g)"
    },
    "escargots": {
        "display_name": "Escargots",
        "calories_per_serving": 220,
        "serving_description": "1 serving (~100 g, with butter)"
    },
    "falafel": {
        "display_name": "Falafel",
        "calories_per_serving": 330,
        "serving_description": "4 balls (~150 g)"
    },
    "filet_mignon": {
        "display_name": "Filet Mignon",
        "calories_per_serving": 430,
        "serving_description": "1 steak (~200 g)"
    },
    "fish_and_chips": {
        "display_name": "Fish and Chips",
        "calories_per_serving": 800,
        "serving_description": "Fish fillet + fries (~350 g)"
    },
    "foie_gras": {
        "display_name": "Foie Gras",
        "calories_per_serving": 450,
        "serving_description": "1 small portion (~80 g)"
    },
    "french_fries": {
        "display_name": "French Fries",
        "calories_per_serving": 320,
        "serving_description": "1 medium serving (~120 g)"
    },
    "french_onion_soup": {
        "display_name": "French Onion Soup",
        "calories_per_serving": 280,
        "serving_description": "1 bowl with cheese (~300 ml)"
    },
    "french_toast": {
        "display_name": "French Toast",
        "calories_per_serving": 300,
        "serving_description": "2 slices (~150 g)"
    },
    "fried_calamari": {
        "display_name": "Fried Calamari",
        "calories_per_serving": 350,
        "serving_description": "1 plate (~180 g)"
    },
    "fried_rice": {
        "display_name": "Fried Rice",
        "calories_per_serving": 330,
        "serving_description": "1 cup (~200 g)"
    },
    "frozen_yogurt": {
        "display_name": "Frozen Yogurt",
        "calories_per_serving": 180,
        "serving_description": "1 cup (~150 g)"
    },
    "garlic_bread": {
        "display_name": "Garlic Bread",
        "calories_per_serving": 190,
        "serving_description": "2 slices (~70 g)"
    },
    "gnocchi": {
        "display_name": "Gnocchi",
        "calories_per_serving": 330,
        "serving_description": "1 plate (~200 g)"
    },
    "greek_salad": {
        "display_name": "Greek Salad",
        "calories_per_serving": 220,
        "serving_description": "1 bowl (~200 g)"
    },
    "grilled_cheese_sandwich": {
        "display_name": "Grilled Cheese Sandwich",
        "calories_per_serving": 400,
        "serving_description": "1 sandwich (~180 g)"
    },
    "grilled_salmon": {
        "display_name": "Grilled Salmon",
        "calories_per_serving": 350,
        "serving_description": "1 fillet (~180 g)"
    },
    "guacamole": {
        "display_name": "Guacamole",
        "calories_per_serving": 220,
        "serving_description": "1 small bowl (~100 g)"
    },
    "gyoza": {
        "display_name": "Gyoza",
        "calories_per_serving": 230,
        "serving_description": "6 dumplings (~150 g)"
    },
    "hamburger": {
        "display_name": "Hamburger",
        "calories_per_serving": 350,
        "serving_description": "1 burger (~150 g)"
    },
    "hot_and_sour_soup": {
        "display_name": "Hot and Sour Soup",
        "calories_per_serving": 150,
        "serving_description": "1 bowl (~300 ml)"
    },
    "hot_dog": {
        "display_name": "Hot Dog",
        "calories_per_serving": 280,
        "serving_description": "1 hot dog in bun (~120 g)"
    },
    "huevos_rancheros": {
        "display_name": "Huevos Rancheros",
        "calories_per_serving": 420,
        "serving_description": "1 plate (~250 g)"
    },
    "hummus": {
        "display_name": "Hummus",
        "calories_per_serving": 200,
        "serving_description": "1 small bowl (~100 g)"
    },
    "ice_cream": {
        "display_name": "Ice Cream",
        "calories_per_serving": 210,
        "serving_description": "1 large scoop (~90 g)"
    },
    "lasagna": {
        "display_name": "Lasagna",
        "calories_per_serving": 350,
        "serving_description": "1 square (~200 g)"
    },
    "lobster_bisque": {
        "display_name": "Lobster Bisque",
        "calories_per_serving": 300,
        "serving_description": "1 bowl (~300 ml)"
    },
    "lobster_roll_sandwich": {
        "display_name": "Lobster Roll Sandwich",
        "calories_per_serving": 450,
        "serving_description": "1 roll (~220 g)"
    },
    "macaroni_and_cheese": {
        "display_name": "Macaroni and Cheese",
        "calories_per_serving": 320,
        "serving_description": "1 cup (~200 g)"
    },
    "macarons": {
        "display_name": "Macarons",
        "calories_per_serving": 70,
        "serving_description": "1 macaron (~20 g)"
    },
    "miso_soup": {
        "display_name": "Miso Soup",
        "calories_per_serving": 60,
        "serving_description": "1 bowl (~250 ml)"
    },
    "mussels": {
        "display_name": "Mussels",
        "calories_per_serving": 230,
        "serving_description": "1 bowl (~200 g with shells)"
    },
    "nachos": {
        "display_name": "Nachos",
        "calories_per_serving": 600,
        "serving_description": "Shared plate (~250 g)"
    },
    "omelette": {
        "display_name": "Omelette",
        "calories_per_serving": 190,
        "serving_description": "2–3 egg omelette (~150 g)"
    },
    "onion_rings": {
        "display_name": "Onion Rings",
        "calories_per_serving": 350,
        "serving_description": "1 basket (~150 g)"
    },
    "oysters": {
        "display_name": "Oysters",
        "calories_per_serving": 120,
        "serving_description": "6 oysters (~100 g)"
    },
    "pad_thai": {
        "display_name": "Pad Thai",
        "calories_per_serving": 450,
        "serving_description": "1 plate (~300 g)"
    },
    "paella": {
        "display_name": "Paella",
        "calories_per_serving": 450,
        "serving_description": "1 plate (~300 g)"
    },
    "pancakes": {
        "display_name": "Pancakes",
        "calories_per_serving": 175,
        "serving_description": "1 medium pancake (~60 g)"
    },
    "panna_cotta": {
        "display_name": "Panna Cotta",
        "calories_per_serving": 250,
        "serving_description": "1 ramekin (~120 g)"
    },
    "peking_duck": {
        "display_name": "Peking Duck",
        "calories_per_serving": 450,
        "serving_description": "1 serving with skin (~180 g)"
    },
    "pho": {
        "display_name": "Pho",
        "calories_per_serving": 350,
        "serving_description": "1 bowl (~400 g)"
    },
    "pizza": {
        "display_name": "Pizza",
        "calories_per_serving": 280,
        "serving_description": "1 slice (~100 g)"
    },
    "pork_chop": {
        "display_name": "Pork Chop",
        "calories_per_serving": 380,
        "serving_description": "1 chop (~180 g)"
    },
    "poutine": {
        "display_name": "Poutine",
        "calories_per_serving": 740,
        "serving_description": "1 plate fries + gravy + cheese (~350 g)"
    },
    "prime_rib": {
        "display_name": "Prime Rib",
        "calories_per_serving": 700,
        "serving_description": "1 large slice (~250 g)"
    },
    "pulled_pork_sandwich": {
        "display_name": "Pulled Pork Sandwich",
        "calories_per_serving": 550,
        "serving_description": "1 sandwich (~250 g)"
    },
    "ramen": {
        "display_name": "Ramen",
        "calories_per_serving": 480,
        "serving_description": "1 bowl (~400 g)"
    },
    "ravioli": {
        "display_name": "Ravioli",
        "calories_per_serving": 280,
        "serving_description": "8 pieces (~200 g)"
    },
    "red_velvet_cake": {
        "display_name": "Red Velvet Cake",
        "calories_per_serving": 360,
        "serving_description": "1 slice (~125 g)"
    },
    "risotto": {
        "display_name": "Risotto",
        "calories_per_serving": 320,
        "serving_description": "1 bowl (~220 g)"
    },
    "samosa": {
        "display_name": "Samosa",
        "calories_per_serving": 260,
        "serving_description": "2 medium pieces (~120 g)"
    },
    "sashimi": {
        "display_name": "Sashimi",
        "calories_per_serving": 150,
        "serving_description": "1 plate assorted (~150 g)"
    },
    "scallops": {
        "display_name": "Scallops",
        "calories_per_serving": 220,
        "serving_description": "6 seared scallops (~150 g)"
    },
    "seaweed_salad": {
        "display_name": "Seaweed Salad",
        "calories_per_serving": 110,
        "serving_description": "1 bowl (~100 g)"
    },
    "shrimp_and_grits": {
        "display_name": "Shrimp and Grits",
        "calories_per_serving": 520,
        "serving_description": "1 bowl (~300 g)"
    },
    "spaghetti_bolognese": {
        "display_name": "Spaghetti Bolognese",
        "calories_per_serving": 400,
        "serving_description": "1 plate (~250 g)"
    },
    "spaghetti_carbonara": {
        "display_name": "Spaghetti Carbonara",
        "calories_per_serving": 420,
        "serving_description": "1 plate (~250 g)"
    },
    "spring_rolls": {
        "display_name": "Spring Rolls",
        "calories_per_serving": 190,
        "serving_description": "2 fried rolls (~100 g)"
    },
    "steak": {
        "display_name": "Steak",
        "calories_per_serving": 680,
        "serving_description": "1 steak (~250 g)"
    },
    "strawberry_shortcake": {
        "display_name": "Strawberry Shortcake",
        "calories_per_serving": 320,
        "serving_description": "1 slice (~130 g)"
    },
    "sushi": {
        "display_name": "Sushi",
        "calories_per_serving": 300,
        "serving_description": "8 mixed pieces (~200 g)"
    },
    "tacos": {
        "display_name": "Tacos",
        "calories_per_serving": 230,
        "serving_description": "1 taco (~100 g)"
    },
    "takoyaki": {
        "display_name": "Takoyaki",
        "calories_per_serving": 350,
        "serving_description": "6 balls (~200 g)"
    },
    "tiramisu": {
        "display_name": "Tiramisu",
        "calories_per_serving": 240,
        "serving_description": "1 slice (~120 g)"
    },
    "tuna_tartare": {
        "display_name": "Tuna Tartare",
        "calories_per_serving": 220,
        "serving_description": "1 serving (~150 g)"
    },
    "waffles": {
        "display_name": "Waffles",
        "calories_per_serving": 290,
        "serving_description": "1 waffle (~75 g)"
    },
}


def get_food_info(label: str):
    """
    Returns (display_name, calories_per_serving, serving_description)
    or (None, None, None) if not found.
    """
    info = FOOD_CALORIES.get(label)
    if info is None:
        return None, None, None

    return (
        info["display_name"],
        info["calories_per_serving"],
        info["serving_description"],
    )



def get_food_info(label: str):
    """
    Returns (display_name, calories_per_serving, serving_description)
    or (None, None, None) if the food is not in the database.
    """
    info = FOOD_CALORIES.get(label)
    if info is None:
        return None, None, None

    return (
        info["display_name"],
        info["calories_per_serving"],
        info["serving_description"],
    )
