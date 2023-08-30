from app import app, db
from app.models import Document

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Document': Document}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
