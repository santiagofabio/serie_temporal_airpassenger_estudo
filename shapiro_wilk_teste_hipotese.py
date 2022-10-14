def shapiro_wilk_teste_hipotese(statistic,p_value, alpha):
     from scipy import stats
     alpha =0.05 # significancia
     print("-----Shapiro-Wilk Test---------")
     print('Statistic: {:.5f} '.format(statistic))
     print('p_value: {:.5f} '.format(p_value))

     if p_value>alpha:
        print(f'Hipotese H0 aceita: Distribuição Normal')
     else: 
        print(f'Hipotese H1 aceita: Não Distribuição Normal')
 
     print("-----------------------------")
     return(0)