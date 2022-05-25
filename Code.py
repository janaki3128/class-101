import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)  
        file = open(file_from, 'rb')
        dbx.files_upload(file.read(), file_to)
    
    
    def main():
        access_token = 'sl.BIQWoIVv_dya2THp-CPNHkLpR0pE8_8pW4eE8ehUQboABXgSTSiPB68f0vwNMHOc8EZm1Y7UXeE7Bkyysu1so2bGN1Qo_Me9nPtSEC4iGJlL7IF3T2ieV8ZrX418oKv_uZHaEuooMyc'
        transfer_data = TransferData(access_token)

        file_from = "C:/Users/hp/Desktop/Class-101/Trail.text.txt"
        file_to = "/projects/Trial_text.txt"

        transfer_data.upload_file(file_from, file_to)
        print("Files has been moved")

main()