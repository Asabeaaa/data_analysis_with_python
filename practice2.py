#PYTHON FOR DATA ANALYTICS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.linear_model import LinearRegression

cvs_path='Documents//cars.csv'
df=pd.read_csv(cvs_path) #creates data frame
#print(df.head())
df.to_csv('Desktop//cars2.csv')
#print(df.dtypes)
#print(df.describe(include='all'))
#print(df.info())

#removing missing values
data=df.replace("?", "NaN")
#print(data)
data.to_csv('Desktop//cars2.csv')
data=data.drop([0,1,2,3,5,7,9,14,15,16,17,43,44,45,46,48,49,63,66,71,73,74,75,82,83,84,109,110,113,114,124,126,127,128,129,130,131,181,189,191,192,193], axis=0)
data.to_csv('Desktop//cars2.csv')
data=data.drop([55,56,57,58],axis=0)
data.to_csv('Desktop//cars2.csv')

data['city-mpg']=235/data['city-mpg']
data=data.rename(columns={'city-mpg': 'city-L/100km'})
data.to_csv('Desktop//cars2.csv')

#print(data.dtypes)
#data formatting
data['price']=data['price'].astype('int')
data['peak-rpm']=data['peak-rpm'].astype('int')
data['horsepower']=data['horsepower'].astype('int')
data['stroke']=data['stroke'].astype('float')
data['bore']=data['bore'].astype('float')
data['normalized-losses']=data['normalized-losses'].astype('int')

#normalization
data['length']=data['length']/data['length'].max()
data['width']=data['width']/data['width'].max()
data['height']=data['height']/data['height'].max()
data.to_csv('Desktop//cars2.csv')

#binning
bins=np.linspace(min(data['price']),max(data['price']),4)
group_names=['Low','Medium','High']
data['price-binned']=pd.cut(data['price'],bins,labels=group_names,include_lowest=True)
data.to_csv('Desktop//cars2.csv')

#plotting a histogram of prices
#x=data['price']
#plt.hist(x,bins=4)
#plt.xlabel("Price")
#plt.ylabel("Count")
#plt.title('Histogram of Price Vs Count')
#plt.show()

#getting dummies for fuel
dummy=pd.get_dummies(data['fuel-type'])
data=pd.concat([data,dummy],axis=1)
data.to_csv('Desktop//cars2.csv')

#descriptive statistics
#print(data.describe())

#creating value count
drive_wheels_counts=data['drive-wheels'].value_counts()
y=drive_wheels_counts.rename_axis('drive-wheels').to_frame('value_counts')
drive_wheels_counts.index.name='drive-wheels'
#print(y)

#boxplot
#sns.boxplot(x='drive-wheels',y='price',data=data)
#plt.show()

#scatter plot
#y=data['engine-size']
#x=data['price']
#plt.xlabel("Price")
#plt.ylabel("Engine Size")
#plt.title('Scatterplot of Engine size Vs Price')
#plt.scatter(x,y)
#plt.show()

#groupby
df_test=data[['drive-wheels','body-style','price']]
df_group=df_test.groupby(['drive-wheels','body-style'],as_index=False).mean()
#print(df_group)

#pivot table
df_pivot=df_group.pivot(index='drive-wheels',columns='body-style')
#print(df_pivot)

#heat maps
plt.pcolor(df_pivot,cmap='RdBu')
plt.colorbar()
#plt.show()




