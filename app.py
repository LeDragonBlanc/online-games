from supabase import create_client, Client
from dotenv import dotenv_values
from flask import Flask, render_template


KEYS = dotenv_values('.env')
# Vos informations Supabase
supabase_url = KEYS['SUPABASE_URL']
supabase_key = KEYS['SUPABASE_KEY']

# Créer un client Supabase
supabase: Client = create_client(supabase_url, supabase_key)

response = supabase.table("games").select("*").execute()

app = Flask(__name__)

# Données fictives des cartes avec des URLs pour redirection
cards_data = response.data
for card in cards_data:
    if not card['image_url']:
        card['image_url'] = 'https://via.placeholder.com/300x200'

@app.route('/')
def index():
    return render_template('index.html', cards=cards_data)

if __name__ == '__main__':
    app.run(debug=True)
