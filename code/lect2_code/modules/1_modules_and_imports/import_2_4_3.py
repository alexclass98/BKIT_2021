import os
from module_1 import sum1 as module_1_sum1
from module_2 import sum1 as module_2_sum1

# import * рекомендуется только во вспомогательном коде
# при отладке, написании тестов и т.д.

print('Hello from {}'.format(os.path.basename(__file__)))

#a=2
#b=3

a,b = 2,3

print('{} + {} = {}'.format(a, b, module_1_sum1(a,b)))
print('{} + {} = {}'.format(a, b, module_2_sum1(a,b)))
