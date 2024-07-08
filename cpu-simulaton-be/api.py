from manoAssembler import Assembler
from manoMachine import Register, Memory, Computer
from flask import Flask, request
from flask_cors import CORS

computer = Computer()

api = Flask(__name__)

CORS(api)

@api.route("/memory/write", methods=["POST"])
def writeMemory():
    if request.method == 'POST':
        json = request.json
        address = json.get("address")
        value = json.get("value")
        print(address, value)
        return ('', 204)

@api.route("/memory/bulk_write", methods=["POST"])
def bulkWrite():
    if request.method == "POST":
        json = request.json
        data = json.get("data")
        return ('', 204)
    
@api.route("/memory/read/<address>")
def read(address):
    pass 

@api.route("/memory/bulk_read/<bulk_address>")
def bulkRead(bulk_address):
    pass

@api.route("/register/write", methods=["POST"])
def writeRegister():
    return ('', 204) 

@api.route("/register/read")
def readRegister():
    print(computer.read_register())
    return ('', 204)

@api.route("/core/execute",methods=["POST"])
def execute():
    if request.method == "POST":
      json = request.json
      instructions = json.get("instructions")
      assembler = Assembler(instructions)
      program_start = assembler.load(computer.ram)
      computer.run(program_start)
      print(computer.ram.bulk_read())
    return computer.read_register()

@api.route("/core/compile",methods=["GET", "POST"])
def compile():
    if request.method == "POST":
        json = request.json
        instructions = json.get("instructions")
        assembler = Assembler(instructions)
        program_start = assembler.load(computer.ram)
        return ('', 204)

if __name__ == "__main__":
  api.run(host="localhost", port="8000", debug=True)
