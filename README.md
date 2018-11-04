# GradeCurve package

## Introduction

The goal of this package is to provide an easy way to curve grades on a test.
This package was developed as part of Udacity's Data Scientist nanodegree program,
to illustrate the ideas of object-oriented programming.

## Intallation

This package has been uploaded to PyPi, so can be installed by typing in
the command line:

```pip install grade-curve```

In order to run properly, the following packages need to be installed:
- matplotlib
- numpy
- pandas
- scipy
- math

## Components

This package contains three classes and associated methods.

### General Distribution

This class is the parent class, stored in Generaldistribution.py. 
The class Distribution is used for all distributions. Its attributes:
- mean (float) representing the mean value of the distribution
- stdev (float) representing the standard deviation of the distribution
- data (list of floats) a list of floats extracted from the data file

Its methods:
- calculate_percentile: given a point on a distribution, get its percentile rank
- read_data_file: read data from a txt or csv file

### Gaussian Distribution

This class, Gaussian, stored in Gaussiandistribution.py
 is a child of the Generaldistribution class. It extends the parent class
 with the following methods:
 - calculate_mean
 - calculate_stdev
 - calculate_zscore
 - plot_histogram
 - pdf to calculate the probability density function at a given point
 - plot_histogram_pdf to plot the normalized histogram of the data and a plot of the 
probability density function along the same range
- the add magic method to add two Gaussian together
- the repr magic method displays the mean and standard distribution of the
object

### Grade Curve

The GradeCurve class, stored in GradeCurve.py, inherits
from the Gaussian class. The main addition is the curve method, which allows
to curve grades on a test to get letter grades.

## Usage

Here is the signature of the curve method:

`curve(self, default = True, grades = None, percentiles = None, z_scores = None,
              write_txt = False, write_csv = False)`

The curve method has several arguments:
- default: this argument specifies whether default
cutoffs of A until 90, B until 80, C until 70, D until 60 and F otherwise 
should be used
- grades (dict): a dictionary of letter grades and corresponding 
raw grades cutoffs 
- percentiles (dict): a dictionary of letter grades and 
their corresponding percentile cutoffs
- z_scores (dict): a dictionary of letter grades and 
their corresponding z-scores cutoffs
- write_txt (bool): whether to write the results to a txt file or not
- write_csv (bool): whether to write the results to a csv file or not

**If default is set to True, none of the grades, percentiles, z_scores arguments
can be passed.** **Similarly, only one of grades, percentiles, z_scores can be specified,
and if either exists, default cannot be True.**

This method prints out a dataframe to the console with the original
grades and their corresponding letter grades, unless the caller chooses to 
save it to CSV or txt file.

One example, using the default:

```
from GradeCurve import GradeCurve

grades = GradeCurve()
grades.read_data('../numbers.csv')
grades.curve()

```

In order to use percentiles cutoffs and save the result to a CSV file:

```
from GradeCurve import GradeCurve

grades = GradeCurve()
grades.read_data('../numbers.csv')
grades.curve(default = False, percentiles = {'A+': 95, 'A': 90, 'B+'; 85,
'B': 80, 'C+':70, 'C': 60, 'D': 50}, write_csv = True)

```

## License

Copyright 2018 Celestin Hermez <COPYRIGHT HOLDER>

Permission is hereby granted, free of charge, 
to any person obtaining a copy of this software 
and associated documentation files (the "Software"), 
to deal in the Software without restriction, 
including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons 
to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall 
be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
USE OR OTHER DEALINGS IN THE SOFTWARE.