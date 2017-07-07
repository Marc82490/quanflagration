from app import db

class Symbol(db.Model):
    """
    Create class for SQLite table holding stock symbols
    """
    id = db.Column(db.Integer, primary_key=True)
    ticker_symbol = db.Column(db.String(80), index=True, unique=True)

    def __repr__(self):
        return '%r' % self.ticker_symbol

    def serialize(self):
        return {
            'ticker_symbol': self.ticker_symbol,
        }

class User(db.Model):
    """
    Create class for SQLite table holding user information
    """
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text, index=True, unique=True)
    pass_hash = db.Column(db.Text)

    def __repr__(self):
        return '%r' % self.user_name
