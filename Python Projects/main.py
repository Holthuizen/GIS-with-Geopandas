import geopandas
import numpy


countries_gdf = geopandas.read_file("tl_2019_06_tract.shp")

print(countries_gdf.head())

