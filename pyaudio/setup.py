from pythonforandroid.toolchain import PythonRecipe
from os.path import exists, join



class PyAudio(PythonRecipe):

    site_packages_name = 'Pyaudio'
    version = '0.2.11'
    url = 'http://example.com/example-{version}.tar.gz'


    depends = ['python3', 'portaudio']  




recipe = PyAudio()