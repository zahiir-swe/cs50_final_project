# Ayyoub's portfolio website
#### Video Demo:  <URL HERE>
#### Description:
A personal portfolio website presenting who I am, my skills and my projects, with a contact form to get in touch.

The site has a responsive sidebar that collapses to icons on desktop and turns into a bottom navigation bar on mobile. It is made of four pages: **About**, **Skills**, **Projects** and **Contact**. Messages sent through the contact form are stored in a SQLite database.

**Tech stack:** HTML, CSS and vanilla JavaScript on the front end, Flask (Python) on the back end, and SQLite for the database.

#### Run it locally:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
flask run
```