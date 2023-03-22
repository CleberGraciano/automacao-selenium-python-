from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
import os
import urllib
import shutil

options = Options()
download_dir = "D:\dowload"
diretorioOficial = "D:\Cursos-Igreja"
pasteCurso =""

options.add_experimental_option("prefs", {
  "download.default_directory": download_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})


# options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=options)
driver.set_page_load_timeout(30)
driver.maximize_window()

driver.get('https://padrepauloricardo.org/entrar')


def findElementWait(seletor, typeSeletor):
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located((typeSeletor, seletor)))
    return driver.find_element(By.XPATH, seletor)

def findElementClick(seletor):
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, seletor)))
    return driver.find_element(By.XPATH, seletor).click()

def getAttribute(seletor, seletorCss, attribute):
    WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.XPATH, seletor)))
    return driver.find_element(By.CLASS_NAME, seletorCss).get_attribute(attribute)

def findElementInput(seletor, texto):
    objeto = driver.find_element(By.XPATH, seletor)
    objeto.send_keys(texto)

def moverArquivosComExtensao(pastaOrigem, pastaDestino):
    for diretorio, subpastas, arquivos in os.walk(pastaOrigem):
        for cont in range(len(arquivos)):
            shutil.move(pastaOrigem+"/"+arquivos[cont], pastaDestino+"/"+arquivos[cont])
            print("Arquivos movido com sucesso!!")      


def getNameCouse(link, parteUrl):
    return link.split('/')[0:][parteUrl]



def listComponent(classeLoop, seletor, atributo):
    time.sleep(5) 
    lista_cursos = driver.find_elements_by_class_name(classeLoop)
    lista = {}
    for i in lista_cursos:
        lista[i.get_attribute(seletor)]=i.get_attribute(atributo)
    return lista

def get_module_course(link):
    driver.get(link)
    for name, modulo in listComponent('class', 'id', 'href').items():
        print('======= Dowload do modulo: '+modulo+' =========')
        print(getNameCouse(modulo, 4))
        dowload(modulo)
        path = os.path.join(diretorioOficial, pasteCurso)
    # time.sleep(10)    
    moverArquivosComExtensao(download_dir, path)

def downloadRename(href, src_dir, newNameFile):
    fullfilename = os.path.join(src_dir, newNameFile)
    urllib.urlretrieve(href, fullfilename) 

def dowloadMaterialPDF(link):
    driver.get(link)
    findElementClick('/html/body/div[3]/section[1]/section/section/section/a[3]')
    time.sleep(2)
    url_aula  = getAttribute('//*[@id="download-content"]/li/a', 'downloads-item__link', 'href')
    print("Link dowalod: "+url_aula)
    downloadRename(url_aula, download_dir, getNameCouse(url_aula, 8))       

def dowload(link):
    driver.get(link)
    findElementClick('/html/body/div[3]/section[1]/section/section/section/a[3]')
    time.sleep(2)
    url_aula  = getAttribute('//*[@id="download-content"]/li/a', 'downloads-item__link', 'href')
    print("Link dowalod: "+url_aula)
    downloadRename(url_aula, download_dir, getNameCouse(url_aula, 8))
    # time.sleep(5)

def createDirectorie(pathUrl, namePaste):
    root_path = pathUrl
    path = os.path.join(root_path, namePaste)
    os.mkdir(path)


findElementClick('//*[@id="om-zt4mvrk6kcnlktpkm5ja-yesno"]/div/button')
findElementClick('//*[@id="c-p-bn"]')
findElementInput('//*[@id="inputEmail"]', 'EMAIL')
findElementInput('//*[@id="inputPassword"]','SENHA')
findElementClick('//*[@id="loginForm"]/div[6]/button')     
for name, curso in listComponent('course-card', 'title', 'href').items():
    print('========= Nome do Curso: '+curso+' ============')
    print(name)
    createDirectorie(diretorioOficial, getNameCouse(curso,4))
    pasteCurso = getNameCouse(curso,4)
    get_module_course(curso)
driver.quit() 


