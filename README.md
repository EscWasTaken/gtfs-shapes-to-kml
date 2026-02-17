# GTFS-Shapes-To-KML
Convert a GTFS shapes.txt to a KML file for work in Google Earth and GIS software.

## Usage
1. Download and install Python. This program was created specifcally on version 3.14.3 but should work on others. [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Download the latest ZIP archive from [releases](https://github.com/EscWasTaken/gtfs-shapes-to-kml/releases) and extract it into a new folder.
3. Open a terminal (Bash / Powershell / Command Prompt) in the folder and create a new virtual environment with: `python -m venv`
4. Activate the virtual environment with one of the following (Windows users try the last two):

| Shell      | Command to activate virtual environment |
|------------|-----------------------------------------|
| bash/zsh   | `source venv/bin/activate`              |
| fish       | `source venv/bin/activate.fish`         |
| csh/tcsh   | `source venv/bin/activate.csh`          |
| pwsh       | `venv/bin/Activate.ps1`                 |
| cmd.exe    | `venv\Scripts\activate.bat`             |
| PowerShell | `venv\Scripts\Activate.ps1`             |
> Source: [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html) 17/02/2026

5. Install the dependencies by runnning `pip install -r requirements.txt`
6. Place your `shapes.txt` in the same folder as `main.py` and ensure there is no `shapes.kml` file present.
7. Run `python main.py` in your terminal, and wait for it to finish. Once it does you should now have a `shapes.kml` file present.

## What is a GTFS shapes.txt file?
See [https://gtfs.org/documentation/schedule/examples/shapes/](https://gtfs.org/documentation/schedule/examples/shapes/) and [https://gtfs.org/documentation/schedule/reference/#shapestxt](https://gtfs.org/documentation/schedule/reference/#shapestxt).
Despite having a txt file extention, all data is in CSV format and looks like so:
| shape_id        | shape_pt_lat | shape_pt_lon | shape_pt_sequence | shape_dist_traveled |
|-----------------|--------------|--------------|-------------------|---------------------|
| 2-ALM-vpt-1.1.R | -37.86818462 | 145.07969648 | 1                 | 0.00                |
| 2-ALM-vpt-1.1.R | -37.86791019 | 145.07974521 | 2                 | 30.81               |
| 2-ALM-vpt-1.1.R | -37.86726871 | 145.07986577 | 3                 | 102.92              |
> Source [https://discover.data.vic.gov.au/dataset/gtfs-schedule](https://discover.data.vic.gov.au/dataset/gtfs-schedule) 14/02/2026
