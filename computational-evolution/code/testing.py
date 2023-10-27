"""Testing module"""

from environment import Environment
from time import time


# sizes = [20, 40, 60, 80, 100]

# total_t = time()
# for i in range(5):
#     for j in range(4):
        
#         env = Environment(size=sizes[i], sim_num=j+1)
#         t0 = time()
#         env.run(data='none')
#         print('env_size',sizes[i],'simulation',j+1,'time_taken =',time()-t0)

# print('TOTAL TIME',time()-total_t)

env = Environment(sim_num=1)

env.run()