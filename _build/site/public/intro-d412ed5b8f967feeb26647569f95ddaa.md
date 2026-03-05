# Introduction

This is a collection of notebooks that sets up a nested Regional Ocean Modeling System (ROMS) domain in Hvalfjörður, Iceland using ROMS-TOOLS and conducts comprehensive model-observation comparisons. The notebooks document the complete workflow from model configuration and forcing file preparation to validation against field observations and analysis of Ocean Alkalinity Enhancement (OAE) experiments.

% A figure of a photograph of some mountains, followed by a caption
:::{figure} https://github.com/ubbu36/C-Star-in-Hvalfjordur/blob/main/20240718_THRAINN_534860.jpg
:label: fig:fjord

A photograph of Hvalfjörður, Iceland. July 2024
:::

## Model Setup

The model configuration uses a four-level nested grid approach to resolve the transition from the open North Atlantic Ocean to the fjord-scale dynamics of Hvalfjörður:

- **`setup_iceland0.ipynb`**: Configures the outermost ROMS grid (Iceland0) covering the broader North Atlantic region. This notebook generates the base grid, sets up tidal forcing, atmospheric surface forcing, initial conditions from GLORYS reanalysis, and boundary conditions for the nested domains.

- **`setup_iceland1.ipynb`**: Prepares the first nested grid (Iceland1) with higher resolution, importing and updating the grid from the parent domain, setting up tidal forcing, initial conditions from Iceland0, surface forcing, and defining the next nested grid (Iceland2).

- **`setup_iceland2.ipynb`**: Configures the high-resolution regional grid (Iceland2) covering the Icelandic shelf and approaches to Hvalfjörður. This includes grid generation/import, tidal forcing, initial conditions from Iceland1 ROMS restart files, surface forcing, definition of the nested Iceland3 grid, and customization of river forcing.

- **`setup_iceland3.ipynb`**: Finalizes the innermost fjord-scale ROMS configuration (Iceland3) for Hvalfjörður, including grid loading, tidal forcing, surface forcing, river forcing customization, and initial conditions from Iceland2.

- **`passive_tracer_setup.ipynb`**: Adds a passive dye tracer to an existing Iceland2 run and prepares consistent initial and boundary conditions for tracer experiments, including modifying the initial restart file and updating boundary files.

All setup notebooks utilize ROMS-TOOLS for grid generation, forcing file preparation, and boundary condition handling.

## Site Overview and Grid Structure

- **`site_description.ipynb`**: Gathers site-description plots for Hvalfjörður, including bathymetry, regional setting, local forcings (wind roses, sea level anomalies), and locations of CTD casts and moorings used for model validation.

- **`grid_overview.ipynb`**: Provides an overview of the nested ROMS grids used to establish the Hvalfjörður model domain, including grid loading, outline computation, and map plotting to visualize the four-level nesting structure.

## Model-Observation Comparisons

The notebooks include comprehensive comparisons between model output and field observations:

- **`velocity_analysis.ipynb`**: Compares observed horizontal currents from HF radar/ADCP stations with ROMS model output. This includes data loading, model extraction, time series comparison, wind-rose style summaries of current direction and speed, spectral analysis of tidal and subtidal variability, and vertical profile comparisons of observed and modeled currents.

- **`ssh_comparison.ipynb`**: Compares Grundartangi tidal gauge sea-level data with the Iceland2 model sea-surface height (`zeta`), including gauge data loading, model extraction, time series comparison, and mean-offset correction.

- **`ctd_comparison.ipynb`**: Compares HAFRO CTD profiles in Hvalfjörður with the Iceland2_MARBL_2024 model solution. This includes data loading, grid/regridding, profile comparison, section plots, and biogeochemical diagnostics.

- **`bgc_analysis.ipynb`**: Compares observed and modeled dissolved inorganic carbon (DIC), alkalinity, and nutrients at CTD stations along Hvalfjörður, including observation processing, model field regridding, normalized metrics, spatial structure visualization, and nutrient comparison.

- **`sf6_observations.ipynb`**: Analyzes the SF₆ (sulfur hexafluoride) tracer observations collected during the November 2024 field trial in Hvalfjörður. SF₆ was released as a passive tracer analogue to study the dispersion and transport of an alkalinity enhancement plume. The notebook covers data loading, spatial visualization, longitudinal analysis, and plume diagnostics.

- **`sf6_model.ipynb`**: Compares modeled passive dye from Iceland2 with the observed SF₆ tracer in Hvalfjörður, including observation processing, model dye field loading and scaling, like-for-like diagnostics, and plume centroid comparison.

## Model Solution Visualization

- **`model_solution.ipynb`**: Provides a curated set of plots and diagnostics from the Iceland3_MARBL_2024 solution in Hvalfjörður, covering file selection, visualization of core fields (temperature, salinity, currents), time evolution, and assembling publication-ready figures.

- **`dye_movie.ipynb`**: Creates an animated movie of a surface dye/alkalinity tracer release in Iceland4 overlaid on an OpenStreetMap basemap, including grid and depth metrics, tracer scaling, regridding, and animation generation.

## Ocean Alkalinity Enhancement (OAE) Experiment and Analysis

- **`oae_analysis.ipynb`**: Analyzes the Iceland3_MARBL_2024 OAE experiments in Hvalfjörður, focusing on alkalinity enhancement, CO₂ removal efficiency (CDR efficiency), surface snapshots, time series, background sensitivity, and integrated diagnostics. This notebook provides comprehensive analysis of the OAE field trial, quantifying the efficiency of carbon dioxide removal through alkalinity enhancement and examining the spatial and temporal evolution of the enhanced alkalinity plume.