from zipfile import ZipFile

with ZipFile("data\\news.zip", "r") as zObject:
    zObject.extractall("data")