from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
    
    
    
    # Implement search here !
    params = ["id","name","age","occupation"]
    if any( i in params for i in  args):
        id = args.get('id')
        name = args.get('name')
        age = args.get('age')
        occupation = args.get('occupation')
        filteredUsers = []
        for user in USERS:
            if (user["id"]  == id or ( name.lower() in user["name"].lower() if name is not None else '')  or 
                (( user["age"]  == int(age) or user["age"]  == (int(age) + 1) or user["age"]  == (int(age) - 1) ) if age is not None else '' ) or 
                (occupation in user["occupation"] if occupation is not None else '')):
                filteredUsers.append(user)
        sortedUsers = sorted(filteredUsers,key=lambda k:(k["id"],k["name"],k["age"],k["occupation"]))
        return sortedUsers
    else:
     return USERS
