# Dataset information

Source of the File: https://www.ncei.noaa.gov/cdo-web/datasets/GHCND/locations/FIPS:PK/detail#stationlist

Date accessed: September 12, 2025.

Description:  NOAA data for weather stations in Pakistan. Date range from 1970 to today.

Size: 2.8 MB, shape (146161,17)

License: Unsure. Federal Government data.

# Methods

## Tools/libraries used:

- pandas: Primary data manipulation and cleaning
- tkinter: File selection dialog for dynamic data loading
- os: Directory management and file path operations
- numpy: Numerical operations and array handling
- matplotlib and seaborn :- Data viz
- Scipy: Stats operations.

## Data load-up

- Implemented a small tkinter function to load data from path.

## Data cleanup

- Renamed the cyptic column `PRCP` to `precipitation_original`
- `precipitation_original` has alot of missing values. Instead of just dropping the empty rows, a copy of `precipitation_original` was created where the `na`s were filled with 0. This kept the chain of provinence for what was done with missing values.
- Split the Date column from a single `year-day-month` format to three columns for each data level.
- Split the main datafile into multiple files. One subframe/file for each file

## Data inference

- Used a forward-filling heuristic to take the station-ID with (elevation, longitude, lattitude) and fill out same station-IDs that do not have said meta-data.


## Exploratory Data analysis

### Summary stats generated:-

- Mean :- Mean of annual percipitation across stations.
- Median :- Median of annual percipitation across stations.
- Range :- Range values for percipitation between and across stations.
- Slopes :- What are the general trends in precipitation.
- Pearson's R :- Are the stations in sync in how they change.

### Visualizatoins

- Bar graphs of means and medains (facet wrapped).
- Trendlines.
- Scatter plot of rates of change with regards to latitude, longtitude and elevation.

### Patterns observed

- Over the past 50 years, the average rate of precipitation has generally increased. The patterns of flooding in that region of the world may be explained by this. 
- The rates of changes are somewhat similar between the stations.

# Results

- Key findings :- The rate of percipitation has consistently ticked upward in the last 50 years. This perhaps explains the trends of flooding in that part of the world. And the stations are somewhat similar in how they are recording wet and dry conditions.

- ![A facet of the means]("Images/Means.png" "An image that very clearly shows the 2021 flodding.")


- Interesting: Plotting the means and the medians in histograms, one can actually see the massive floods that took place in Pakistan around 2019/2020. This jumps out as a skyscraper in the data. 

# Collaboration notes

The team dynamic was that Hamna is a beginner in python programming and Rijan is more experienced. So, that being the case Hamna did the "rough draft" for Data clean-up.  Rijan participated in both Data clean up,  EDA, Data visualization, code formatting, function creation, simulated the merger conflict and the final draft of the code.

## Hamna:- 

- Rijan and Hamna met to discuss data procurement. 
- Ultimately, Hamna picked out NOAA, procured the data and did the rought draft of the data clean up.
- Created the repo and uploaded the files.

## Rijan :-

- Took Hamna's rough draft python script with data clean up code and converted it to a jupyter notebook.
- Re-factored the rough draft code to aid reproducibility (i.e. removed hard-coded paths and converted logic into functions).
- Wrangled the date metadata.
- Calculated summary statistics.
- Did data visualization.
- Wrote the README.
- Simulated the merge conflict.
- Created the `requirements.txt` file.

# Reproducibility Instructions

- So, long as you have the listed packages mentioned there should be no trouble running the workflow.
- When the notebook prompts you to submit a file - please submit the data file `data/Raw \data.csv`.s
- Please see the `requirements.txt` file.

# Merge conflicts

- Due to time constraints Rijan had to simulate a merge conflict. I made a commit from one machine and continued working on a different machine without pulling. I made a second commit from a different machine thus creating the conflict.