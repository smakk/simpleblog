from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Date,Text
from sqlalchemy.orm import sessionmaker

from flask import g

from myapp import app
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()
def connect_db(config):
    engine = create_engine(config)
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    return DBSession()

def get_db():
    with app.app_context():
        if not hasattr(g, 'db'):
            g.db = connect_db(app.config['connect'])
        return g.db
    
def close_db():
    if hasattr(g, 'db'):
        g.db.close()

@app.teardown_appcontext
def tear_down(error):
    close_db()
    if error is not None:
        print(error)
    
class article_info(Base):
    __tablename__ = 'arti_info'
    id = Column(Integer ,primary_key = True)
    time = Column(Date , nullable = False)
    auther = Column(String(20) , nullable = False)
    article_type = Column(String(20) , nullable = True)
    title = Column(String(50) , nullable = False)
    article_context = Column(String(100) , nullable = False)
    article_addr = Column(String(50) , nullable = False)
    extra_info = Column(String(100) , nullable = False)
    type_addr = Column(String(50) , nullable = False)
    article_id = Column(Integer , nullable = False , unique = True)
    read_num = Column(Integer , nullable = False)
    recommand_star = Column(Integer , nullable = False)
    
class article(Base):
    __tablename__ = 'article'
    arti_id = Column(Integer , ForeignKey('arti_info.article_id') ,primary_key = True)
    cont = Column(Text , nullable = False)


class arti_type(Base):
    __tablename__= 'arti_type'
    type_name = Column(String(20),primary_key = True)
    
# create table
articles = []
article_types = []
db = get_db()
for item in db.query(article_info).all():
    articles.append(item)
for item in db.query(arti_type).all():
    article_types.append(item)
