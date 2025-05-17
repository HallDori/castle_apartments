# castle_apartments

```bash
# Unzip the archive wherever you like
unzip castle_apartments.zip
cd castle-apartments
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# copy env file and fill in secrets
cp .env.example .env
# open .env and add: DJANGO_SECRET_KEY=…  DATABASE_URL=…  You can find them in settings.py

python manage.py migrate
python manage.py runserver

# if you want to add data to the website or look at the database then you can go to /admin
#create a super user for admin privalidges
python manage.py createsuperuser

#if you want to log in as a normal user try
username: goblin
psw: #abc12345

#then log in with on another browser like incognito
#This is Rick grimes
username: John 
psw: #abc1235

#This is Walter white
username: Halli
psw:123

#this is Michael
username: seller1
psw:#abc12345

#this allows you to test the purchase offer and the finalisation, the seller can accept or reject
#Extra req
#You can link a seller to a user, when a user that is considered a seller logs in, he sees in his nav bar
#seller dashboard which lets the seller look at the offers to their property, there the seller sees the info
#of the purchase_offer and there he can accept or deny it 
#that updates it for the buyer and he either sees rejected or he can finalise the order
#initialise also allows the user to try again if the user leaves mid process, if he has completed it
#then it will say that it is done