import numpy as np
import pandas as pd

df_2012 = pd.read_csv('News_2012.csv')
df_2013 = pd.read_csv('News_2013.csv')
df_2014 = pd.read_csv('News_2014.csv')
df_2015 = pd.read_csv('News_2015.csv')
df_2016 = pd.read_csv('News_2016.csv')
df_2017 = pd.read_csv('News_2017.csv')
df_2018 = pd.read_csv('News_2018.csv')
df_2019 = pd.read_csv('News_2019.csv')
df_2020 = pd.read_csv('News_2020.csv')
df_2021 = pd.read_csv('News_2021.csv')
df_2022 = pd.read_csv('News_2022.csv')

cat_2012 = df_2012['category'].unique()
cat_2013 = df_2013['category'].unique()
cat_2014 = df_2014['category'].unique()
cat_2015 = df_2015['category'].unique()
cat_2016 = df_2016['category'].unique()
cat_2017 = df_2017['category'].unique()
cat_2018 = df_2018['category'].unique()
cat_2019 = df_2019['category'].unique()
cat_2020 = df_2020['category'].unique()
cat_2021 = df_2021['category'].unique()
cat_2022 = df_2022['category'].unique()

common_elements = set(cat_2012).intersection(cat_2013,cat_2014,cat_2015,cat_2016,cat_2017,cat_2018,cat_2019,cat_2020,cat_2021,cat_2022)
print(common_elements)

