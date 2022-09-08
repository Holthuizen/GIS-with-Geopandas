# GIS-with-Geopandas
Working with geopandas

# Installation
Installing geopandas should be as simple as running pip install geopandas or conda install geopandas but for me, both methods failed to install or function properly on windows (on MacOS pip does seem to work)

A more reliable installation procedure is as follows:

(this tutorial relies on the use of a commandline/terminal)
Before starting, make sure you have a somewhat modern version of python 3.7 or higher is recommended, and an up to data version of pip with "wheel" package installed.

1.	Make sure to meet the requirements above
2.	Download the following files form : https://www.lfd.uci.edu/~gohlke/pythonlibs/
3.	Download the following binaries: GDAL, Pyproj, Fiona, Shapely matching the version of Python and OS (32-bit or 64-bit).
(E.g. for Python v3.7x (64-bit), GDAL package should be GDAL 3.1.2 cp37 cp37m win_amd64.whl.)
4.	Create a folder to use for GIS related python projects: `mkdir GIS`, native to this folder: `cd GIS`
5.	For each file in the folder run: `pip install <filename>` for example : `pip install GDAL-3.4.3-cp310-cp310-win_amd64.whl` the recommended order: GDAL, pyproj, Fiona, Shapely  
6.	When all files are installed correctly the final step is to run: `pip install geopandas`
	
OPTIONAL: When using pyhon for data science, working with Jupyter Lab is often desired (Requires NodeJS to be installed).

8.	`pip install jupyterlab`
9.	`jupyter-lab`
  
It is not unlikely that some packages have trouble installing, make sure to check that you have the correct .whl file. If all fails, you can also try to install those packets with the normal `pip install command`.
