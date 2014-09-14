# -*- coding: utf-8 -*-

import thinkbayes2
import thinkplot

d6=thinkbayes2.Pmf(range(1,7))
three=d6+d6+d6
three.Incr(1000)
three.Incr(.5)
three.Incr(1.5)
three.Normalize()

print 'PMF of three dice'
print three


#print('{val} {prob}'.format(val='Value',prob='Prob'))
for v,p in three.Items():
    vlist=str(v).split('.')
    if len(vlist)==1:
        vlist.append('')
    print(vlist[0],vlist[1])
    #print('{val:>8,f}  {prob:<}'.format(val=float(v),prob=p))
    
print('10.3'.split('.'))
#no fill
    #aling
    
#print "Job {item:15} {value[0]:>6}.{value[1]:<6} {units:3}".format(item=job_IDs[i]+':', value=memory_used[i].split('.') if '.' in memory_used[i] else (memory_used[i], '0'), units=memory_units[i])
#three.Print()
    