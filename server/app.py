#!/usr/bin/env python3
from models import db, Restaurant, RestaurantPizza, Pizza
from flask_migrate import Migrate
from flask import Flask,jsonify, request, make_response
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)


# @app.route("/")
# def index():
#     return "<h1>Code challenge</h1>"

class Home(Resource):
    def get(self):
        title={
            "message":"WELCOME TO THE PIZZA RESTAURANT API"
        }
        return make_response(title, 200)
    
api.add_resource(Home,"/")    
    
class Restaurants(Resource):
    def get(self):
        restaurants = [restaurant.to_dict() for restaurant in Restaurant.query.all()]
        return make_response(restaurants,200)

api.add_resource(Restaurants,"/restaurants")    

class RestaurantByID(Resource):
    def get(self,id):
        restaurant = Restaurant.query.filter(Restaurant.id == id).first()
        if restaurant:
           return make_response(jsonify(restaurant.to_dict()),200)
        else:
            return make_response(jsonify({"error": "Restaurant not found"}), 404)
        
    def delete(self,id):
        restaurant = Restaurant.query.filter(Restaurant.id == id).first()
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            return make_response("",204)
        else:
            return make_response(jsonify({"error": "Restaurants not found"}), 404)   
        
            
        
api.add_resource(RestaurantByID,"/restaurants/<int:id>")  

class Pizzas(Resource):
    def get(self):
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()] 
        return make_response(pizzas,200)    
    
api.add_resource(Pizzas,"/pizzas")

class RestaurantPizza(Resource):
    def post(self):
        data = request.get_json()
             
        

if __name__ == "__main__":
    app.run(port=5555, debug=True)
