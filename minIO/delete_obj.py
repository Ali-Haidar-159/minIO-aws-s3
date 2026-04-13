from minio import Minio

from minIO.connect import connect_minIO

_,client = connect_minIO()


def delete_obj() :
    client.remove_object(
        "demobucket",
        "Screenshot from 2026-04-13 11-39-48.png"
    )

    return True