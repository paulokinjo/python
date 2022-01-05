# Python Data Analysis

## Modules
```
$ sudo apt-get install -y python3-pip
$ pip3 install ipython
$ python3 -m IPython

$ pip3 install jupyter
$ sudo cp .local/bin/jupyter-notebook /usr/sbin/

$ pip3 install ipykernel
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ python3 -m ipykernel install --user --name=venv
$ jupyter-notebook --ip 0.0.0.0 --port 8888
```

# More
```
$ jupyter kernelspec list

$ jupyter kernelspec uninstall venv
```