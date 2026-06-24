<p align="center">
  <img src="static/logo.png" alt="sk8e-stuff logo" width="200">
</p>

<h1 align="center">sk8e-stuff</h1>

<p align="center">A Django e-commerce site for a skate shop — catalog, cart, blog, and a REST API.</p>

---

## Features

- **Catalog** — categories (tree-structured), products with multiple images, stock & pricing
- **Cart & checkout** — add to cart, edit cart, place order
- **Blog** — categories, tags, comments (moderated)
- **Accounts** — custom user model with phone & avatar
- **Content pages** — flat pages, homepage carousels, global site settings
- **REST API** — catalog, blog, and login endpoints under `/api/`

## Stack

| | |
|---|---|
| Backend | Django 3.2, DRF |
| Database | PostgreSQL |
| Images | Pillow, django-imagekit |
| Editor | TinyMCE |
| Categories | django-mptt |
| Frontend | Django templates, Owl Carousel, Lightbox |

## Structure

```
config/      settings, root urls
apps/
  main/      home, pages, carousels, site settings
  catalog/   categories, products, images
  order/     cart & checkout
  user/      custom user, auth
  blog/      articles, tags, comments
  api/       DRF endpoints
templates/   HTML, per app
static/      CSS, images, vendor JS
media/       uploads
data/        seed JSON (pages, settings)
```

## Setup

```bash
pip install -r requirements.txt
```

Create a PostgreSQL DB matching `config/settings.py`:

```python
NAME = 'sk8e_stuff_db'
USER = 'sk8e_stuff_db_user'
PASSWORD = '1'
```

Then:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Site: `127.0.0.1:8000` · Admin: `127.0.0.1:8000/admin`

Optional seed data:

```bash
python manage.py loaddata data/settings.json
```

## Routes

| Path | Page |
|---|---|
| `/` | Home |
| `/catalog/` `/catalog/<slug>/` `/catalog/product/<id>/` | Categories → products → detail |
| `/order/cart/` `/order/add/` `/order/create/` | Cart & checkout |
| `/blog/` `/blog/<cat_id>/` `/blog/<cat_id>/<id>/` | Categories → articles → detail |
| `/user/login/` `/register/` `/logout/` | Auth |
| `/api/...` | REST API |
| `/admin/` | Admin |
| `/<slug>/` | Flat pages (catch-all) |
