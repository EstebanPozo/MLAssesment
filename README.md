# MLAssesment
Niologic MLAssesment


Niologic MLAssesment is a set of tasks related to data science and machine learning using 
the Seattle 911 dataset for Niologic.

Input:
* The input of your model should take a vector with at least the date/time
Output:
* The output should contain the call volume (count) of 911 calls predicted for this time period.
* Please  provide a backtesting plot comparing the actual (measured)  call volume vs. predicted call volume for a month and a week.
* Please  think about measures to judge the quality and certainty of predictions  and provide
them as well.

<p align="center">
  <img src="./img/inputdata.png" alt="Data RAw" width="738">
</p>

## Explanation of design 
The number of days where a call has occurred are added using python in order to have a single entry for each day. Afterwards, the received data is transofrmed into two vectors
that will represent X and y using a function. Feature engineering using DataPrep and BigQuery are caried out.


The training, testing nd validation data is split using this dataframe. Afterwards the model is trained and the output printed.

## Assumptions
* No weather data available on database. So this feature has not been taken into account.
* No distinction between  type of calls (fire, hazmat etc.) has been made.

## How It Works

1. Run the MLAssessment jupyter source file. This is the main file of the project. 
2. Files such as train.py can be found in the project as requested. These files are generated using writefile following the requirements.
3. The CSV file Seattle_Real_Time_Fire_911_Calls-v.csv is the preprocessed database.
4. utest.py works by running a test over datainput.py in order to check the returned value.


## Rules:

1.   Use a library for machine  learning like Scikit.Learn or Tensorflow (or Keras or TFX) or CatBoost with a Scikit.Learn pipeline (e.g. you can use Google AI platform with a test account or  https://colab.research.google.com/ to run your code,
2.   Provide us with a ML pipeline of getting data in, processing data (scoring) and retrieving back data,
3.   Use a Jupyter notebook to create your ML code. Please  subdivide your code into training, preprocessing, testing, model and write the code from notebook to separate files (e.g. train.py via writefile),
4.   We need to be able to run and build your code ourselves,  so please  submit your code as a collection of source  code and supporting files, without any compiled code.
5.   Please  include a brief explanation  of your design and assumptions, along with your code, as
well as detailed instructions  to run your application (in your README as markdown).
6.   We assess a number  of things including the design aspect  of your solution and your object oriented  (or functional) programming  skills. While these  are small problems,  we expect  you to submit what you believe is production-quality  code; code that you'd be able to run, maintain, and evolve. You should not gold plate your solution, however we are looking for something more than a bare-bones algorithm (KISS & YARN).
7.   We want our hiring process to be fair, and for everyone  to start from the same  place. To
enable  this, we request that you do not share  or publish these  problems. Do not copy ready- made solutions from the web. 

## Usage
Requires a CSV database with the datetime where the call is displayed. This vector must be preprocessed in order to show the year-month-day date format.


