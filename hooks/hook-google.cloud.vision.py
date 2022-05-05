from PyInstaller.utils.hooks import copy_metadata

datas = copy_metadata('gcloud')
datas += copy_metadata('google-cloud-coreg')
datas += copy_metadata('google-cloud-vision')
datas += copy_metadata('google-cloud-translate')
datas += copy_metadata('google-api-core')
