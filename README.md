# GIS-with-Geopandas
Working with geopandas


## Intallation

Installing geopandas should be as simple as running `pip install geopandas` or `conda install geopandas` but for me, both methods faild to install or function propory on windows (on MacOs pip does seem to work)

A more reliable installation procedure is as follows: 

Using the terminal/cmd

Before starting, make sure you have a somewhat modern version of python 3.7 or higer is recomanded, and an up to data version of pip with "wheel" packege installed.

1) Make sure to meet the requirments above
2) Download the following files form : https://www.lfd.uci.edu/~gohlke/pythonlibs/ 
3) Download the following binaries: GDAL, Pyproj, Fiona, Shapely matching the version of Python and OS (32-bit or 64-bit).  
  (E.g. for Python v3.7x (64-bit), GDAL package should be GDAL‑3.1.2‑cp37‑cp37m‑win_amd64.whl.)
4) Create a folder to use for GIS related python projects `mkdir GIS`, move into this folder `cd GIS`  
5) Place the files in the folder of step 4
6) Open a terminal in this location
7) For each file in the folder run `pip install <filename>` for example : `pip install GDAL-3.4.3-cp310-cp310-win_amd64.whl`
   the recomanded order: GDAL, pyproj, Fiona, Shapely
![afbeelding](https://user-images.githubusercontent.com/45522614/189144455-03948d87-2acc-495a-ac64-33520caca760.png)

8) When all files are installed correctly the final step is to run `pip install geopandas` 

OPTIONAL: when using pyhon for datascience, working with jupyter lab is often required.
Required: nodejs to be installed. 

9) `pip install jupyterlab` 
10) `jupyter-lab`

Its not unlikely that some packages have trouble installing, make sure to check that you have the correct .whl file. If all fails you can also try to install those packets with the normal pip install <packet name> command. 


