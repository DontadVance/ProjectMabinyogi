# Vince
## Learning Flask
- read the comments provided on routes.py
- place any HTML files to render in our project's templates folder, this is a common Flask practice as flask will look for this directory
when using render_template and it saves us time on specifying the file path
- in similar fashion, the CSS files should go within the static folder
- **NOTE: I highly recommend starting with a layout HTML file that we can extend to the rest of our files**
  - Jinga (Flask's Python HTML templating language) provides easy HTML inheritance
    - e.g. the layout page may contain something all pages share in common, such as a navbar or a footer
  - not sure if we'll need more than 1-2 pages but it's a good practice to have
- **ACCESSING SITE:**
  - I've gone ahead and set up a placeholder HTML file so that the site will run on initial run
  - Navigate to the project folder and run "run.py"
  - the site will be at "localhost:5000/" where the / specifies our route

  
# Dylan
## Learning Flask
- added a .gitignore file; feel free to edit.
- initiated templates and Jinja-friendly CSS links
- added a static folder for CSS
- added default.html; we can use this as our 'base' template. index.html extends default.html.

## (9/1/2020)
- added an 'about' page with route
- making modifications to the index page, which will serve as our primary page for character creation;
need to discuss and outline potential layouts before implementation.
- **Note: May need to reload page + cache for proper updates. (Shift-Ctrl-R on Chrome).
