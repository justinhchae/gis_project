# gis_project
 A Starter Template for GIS in Python with a complete working environment.

## About 
Just enough code to get started with GIS stuff in Python.

## Usage
* Use this template repository to build scripts for GIS analysis in Python. 
* Keep this project and its environment separate from your primary project to avoid weird dependency conflicts.

## Getting Started
* Clone this repository.
* With Anaconda, create a new environment from the provided yml file or see below for step-by-step instructions.
```bash
conda env create -f environment.yml
```
* Activate the new gis_project conda env
* Run the sample project with:
```bash
python3 main.py
```
## Key References
* Based on the Geoplot [heatmap examples page](https://geopandas.org/gallery/plotting_with_geoplot.html)

## About GIS in Python
* The two key libraries for doing GIS stuff in Python are Geoplot and Geopandas. Unfortunately, they have some intricate dependencies that can be difficult to get a project off the ground.
* The problem solved by this template is avoiding breaking your conda env when trying to install the GIS libraries by creating a separate env specifically for GIS things. This is as recommended by the developers. 
* Classic env conflicts include issues where the installation wheel takes a really long time to run and when there are strange directory errors about missing images and the like. These issues are mostly solved by setting strict channel priorities and allowing the installers to work with very specific scope. See resource sections below.

## Notable Packages that are Installed
* Python 3.8
* Geoplot
* Geopandas

## Project-Specific Resources
* Conda Set Channel Strict conda-forge. Recommend setting this in base env so that each new env you create inherits:
  ```bash
  # This setting is required to allow geoplot and geopandas to install their exact dependencies.
  conda config --set channel_priority strict
  ```
* Create Conda Environment:
  ```bash
  conda create -n gis_project python=3.8
  ```
* Activate Conda Environment:
  ```bash
  conda activate gis_project
  ```
* Install Geoplot, per [documentation](https://anaconda.org/conda-forge/geoplot):
  ```bash
  # allow the installer to install all necessary dependencies from conda-forge
  conda install geoplot -c conda-forge
  ```
* Install Geopandas, per [documentation](https://geopandas.org/getting_started/install.html):
  ```bash
  # allow the installer to install all necessary dependencies from conda-forge
  conda install geopandas -c conda-forge 
  ```
## General Resources Mostly Based on [Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* Feature Resolver:
  ```bash
  pip install texthero --use-feature=2020-resolver
  ```
* Upgrade Pip:
  ```bash
  pip3 install --upgrade pip
  ```
* List Conda Environments:
  ```bash
  conda env list
  ```
* Remove/Delete Environment:
  ```bash
  conda remove -n gis_project --all
  ```
* Display History of Revisions:
  ```bash
  conda list --revisions
  ```  
* Export Environment:
  ```bash
  conda env export > environment.yml
  ```  
* Git Things:
  ```bash
  # remove a folder dir from git tracking
  git rm -r --cached .idea/
  # remove the DS store file
  git rm --cached .DS_Store
  # reset the cache
  git rm -r --cached .
  ```
  
## Data Sources for Cook County, IL:
* Polygons: [Political Boundaries](https://datacatalog.cookcountyil.gov/GIS-Maps/Historical-ccgisdata-Political-Township-2016/uvx8-ftf4)
* Points: [Income by Zip Code](https://censusreporter.org/data/table/?table=B19001G&geo_ids=05000US17031,860|05000US17031&primary_geo_id=05000US17031)
