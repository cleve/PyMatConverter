# setup.py
import glob
from distutils.core import setup

try:
  import py2exe
  
except:
  pass

     

setup(

name="PyMatConverter",  
version="1.0",  
description="Convertir multiples archivos con vectores en una planilla excel.",  
author="Mauricio Cleveland",  
author_email="mauricio.cleveland en gmail",  
url="http://www.universodigital.cl",  
license="GPL",  

windows = [
        {
            "script": "app.py",
            "icon_resources": [(1, "img/pulsar.ico")]
        }
    ],

data_files=[('img', glob.glob('img/*.png')),
            ('img', glob.glob('img/*.ico')),
            ('img', glob.glob('img/*.dat'))],


)
