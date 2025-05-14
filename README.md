# castle_apartments
```bash
git clone https://github.com/<org>/castle-apartments.git
cd castle-apartments
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# copy env file and fill in secrets
cp .env.example .env
# open .env and add: DJANGO_SECRET_KEY=…  DATABASE_URL=…

python manage.py migrate
python manage.py runserver