![Github]https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white(https://github.com/LSalimene/PoissonFuncaoCorrente)

PoissonFuncaoCorrente

Esse pacote utiliza métodos númericos iterativos para resolver a equação que relaciona a Função Corrente com a vorticidade. 

Use o gerenciador de pacotes pip para instalar o pacote PoissonFuncaoCorrente com o comando:

pip install PoissonFuncaoCorrente

O pacote PoissonFuncaoCorrente é liberado sob a licença [MIT].

## Exemplo de utilização
```
import PoissonFuncaoCorrente as fcp
import numpy as np
import matplotlib.pyplot as plt 
N = 100
xmax = 1
xmin = -1
ymax = 1
ymin = -1
x = np.linspace(xmin,xmax,num=N)
y = np.linspace(ymin,ymax,num=N)
X,Y = np.meshgrid(x,y)
u = (Y/(np.sqrt(X**2+Y**2)))*(1/(2*np.pi))
v = (-X/(np.sqrt(X**2+Y**2)))*(1/(2*np.pi))
lx = xmax-xmin
ly = ymax-ymin
dx = lx / (N-1)
dy = ly / (N-1)

psi = fcp.funcaocorrente(u,v,dx,dy)
```
