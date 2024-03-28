import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean 

df = df[(df>df.quantile(0.025))&(df<df.quantile(0.975))].dropna()



def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 6))
    plt.plot(df,color="r")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar["month"] = [d.strftime('%b') for d in df_bar.date]
    df_bar["year"] = [d.year for d in df_bar.date]
    df_bar = df_bar.groupby(["year","month"])["value"].mean()
    df_bar = df_bar.reset_index()
    

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.barplot(x="year", y="value", hue="month", data=df_bar,
                hue_order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    ax.legend(title="Months")
    ax.legend(["January","February","March","April","May","June","July","August","September","October","November","December"])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig,ax = plt.subplots(1,2,figsize=(15,6))
    sns.boxplot(x="year", y="value", data=df_box, ax=ax[0],palette="YlOrBr")
    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1],
                order= ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],palette="viridis")
    ax[0].set_title("Year-wise Box Plot (Trend)",)
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    plt.tight_layout()





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

