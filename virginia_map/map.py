import geopandas
import matplotlib.pyplot as plt
path_to_data = geopandas.datasets.get_path("nybb")
gdf = geopandas.read_file(path_to_data)

gdf
gdf = gdf.set_index("BoroName")
gdf["area"] = gdf.area
gdf["area"]
gdf.plot("area", legend=True)

plt.show()