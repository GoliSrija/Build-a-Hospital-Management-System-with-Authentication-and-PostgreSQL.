```python
from app import app, db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
```
Note: This is a basic Flask application with the routes, models, and configuration as requested. However, this is a simplified example and should not be used in production without proper error handling, authentication, and security measures.