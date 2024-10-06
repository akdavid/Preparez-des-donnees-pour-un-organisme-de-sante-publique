import numpy as np
import pandas as pd
from typing import Any, Set, List
import matplotlib.pyplot as plt
import seaborn as sns


def nan_rate_by_columns(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the nan rate for each column in a pandas DataFrame.

    Parameters:
    - df: pandas DataFrame

    Returns:
    - tx: pandas Series
        A Series containing the nan rates for each column in the DataFrame.
        The values are formatted as percentages (e.g., '10.00%').

    Example:
    >>> nan_rates = nan_rate_by_columns(my_dataframe)
    >>> print(nan_rates)
    column1    5.00%
    column2    0.00%
    column3   12.50%
    dtype: object
    """
    # Calculate nan rates for each column
    nan_rates = df.isnull().sum(axis=0) / df.shape[0] * 100.00
    
    # Format nan rates as percentages
    tx = nan_rates.transform(lambda x: '{:02.2f}'.format(x)+' %')
    
    return tx

def count_columns_by_nan_rate(df: pd.DataFrame, threshold: float = 50.0) -> int:
    """
    Function returning the number of columns with nan rate above a given threshold.
    
    Parameters:
    - df: pandas DataFrame
    - threshold: float, the nan rate threshold (default is 50)
    
    Returns:
    - count: int, the number of columns with nan rate above the threshold
    """
    nan_rates = df.isnull().sum(axis=0) / df.shape[0] * 100.00
    above_threshold = nan_rates[nan_rates > threshold]
    count = above_threshold.shape[0]
    return count

def calculate_nutriscore_nutrigrade(energy_100g: float,
    saturated_fat_100g: float,
    sugars_100g: float,
    fiber_100g: float,
    proteins_100g: float,
    sodium_100g: float
) -> list:
    """
    Calculate Nutri-Score and Nutri-Grade based on the given nutritional values.

    Parameters:
    - energy_100g (float): Energy content per 100g.
    - saturated_fat_100g (float): Saturated fat content per 100g.
    - sugars_100g (float): Sugars content per 100g.
    - fiber_100g (float): Fiber content per 100g.
    - proteins_100g (float): Proteins content per 100g.
    - sodium_100g (float): Sodium content per 100g.

    Returns:
    - list: A list containing Nutri-Score and Nutri-Grade.

    Nutri-Score Calculation:
    Points for nutrients to limit (points A):
    - Based on energy, sugars, saturated fat, and sodium content.

    Points for nutrients to favor (points C):
    - Based on fiber and proteins content.

    Nutri-Score is calculated as points A minus points C.

    Nutri-Grade:
    - 'a': Nutri-Score <= -1
    - 'b': -1 < Nutri-Score <= 2
    - 'c': 2 < Nutri-Score <= 10
    - 'd': 10 < Nutri-Score <= 18
    - 'e': Nutri-Score > 18
    """
    
    
    # Points pour les nutriments à limiter (points A)
    points_limitants = 0

    if energy_100g <= 335:
        points_limitants += 0
    elif 335 < energy_100g <= 670:
        points_limitants += 1
    elif 670 < energy_100g <= 1005:
        points_limitants += 2
    elif 1005 < energy_100g <= 1340:
        points_limitants += 3
    elif 1340 < energy_100g <= 1675:
        points_limitants += 4
    elif 1675 < energy_100g <= 2010:
        points_limitants += 5
    elif 2010 < energy_100g <= 2345:
        points_limitants += 6
    elif 2345 < energy_100g <= 2680:
        points_limitants += 7
    elif 2680 < energy_100g <= 3015:
        points_limitants += 8
    elif 3015 < energy_100g <= 3350:
        points_limitants += 9
    elif energy_100g > 3350:
        points_limitants += 10

    if sugars_100g <= 4.5:
        points_limitants += 0
    elif 4.5 < sugars_100g <= 9:
        points_limitants += 1
    elif 9 < sugars_100g <= 13.5:
        points_limitants += 2
    elif 13.5 < sugars_100g <= 18:
        points_limitants += 3
    elif 18 < sugars_100g <= 22.5:
        points_limitants += 4
    elif 22.5 < sugars_100g <= 27:
        points_limitants += 5
    elif 27 < sugars_100g <= 31:
        points_limitants += 6
    elif 31 < sugars_100g <= 36:
        points_limitants += 7
    elif 36 < sugars_100g <= 40:
        points_limitants += 8
    elif 40 < sugars_100g <= 45:
        points_limitants += 9
    elif sugars_100g > 45:
        points_limitants += 10

    if saturated_fat_100g <= 1:
        points_limitants += 0
    elif 1 < saturated_fat_100g <= 2:
        points_limitants += 1
    elif 2 < saturated_fat_100g <= 3:
        points_limitants += 2
    elif 3 < saturated_fat_100g <= 4:
        points_limitants += 3
    elif 4 < saturated_fat_100g <= 5:
        points_limitants += 4
    elif 5 < saturated_fat_100g <= 6:
        points_limitants += 5
    elif 6 < saturated_fat_100g <= 7:
        points_limitants += 6
    elif 7 < saturated_fat_100g <= 8:
        points_limitants += 7
    elif 8 < saturated_fat_100g <= 9:
        points_limitants += 8
    elif 9 < saturated_fat_100g <= 10:
        points_limitants += 9
    elif saturated_fat_100g > 10:
        points_limitants += 10

    if sodium_100g <= 90:
        points_limitants += 0
    elif 90 < sodium_100g <= 180:
        points_limitants += 1
    elif 180 < sodium_100g <= 270:
        points_limitants += 2
    elif 270 < sodium_100g <= 360:
        points_limitants += 3
    elif 360 < sodium_100g <= 450:
        points_limitants += 4
    elif 450 < sodium_100g <= 540:
        points_limitants += 5
    elif 540 < sodium_100g <= 630:
        points_limitants += 6
    elif 630 < sodium_100g <= 720:
        points_limitants += 7
    elif 720 < sodium_100g <= 810:
        points_limitants += 8
    elif 810 < sodium_100g <= 900:
        points_limitants += 9
    elif sodium_100g > 900:
        points_limitants += 10

    
    # Points pour les nutriments à favoriser (points C)
    points_favorables = 0

    if fiber_100g <= 0.7:
        points_favorables += 0
    elif 0.7 <= fiber_100g <= 1.4:
        points_favorables += 1
    elif 1.4 <= fiber_100g <= 2.1:
        points_favorables += 2
    elif 2.1 <= fiber_100g <= 2.8:
        points_favorables += 3
    elif 2.8 <= fiber_100g <= 3.5:
        points_favorables += 4
    elif fiber_100g > 3.5:
        points_favorables += 5
    
    if proteins_100g <= 1.6:
        points_favorables += 0
    elif 1.6 <= proteins_100g <= 3.2:
        points_favorables += 1
    elif 3.2 <= proteins_100g <= 4.8:
        points_favorables += 2
    elif 4.8 <= proteins_100g <= 6.4:
        points_favorables += 3
    elif 6.4 <= proteins_100g <= 8.0:
        points_favorables += 4
    elif proteins_100g > 8.0:
        points_favorables += 5
    
    # Calcul du Nutri-Score final
    nutriscore = points_limitants - points_favorables
    
    # Calcul du Nutri-Grade final
    if nutriscore <= -1:
        nutrigrade = 'a'
    elif -1<nutriscore<=2:
        nutrigrade = 'b'
    elif 2<nutriscore<=10:
        nutrigrade = 'c'
    elif 10<nutriscore<=18:
        nutrigrade = 'd'
    elif 18<nutriscore:
        nutrigrade = 'e'
    else:
        print('There was an error during the nutriscore calculation.')
    
    return [nutriscore, nutrigrade]


def fill_missing_nutriscore(row: pd.Series) -> float:
    """
    Fill missing values in the 'nutrition_score_fr_100g' column using the given nutritional values.

    Parameters:
    - row (pd.Series): A row from a DataFrame containing nutritional information.

    Returns:
    - float: The calculated Nutri-Score.
    """
    if np.isnan(row['nutrition_score_fr_100g']):
        columns = ['energy_100g', 'saturated_fat_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'sodium_100g']
        values = row[columns].values
        energy_100g, saturated_fat_100g, sugars_100g, fiber_100g, proteins_100g, sodium_100g = values.flatten().tolist()
        return calculate_nutriscore_nutrigrade(energy_100g, saturated_fat_100g, sugars_100g, fiber_100g, proteins_100g, sodium_100g)[0]
    else:
        return row['nutrition_score_fr_100g']

def fill_missing_nutrigrade(row: pd.Series) -> str:
    """
    Fill missing values in the 'nutrition_grade_fr' column using the given nutritional values.

    Parameters:
    - row (pd.Series): A row from a DataFrame containing nutritional information.

    Returns:
    - str: The calculated Nutri-Grade.
    """
    if pd.isnull(row['nutrition_grade_fr']):
        columns = ['energy_100g', 'saturated_fat_100g', 'sugars_100g', 'fiber_100g', 'proteins_100g', 'sodium_100g']
        values = row[columns].values
        energy_100g, saturated_fat_100g, sugars_100g, fiber_100g, proteins_100g, sodium_100g = values.flatten().tolist()
        return calculate_nutriscore_nutrigrade(energy_100g, saturated_fat_100g, sugars_100g, fiber_100g, proteins_100g, sodium_100g)[1]
    else:
        return row['nutrition_grade_fr']
