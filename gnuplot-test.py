#!/usr/bin/python -O

import Gnuplot

data = [[0,0],[1,1],[2,4],[3,9],[4,16]]
data2 = [[0,0],[1,1],[2,8],[3,27],[4,64]]
g = Gnuplot.Gnuplot(persist=1)
#g('set data style linespoints')
g('set data style boxes')
g('set boxwidth 0.75')
g('set style fill solid 1.0')
g.plot(data2)
g.replot(data)
#g.hardcopy(filename="plot-text.ps")

