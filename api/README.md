## Consume & create API
- Flask + SQLAlchemy
- Postman: https://www.postman.com/
- Run the following cmds in Python Console to create the db:
```
from consume_api import db
db.create_all()
db.session.commit()
```