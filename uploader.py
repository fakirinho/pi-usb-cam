from ftplib import FTP


class Uploader:
    def connect(self, hostname, username, password):
        raise NotImplementedError()

    def disconnect(self):
        raise NotImplementedError()

    def upload(self, data, uploaded_name, destination=None):
        raise NotImplementedError()


class FtpUploader(Uploader):
    def __init__(self):
        self.connection = None

    def connect(self, hostname, username, password):
        self.connection = FTP(hostname, username, password)

    def disconnect(self):
        resp = None
        try:
            if self.connection is not None:
                resp = self.connection.quit()
        finally:
            # if call to self.connection.quit() succeeds, calling close() below is not needed
            if resp is not None and self.connection is not None:
                self.connection.close()

    def upload(self, data, uploaded_name, destination=None):
        if self.connection is not None:
            if destination is not None and self.connection.pwd() != destination:
                self.connection.cwd(destination)
            self.connection.storbinary('STOR ' + uploaded_name, data)
