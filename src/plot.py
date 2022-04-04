import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plot:

    def __init__(self, figure, maxFigures=10):
        self.maxFigures = maxFigures
        self.figure = plt.figure()


    # add a vector plot to the  figure, figure(main)
    def addVector(self, Vector):
        """
        :type val: Vector (object)
        :rtype: added (boolean)
        """

        added = True

        # condition to change axes limits:
        # if one of the coordinates of the vector
        # we want to add is greater than one of the current
        # limits, we resize



        return added

    def clearPlot(self):
        """
        :type val: Vector (object)
        :rtype: added (boolean)
        """
        #self.plt.cla()


        return


    # axes may need to be resized after
    # vector deletion
    def resizePlot(self):
        """
        :type val: Vector (object)
        :rtype: added (boolean)
        """


        return
