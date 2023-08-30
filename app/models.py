from app import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)

    def __repr__(self):
        return f"<Document {self.title}>"
