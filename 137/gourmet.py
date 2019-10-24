#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter, defaultdict
from operator import itemgetter

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

ALL_WINES = RED_WINES + WHITE_WINES + SPARKLING_WINES

wine_dict = {
    "red": RED_WINES,
    "white": WHITE_WINES,
    "sparkling": SPARKLING_WINES,
    "all": ALL_WINES,
}


def _similarity(wine, cheese):
    wine_counter = Counter(wine.lower())
    cheese_counter = Counter(cheese.lower())

    return sum((wine_counter & cheese_counter).values()) / (
        1 + pow(len(wine) - len(cheese), 2)
    )


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type not in ["white", "red", "sparkling", "all"]:
        raise ValueError
    best_scores = []
    for wine in wine_dict[wine_type]:
        best_scores.append(
            max(
                [(wine, cheese, _similarity(wine, cheese)) for cheese in CHEESES],
                key=itemgetter(2),
            )
        )
    return max(best_scores, key=itemgetter(2))


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    all_wine_scores = defaultdict(Counter)
    for wine in ALL_WINES:
        for cheese in CHEESES:
            all_wine_scores[wine][cheese] = _similarity(wine, cheese)

    top_wine_scores = []
    for wine in all_wine_scores:
        best_cheeses = sorted(
            all_wine_scores[wine].most_common(), key=lambda ch: (-ch[1], ch[0])
        )
        top_wine_scores.append(
            (wine, [sorted_cheese for sorted_cheese, score in best_cheeses[:5]])
        )

    return sorted(top_wine_scores)
