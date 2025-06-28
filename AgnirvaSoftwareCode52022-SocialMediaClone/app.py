# app.py
import os  # Importing the os module to interact with the operating system (Commented by Agnirva.com)
from flask import Flask, render_template, redirect, url_for, request, flash  # Importing necessary Flask functions for handling routes and templates (Commented by Agnirva.com)
from flask_sqlalchemy import SQLAlchemy  # Importing SQLAlchemy for database integration (Commented by Agnirva.com)
from flask_login import (
    LoginManager,  # Importing LoginManager to manage user sessions (Commented by Agnirva.com)
    login_user,  # Importing login_user to log a user into the session (Commented by Agnirva.com)
    login_required,  # Importing login_required to protect routes from unauthorized access (Commented by Agnirva.com)
    logout_user,  # Importing logout_user to log a user out of the session (Commented by Agnirva.com)
    UserMixin,  # Importing UserMixin to easily handle user authentication (Commented by Agnirva.com)
    current_user,  # Importing current_user to get information about the logged-in user (Commented by Agnirva.com)
)
from werkzeug.security import generate_password_hash, check_password_hash  # Importing functions to securely hash and check passwords (Commented by Agnirva.com)
from werkzeug.utils import secure_filename  # Importing secure_filename to safely handle file names (Commented by Agnirva.com)
from datetime import datetime  # Importing datetime to handle date and time (Commented by Agnirva.com)

# Configuration (Commented by Agnirva.com)
AgnirvaApp = Flask(__name__)  # Initialize Flask application (Commented by Agnirva.com)
AgnirvaApp.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a real secret key (Commented by Agnirva.com)
AgnirvaApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instagram_clone.db'  # URI for the database connection (Commented by Agnirva.com)
AgnirvaApp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking to save resources (Commented by Agnirva.com)
AgnirvaApp.config['UPLOAD_FOLDER'] = 'static/uploads'  # Folder to store uploaded files (Commented by Agnirva.com)
AgnirvaApp.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # Define the allowed file extensions for uploads (Commented by Agnirva.com)

# Initialize extensions (Commented by Agnirva.com)
AgnirvaDB = SQLAlchemy(AgnirvaApp)  # Initialize the database extension (Commented by Agnirva.com)
AgnirvaLoginManager = LoginManager()  # Initialize the login manager for user authentication (Commented by Agnirva.com)
AgnirvaLoginManager.login_view = 'login'  # Specify the login endpoint to redirect unauthenticated users (Commented by Agnirva.com)
AgnirvaLoginManager.init_app(AgnirvaApp)  # Bind the login manager to the Flask app (Commented by Agnirva.com)

# Models (Commented by Agnirva.com)
class AgnirvaUser(UserMixin, AgnirvaDB.Model):
    __tablename__ = 'agnirvauser'  # Explicitly set table name (Commented by Agnirva.com)
    id = AgnirvaDB.Column(AgnirvaDB.Integer, primary_key=True)  # Primary key column for the user (Commented by Agnirva.com)
    username = AgnirvaDB.Column(AgnirvaDB.String(150), nullable=False, unique=True)  # Unique username column (Commented by Agnirva.com)
    password = AgnirvaDB.Column(AgnirvaDB.String(150), nullable=False)  # Password column (Commented by Agnirva.com)
    posts = AgnirvaDB.relationship('AgnirvaPost', backref='author', lazy=True)  # One-to-many relationship with AgnirvaPost (Commented by Agnirva.com)

class AgnirvaPost(AgnirvaDB.Model):
    __tablename__ = 'agnirvapost'  # Explicitly set table name (Commented by Agnirva.com)
    id = AgnirvaDB.Column(AgnirvaDB.Integer, primary_key=True)  # Primary key column for the post (Commented by Agnirva.com)
    image_file = AgnirvaDB.Column(AgnirvaDB.String(150), nullable=False, default='default.jpg')  # Image file path for the post (Commented by Agnirva.com)
    caption = AgnirvaDB.Column(AgnirvaDB.Text, nullable=True)  # Caption for the post (optional) (Commented by Agnirva.com)
    likes = AgnirvaDB.Column(AgnirvaDB.Integer, default=0)  # Like counter for the post (Commented by Agnirva.com)
    user_id = AgnirvaDB.Column(AgnirvaDB.Integer, AgnirvaDB.ForeignKey('agnirvauser.id'), nullable=False)  # Foreign key reference to AgnirvaUser (Commented by Agnirva.com)
    comments = AgnirvaDB.relationship('AgnirvaComment', backref='post', lazy=True)  # One-to-many relationship with AgnirvaComment (Commented by Agnirva.com)

class AgnirvaComment(AgnirvaDB.Model):
    __tablename__ = 'agnirvacomment'  # Explicitly set table name (Commented by Agnirva.com)
    id = AgnirvaDB.Column(AgnirvaDB.Integer, primary_key=True)  # Primary key column for the comment (Commented by Agnirva.com)
    content = AgnirvaDB.Column(AgnirvaDB.Text, nullable=False)  # Content of the comment (Commented by Agnirva.com)
    post_id = AgnirvaDB.Column(AgnirvaDB.Integer, AgnirvaDB.ForeignKey('agnirvapost.id'), nullable=False)  # Foreign key reference to AgnirvaPost (Commented by Agnirva.com)
    user_id = AgnirvaDB.Column(AgnirvaDB.Integer, AgnirvaDB.ForeignKey('agnirvauser.id'), nullable=False)  # Foreign key reference to AgnirvaUser (Commented by Agnirva.com)

    user = AgnirvaDB.relationship('AgnirvaUser', backref='comments')  # Relationship to AgnirvaUser (Commented by Agnirva.com)

# User loader for Flask-Login (Commented by Agnirva.com)
@AgnirvaLoginManager.user_loader  # Decorator to load user by ID (Commented by Agnirva.com)
def AgnirvaLoadUser(user_id):
    return AgnirvaUser.query.get(int(user_id))  # Query the database for user by ID and return the result (Commented by Agnirva.com)

# Context processor to inject current year into templates (Commented by Agnirva.com)
@AgnirvaApp.context_processor  # Decorator to create context for templates (Commented by Agnirva.com)
def inject_current_year():
    return {'current_year': datetime.utcnow().year}  # Inject current year into the template context (Commented by Agnirva.com)

# Helper function to check allowed file extensions (Commented by Agnirva.com)
def AgnirvaAllowedFile(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in AgnirvaApp.config['ALLOWED_EXTENSIONS']  # Ensure the extension is allowed (Commented by Agnirva.com)

# Routes (Commented by Agnirva.com)
@AgnirvaApp.route('/', endpoint='index')  # Define route for the homepage (Commented by Agnirva.com)
def AgnirvaIndex():
    Agnirvaposts = AgnirvaPost.query.order_by(AgnirvaPost.id.desc()).all()  # Retrieve all posts ordered by ID in descending order (Commented by Agnirva.com)
    return render_template('index.html', posts=Agnirvaposts)  # Render the index page with posts (Commented by Agnirva.com)

@AgnirvaApp.route('/register', methods=['GET', 'POST'], endpoint='register')  # Defining the route for user registration (Commented by Agnirva.com)
def AgnirvaRegister():
    if request.method == 'POST':  # Check if the form is submitted using POST method (Commented by Agnirva.com)
        Agnirvauusername = request.form.get('username')  # Get the username entered by the user (Commented by Agnirva.com)
        Agnirvapassword = request.form.get('password')  # Get the password entered by the user (Commented by Agnirva.com)

        # Check if the username already exists in the database (Commented by Agnirva.com)
        if AgnirvaUser.query.filter_by(username=Agnirvauusername).first():
            flash('Username already exists.')  # Inform the user that the username is already taken (Commented by Agnirva.com)
            return redirect(url_for('register'))  # Redirect the user back to the registration page (Commented by Agnirva.com)

        # Hash the password using SHA256 to store it securely (Commented by Agnirva.com)
        Agnirvahashed_password = generate_password_hash(Agnirvapassword, method='sha256')  # Generate a hashed password (Commented by Agnirva.com)
        
        # Create a new user object with the provided username and hashed password (Commented by Agnirva.com)
        Agnirvanew_user = AgnirvaUser(username=Agnirvauusername, password=Agnirvahashed_password)  # Create a new user instance (Commented by Agnirva.com)

        AgnirvaDB.session.add(Agnirvanew_user)  # Add the new user to the session (Commented by Agnirva.com)
        AgnirvaDB.session.commit()  # Commit the changes to the database (Commented by Agnirva.com)

        flash('Registration successful. Please log in.')  # Notify the user that registration was successful (Commented by Agnirva.com)
        return redirect(url_for('login'))  # Redirect the user to the login page (Commented by Agnirva.com)

    return render_template('register.html')  # If the method is GET, render the registration page (Commented by Agnirva.com)

@AgnirvaApp.route('/login', methods=['GET', 'POST'], endpoint='login')
def AgnirvaLogin():
    if request.method == 'POST':  # If the form is submitted via POST method (Commented by Agnirva.com)
        Agnirvauusername = request.form.get('username')  # Get the username from the form (Commented by Agnirva.com)
        Agnirvapassword = request.form.get('password')  # Get the password from the form (Commented by Agnirva.com)

        Agnirvauuser = AgnirvaUser.query.filter_by(username=Agnirvauusername).first()  # Query to find the user by username (Commented by Agnirva.com)
        if not Agnirvauuser or not check_password_hash(Agnirvauuser.password, Agnirvapassword):  # Check if the user exists and if password matches (Commented by Agnirva.com)
            flash('Invalid credentials.')  # Display error message if credentials are invalid (Commented by Agnirva.com)
            return redirect(url_for('login'))  # Redirect back to the login page (Commented by Agnirva.com)

        login_user(Agnirvauuser)  # Log in the user (Commented by Agnirva.com)
        return redirect(url_for('index'))  # Redirect to the index page after successful login (Commented by Agnirva.com)

    return render_template('login.html')  # Render the login page if method is GET (Commented by Agnirva.com)

@AgnirvaApp.route('/logout', endpoint='logout')
@login_required  # This decorator ensures the user is logged in before logging out (Commented by Agnirva.com)
def AgnirvaLogout():
    logout_user()  # Log out the current user (Commented by Agnirva.com)
    return redirect(url_for('index'))  # Redirect to the index page after logout (Commented by Agnirva.com)

@AgnirvaApp.route('/upload', methods=['GET', 'POST'], endpoint='upload')  # Route to handle file upload (Commented by Agnirva.com)
@login_required  # Ensures the user is logged in before accessing this route (Commented by Agnirva.com)
def AgnirvaUpload():
    if request.method == 'POST':  # If the form is submitted via POST (Commented by Agnirva.com)
        if 'image' not in request.files:  # Check if the 'image' file is present in the request (Commented by Agnirva.com)
            flash('No file part.')  # Display error message if no file is found (Commented by Agnirva.com)
            return redirect(request.url)  # Redirect back to the same page (Commented by Agnirva.com)

        Agnirvafile = request.files['image']  # Retrieve the uploaded image file from the request (Commented by Agnirva.com)
        
        if Agnirvafile.filename == '':  # Check if the uploaded file has no name (Commented by Agnirva.com)
            flash('No selected file.')  # Display error message if no file is selected (Commented by Agnirva.com)
            return redirect(request.url)  # Redirect back to the same page (Commented by Agnirva.com)

        if Agnirvafile and AgnirvaAllowedFile(Agnirvafile.filename):  # Check if the file is valid and allowed (Commented by Agnirva.com)
            Agnirvafilename = secure_filename(Agnirvafile.filename)  # Secure the filename to prevent unsafe characters (Commented by Agnirva.com)
            
            # To prevent filename collisions, prepend the username and timestamp (Commented by Agnirva.com)
            Agnirvafilename = f"{current_user.username}_{int(datetime.utcnow().timestamp())}_{Agnirvafilename}"  # Create unique filename with username and timestamp (Commented by Agnirva.com)
            
            Agnirvafilepath = os.path.join(AgnirvaApp.config['UPLOAD_FOLDER'], Agnirvafilename)  # Set the file path where the file will be saved (Commented by Agnirva.com)
            Agnirvafile.save(Agnirvafilepath)  # Save the file to the specified path (Commented by Agnirva.com)

            Agnirvacaption = request.form.get('caption')  # Retrieve the caption for the post from the form (Commented by Agnirva.com)
            
            # Create a new post object with the image file and caption (Commented by Agnirva.com)
            Agnirvanew_post = AgnirvaPost(image_file=Agnirvafilename, caption=Agnirvacaption, author=current_user)  # Create a new post instance (Commented by Agnirva.com)
            
            AgnirvaDB.session.add(Agnirvanew_post)  # Add the new post to the database session (Commented by Agnirva.com)
            AgnirvaDB.session.commit()  # Commit the session to save the post in the database (Commented by Agnirva.com)

            flash('Post uploaded successfully.')  # Display success message (Commented by Agnirva.com)
            return redirect(url_for('index'))  # Redirect the user to the index page (Commented by Agnirva.com)

        else:
            flash('Invalid file type.')  # Display error message if the file type is not allowed (Commented by Agnirva.com)
            return redirect(request.url)  # Redirect back to the same page (Commented by Agnirva.com)

    return render_template('upload.html')  # Render the upload page template (Commented by Agnirva.com)

@AgnirvaApp.route('/profile/<int:agnirvauuser_id>', endpoint='profile')  # Route for user profile page (Commented by Agnirva.com)
def AgnirvaProfile(agnirvauuser_id):
    Agnirvauuser = AgnirvaUser.query.get_or_404(agnirvauuser_id)  # Fetch user by ID, or 404 if not found (Commented by Agnirva.com)
    Agnirvauposts = Agnirvauuser.posts  # Get posts related to the user (Commented by Agnirva.com)
    return render_template('profile.html', user=Agnirvauuser, posts=Agnirvauposts)  # Render the profile page with user data and posts (Commented by Agnirva.com)

@AgnirvaApp.route('/like/<int:agnirvapost_id>', methods=['POST'], endpoint='like')  # Route for liking a post (Commented by Agnirva.com)
@login_required  # Ensures the user is logged in before liking a post (Commented by Agnirva.com)
def AgnirvaLike(agnirvapost_id):
    Agnirvapost = AgnirvaPost.query.get_or_404(agnirvapost_id)  # Fetch the post by ID, or 404 if not found (Commented by Agnirva.com)
    Agnirvapost.likes += 1  # Increment the like count for the post (Commented by Agnirva.com)
    AgnirvaDB.session.commit()  # Commit the change to the database (Commented by Agnirva.com)
    return redirect(url_for('index'))  # Redirect to the homepage (Commented by Agnirva.com)

@AgnirvaApp.route('/comment/<int:agnirvapost_id>', methods=['POST'], endpoint='comment')  # Route for posting a comment (Commented by Agnirva.com)
@login_required  # Ensures the user is logged in before commenting (Commented by Agnirva.com)
def AgnirvaCommentRoute(agnirvapost_id):
    Agnirvacontent = request.form.get('comment')  # Get the comment content from the form (Commented by Agnirva.com)
    if Agnirvacontent:  # If there is content in the comment (Commented by Agnirva.com)
        Agnirvanew_comment = AgnirvaComment(  # Create a new comment object (Commented by Agnirva.com)
            content=Agnirvacontent, post_id=agnirvapost_id, user_id=current_user.id  # Set the comment's content, related post, and user (Commented by Agnirva.com)
        )
        AgnirvaDB.session.add(Agnirvanew_comment)  # Add the new comment to the database session (Commented by Agnirva.com)
        AgnirvaDB.session.commit()  # Commit the comment to the database (Commented by Agnirva.com)
    return redirect(url_for('index'))  # Redirect to the homepage after posting the comment (Commented by Agnirva.com)

# Initialize the database and add dummy data (Commented by Agnirva.com)
if __name__ == '__main__':
    with AgnirvaApp.app_context():  # Set the application context for accessing app-specific resources (Commented by Agnirva.com)
        AgnirvaDB.create_all()  # Ensure all database tables are created before starting (Commented by Agnirva.com)

        # Create upload folder if it doesn't exist
        if not os.path.exists(AgnirvaApp.config['UPLOAD_FOLDER']):  # Check if the upload folder path exists (Commented by Agnirva.com)
            os.makedirs(AgnirvaApp.config['UPLOAD_FOLDER'])  # Create the folder if it doesn't exist (Commented by Agnirva.com)

        # Check if there are any users; if not, add dummy data
        if AgnirvaUser.query.first() is None:  # Verify if the user table is empty (Commented by Agnirva.com)
            # Create Dummy Users
            Agnirvauuser1 = AgnirvaUser(  # Create a dummy user "Alice" with a hashed password (Commented by Agnirva.com)
                username='alice',
                password=generate_password_hash('password', method='sha256')
            )
            Agnirvauuser2 = AgnirvaUser(  # Create a dummy user "Bob" with a hashed password (Commented by Agnirva.com)
                username='bob',
                password=generate_password_hash('password', method='sha256')
            )
            Agnirvauuser3 = AgnirvaUser(  # Create a dummy user "Charlie" with a hashed password (Commented by Agnirva.com)
                username='charlie',
                password=generate_password_hash('password', method='sha256')
            )
            AgnirvaDB.session.add_all([Agnirvauuser1, Agnirvauuser2, Agnirvauuser3])  # Add the dummy users to the database session (Commented by Agnirva.com)
            AgnirvaDB.session.commit()  # Commit the changes to save users to the database (Commented by Agnirva.com)

            # Create Dummy Posts
            Agnirvapost1 = AgnirvaPost(  # Create a dummy post by "Alice" (Commented by Agnirva.com)
                image_file='default.jpg',
                caption='Hello from Alice!',
                author=Agnirvauuser1
            )
            Agnirvapost2 = AgnirvaPost(  # Create a dummy post by "Bob" (Commented by Agnirva.com)
                image_file='default.jpg',
                caption='Bob\'s first post!',
                author=Agnirvauuser2
            )
            Agnirvapost3 = AgnirvaPost(  # Create a dummy post by "Charlie" (Commented by Agnirva.com)
                image_file='default.jpg',
                caption='Charlie\'s awesome pic!',
                author=Agnirvauuser3
            )
            AgnirvaDB.session.add_all([Agnirvapost1, Agnirvapost2, Agnirvapost3])  # Add the dummy posts to the database session (Commented by Agnirva.com)
            AgnirvaDB.session.commit()  # Commit the changes to save posts to the database (Commented by Agnirva.com)

            # Create Dummy Comments
            Agnirvacomment1 = AgnirvaComment(  # Add a comment from Bob on Alice's post (Commented by Agnirva.com)
                content='Nice post!',
                post_id=Agnirvapost1.id,
                user_id=Agnirvauuser2.id
            )
            Agnirvacomment2 = AgnirvaComment(  # Add a comment from Alice responding to Bob on her post (Commented by Agnirva.com)
                content='Thank you!',
                post_id=Agnirvapost1.id,
                user_id=Agnirvauuser1.id
            )
            Agnirvacomment3 = AgnirvaComment(  # Add a comment from Alice on Charlie's post (Commented by Agnirva.com)
                content='Great picture!',
                post_id=Agnirvapost3.id,
                user_id=Agnirvauuser1.id
            )
            Agnirvacomment4 = AgnirvaComment(  # Add a comment from Charlie on Bob's post (Commented by Agnirva.com)
                content='Love it!',
                post_id=Agnirvapost2.id,
                user_id=Agnirvauuser3.id
            )
            AgnirvaDB.session.add_all([Agnirvacomment1, Agnirvacomment2, Agnirvacomment3, Agnirvacomment4])  # Add the dummy comments to the database session (Commented by Agnirva.com)
            AgnirvaDB.session.commit()  # Commit the changes to save comments to the database (Commented by Agnirva.com)

    AgnirvaApp.run(debug=True)  # Start the application in debug mode (useful for development) (Commented by Agnirva.com)
if __name__ == '__main__':
    with AgnirvaApp.app_context():  # Set the application context for accessing app-specific resources (Commented by Agnirva.com)
        AgnirvaDB.create_all()  # Ensure all database tables are created before starting (Commented by Agnirva.com)

        # Create upload folder if it doesn't exist
        if not os.path.exists(AgnirvaApp.config['UPLOAD_FOLDER']):  # Check if the upload folder path exists (Commented by Agnirva.com)
            os.makedirs(AgnirvaApp.config['UPLOAD_FOLDER'])  # Create the folder if it doesn't exist (Commented by Agnirva.com)

        # Check if there are any users; if not, add dummy data
        if AgnirvaUser.query.first() is None:  # Verify if the user table is empty (Commented by Agnirva.com)
            # Create Dummy Users
            Agnirvauuser1 = AgnirvaUser(  # Create a dummy user "Alice" with a hashed password (Commented by Agnirva.com)
                username='alice',
                password=generate_password_hash('password', method='sha256')
            )
            Agnirvauuser2 = AgnirvaUser(  # Create a dummy user "Bob" with a hashed password (Commented by Agnirva.com)
                username='bob',
                password=generate_password_hash('password', method='sha256')
            )
            Agnirvauuser3 = AgnirvaUser(  # Create a dummy user "Charlie" with a hashed password (Commented by Agnirva.com)
                username='charlie',
                password=generate_password_hash('password', method='sha256')
            )
            AgnirvaDB.session.add_all([Agnirvauuser1, Agnirvauuser2, Agnirvauuser3])  # Add the dummy users to the database session (Commented by Agnirva.com)
            AgnirvaDB.session.commit()  # Commit the changes to save users to the database (Commented by Agnirva.com)

            # Create Dummy Posts
            Agnirvapost1 = AgnirvaPost(  # Create a dummy post by "Alice" (Commented by Agnirva.com)
                image_file='default.jpg',
                caption='Hello from Alice!',
                author=Agnirvauuser1
            )
            Agnirvapost2 = AgnirvaPost(  # Create a dummy post by "Bob" (Commented by Agnirva.com)
                image_file='default.jpg',
                caption='Bob\'s first post!',
                author=Agnirvauuser2
            )
            Agnirvapost3 = AgnirvaPost(  # Create a dummy post by "Charlie" (Commented by Agnirva.com)
                image_file='default.jpg',
                caption='Charlie\'s awesome pic!',
                author=Agnirvauuser3
            )
            AgnirvaDB.session.add_all([Agnirvapost1, Agnirvapost2, Agnirvapost3])  # Add the dummy posts to the database session (Commented by Agnirva.com)
            AgnirvaDB.session.commit()  # Commit the changes to save posts to the database (Commented by Agnirva.com)

            # Create Dummy Comments
            Agnirvacomment1 = AgnirvaComment(  # Add a comment from Bob on Alice's post (Commented by Agnirva.com)
                content='Nice post!',
                post_id=Agnirvapost1.id,
                user_id=Agnirvauuser2.id
            )
            Agnirvacomment2 = AgnirvaComment(  # Add a comment from Alice responding to Bob on her post (Commented by Agnirva.com)
                content='Thank you!',
                post_id=Agnirvapost1.id,
                user_id=Agnirvauuser1.id
            )
            Agnirvacomment3 = AgnirvaComment(  # Add a comment from Alice on Charlie's post (Commented by Agnirva.com)
                content='Great picture!',
                post_id=Agnirvapost3.id,
                user_id=Agnirvauuser1.id
            )
            Agnirvacomment4 = AgnirvaComment(  # Add a comment from Charlie on Bob's post (Commented by Agnirva.com)
                content='Love it!',
                post_id=Agnirvapost2.id,
                user_id=Agnirvauuser3.id
            )
            AgnirvaDB.session.add_all([Agnirvacomment1, Agnirvacomment2, Agnirvacomment3, Agnirvacomment4])  # Add the dummy comments to the database session (Commented by Agnirva.com)
            AgnirvaDB.session.commit()  # Commit the changes to save comments to the database (Commented by Agnirva.com)

    AgnirvaApp.run(debug=True)  # Start the application in debug mode (useful for development) (Commented by Agnirva.com)
