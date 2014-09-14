# -*- coding: utf-8 -*-

import thinkbayes2
import thinkplot
import cmath

#==============================================================================
#     def Print(self):
#         """Prints the Pmf in a table format.
# 
#         returns: Pmf
#         """
#         for v, p in self.Items():
#             print('{val:>8,}  {prob:<}'.format(val=v,prob=p))
#         return self
#==============================================================================


d6=thinkbayes2.Pmf(range(1,7))
three=d6+d6+d6
print 'PMF of three dice'
three.Print()

#thinkplot.Hist(d6)
#thinkplot.Hist(d6+d6)
thinkplot.Hist(three)
#thinkplot.Hist(d6+d6+d6+d6+d6)

print 'parentheses'
print('Mean:',three.Mean(),'Var:',three.Var())
print three.Mean(),three.Var()
print 'format'
print("{0:,.5f}".format(three.Mean()),"{0:.5f}".format(three.Var()))
print "{0:,.5f}".format(three.Mean()),"{0:.5f}".format(three.Var())
#this returns a string, but can be wrapped with float()
print("%.5f" % three.Var()) #old way

print '\nstd'
print("{0:,.5f}".format(three.Var()**.5))
print("{0:,.5f}".format(cmath.sqrt(three.Var())))
print cmath.sqrt(-1)

print "\n{0}: {1:,.5f}".format('Pr{three>16}',three.ProbGreater(16))
print "\n{0}: {1:,.5f}".format('random value from three:',three.Random())

threegiven9=d6+d6+d6
for n in range (3,9):
    threegiven9.Set(n,0) #strange... shows values as integers instead of floats
threegiven9.Normalize()
threegiven9.Print()


thinkplot.Hist(threegiven9)
print "\n{0}: {1:,.5f}".format('Pr{threegiven9>16}',threegiven9.ProbGreater(16))
