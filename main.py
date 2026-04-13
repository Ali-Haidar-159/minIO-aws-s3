from minIO.connect import connect_minIO
from minIO.create_bucket import create_new_bucket
from minIO.download_obj import download_obj
from minIO.upload_obj import upload_obj
from minIO.get_obj_url import get_obj_url
from minIO.delete_obj import delete_obj
from minIO.get_list_obj import get_objects



def main() :
    # isConnected,_ = connect_minIO()
    # if isConnected :
    #     print("MinIo is successfully connected")


    # isCreated = create_new_bucket()
    # if isCreated : 
    #     print("Bucket is Created")

    
    # isDownload = download_obj()
    # if isDownload : 
    #     print("Image Downloaded")


    # isUpload = upload_obj()
    # if isUpload : 
    #     print("Image Uploaded")


    # presigned_url = get_obj_url()
    # if presigned_url : 
    #     print("The presigned url for access : ",presigned_url)


    # isDeleted = delete_obj()
    # if isDeleted : 
    #     print("Object Deleted")


    objects = get_objects()
    if objects : 
        for obj in objects :
            print("Objects : ",obj.object_name)


if __name__ == "__main__" :
    main()