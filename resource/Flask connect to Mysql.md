**Use Flask-SQLALCHEMY connect to Mysql**

1. pip install flask-mysqldb

2. pip insatll flask-sqlalchemy

3. URL:

   mysql://username:password@hostname/database

4. app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost:3306/databasename?charset=utf8'

5. app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

