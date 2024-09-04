# Satellite-Imagery-Analysis-NDVI-and-NDMI-Calculation
This project processes multispectral satellite images to calculate and analyze two important indices: the Normalized Difference Vegetation Index (NDVI) and the Normalized Difference Moisture Index (NDMI). These indices are used to assess vegetation health and moisture content in the land surface.

## Overview

- **NDVI**: Measures vegetation health by comparing the reflectance of near-infrared (NIR) and red light.
- **NDMI**: Assesses moisture content by comparing NIR and short-wave infrared (SWIR) reflectance.

The script reads a satellite image stored as a GeoTIFF file, calculates the NDVI and NDMI, and saves the results as new GeoTIFF files. It also computes the average values of these indices across the image.

## Features

- **Multispectral Image Processing**: Reads a satellite image with multiple spectral bands.
- **NDVI Calculation**: Computes NDVI using the NIR and red bands.
- **NDMI Calculation**: Computes NDMI using the NIR and SWIR bands.
- **GeoTIFF Export**: Saves the NDVI and NDMI calculations as new GeoTIFF files.
- **Average Index Calculation**: Outputs the average NDVI and NDMI values for the entire image.
