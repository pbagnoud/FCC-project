import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv",header=0)

# Add 'overweight' column
df['overweight'] = ((df["weight"]/(df["height"]/100)**2) > 25)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = (df["cholesterol"] > 1)
df["gluc"] = (df["gluc"] > 1)
for cat in ["cholesterol", "gluc","smoke","alco","active","overweight"]:
    df[cat]=df[cat].apply(lambda x: int(x))


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,value_vars=["cholesterol", "gluc","smoke","alco","active","overweight"],id_vars=["cardio"])
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat =df_cat.groupby(by="cardio").value_counts()
    df_cat.name = "total"
    df_cat=df_cat.to_frame()
    #df_cat["value_count"]=df_cat.value_counts()

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, x="variable", y="total", hue="value",
     col="cardio", kind="bar", order= ["active","alco","cholesterol", "gluc","overweight","smoke"])


    # Get the figure for the output
    fig = sns.catplot(data=df_cat, x="variable", y="total", hue="value",
     col="cardio", kind="bar", order= ["active","alco","cholesterol", "gluc","overweight","smoke"]).fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    clean_ap = (df['ap_lo'] <= df['ap_hi'])
    clean_height= (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    clean_weight= (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[clean_height & clean_weight & clean_ap]
    df_heat.rename({"sex":"gender"})
    # Calculate the correlation matrix
    corr = df_heat.corr(method="pearson")
    label_corr = corr.apply(lambda x: round(x,1))


    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype = bool)
    mask[np.triu_indices_from(mask)] = True



    # Set up the matplotlib figure
    fig, ax = plt.subplots(1,1,figsize=(10,8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr,annot=True,mask=mask,fmt=".1f", ax=ax,vmin=-0.5,vmax=0.5, cmap="icefire",linecolor="white",linewidths=2)
    fig.tight_layout()




    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

