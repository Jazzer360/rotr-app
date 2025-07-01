import reflex as rx

from ..components.navbar import NavState
from ..template import template


vendors = [
    {
        'vendor': 'Aroi Thai Cuisine',
        'menu': [
            {
                'item': 'Orange Chicken',
                'price': '$10',
                'desc': """
                    Jasmine Rice, Batter (Rice Flour, Water), Green Onion,
                    Sesame Seed, Homemade Sauce
                """
            },
            {
                'item': 'Pad Thai',
                'desc': """
                    Yellow Onion, Green Onion, Egg, Rice Noodle, Bean Sprout,
                    Cabbage, Homemade Sauce
                """,
                'options': [
                    {
                        'option': 'Chicken',
                        'price': '$10'
                    },
                    {
                        'option': 'Beef',
                        'price': '$11'
                    },
                    {
                        'option': 'Shrimp',
                        'price': '$12'
                    }
                ]
            },
            {
                'item': 'Thai Fried Rice',
                'desc': """
                    Jasmine Rice, Carrot, Egg, Black Soy Sauce (Sweet),
                    Homemade Sauce
                """,
                'options': [
                    {
                        'option': 'Chicken',
                        'price': '$10'
                    },
                    {
                        'option': 'Beef',
                        'price': '$11'
                    },
                    {
                        'option': 'Shrimp',
                        'price': '$12'
                    }
                ]
            },
            {
                'item': 'Pad Kee Mao',
                'desc': """
                    Carrot, Yellow Onion, Green Onion, Wide Rice Noodle,
                    Green Bell Pepper, Sweet Bell Pepper, Broccoli, Basil,
                    Homemade Sauce
                """,
                'options': [
                    {
                        'option': 'Chicken',
                        'price': '$10'
                    },
                    {
                        'option': 'Beef',
                        'price': '$11'
                    },
                    {
                        'option': 'Shrimp',
                        'price': '$12'
                    }
                ]
            },
            {
                'item': 'Pad See Ew',
                'desc': """
                    Carrot, Yellow Onion, Wide Rice Noodle, Broccoli, Egg,
                    Homemade Sauce
                """,
                'options': [
                    {
                        'option': 'Chicken',
                        'price': '$10'
                    },
                    {
                        'option': 'Beef',
                        'price': '$11'
                    },
                    {
                        'option': 'Shrimp',
                        'price': '$12'
                    }
                ]
            },
            {
                'item': 'Egg Rolls',
                'desc': """
                    Pork, Pastry Wrap, Cabbage, Carrot, Yellow Onion, Egg,
                    Bean Thread, Homemade Sauce
                """,
                'price': '4 for $7'
            },
            {
                'item': 'Crab Rangoon',
                'desc': """
                    Imitation Crab, Cream Cheese, Garlic Powder, Onion Powder,
                    Green Onion, Wonton Wrap, Homemade Sauce
                """,
                'price': '4 for $7'
            },
            {
                'item': 'Jasmine Rice',
                'price': '$2'
            },
            {
                'item': 'Bubble Tea',
                'price': '$5',
                'desc': """
                    Ice, 2% Milk, Flavor Powder, Sugar, Coffee Creamer,
                    Tapioca Pearls, Whipped Cream
                """
            },
            {
                'item': 'Thai Tea',
                'price': '$3',
                'desc': """
                    Thai Tea, Water, Sugar, Heavy Cream
                """
            },
            {
                'item': 'Water',
                'price': '$1'
            }
        ]
    },
    {
        'vendor': 'Cheese Carriage',
        'menu': [
            {
                'item': 'Cheese Curds',
                'price': '$8'
            },
            {
                'item': 'Corn Dog',
                'price': '$6'
            },
            {
                'item': 'Pop & Water',
                'price': '$3'
            }
        ]
    },
    {
        'vendor': 'The Cup Truck',
        'menu': [
            {
                'item': "The 'Simp' Smashie",
                'desc': """
                    1/4lb custom blended Welcome Meats' beef n' bacon smash
                    burger served on a brioche bun.  Add an extra patty and/or
                    enjoy with American cheese!"""
            },
            {
                'item': 'The Fancified Smashie',
                'desc': """
                    This 1/4lb custom-blended Welcome Meats' beef n' bacon
                    smashburger is topped with Gruyere cheese, arugula n' dried
                    cherry compote n' served on a brioche bun.  Stop drooling
                    on your screens n' come see us at the truck.
                """
            },
            {
                'item': 'The Ultimate Smashie',
                'desc': """
                    We're not foolin' around with this one!  Double 1/4lb
                    patties layered with red onion, American cheese, Cup Truck
                    secret sauce n' smashed again on a brioche bun.
                """
            },
            {
                'item': 'Burnt End Wein!',
                'desc': """
                    What can we say?  This all-beef burnt end dog aims to
                    please!

                    Try our "Top Shelf Wein": Topped with pineapple relish n'
                    shiracha mayo.  It's like no other wein!
                """
            },
            {
                'item': 'Chopped Italian Sammie',
                'desc': """
                    Watch your drool for this one...hoagie bun stuffed with
                    diced mortadella, capicola, red onion, tomato,
                    pepperoncini, smoked Gouda cheese, lettuce n' italian mayo!
                """
            },
            {
                'item': 'Not Average Egg Salad Sammie',
                'desc': """
                    Slow your scroll....This is NOT your average egg salad.
                    Hard boiled eggs tossed with capers, shallots, parsley,
                    Welcome Meat's bacon, parmesan-black garlic dressing n'
                    arugula, piled on a hoagie bun.  Even Grandma will be
                    impressed!
                """
            },
            {
                'item': 'Wingy Dingy',
                'desc': """
                    Just because it's fun to say.

                    4 wing n' drummies tossed in a chipotle-peach
                    glaze....What's not to love?
                """
            },
            {
                'item': 'Seasoned Shoestring fries',
                'desc': """
                    Fried to perfection n' seasoned with Seth's pantry of
                    spices.
                """
            },
            {
                'item': 'Fancy fries',
                'desc': """
                    Fried to perfection n' topped with bacon n' cheese.  What
                    could be better?
                """
            },
            {
                'item': 'Fancy Pants Cheesy Mac',
                'desc': """
                    Not your 'pedestrian' mac n' cheese.  Smoked Gouda n'
                    American cheese topped with a special crunch
                """
            },
            {
                'item': 'Farro-Arugula salad',
                'desc': """
                    Peppery arugula meets nutty farro in this bold, bitey salad
                    that eats like it means it.!
                """
            },
            {
                'item': 'Funfetti Cupcake',
                'desc': """
                    Addie whips these cupcakes up from scratch n' donates $.50
                    from every cupcake to a local non-profit!
                """
            },
            {
                'item': 'kookies for kidneys - Chocolate Chip Kookie',
                'desc': """
                    Inspired by her sister, Parker is raising money for a cause
                    close to her heart...n' kidneys!  Try Parker's Kookies for
                    Kidneys!  This week's flavor is chocolate chip.
                    \n
                    **Parker received a life-saving kidney transplant at 6
                    years old.  At 7, she is now raising money for CKD
                    research!**
                """
            },
            {
                'item': 'Local Rhubarb crisp',
                'desc': """
                    No one is sad about rhubarb season!  Enjoy this fresh n'
                    local rhubarb crisp baked perfectly in a 5-inch round pan.
                    Enough for 2 people, or 1 lover of rhubarb!
                """
            },
            {
                'item': 'Oreo pop',
                'desc': """
                    Think cake-pop, but made with crushed Oreos on a stick with
                    crunchy chocolate coating.
                """
            },
            {
                'item': "Reece's peanut butter cup Ice cream Cake",
                'desc': """
                    Crushed Oreo base, homemade chocolate layer topped with
                    creamy Reese's Peanut Butter Cup ice cream n' more crushed
                    Oreos n' homemade chocolate sauce.
                """
            },
            {
                'item': 'Local Strawberry Buttermilk ice cream',
                'desc': """
                    Sun-kissed June n' everbearing strawberries picked fresh
                    from our garden, churned with sweet n' creamy buttermilk
                    into frozen perfection.
                """
            }
        ]
    },
    {
        'vendor': "Ole's Gathering Place",
        'menu': [
            {
                'item': 'Smoked Pork Sandwich',
                'price': '$8',
                'options': [
                    {
                        'option': 'w/ coleslaw, smoked baked beans',
                        'price': '$12'
                    }
                ]
            },
            {
                'item': 'Smoked Brisket Sandwich',
                'price': '$10',
                'options': [
                    {
                        'option': 'w/ coleslaw, smoked baked beans',
                        'price': '$14'
                    }
                ]
            },
            {
                'item': 'Queso Bacon Mac and Cheese',
                'price': '$10',
                'options': [
                    {
                        'option': 'w/ pork',
                        'price': '$12'
                    },
                    {
                        'option': 'w/ brisket',
                        'price': '$14'
                    }
                ]
            },
            {
                'item': 'Queso Nachos (onion, tomato, jalapeno)',
                'price': '$10',
                'options': [
                    {
                        'option': 'w/ pork',
                        'price': '$12'
                    },
                    {
                        'option': 'w/ brisket',
                        'price': '$14'
                    }
                ]
            },
            {
                'item': 'Oledelphia (pork)',
                'price': '$12'
            },
            {
                'item': 'Oledelphia (brisket)',
                'price': '$14',
                'options': [
                    {
                        'option': 'w/ coleslaw, smoked baked beans',
                        'price': '$16'
                    }
                ]
            },
            {
                'item': 'Side of colelsaw, smoked baked beans',
                'price': '$3'
            },
            {
                'item': 'Pepsi, Mt. Dew, Dr. Pepper, Diet Dr. Pepper',
                'price': '$1'
            }
        ]
    },
    {
        'vendor': 'TNT Indian Style Tacos',
        'menu': [
            {
                'item': 'Indian Taco',
                'options': [
                    {
                        'option': 'w/ Seasoned Beef',
                        'price': '$10'
                    },
                    {
                        'option': 'w/ Pinto Beans',
                        'price': '$10'
                    },
                    {
                        'option': 'w/ Beef & Beans',
                        'price': '$11'
                    }
                ]
            },
            {
                'item': 'Taco Salad w/ Seasoned Beef',
                'price': '$10'
            },
            {
                'item': 'Nacho Supreme w/ Seasoned Beef',
                'price': '$10'
            },
            {
                'item': 'Nachos (Chips & Cheese)',
                'price': '$6'
            },
            {
                'item': 'Elephant Ear (Fry Bread)',
                'price': '$5',
                'options': [
                    {
                        'option': 'w/ Ice Cream',
                        'price': '$7'
                    }
                ]
            },
            {
                'item': 'Pop & Water',
                'price': '$2'
            }
        ]
    }
]


def menu_item(item: dict) -> rx.Component:
    if 'options' in item:
        options = [menu_option(option) for option in item.get('options')]
    else:
        options = None
    desc = item['desc'] if 'desc' in item else None
    return rx.box(
        rx.hstack(
            rx.text(item.get('item'), size='3'),
            rx.spacer(),
            rx.text(item.get('price'), size='3')
        ),
        rx.text(
            desc,
            size='2',
            margin_left='2em',
            font_style='italic'
        ),
        options,
        width='100%'
    )


def menu_option(option: dict):
    return rx.hstack(
        rx.spacer(),
        rx.text(option.get('option'), margin_left='1em'),
        rx.text(option.get('price')),
    )


def vendor_item(menu: dict) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.card(
                rx.heading(menu.get('vendor'), margin_bottom='1em'),
                rx.vstack(
                    [menu_item(item) for item in menu.get('menu')]
                ),
                width='100%'
            ),
            align='center'
        ),
        size='1',
        padding='8px',
        width='100%'
    )


@rx.page(
    route='/food',
    title='Food Vendors',
    on_load=NavState.update)
@template
def schedule() -> rx.Component:
    return rx.box(
        [vendor_item(vendor) for vendor in vendors],
        width='100%',
        align='center'
    )
