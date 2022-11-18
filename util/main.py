from abc import ABC
from util.gestionar_dao import GestionarDAO
from util.gestionar_modelo import GestionarModelo
from dao.etapa_dao import Etapa_DAO
from model.area import Area
from model.barrio import Barrio
from model.comuna import Comuna
from model.empresa import Empresa
class Main(ABC):
    
    @classmethod
    def main(cls):
        #importar dataset .csv a la base de datos
        archivo_csv = "observatorio-de-obras-urbanas.csv"
        #archivo_csv = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/secretaria-general-y-relaciones-internacionales/ba-obras/observatorio-de-obras-urbanas.csv"
        GestionarDAO.importar_csv(archivo_csv)

        #agregar aquí su código para completar las funcionalidades del TP
        a1 = Area("Corporación Buenos Aires Sur") 
        print(a1)
        b1= Barrio("balvanera","3")
        print(b1)
        c1=Comuna("3")
        print(c1)
        empresa=Empresa("453322","pedro construcciones")
        print(empresa)