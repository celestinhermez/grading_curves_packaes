from Gaussiandistribution import Gaussian

class GradeCurve(Gaussian):
    """ Class for curving grades on a test, either based on a Gaussian
     distribution or on percentiles

    Attributes:
    	mean (float) representing the mean value of the distribution
    	stdev (float) representing the standard deviation of the distribution
    	data_list (list of floats) a list of floats extracted from the data file of grades

    """

    def __init__(self, mu = 0, stdev = 1):

        Gaussian.__init__(self, mu, stdev)