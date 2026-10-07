# Ayyoub's portfolio website
#### Video Demo: https://youtu.be/8TKxGn0SyCI
#### Description:

A personal portfolio website that presents who I am, what I can do and what I have built, with a contact form to get in touch. The goal was to build a complete, responsive site from scratch with a lightweight stack: no front-end framework, just HTML, CSS and vanilla JavaScript, served by a small Flask application.

The site is made of four pages:

- **About**: a short introduction with my name, a presentation and two buttons leading to the skills and projects pages.
- **Skills**: a set of cards describing my skills, next to an animated column of technology logos that scrolls vertically with a perspective and fade effect. On smaller screens it becomes a horizontal strip.
- **Projects**: a list of projects displayed as alternating bands, each with an automatically numbered counter, a description, technology tags and a link.
- **Contact**: a form (name, email, message). Submitted messages are validated on the server and stored in a SQLite database.

## Features

- Collapsible sidebar on desktop, with a smooth width transition.
- Bottom navigation bar on mobile, like a native app, with support for the safe area on phones with a gesture bar.
- Fluid layout built with `flexbox`, `grid` and `clamp()`, so text and spacing adapt to the screen size without many breakpoints.
- Staggered appearance animations on cards and project bands, disabled for users who prefer reduced motion.
- Contact form with server-side validation, flash messages, and form values preserved when there is an error.
- Navigation links generated from a single list, with the active page highlighted automatically.

## Tech stack

- **Front end:** HTML, CSS, vanilla JavaScript, Jinja templates, Font Awesome icons, Poppins and Yellowtail fonts.
- **Back end:** Python with Flask.
- **Database:** SQLite, accessed with the standard `sqlite3` module.

## Project structure

```
.
├── app.py              # Flask app, database connection and routes
├── app.db              # SQLite database (created on first run, not versioned)
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (not versioned)
├── .gitignore
├── static/
│   ├── styles.css      # All the styles, including responsive rules
│   ├── main.js         # Sidebar toggle
│   └── illustration.png
└── templates/
    ├── base.html       # Layout shared by every page: sidebar and navigation
    ├── index.html      # About page
    ├── skills.html
    ├── projects.html
    └── contact.html
```

## How it works

- `app.py` creates the Flask app, opens the SQLite database and creates the `messages` table if it does not exist. Each page has its own route, and `/contact` accepts both GET (display the form) and POST (validate and save the message).
- The messages table stores an id, the sender's name, email, the message and the date it was sent.
- Every template extends `base.html`, which contains the sidebar. The navigation links are defined in a single list, and the `active` class is set by comparing each link with the current route.
- The sidebar logic is only a class toggle in `main.js`. The animation itself is done in CSS with a transition, which keeps the JavaScript minimal.

## Design choices

- **No front-end framework.** The site is small and mostly static, so plain HTML, CSS and JavaScript keep it fast and easy to maintain.
- **SQLite.** The only dynamic feature is the contact form. A single file database needs no server and is enough for this use.
- **Post/Redirect/Get on the contact form.** After a successful submission the user is redirected, which prevents the message from being sent twice if the page is refreshed.
- **CSS-driven animations.** The logo scroller, the card transitions and the sidebar all use CSS, with no animation library.
- **Accessibility.** Buttons are real `<button>` elements, icon-only controls have labels, and decorative elements are hidden from screen readers.

## Run it locally

```bash
git clone <repository-url>
cd <project-folder>

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file at the root of the project:

```
SECRET_KEY=change-me
FLASK_DEBUG=1
FLASK_RUN_PORT=5001
```

Then start the server:

```bash
flask run
```

The site is available at http://127.0.0.1:5001. The `app.db` file is created automatically on the first run.

To read the messages received through the contact form:

```bash
sqlite3 app.db "SELECT * FROM messages;"
```

## Possible improvements

- A protected admin page to read the messages in the browser.
- A `projects` table so projects can be managed from the database.
- Spam protection on the contact form.
- A light theme.
