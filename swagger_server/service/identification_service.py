import os
import tempfile
from functools import reduce

from tinydb import TinyDB, Query

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "identities.json")
db = TinyDB(db_file_path)


def add(identification=None):
    # queries = []
    # query = Query()
    # queries.append(query.first_name == student.first_name)
    # queries.append(query.last_name == student.last_name)
    # query = reduce(lambda a, b: a & b, queries)
    res = db.search(identification)
    # If entry exists in the db, then it is valid.
    if res:
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