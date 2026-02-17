import numpy as np
import pandas as pd
import simplekml

shapes = pd.read_csv("shapes.txt")

kml = simplekml.Kml()
kml.document.name = "shapes"

index = shapes.shape_id.unique()

for i in index:
    ls = kml.newlinestring(name=i)

    path = shapes.loc[shapes["shape_id"] == i]
    lonlat = path[["shape_pt_lon", "shape_pt_lat"]] # KML coords are in longitude/latitude
    
    # Source - https://stackoverflow.com/a/45285308
    # Posted by coldspeed95, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-02-17, License - CC BY-SA 4.0
    ls.coords = [tuple(r) for r in lonlat.to_numpy().tolist()]

kml.save("shapes.kml")