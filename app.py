from flask import Flask, jsonify 
from flask_restful import Resource, Api
import uuid
import datetime;  

app=Flask(__name__)
app.config["JSON_SORT_KEYS"] = False
api=Api(app)


class Generate_UUID(Resource):
    def post(self):
        ct = datetime.datetime.now()
        generatedUUID = {str(ct): str(uuid.uuid1())}
        file1 = open("storage.txt","a")
        file1.write(str(ct)+";"+str(uuid.uuid1())+"\n")
        file1.close

        return jsonify({"generatedUUID": generatedUUID})

    def get(self):
        try:
            file = open("storage.txt","r+")
            store = file.readlines()
            file.close
        except FileNotFoundError:
            return jsonify({"message": "no record available"})
        
        record = {}
        if len(store) < 1:
            return jsonify({"message": "no record available"})
        else:
            for rec in store:
                keyValue = rec.split(";")
                value = keyValue[1].replace('\n','')
                record[keyValue[0]] = value
            reversed_record = {}
            for c in reversed(record):
                reversed_record[c] = record[c]
            return jsonify(reversed_record)

api.add_resource(Generate_UUID,'/')

if __name__ == '__main__':
    app.run(debug=True)