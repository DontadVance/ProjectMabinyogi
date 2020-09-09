# Vince
### (9/7/20)
- should we consider getting rid of the "char_" for form data variables?
- added a utils file to handle utility functions
- form data successfully routes to db according to class
- starting on asset creation


# Dylan
### Learning Flask
- added a .gitignore file; feel free to edit.
- initiated templates and Jinja-friendly CSS links
- added a static folder for CSS
- added default.html; we can use this as our 'base' template. index.html extends default.html.

### (9/1/2020)
- added an 'about' page with route
- making modifications to the index page, which will serve as our primary page for character creation;
need to discuss and outline potential layouts before implementation.
- **Note: May need to reload page + cache for proper updates. (Shift-Ctrl-R on Chrome).**

### (9/3/2020)
- Added a "create" page with route (form.html)
- Migrated character creation from index.html to form.html
- Added WTForm inputs for Name, Stature, Race, Class + Input Validation.
- Modified cluster.py to use an alternative reference; please feel free to change this if you need to! Just make sure it works (I couldn't get the previous format to work).
- Added basic/temporary insertion of web form data into the MongoDB Warrior collection. I did this in order to verify that the web forms were working correctly + for understanding. No guarantee of good practice or implementation!
- Extensive modification to HTML/CSS

### (9/9/2020)
- Added content to index.html and about.html
- Added CSS classes for displaying content
- Added CSS animations for fade-in

# General
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

## MongoDB Notes
- Clusters hold databases
- Databases store collections, which are simply collections of data e.g. restaurants
- Collections store documents, which are entries to the databases
- Indexing will be incredibly useful for debugging and small applications
- Aggregation is where the real fun is at, we can filter and analyze the data based on a given set of criteria. We can use different operators to filter
- **Note:** the default foreign key for documents seem to be "_id" and should be specified, if they aren't, it assigns an object id

- **Querying results are sent back as Pymongo Cursor objects**
  - look into how to interact with said results

- To delete everything from a collection just use "collection.delete_many({})"
- to drop a collection: db.collection_name.drop() ; returns true if one exists, else false
