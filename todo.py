from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def test():
    if request.method== "GET":
        return jsonify({"Name ": "Avi"})
    elif request.method=="POST":
        req_json=request.json
        name=req_json['name']
        return jsonify({"Response":"Posted "+name})

if __name__=='__main__':
    app.run(debug='true')