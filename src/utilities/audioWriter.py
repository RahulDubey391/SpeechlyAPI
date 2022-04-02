from .storeConnection import StoreCon
from ..config.config import Config

class AudioWriter:
    def writeAudio(self,filename,content):
        store = StoreCon()
        bucket = store.get_con(Config.UPLOAD_BUCKET_NAME)
        blob = bucket.blob(filename)
        with blob.open(mode='wb') as f:
            f.write(content)
        print('File Uploaded')
    