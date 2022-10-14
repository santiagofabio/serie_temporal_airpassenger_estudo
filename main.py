from this import d
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
import scipy.stats as stats
from shapiro_wilk_teste_hipotese import shapiro_wilk_teste_hipotese
from scipy import stats
import seaborn as sns
import statsmodels.tsa.stattools
from adf_test import adf_test
from kpss_test import kpss_test
rcParams['figure.figsize'] =[15,6]
rcParams["legend.loc"] ='best'

"""
This dataset provides monthly totals 
of a US airline passengers from 1949 to 1960.
"""

file ='AirPassengers.csv'
dados = pd.read_csv(file, sep =',')


serie_temporal =pd.Series(dados["#Passengers"].values, index=dados["Month"].values)
serie_temporal.plot( label='AirPassengers')
plt.xlabel("Anos")
plt.ylabel("Numbero de passageiros")
plt.legend()
plt.show()


stats.probplot(serie_temporal, dist="norm", plot =plt)
plt.title("Normal QQ plot -Serie AirPassengers")
plt.show()

#Teste de Shapiro Wilk
"""
Perform the Shapiro-Wilk test for normality.

The Shapiro-Wilk test tests the null hypothesis that the data 
was drawn from a normal distribution.

Parameters
        x: array_like (Array of sample data.)
Returns
        statistic: float (The test statistic.)
        p-value: float (The p-value for the hypothesis test.)
"""

statistic,p_value= stats.shapiro(serie_temporal)
alpha =0.05 # significancia
shapiro_wilk_teste_hipotese(statistic,p_value, alpha)

#Transformação Log (Diminuir a variãncia e melhorar a normalidade)
serie_temporal_log =np.log(serie_temporal)
statistic,p_value= stats.shapiro(serie_temporal_log)
shapiro_wilk_teste_hipotese(statistic,p_value, alpha)

stats.probplot(serie_temporal_log, dist="norm", plot =plt)
plt.title("Normal QQ plot- Serie-Log-AirPassengers")
plt.savefig('Normal_QQ_Serie_Log_AirPassengers.png', format='png', dpi=300)
plt.show()


#Serie raiz cubica 
serie_temporal_raiz_cubica = serie_temporal**(1/3)
statistic,p_value= stats.shapiro(serie_temporal_raiz_cubica)
shapiro_wilk_teste_hipotese(statistic,p_value, alpha)
stats.probplot(serie_temporal_raiz_cubica, dist="norm", plot =plt)
plt.title("Normal QQ plot- Serie-Raiz3-AirPassengers")
plt.savefig('Normal_QQ_Serie_Raiz3_AirPassengers.png', format='png', dpi=300)
plt.show()



sns.distplot(serie_temporal,label='Serie-AirPassengers' )
plt.legend()
plt.title('Hist_Serie_AirPassenger')
plt.savefig('Hist_Serie_AirPassengers.png', format='png', dpi=300)
plt.show()


sns.distplot(serie_temporal_log,label='Serie-Log-AirPassengers' )
plt.legend()
plt.title('Hist_Log_AirPassengers')
plt.savefig('Hist_Log_AirPassengers.png', format='png', dpi=300)
plt.show()


sns.distplot(serie_temporal_raiz_cubica,label ='Serie-Raiz3-AirPassengers' )
plt.legend()
plt.title('Hist_Log_Serie_Raiz3_AirPassengers')
plt.savefig('Hist_Log_Serie_Raiz3_AirPassengers.png', format='png', dpi=300)
plt.show()


"""
---------Stationarity and detrending (ADF/KPSS)
Stationarity means that the statistical properties of a time series i.e. mean,
variance and covariance do not change over time.
Many statistical models require the series to be stationary 
to make effective and precise predictions.

Two statistical tests would be used to check the stationarity of a time series 
– Augmented Dickey Fuller (“ADF”) test and
- Kwiatkowski-Phillips-Schmidt-Shin (“KPSS”) test. 
A method to convert a non-stationary time series into stationary series shall also be used.
"""


adf_test(serie_temporal)

#Teste Kpss
kpss_test(serie_temporal)


#Diferenciacao de uma serie
serie_temporal_diferenciada = np.diff(serie_temporal)
plt.plot(serie_temporal_diferenciada, label ='Serie diferencial')
plt.legend()
plt.show()
kpss_test(serie_temporal_diferenciada)
#Verificar a normalidade da serie temporal