# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:10:36 2024

@author: nikol
"""

import rasterio
import numpy as np
# import matplotlib.pyplot as plt

img = rasterio.open('response_bands.tiff')
full_img = img.read()

num_bands = img.count
print(f"Satelite image contains {num_bands} bands \n")

# Metadata
# meta = img.meta
# print(meta)

# Coordinate reference şystem
# crs = img.crs

# Normalized Difference Vegetation Index
# NDVI = (NIR - Red)/(NIR + Red) 
# To calculate Normalized Difference Moisture Index we assume Sentinel-2 since we have 13th bands
# NDMI = (NIR - SWIR) / (NIR * SWIR)
# NDMI = (B08 – B11)/(B08 + B11)
# NIR  is 8th band, Red is 4th band, SWIR is 11th band
# 4th band --> convert to float
red_img = full_img[3].astype('f4')
# 8th band --> convert to float
nir_img = full_img[7].astype('f4')
# 11th band --> convert to float
swir_img = full_img[10].astype('f4')

# NDVI calculation
ndvi = np.divide(np.subtract(nir_img, red_img), np.add(nir_img, red_img))
# Convert leftover nan values to -1
ndvi = np.nan_to_num(ndvi, -1)

# NDMI calculation
ndmi = np.divide(np.subtract(nir_img, swir_img), np.add(nir_img, swir_img))
# Convert leftover nan values to -1
ndmi = np.nan_to_num(ndmi, -1)

"""
Visualize NDVI picture
"""
# plt.figure()
# plt.imshow(ndvi, cmap = 'viridis')
# plt.colorbar()
# plt.title('NVDI of satelite image')

"""
Visualize NDMI picture
"""
# plt.figure()
# plt.imshow(ndmi, cmap = 'viridis')
# plt.colorbar()
# plt.title('NDMI of satelite image')

"""
Saving NVDI and NDMI image as tiff
"""
profile_ndvi = {
    'driver': 'GTiff',
    'dtype': 'float32',
    'nodata': None,
    'width': ndvi.shape[1],
    'height': ndvi.shape[0],
    'count': 1,  # single band
    'crs': rasterio.crs.CRS.from_epsg(32633),
    'transform': rasterio.transform.Affine(9.99852737238969, 0.0, 632737.7415393547,
                                           0.0, -9.986633815398687, 4781964.911356853)
}

with rasterio.open('ndvi.tiff', 'w', **profile_ndvi) as dst:
    dst.write(ndvi, 1)  # Write the array to the first band  
   
print("NDVI image has been saved as ndvi.tiff \n")    
    
profile_ndmi = {
    'driver': 'GTiff',
    'dtype': 'float32',
    'nodata': None,
    'width': ndmi.shape[1],
    'height': ndmi.shape[0],
    'count': 1,  # single band
    'crs': rasterio.crs.CRS.from_epsg(32633),
    'transform': rasterio.transform.Affine(9.99852737238969, 0.0, 632737.7415393547,
                                           0.0, -9.986633815398687, 4781964.911356853)
}

with rasterio.open('ndmi.tiff', 'w', **profile_ndmi) as dst:
    dst.write(ndmi, 1)  # Write the array to the first band

print("NDMI image has been saved as ndmi.tiff \n")  

"""
Average value of NDVI and NDMI calculation
"""

# Calculate the average NDMI value
average_ndvi = np.mean(ndvi)

print(f'Average NDVI value for the entire image: {average_ndvi} \n')

# Calculate the average NDMI value
average_ndmi = np.mean(ndmi)

print(f'Average NDMI value for the entire image: {average_ndmi} \n')
