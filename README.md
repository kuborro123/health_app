recipe_app/                    # Your main project folder
├── app.py                     # Main Flask application
├── config.py                  # Configuration settings  
├── requirements.txt           # Python dependencies
├── models/                    # Database models
│   ├── __init__.py
│   ├── recipe.py             # Recipe model
│   ├── ingredient.py         # Ingredient model
│   ├── user.py               # User model
│   └── nutrition.py          # For macro tracking
├── scrapers/                  # Web scraping modules
│   ├── __init__.py
│   ├── base_scraper.py       # Base scraper class
│   ├── allrecipes_scraper.py # AllRecipes scraper
│   └── bbc_scraper.py        # BBC Good Food scraper
├── api/                       # API routes
│   ├── __init__.py
│   ├── recipes.py            # Recipe CRUD operations
│   ├── ingredients.py        # Ingredient operations
│   └── nutrition.py          # Macro tracking
├── utils/                     # Utility functions
│   ├── __init__.py
│   ├── usda_nutrition.py     # USDA API integration
│   └── helpers.py            # General helper functions
├── static/                    # Frontend files (CSS, JS)
│   ├── css/
│   ├── js/
│   └── images/
└── templates/                 # HTML templates
    ├── base.html
    ├── index.html
    └── recipes/
        ├── list.html
        └── detail.html
