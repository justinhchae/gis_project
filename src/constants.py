import os

WORKFLOW_ROOT = os.environ['PWD']
MAP_DATA_PATH = os.path.join(WORKFLOW_ROOT, 'map_data')

TOWNSHIP_POLYGONS_GEOJSON = os.sep.join([MAP_DATA_PATH, "Historical - ccgisdata - Political Township 2016.geojson"])
INCOME_POLYGONS_GEOJSON = os.sep.join([MAP_DATA_PATH, "acs2019_5yr_B19001_86000US60645.geojson"])
TOWNSHIP_POINTS_GEOJSON = os.sep.join([MAP_DATA_PATH, "il_towns_zip_codes.geojson"])