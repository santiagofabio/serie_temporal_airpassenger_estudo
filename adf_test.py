def adf_test(serie_temporal):
     """
      ---------ADF test
       ADF test is used to determine the presence of unit root in the series, 
       and hence helps in understand if the series is stationary or not. 
       The null and alternate hypothesis of this test are:
              * Null Hypothesis: The series has a unit root. (non-stationary.)
              * Alternate Hypothesis: The series has no unit root. (Stationary.)

        If the null hypothesis in failed to be rejected,
        this test may provide evidence that the series is non-stationary
     """
     
     from statsmodels.tsa.stattools import adfuller
     import pandas as pd
    
     print("Results of Dickey-Fuller Test:")
     dftest = adfuller(serie_temporal, autolag="AIC")
     dfoutput = pd.Series(
        dftest[0:4],
        index=[
            "Test Statistic",
            "p-value",
            "#Lags Used",
            "Number of Observations Used",
        ],
     ) 
    
     for key, value in dftest[4].items():
          dfoutput["Critical Value (%s)" % key] = value
     print(dfoutput)
