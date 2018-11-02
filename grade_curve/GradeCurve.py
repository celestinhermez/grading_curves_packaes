from Gaussiandistribution import Gaussian
import pandas as pd

class GradeCurve(Gaussian):
    """ Class for curving grades on a test, either based on a Gaussian
     distribution or on percentiles. It returns a dataframe with the original grades and the associated letter,
     with the option of writing it to a text or csv file

    Attributes:
    	mean (float) representing the mean value of the distribution
    	stdev (float) representing the standard deviation of the distribution
    	data_list (list of floats) a list of floats extracted from the data file of grades

    """

    def __init__(self, mu = 0, stdev = 1):

        Gaussian.__init__(self, mu, stdev)

    def curve(self, default = True, grades = None, percentiles = None, z_scores = None,
              write_txt = False, write_csv = False):
        """Function to curve the grades on a test

        Args:
            default (bool): whether to use default cutoff values, i.e. A until 90, B until 80, C until 70, D until 60
            and F otherwise
            grades (dict): a dictionary of raw grades cutoffs and the corresponding letter grades
            percentiles (dict): a dictionary of grades and their corresponding percentile cutoffs
            z_scores (dict): a dictionary of grades and their corresponding z-scores cutoffs
            write_txt (bool): whether to write the results to a txt file or not
            write_csv (bool): whether to write the results to a csv file or not

        Returns:
            a Pandas dataframe of the original grades and the corresponding letter grades

        """
        # we assert that either the default is chosen or one of the other 3 arguments
        assert (default or (grades is not None or percentiles is not None or z_scores is not None)), \
                "Must choose the default cutoffs or any of the other three possible cutoffs"


        if default:

            # We check that not both the default and other arguments are being passed
            assert (grades is None and percentiles is None and z_scores is None), \
                "Cannot pass an argument if the default cutoffs are chosen"

            # We use a dictionary to store the cutoffs, loop through all the grades to check where they fall compared
            # to the cutoff. Important to have the lower bound otherwise it will fail

            letter_grades = list()
            cutoffs = {'A': 90, 'B': 80, 'C': 70, 'D': 60, 'F': 0}
            reverse_cutoffs = {v: k for k, v in cutoffs.items()}

            for grade in self.data:
                for cutoff in cutoffs.values():
                    if grade >= cutoff:
                        letter_grades.append(reverse_cutoffs[cutoff])
                        break

            # We create a dataframe to return, and write it to csv or txt if the user so chooses

            curved_grades = pd.DataFrame({"Original Grades": self.data, "Letter Grades": letter_grades})
            curved_grades = curved_grades[['Original Grades', 'Letter Grades']]

        # Work with other raw grade cutoffs
        # Remember to add the zero lower bound, whether the user put it or not we will need it for the implementation

        # Work with percentile cutoffs, add lower bound (0 in this case)

        # Work with z-scores cutoffs, add lower bound (-Inf)

        else:
            assert ((grades is not None and percentiles is None and z_scores is None) or \
                   (grades is None and percentiles is not None and z_scores is None) or \
                   (grades is None and percentiles is None and z_scores is not None)),\
                "Only one of the three arguments grades, percentiles and z_score can be passed"

        if write_csv:
            curved_grades.to_csv('curved_grades.csv', index = False)

        if write_txt:
            with open('curved_grades.txt', 'w') as file:
                for i in range(curved_grades.shape[0]): #for each row of the dataframe
                    file.write('{}: {}'.format(curved_grades.iloc[i, 0],
                                               curved_grades.iloc[i, 1]))
                    file.write('\n')

        return(curved_grades)