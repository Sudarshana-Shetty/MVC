import json
from flask import Blueprint, request, jsonify
from controller import mainController as main


bp = Blueprint(__name__, "allRoutes")
mainController = main.MainController()


@bp.route("/insert", methods=["POST"])
def insertData():
    u = request.get_json()
    response = mainController.insertUser(u)    
    return jsonify(response)

'''
@bp.route("/update", methods=["POST"])
def updateData():
    u = request.get_json()
    response = mainController.updateUser(u)
    return jsonify(response)

@bp.route("/delete", methods=["POST"])
def deleteData():
    u = request.get_json()
    response = mainController.deleteUser(u)
    return jsonify(response) '''