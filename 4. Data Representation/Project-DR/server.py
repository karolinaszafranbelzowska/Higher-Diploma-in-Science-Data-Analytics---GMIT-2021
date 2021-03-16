# Karolina Szafran-Belzowska, 
# Data Representation, project 2020
# Code taken from https://github.com/andrewbeattycourseware/dataRepresenation2020, 06/12/2020


from EmployeeDAO import employeeDAO

from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
   return  "Hello, World!!" # Server is working!

# getAll 
# curl http://127.0.0.1:5000/employee

@app.route('/employee') # works
def getAll():
   return jsonify(employeeDAO.getAll())

# findById
# curl http://127.0.0.1:5000/employee/123

@app.route('/employee/<int:employee_ID>') # works
def findById(employee_ID): 
    return jsonify(employeeDAO.findById(employee_ID))

# create
# curl -X POST -d "{\"employee_ID\":\"125\", \"employee_Name\":\"Karolina\", \"employee_Dept_ID\": 155,\"employee_Salary\":400.00}" -H "Content-Type:application/json" http://127.0.0.1:5000/employee
# curl http://127.0.0.1:5000/employee

@app.route('/employee', methods=['POST']) # works
def create(): 
    if not request.json: #abort the request if it is not in the correct json format
        abort(400)
    # if it is correct request do this
    person = {
        "employee_ID":request.json["employee_ID"], 
        "employee_Name": request.json["employee_Name"],
        "employee_Dept_ID": request.json["employee_Dept_ID"],
        "employee_Salary": request.json["employee_Salary"]
    }
    return jsonify(employeeDAO.create(person))

# update
# curl -X PUT -d "{\"employee_Name\":\"new Person\", \"employee_Dept_ID\":155, \"employee_Salary\":400}" -H "Content-Type:application/json" http://127.0.0.1:5000/employee/124
# curl http://127.0.0.1:5000/employee

@app.route('/employee/<int:employee_ID>', methods=['PUT'])
def update(employee_ID):
    foundPerson = employeeDAO.findById(employee_ID)
    print(foundPerson)
    if foundPerson == {}:
        return jsonify({}), 404
    currentPerson = foundPerson
    if 'employee_Name' in request.json:
        currentPerson['employee_Name'] = request.json['employee_Name']
    if 'employee_Dept_ID' in request.json:
        currentPerson['employee_Dept_ID'] = request.json['employee_Dept_ID']
    if 'employee_Salary' in request.json:
        currentPerson['employee_Salary'] = request.json['employee_Salary']
    employeeDAO.update(currentPerson)
    return jsonify(currentPerson)

# delete
# curl -X DELETE http://127.0.0.1:5000/employee/124
# curl http://127.0.0.1:5000/employee

@app.route('/employee/<int:employee_ID>', methods=['DELETE'])
def delete(employee_ID):
    employeeDAO.delete(employee_ID)
    return jsonify({"done":True})




if __name__ == "__main__":
    app.run(debug=True)
