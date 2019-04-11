import acquire_zillow
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#drop columns that don't seem valuable
# df = df.drop(columns=(['id', 'finishedsquarefeet12', 'fips', 'fullbathcnt', 'regionidcity', 'regionidcounty', 'regionidneighborhood', 'roomcnt', 'unitcnt', 'structuretaxvaluedollarcnt', 'taxdelinquencyyear', 'censustractandblock', 'airconditioningdesc', 'heatingorsystemdesc', 'propertylandusedesc']))

#make histograms
def make_hist(df):
    plt.figure(figsize=(16, 10))
    for i, col in enumerate(df):
        plot_number = i + 1 
        series = df[col]
        plt.subplot(4, 3, plot_number)
        plt.title(col)
        series.hist(bins=20, density=False, cumulative=False, log=False)

#make pairplot/heat
def make_pair_heat(df):
    sns.pairplot(df)
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), cmap='Blues', annot=True)

#make boxplots
def make_box(df):
    plt.figure(figsize=(16, 10))
    for i, col in enumerate(df):
        plot_number = i + 1
        series = df[col]
        plt.subplot(4, 3, plot_number)
        plt.title(col)
        sns.boxplot(data=series)

#make jointplot
def make_jointplot(df):
    for i, col in enumerate(df):
        plot_number = i + 1 
        series = df[col]
        j = sns.jointplot(col, "logerror", data=df, kind='reg', height=5);
        plt.show()

#make relplots
def make_relplot(df, 'x', 'y', 'hue'):
    for i, col in enumerate(df):
        plot_number = i + 1 
        series = df[col]
        sns.relplot(x='x', y='y', hue='hue', data=df)
        plt.show()