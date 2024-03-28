import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', header=0)


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Measured Sea Level')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')


    # Create first line of best fit
    lin_regression_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880,2051), lin_regression_all.slope*range(1880,2051) + lin_regression_all.intercept,
            label="Trend since 1880",color='tab:orange')

    # Create second line of best fit
    lin_regression_recent = linregress(df[df['Year']>=2000]['Year'], df[df['Year']>=2000]['CSIRO Adjusted Sea Level'])
    
    plt.plot(range(2000,2051), lin_regression_recent.slope*range(2000,2051) + lin_regression_recent.intercept, 
             label='Trend Since 2000',color= 'r')

    plt.legend()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()