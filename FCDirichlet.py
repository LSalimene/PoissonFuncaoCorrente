import numpy as np
def fcDirichlet(u,v,dx,dy,l=2500,CC1=0,CC2=0,CC3=0,CC4=0):
    """
    Esta função realiza o cálculo da Função Corrente a partir de um campo de velocidade conhecido com a opção de escolha dos valores da Condição de Contorno de Dirichlet nas bordas.
        
    Argumentos:
    u : numpy.ndarray
        Matriz com a componente u da velocidade.
    v : numpy.ndarray
        Matriz com a componente v da velocidade.
    dx : float
        Distância entre cada ponto da grade em x.
    dy : float
        Distância entre cada ponto da grade em y.
    l : int, optional
        Número de iterações que o método irá utilizar (padrão é 2500).

    CC1 : int, optional
        Condição de contorno para o canto superior esquerdo (padrão=0)
    CC2 : int, optional
        Condição de contorno para o canto superior direito, opcional (padrão=0)
    CC3 : int, optional
        Condição de contorno para o canto inferior esquerdo, opcional (padrão=0)
    CC4 : int, optional
        Condição de contorno para o canto inferior direito, opcional (padrão=0)
        
    Resultados:
    Função Corrente calculada numericamente pelo método iterativo com `l` iterações]
    """
    dudy, dudx = np.gradient(u, dx, dy)
    dvdy, dvdx = np.gradient(v, dx, dy)
    omega = dvdx - dudy
    psi = np.zeros_like(omega) 
    k = 0
    for i in range(v.shape[0]):
         for j in range (v.shape[1]):
            if i==0:
                psi[0,j] = CC1
            if j==0:
                psi[0,1] = CC2
            elif i==v.shape[0]-1:
               psi[v.shape[0]-1,j] = CC3
            elif j==v.shape[1]-1:
                psi[i,v.shape[1]-1] = CC4
            else:
                psi[i,j]=0

    while k<l:
        for i in range(1,v.shape[0]-1):
            for j in range (1,v.shape[1]-1):
                    psi[i,j] = 0.25*(psi[i+1,j]+psi[i,j+1]+psi[i-1,j]+psi[i,j-1]-(dy*dx*omega[i,j]))
        k = k+1
    return psi
