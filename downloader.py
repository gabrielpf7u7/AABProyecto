import urllib.request
import config

path_to_csv = config.PATH_TO_CSV
path_to_download = config.PATH_TO_DOWNLOAD


def download():
    with open(path_to_csv) as data:
        print("Inicialdo proceso de descarga segun el archivo {}".format(path_to_csv.split("/")[-1]))
        line = data.readline()
        cnt = 0
        while line:
            url = line[1:-2]
            if "http" in url:
                file_name = url.split("https://image.portalinmobiliario.cl/Portal/Propiedades/")[1]
                urllib.request.urlretrieve(url, path_to_download+'/data/'+file_name)
                cnt += 1
                print("Downloaded {} from {}".format(file_name, url))
            line = data.readline()
        print("Finalizado el proceso de descarga, se descargaron {} archivos".format(cnt))
