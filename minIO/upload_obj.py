from minio import Minio

from minIO.connect import connect_minIO

_,client = connect_minIO()


def upload_obj() :
    client.fput_object(
        "users",
        "ss_1.png",
        "ss.png"
    )

    return True