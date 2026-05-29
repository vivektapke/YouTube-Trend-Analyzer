import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/youtube.csv")
print(df.head())

print(df.info())
print(df.isnull().sum())

df.dropna(inplace=True)

df['category_id'].value_counts().head(10).plot(kind='bar')
plt.title("Top Categories")
plt.show()

df.sort_values(by='views', ascending=False).head(10)

sns.scatterplot(x='views', y='likes', data=df)
plt.title("Views vs Likes")
plt.show()

df['engagement'] = df['likes'] / df['views']

df.sort_values(by='engagement', ascending=False).head(10)

df.groupby('category_id')['views'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Avg Views per Category")
plt.show()

