from pythonforandroid.toolchain import PythonRecipe
from os.path import exists, join



class PyAudio(PythonRecipe):

    site_packages_name = 'PyAudio'
    version = '0.2.13'
    url = 'https://files.pythonhosted.org/packages/91/a0/f439da954d78a987298cb8d1ca1b141c53b1d1d1c7a50e17198ed061b9ac/PyAudio-0.2.13.tar.gz'
    install_in_hostpython = True
    


    depends = ['python3', 'portaudio', 'portaudio19-dev', 'python-pyaudio', 'gcc-multilib']
    patches = [
       "setup.patch"
    ]




recipe = PyAudio()
