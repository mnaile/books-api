from extensions.extensions import db

class Books(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    page = db.Column(db.Integer(), nullable=False)
    author = db.Column(db.String(), nullable=False)

    def save_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def update_db(self, **kwargs):
        for key,val in kwargs.items():
            setattr(self, key, val)

        self.save_db()