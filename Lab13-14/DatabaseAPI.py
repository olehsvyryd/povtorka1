import configparser
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request

application = Flask(__name__)

config = configparser.ConfigParser()
config.read('E:\Games\Lab13-14\products_db.conf')

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.get('DB', 'user') + \
                                                ':' + config.get('DB', 'password') + '@' + \
                                                config.get('DB', 'host') + '/' + config.get('DB', 'db')

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mysql = SQLAlchemy()
mysql.init_app(application)


class ComputerModel(mysql.Model):


    __tablename__ = "computer"
    id = mysql.Column(mysql.Integer, primary_key=True)
    price = mysql.Column(mysql.Integer, nullable=False)
    weight = mysql.Column(mysql.Integer, nullable=False)
    producer = mysql.Column(mysql.String(20), nullable=False)
    material = mysql.Column(mysql.String(20), nullable=False)
    type = mysql.Column(mysql.String(20), nullable=False)

    def __repr__(self):
        return '<Products (%s, %s, %s, %s, %s) >' % (self.price, self.producer, self.weight, self.material, self.type)


@application.route("/")
def hello():
    return "Hello World!"


@application.route('/computer', methods=['POST'])
def create_product():
    id = request.json['id']
    price = request.json['price']
    producer = request.json['producer']
    weight = request.json['weight']
    material = request.json['material']
    type = request.json['type']
    curr_session = mysql.session

    computer = ComputerModel(id=id, price=price, producer=producer, weight=weight, material=material, type=type)

    try:
        curr_session.add(computer)
        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()

    package_id = computer.id
    data = ComputerModel.query.filter_by(id=package_id).first()

    config.read('E:\Games\Lab13-14\products_db.conf')

    result = [data.price, data.producer, data.weight, data.material, data.type]

    return jsonify(session=result)


@application.route('/computer', methods=['GET'])
def get_product():
    data = ComputerModel.query.all()

    data_all = []

    for computer in data:
        data_all.append([computer.price, computer.producer, computer.weight, computer.material, computer.type])

    return jsonify(products=data_all)


@application.route('/computer', methods=['PATCH'])

    try:
        computer = ComputerModel(['PATCH'])
def update_product():
    global computer
    id = request.get_json['id']
    price = request.get_json['price']
    producer = request.get_json['producer']
    weight = request.get_json['weight']
    material = request.get_json['material']
    type = request.get_json['type']
    curr_session = mysql.session.query.filter_by(id=id).first()
        computer.price = producer
        computer.weight = weight
        computer.price = price
        computer.material = material
        computer.type = type
        curr_session.commit()
    except:
        curr_session.rollback()
        curr_session.flush()

    product_id = computer.id
    data = ComputerModel.query.filter_by(id=product_id).first()

    config.read('E:\Games\Lab13-14/Lab13-14\products_db.conf')

    result = [data.price, data.producer, data.weight, data.material, data.type]

    return jsonify(session=result)


@application.route('/computer/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    curr_session = mysql.session

    ComputerModel.query.filter_by(id=product_id).delete()
    curr_session.commit()

    return get_product()


if __name__ == "__main__":
    application.run()