def kpss_test(timeseries):
     """
     ------------KPSS test--------------
     KPSS is another test for checking the stationarity of a time series.
      The null and alternate hypothesis for the KPSS test are opposite that of the ADF test.
         Null Hypothesis: The process is trend stationary.
        Alternate Hypothesis: The series has a unit root (series is not stationary).
    
     """
    
     from statsmodels.tsa.stattools import kpss
     import pandas as pd
     print("Results of KPSS Test:")
     kpsstest = kpss(timeseries, regression="c", nlags="auto")
     kpss_output = pd.Series(
        kpsstest[0:3], index=["Test Statistic", "p-value", "Lags Used"]
     )
     for key, value in kpsstest[3].items():
         kpss_output["Critical Value (%s)" % key] = value
         
     print(kpss_output)