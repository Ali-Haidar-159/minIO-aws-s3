from minio import Minio

from minIO.connect import connect_minIO

_,client = connect_minIO()


def get_objects() :
    objects = client.list_objects("users")

    return objects