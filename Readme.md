# Django Blog Collaboration Guide

## Project Overview

This is a simple blog project built with Django. The backend is handled using Django, while the frontend is designed using pure HTML and CSS. The frontend work is done separately in the `frontend/` folder, and the backend team integrates it manually into Django.

## Project Structure

```
tsekpoe/
├── manage.py
│
├── frontend/                 # Your working directory (HTML & CSS only)
│   ├── css/
│   │   ├── responsive_styles.css
│   │   ├── styles.css
│   ├── design_guide/
│   │   ├── Post Card1.png
│   │   ├── tsekpoe-blog-designMain.png
│   │   ├── tsekpoe-blog-designPosts.png
│   ├── fonts/
│   │   ├── MILKER.OTF
│   ├── images/
│   ├── js/
│   ├── pages/
│   │   ├── main.html
│   │   ├── readme.md
│
├── tblog/                    # Django blog app (backend) (me)
│   ├── ....
│   ├── migrations/...
│   ├── static/...
│   │   │   ├── MILKER.OTF
│   ├── templates/...
│
└── tsekpoe/....              # Django project settings
```

## How We Work Together

1. **Frontend Developer:** Works in the `frontend/` folder and writes only HTML and CSS (no Django code needed).
2. **Backend Developer:** Manually copies and integrates the HTML files into Django's `templates/` and moves CSS, images, and JS into Django's `static/` folder.
3. **Version Control:** We use GitHub to push and pull updates. The frontend developer commits to `frontend/`, while the backend developer integrates changes into Django.

## Important Notes for the Frontend Developer

- Do not modify files inside `tblog/`.
- Keep all CSS in `frontend/css/`.
- Keep images in `frontend/images/`.
- Use relative paths for linking styles and images (e.g., `<link rel="stylesheet" href="css/style.css">`).

## Important Notes for the Backend Developer

- Move HTML files from `frontend/pages/` to `tblog/templates/` and add Django template tags (`{% %}` and `{{ }}`) where needed.
- Move CSS, JS, and images into `tblog/static/` and update file paths using `{% static %}`.
- Ensure Django can render the templates correctly after integration.

## Git Workflow

1. **Frontend Developer:**

   - Works on the `frontend/` folder.
   - Commits and pushes updates to GitHub.
   - Notifies the backend developer when changes are made.

2. **Backend Developer:**

   - Pulls the latest changes from GitHub.
   - Moves and integrates frontend files into Django.
   - Commits the changes to GitHub.

## Need Help?

If there are any questions, reach out in the project chat or issue tracker on GitHub or if you prefer, DM me

