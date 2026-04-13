from minio import Minio

def connect_minIO() :
    try : 
        client = Minio (
            "localhost:9000",
            access_key="admin",
            secret_key="admin123",
            secure=False
        )
            
        return True , client 
    except Exception as e :
          print("Find error to connect with minIO")
    