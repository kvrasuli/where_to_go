# Where to go

"Where to go" is a web application where points of interest are marked on an interactive map of Moscow. By clicking on them, you can see more information, photos, and contacts. 

### What it looks like
This app is deployed at https://rasuli.pythonanywhere.com. Check it out!

### How to run
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip3 install -r requirements.txt
```
Run the Django development server:
```
python manage.py runserver
```
Open https://127.0.0.1:8000 in your browser.

### How to edit data or fill the app database with new data using the admin site
- Open the admin site at https://127.0.0.1:8000/admin/
- Enter admin username and password (available on request)
- Click on "Places"
- Click on "Add place" in the upper right corner or choose an existing place
- Fill/edit the fields, upload photos
- Drug'n'drop the photo's fields to choose the order
- Click "Save"

### How to add new places using a console command
- Run the following command
```
python3 manage.py load_place [link to the new place json file]
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).