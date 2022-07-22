from flask_mongoengine import mongoengine


class User(mongoengine.Document):
    email = mongoengine.EmailField(unique=True)
    mobile_num = mongoengine.StringField(unique=True)
    firstName = mongoengine.StringField(max_length=50)
    lastName = mongoengine.StringField(max_length=50)
    pfp_url = mongoengine.URLField()
    age = mongoengine.IntField()
    employed = mongoengine.BooleanField()
    student = mongoengine.BooleanField()
    username = mongoengine.StringField(required=True,
                                       max_length=50,
                                       unique=True)

    meta = {
        'collection': 'users'
    }


class Comment(mongoengine.Document):
    _id = mongoengine.ReferenceField(User)
    comment = mongoengine.StringField()

    meta = {
        'collection': 'comments'
    }
