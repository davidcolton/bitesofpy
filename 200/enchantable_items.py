from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"

roman_numbers = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5}


@dataclass
class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """

    id_name: str
    name: str
    max_level: int
    description: str
    items: list = field(default_factory=list)

    def __str__(self):
        return f"{self.name} ({self.max_level}): {self.description}"


@dataclass
class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    name: str
    enchantments: list = field(default_factory=list)

    def __str__(self):
        title_name = self.name.replace("_", " ").title()

        # List of enhancements
        enhancements_list = sorted(
            [(e.max_level, e.id_name) for e in self.enchantments], key=lambda x: x[1]
        )

        # Build the print string
        # Start with the Title Name
        print_str = [f"{title_name}: "] + [
            f"  [{e[0]}] {e[1]}" for e in enhancements_list
        ]

        return "\n".join(print_str)


def _clean_items(items):
    strings_to_remove = ["enchanted_", "iron_", "_sm", ".png"]
    for token in strings_to_remove:
        items = items.replace(token, "")
    # Handle fishing_rod
    items = items.replace("fishing_rod", "fishing-rod")
    items_list = items.split("_")
    # Un-handle fishing-rod
    items_list = [w.replace("fishing-rod", "fishing_rod") for w in items_list]
    return items_list


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    enchantment_dict = dict()

    minecraft_items = soup.find("table", {"id": "minecraft_items"})
    minecraft_rows = minecraft_items.find_all("tr")
    for row in minecraft_rows[1:]:
        # Extract the Enchantment details
        cells = row.find_all("td")
        name, id_name = cells[0].text[:-1].split("(")
        max_level = roman_numbers[cells[1].text]
        title = cells[2].text
        items = _clean_items(cells[4].img["data-src"].split("/")[-1])

        # Add the Enchantment Class to the dictionary
        enchantment_dict[id_name] = Enchantment(
            id_name=id_name,
            name=name,
            max_level=max_level,
            description=title,
            items=items,
        )

    return enchantment_dict


def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """

    temp_dict = defaultdict(list)
    for enchantment in data.values():
        for item in enchantment.items:
            temp_dict[item].append(enchantment)

    # Construct the return dictionary
    items_dict = {}
    for key, value in temp_dict.items():
        items_dict[key] = Item(name=key)
        items_dict[key].enchantments.extend(value)
    return items_dict

    return items_dict


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""
