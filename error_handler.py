from flask_restful import abort


def CheckIfRequestIsNotJson(flag: bool):
    if not flag:
        ThrowJsonBodyAbort()

def CheckIfFieldIsMissing(field, fieldName: str):
    if field is None:
        ThrowMissingRequiredField(fieldName)

def CheckIfObjectIsNone(object):
    if object is None:
        ThrowObjectNotFound()

def CheckIfObjectsDoesntExist(flag: bool):
    if not flag:
        ThrowObjectNotFound()

# def CheckIfObjectDoesntExist(object):
#     if object is None:
#         ThrowObjectNotFound()

def CheckIfObjectAlreadyExists(object):
    if object is not None:
        ThrowObjectAlreadyExists()





def ThrowJsonBodyAbort():
    abort(400, msg='Request body cannot be empty and must be JSON formatted')

def ThrowMissingRequiredField(fieldName):
    abort(400, msg=f'Missing required field {fieldName}')

def ThrowObjectNotFound():
    abort(404, msg='Object not found')

def ThrowObjectAlreadyExists():
    abort(400, msg='The object already exists')
