from flask import Flask, render_template, request

app = Flask(__name__)

# Sample gift ideas
gift_ideas = [
    {"name": "Art Set", "age_range": (10, 18), "interests": ["art", "drawing"], "personality": "creative", "price": 25},
    {"name": "Wireless Earbuds", "age_range": (15, 30), "interests": ["music", "tech"], "personality": "logical", "price": 50},
    {"name": "Chess Set", "age_range": (10, 80), "interests": ["games", "strategy"], "personality": "logical", "price": 20},
    {"name": "Aromatherapy Kit", "age_range": (18, 60), "interests": ["wellness", "relaxation"], "personality": "creative", "price": 30},
    {"name": "Notebook Set", "age_range": (12, 35), "interests": ["writing", "journaling"], "personality": "creative", "price": 15},
    {"name": "Smart Watch", "age_range": (18, 50), "interests": ["tech", "fitness"], "personality": "logical", "price": 80},
    {"name": "Customized Mug", "age_range": (10, 70), "interests": ["coffee", "fun"], "personality": "creative", "price": 10}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    age = int(request.form['age'])
    interests = request.form['interests'].lower().split(',')
    personality = request.form['personality'].lower()
    budget = float(request.form['budget'])

    # Filter and recommend gifts
    recommendations = []
    for gift in gift_ideas:
        if gift['age_range'][0] <= age <= gift['age_range'][1] \
           and any(interest.strip() in gift['interests'] for interest in interests) \
           and gift['personality'] == personality \
           and gift['price'] <= budget:
            recommendations.append(gift)

    return render_template('results.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)