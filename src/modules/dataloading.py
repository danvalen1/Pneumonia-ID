import wget
import os
import zipfile

def pullimages(targetdir='data/extracted/'):
    """Pulls pneumonia images from Kaggle. 
    
            Parameters:
                targetdir (str): Where files are to be saved.
            Returns:
                file_locs (list of str): Returns locations for all the extracted images.
                
        Dependencies: wget, os
    """
    # Append slash if not at end of targetdir
    if targetdir[-1] != '/':
        targetdir += '/'
    
    # Make targetdir if doesn't exist
    if not os.path.isdir(targetdir):
        os.mkdir(targetdir)
    
    # create target zip location 
    targetzip = targetdir + 'chest_xray.zip'
    
    # if target zip exists do nothing, else download
    if os.path.isfile(targetzip):
        pass
    else:
        url = 'https://storage.googleapis.com/kaggle-data-sets/17810/23812/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201201%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201201T163801Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=9ea02b7ad92318d5dff63d30f8ac227d05742fef5c483d8759590df5599b41b7896450a24ec1da99e22b79d2ec930c109a911bb0afb78210f948d7fa0c906c4c69d0ffd1060c6da85e4e67596422b80882c157444b10dfccc22e76dd94de48b7bfc748a5dc56bb3be1d0360e99efd942d4ce793682765c0d69f749790043fe77d235ebba261e74588fb67dc4d0f262b03263272cb890ee81ba4e3dda4095bc0f2bf081e93c66ad79fdcf4003a01627f14672c0da82ee44e44bc880fe2b1ee830447c9e991fb388115026533c857eb563b9a395e59c7f9b06af1170764e350d0dbcff9f10b7f5d0bc47c16fc1350b0a9a6b12984e060e4fbf628355fbe8d69f4b'
        wget.download(url, targetzip)
    
    # Unzip images and save locations of same 
    file_locs = Unzip(targetzip)

    return file_locs

def Unzip(targetzip):
    """Unzip a file.
    
            Parameters:
                targetzip (str): String of path to target zip file.
            Returns:
                file_locs (list of str): Returns locations for all the extracted files.
                
        Dependencies: os, zipfile
    """

    # Set and/or create sub-folder
    sub_folder = targetzip.rsplit('/',1)[0] + '/'
    try:
        os.mkdir(sub_folder)
    except:
        pass
    
    # Unzipping file        
    try:
        
        with zipfile.ZipFile(targetzip, 'r') as zip_ref:
            zip_ref.extractall(sub_folder)
            # Get list of files names in zip
            files = zip_ref.namelist()
    except:
        raise
        
    # Return list of locations of extracted files   
    file_locs = [] 
    for file in files:
        file_locs.append(sub_folder + file)
    
    return file_locs