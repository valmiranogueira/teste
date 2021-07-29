from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

api = Flask(__name__)

@api.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)

@api.route('/companies/<cid>', methods=['GET'])
def get_company(cid):
  if type(cid) is str:
    item = list(filter(lambda x:x["id"]==int(cid),companies))
    return json.dumps(item)
  else:
    return "Incorrect type of index: {}".format(type(cid))

if __name__ == '__main__':
  api.run(host='0.0.0.0')
