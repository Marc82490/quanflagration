from app import db

class Symbol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticker_symbol = db.Column(db.String(80), index=True, unique=True)

    def __repr__(self):
        return '<Stock %r>' % self.ticker_symbol