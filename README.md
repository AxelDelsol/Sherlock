![Python application](https://github.com/AxelDelsol/Sherlock/workflows/Python%20application/badge.svg)

# Sherlock
Small API to analyse text and retrieve people's information.

## How to use on UNIX/MAC

1. Clone this repo : `git clone https://github.com/AxelDelsol/Sherlock.git`
2. Move inside the repo : `cd Sherlock`
2. Install the dependencies : `pip install -r requirements.txt`
3. Set up the following environement variables:
    * `export TEXTRAZOR_API_KEY="your_key"`
    * `export FLASK_APP="sherlock"`
4. `flask run`

## How to use on Windows

1. Clone this repo : `git clone https://github.com/AxelDelsol/Sherlock.git`
2. Move inside the repo : `cd Sherlock`
2. Install the dependencies :  `py -m pip install -r requirements.txt`
3. Set up the following environment variables: 
    * `$env:TEXTRAZOR_API_KEY="your_key"`
    * `$env:FLASK_APP="sherlock"`
4. `flask run`

## Build a docker image

1. Clone this repo : `git clone https://github.com/AxelDelsol/Sherlock.git`
2. Move inside the repo : `cd Sherlock`
3. `docker build --build-arg TextRazorKey="your_key" -t sherlock-demo .
4. `docker run -p 5000:5000 sherlock-demo`
5. Visit http://localhost:5000/ and have fun !