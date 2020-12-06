from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

# import datetime
# from datetime import datetime
# datetime.utcnow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, index=True)
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('you cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(500))
    image = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='blogs', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_blog(cls):
        Bloc.blog.clear()

    @classmethod
    def get_blogs(cls):
        blog = Blog.query.filter_by(id = id).all()
        return blog

    def delete(self, id):
        comments = Comment.query.filter_by(id = id).all()
        for comment in comments:
            db.session.delete(comment)
            db.session.commit()

        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Blog {self.content}'

class Comment(db.Model):
    '''
    Comment class to define comment objects
    '''

    __tablename__ ='comments'
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comment(self):
        Comment.comments.clear()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(blog_id = id).all()
        return comments

    

    def __repr__(self):
        return f'Comment{self.comment}'
class Quotes:
    '''
    Quote class to define quote objects
    '''
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote

class Subscription(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), unique=True, index=True)
    email = db.Column(db.String(255), unique = True, index = True)
    
    def __repr__(self):
        return f'Subscription{self.name}'