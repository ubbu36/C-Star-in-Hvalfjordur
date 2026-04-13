
def roms_regrid(gridfile,romsfile):
    import xesmf as xe
    import xarray as xr
    import numpy as np
    grid=gridfile
    grid = grid.rename({"lon_rho": "lon", "lat_rho": "lat"})

    lon_min=(grid.lon.min().values)
    lon_max=(grid.lon.max().values)
    lon_step=((lon_max-lon_min)/len(grid.eta_rho))

    lat_min=(grid.lat.min().values)
    lat_max=(grid.lat.max().values)
    lat_step=((lat_max-lat_min)/len(grid.xi_rho))

    ds_out = xr.Dataset(
        {
            "lon": (["lon"], np.arange(lon_min, lon_max, lon_step), {"units": "degrees_north"}),
            "lat": (["lat"], np.arange(lat_min, lat_max, lat_step), {"units": "degrees_east"}),
        }
    )

    regridder = xe.Regridder(grid, ds_out, "bilinear")
    regrid_file=regridder(romsfile)
    return regrid_file

def roms_regrid_u(gridfile,romsfile):
    import xesmf as xe
    import xarray as xr
    import numpy as np
    romsfile=romsfile.interp(xi_u=romsfile.xi_u+0.5)
    romsfile=romsfile.rename({"xi_u": "xi_rho"})
    
    grid=gridfile
    grid=grid.isel(xi_rho=slice(0,len(grid.xi_rho)-1))
    grid = grid.rename({"lon_rho": "lon", "lat_rho": "lat"})

    lon_min=(grid.lon.min().values)
    lon_max=(grid.lon.max().values)
    lon_step=((lon_max-lon_min)/len(grid.eta_rho))

    lat_min=(grid.lat.min().values)
    lat_max=(grid.lat.max().values)
    lat_step=((lat_max-lat_min)/len(grid.xi_rho))

    ds_out = xr.Dataset(
        {
            "lon": (["lon"], np.arange(lon_min, lon_max, lon_step), {"units": "degrees_north"}),
            "lat": (["lat"], np.arange(lat_min, lat_max, lat_step), {"units": "degrees_east"}),
        }
    )

    regridder = xe.Regridder(grid, ds_out, "bilinear")
    regrid_file=regridder(romsfile)
    return regrid_file

def roms_regrid_v(gridfile,romsfile):
    import xesmf as xe
    import xarray as xr
    import numpy as np
    
    romsfile=romsfile.interp(eta_v=romsfile.eta_v+0.5)
    romsfile=romsfile.rename({"eta_v": "eta_rho"})
    
    grid=gridfile
    grid=grid.isel(eta_rho=slice(0,len(grid.eta_rho)-1))
    grid = grid.rename({"lon_rho": "lon", "lat_rho": "lat"})

    lon_min=(grid.lon.min().values)
    lon_max=(grid.lon.max().values)
    lon_step=((lon_max-lon_min)/len(grid.eta_rho))

    lat_min=(grid.lat.min().values)
    lat_max=(grid.lat.max().values)
    lat_step=((lat_max-lat_min)/len(grid.xi_rho))

    ds_out = xr.Dataset(
        {
            "lon": (["lon"], np.arange(lon_min, lon_max, lon_step), {"units": "degrees_north"}),
            "lat": (["lat"], np.arange(lat_min, lat_max, lat_step), {"units": "degrees_east"}),
        }
    )

    regridder = xe.Regridder(grid, ds_out, "bilinear")
    regrid_file=regridder(romsfile)
    return regrid_file
