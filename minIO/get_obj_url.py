from minio import Minio

from minIO.connect import connect_minIO

_,client = connect_minIO()


def get_obj_url() :
    url = client.presigned_get_object(
        "users",
        "ss_1.png"
    )

    return url