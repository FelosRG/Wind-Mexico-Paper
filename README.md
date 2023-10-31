# Wind-Stat-Forecast
🚧 *This repository contains the code for the paper "Enhancing wind power forecasting by intelligent statistical treatment of the wind resource data at the site" which is currently under review*

Wind power is a key energy source to supply clean energy to meet today ́s energy needs.
Despite the great benefits of this resource, such as zero-emissions, its main drawback is its intermittency.
Deterministic approaches are frequently used to forecast it and to estimate wind power generation. 
However, statistical approaches are more adequate to model this resource. In this paper, we
propose an intelligent statistical approach to forecast the wind energy and to estimate the electricity
that can be produced. First, the seasonality of the wind resource is determined by clustering analysis
of the monthly wind speed probabilistic distribution functions (PDFs) throughout a period of many
years. Next, a methodology that builds the wind resource typical year (WRTY) is introduced to
characterize the wind resource at any given site into so-called statistical seasons. Then, the wind
speed PDF for each season is calculated to estimate the wind energy produced each season and
throughout the year. A wind farm in Baja California, Mexico, is chosen as a case study to validate
the proposed methodology. Seasonality, WRTY and the seasonal, and annual generated energies
are estimated for a wind farm. Results are compared with measured ones showing good agreement.

## Data Source 📝
The data was obtained from the NASA model's API, which can be accessed at the [link](https://data.giss.nasa.gov/gistemp/).

## Code Structure
* In the **notebooks** folder, you will find the notebooks containing the experiments conducted.

* In the **lib** folder, you will find all the supporting code used in the notebooks. For example, in the **lib/energia.py** module, the functions for calculating the annual energy of the sites and more are defined.
## Authors
* **Monica Borunda** <br>
  CONACYT-Tecnológico Nacional de México-Centro Nacional de Investigación y Desarrollo Tecnológico, Cuernavaca, Morelos
  Correspondence: [monicabp@cenidet.tecnm.mx](monicabp@cenidet.tecnm.mx)
  
* **Adrían Ramírez** <br>
  Facultad de Ciencias, Universidad Nacional Autónoma de México, Ciudad de México.
* **Raul Garduño** <br>
 Instituto Nacional de Electricidad y Energias Limpias, Cuernavaca, Morelos.
* **Carlos García Beltran** <br>
  CENIDET, Cuernavaca, Morelos.
* **Rito Mijarez** <br>
  Instituto Nacional de Electricidad y Energias Limpias, Cuernavaca.
