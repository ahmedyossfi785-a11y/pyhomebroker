from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/facts')
def facts():
    banana_facts = [
        {
            'title': 'Bananas are Berries!',
            'description': 'Botanically speaking, bananas are classified as berries, while strawberries are not!'
        },
        {
            'title': 'Ancient Fruit',
            'description': 'Bananas have been around for thousands of years and are believed to be one of the first fruits cultivated by humans.'
        },
        {
            'title': 'Radioactive Fruit',
            'description': 'Bananas contain potassium-40, a radioactive isotope, making them slightly radioactive. But don\'t worry - it\'s completely safe!'
        },
        {
            'title': 'Float on Water',
            'description': 'Bananas are less dense than water, which means they can float!'
        },
        {
            'title': 'Banana Plants are Herbs',
            'description': 'The banana plant is actually a giant herb, not a tree. It can grow up to 25 feet tall!'
        },
        {
            'title': 'Global Production',
            'description': 'Over 100 billion bananas are consumed worldwide each year, making them one of the most popular fruits.'
        }
    ]
    return render_template('facts.html', facts=banana_facts)

@app.route('/nutrition')
def nutrition():
    nutrition_info = {
        'calories': 105,
        'carbs': '27g',
        'fiber': '3g',
        'protein': '1.3g',
        'potassium': '422mg',
        'vitamin_c': '10.3mg',
        'vitamin_b6': '0.4mg',
        'magnesium': '32mg'
    }
    benefits = [
        'Supports heart health with potassium',
        'Aids digestion with dietary fiber',
        'Provides quick energy from natural sugars',
        'Helps regulate blood pressure',
        'Supports immune system function',
        'May improve mood and reduce stress'
    ]
    return render_template('nutrition.html', nutrition=nutrition_info, benefits=benefits)

@app.route('/recipes')
def recipes():
    recipes_list = [
        {
            'name': 'Classic Banana Bread',
            'description': 'Moist and delicious homemade banana bread perfect for breakfast or snack time.',
            'ingredients': ['3 ripe bananas', '2 cups flour', '1 cup sugar', '2 eggs', '1/2 cup butter', '1 tsp baking soda', '1 tsp vanilla']
        },
        {
            'name': 'Banana Smoothie',
            'description': 'A creamy and refreshing smoothie packed with nutrients.',
            'ingredients': ['2 bananas', '1 cup milk', '1/2 cup yogurt', '1 tbsp honey', 'Ice cubes', 'Optional: berries or peanut butter']
        },
        {
            'name': 'Banana Pancakes',
            'description': 'Fluffy pancakes with natural banana sweetness.',
            'ingredients': ['2 ripe bananas', '2 eggs', '1/2 cup flour', '1 tsp baking powder', '1/4 tsp cinnamon', 'Butter for cooking']
        },
        {
            'name': 'Frozen Banana Bites',
            'description': 'A healthy frozen treat covered in chocolate.',
            'ingredients': ['3 bananas', '1 cup dark chocolate chips', '2 tbsp coconut oil', 'Optional toppings: nuts, sprinkles']
        }
    ]
    return render_template('recipes.html', recipes=recipes_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
