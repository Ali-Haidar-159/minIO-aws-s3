from minio import Minio

from minIO.connect import connect_minIO

_,client = connect_minIO()


def download_obj() :
    client.fget_object(
        "demobucket",
        "Screenshot from 2026-04-13 11-39-48.png",
        "download.png"
    )

    return True