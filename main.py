import geoplot as gplt
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

from src import constants

# data from cook county open data and us census
township_boundaries = gpd.read_file(constants.TOWNSHIP_POLYGONS_GEOJSON)
zip_code_data = gpd.read_file(constants.TOWNSHIP_POINTS_GEOJSON)

# call geoplot plot on polygons as ax
ax = gplt.polyplot(township_boundaries)
# plot point data with same axis, ax
gplt.pointplot(zip_code_data,s=1, ax=ax)
# set title
plt.title("Example Plot: IL State-wide Zip Codes and Cook Count Township Boundaries")
# display plot
plt.show()