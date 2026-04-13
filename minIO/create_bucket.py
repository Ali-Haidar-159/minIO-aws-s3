from minio import Minio

from minIO.connect import connect_minIO

_,client = connect_minIO()


def create_new_bucket() :
    if not client.bucket_exists("users"):
        client.make_bucket("users")

    return True