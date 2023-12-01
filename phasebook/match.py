import time
from flask import Blueprint
from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404
    
    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start,"myArray":MATCHES[match_id]}, 200


def is_match(fave_numbers_1, fave_numbers_2):    
    sorted_fave_numbers_1 = sorted(fave_numbers_1,key=lambda k:k)
    sorted_fave_numbers_2 = sorted(fave_numbers_2,key=lambda k:k)
    for number in sorted_fave_numbers_2:
        if number not in sorted_fave_numbers_1:
            return False    
    return True
