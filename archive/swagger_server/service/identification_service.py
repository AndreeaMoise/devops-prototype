import os
# from flask import Flask
import tempfile
from functools import reduce

from tinydb import TinyDB, Query

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "identities.json")
db = TinyDB(db_file_path)

# app = Flask(__name__)


# @app.route('/identify', methods=['POST'])
def add(identification=None):
    print(db_file_path)
    queries = []
    query = Query()

    queries.append(query.truck_id == identification.truck_id)
    queries.append(query.driver_id == identification.driver_id)
    queries.append(query.location.latitude == identification.location.latitude)
    queries.append(query.location.longitude == identification.location.longitude)

    query = reduce(lambda a, b: a & b, queries)
    res = db.search(query)

    # Verify if the res contains also the correct items
    # Assume only one result
    sameItems = True

    if res:
        rawItems = identification.load.items
        resItems = res[0]['load']['items']

        for x in range(len(rawItems)):
            if rawItems[x].sku != resItems[x]['sku'] or rawItems[x].quantity != resItems[x]['quantity']:
                sameItems = False

         # If entry exists in the db, then it is valid.
        if sameItems:
            return 'entry is valid', 200

    db.insert(identification.to_dict())
    return 'entry is created', 201


# def get_by_id(student_id=None, subject=None):
#     student = db.get(doc_id=int(student_id))
#     if not student:
#         return 'not found', 404
#     student['student_id'] = student_id
#     print(student)
#     return student
#
#
# def delete(student_id=None):
#     student = db.get(doc_id=int(student_id))
#     if not student:
#         return 'not found', 404
#     db.remove(doc_ids=[int(student_id)])
#     return student_id