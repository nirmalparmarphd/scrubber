"""
scrubber is a python library to scrub and to clean data quickly!
"""

import pandas as pd
import numpy as np

class scrubber():
    """
    scrubber is a python library to scrub and to clean data quickly!
    """
    def __init__(self) -> None:
        pass
        
    
    def ts_continuity_check(self, df:pd.DataFrame, clm:str, frequency:str="D"):
        """
        Check the continuity of time series dates at the specified frequency.

        Parameters:
        - frequency: str, optional
            The frequency to check continuity. It can be "D" for day, "M" for month, etc.

        Returns:
        - list of missing time intervals
        """
        self.df=df
        self.clm=clm
        self.date_series=df[clm]

        # Sort the DataFrame by the date column
        self.df.sort_values(by=self.clm, inplace=True)

        # Extract the date column as a Series
        date_series = self.date_series

        # Calculate the expected frequency of dates
        min_date = date_series.min()
        max_date = date_series.max()
        date_range = pd.date_range(start=min_date, end=max_date, freq=frequency)

        # Find missing time intervals by comparing the date range with the actual dates in the DataFrame
        missing_intervals = date_range[~date_range.isin(date_series)]

        # converting to pd.DataFrame
        missing_intervals = pd.DataFrame(missing_intervals)
        return missing_intervals
    
    def ts_date_filling(self, df, clm):
        """
        a function to identify missing dates from Time-Series data and fill them
        """
        pass
    

    def ts_fill_missing_dates(self, df:pd.DataFrame, clm:str, frequency="D", method='moving_average', window=3):
            """
            Identify missing dates and fill them with NaN values in the DataFrame.
            Optionally, fill missing values in other columns using a specified method.

            Parameters:
            - frequency: str, optional
                The frequency to check and fill missing dates. It can be "D" for day or "M" for month.
            - method: str, optional
                The method to fill missing values in other columns. Options: 'moving_average'.
            - window: int, optional
                The window size for the moving average (only used if method='moving_average').

            Returns:
            - DataFrame with all dates, including missing dates, and optionally filled missing values.
            """

            # Check continuity and get missing dates
            missing_dates = self.ts_continuity_check(df=df, clm=clm, frequency=frequency)

            if len(missing_dates) == 0:
                return self.df  # No missing dates, return the original DataFrame

            # # Create a DataFrame with the missing dates
            # missing_data = pd.DataFrame({self.clm: missing_dates})
            missing_data = missing_dates.set_index(self.clm)

            # Add NaN values for all columns in the missing dates DataFrame
            missing_data = missing_data.reindex(columns=self.df.columns)

            # Concatenate the original DataFrame and the missing dates DataFrame
            filled_df = pd.concat([self.df, missing_data])

            # Sort the DataFrame by the date column
            filled_df.sort_values(by=self.clm, inplace=True)

            # Fill missing values in other columns using the specified method
            if method == 'moving_average':
                filled_df = filled_df.interpolate(method='linear', limit_area='inside', limit_direction='forward', limit=window)

            return filled_df

    def ts_data_stationary_check(self, df, clm):
        """
        a function to check weather given Time-Series data is stationary or not
        """
        pass


    def ts_data_trend_check(self, df, clm):
        pass


    def ts_data_seasonality_check(self, df, clm):
        pass


    def ts_data_lag_select(self, df, clm):
        pass


    def ts_data_pdq_estimator(self, df, clm):
        pass


    def ts_data_forward_filling(self, df, clm):
        pass


    def ts_data_avg(self, df, clm, method):
        """
        method: 
            moving average (ma)
            exponentially moving average (ema)
            exponentially weighted moving average (ewma)
        """
        pass