from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost:3306/market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False






