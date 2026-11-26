import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Order ID': [101, 102, 103, 104, 105, 106],
    'Item': ['Burger', 'Pizza', 'Sandwich', 'Pizza', 'Burger', 'Pasta'],
    'Quantity': [2, 1, 3, 2, 1, 2],
    'Unit Price': [120, 250, 90, 250, 120, 180],
    'City': ['Patiala', 'Ludhiana', 'Patiala', 'Amritsar', 'Ludhiana', 'Patiala']
}

df = pd.DataFrame(data)

print(df)

print(df.head(3))
print(df.shape)
print(df.columns)

print(df.loc[2])
print(df.iloc[:2, :3])

df.loc[df['Order ID'] == 105, 'Quantity'] = 3
print(df)

df['Total Bill'] = df['Quantity'] * df['Unit Price']
print(df[['Order ID', 'Item', 'Total Bill']])

print(df[df['City'] == 'Patiala'])

print(df.sort_values(by='Total Bill', ascending=False))

grouped = df.groupby('Item')['Quantity'].sum()
print(grouped)

grouped.plot(kind='bar')

plt.title("Total Quantity Ordered for Each Food Item")
plt.xlabel("Food Item")
plt.ylabel("Total Quantity")
plt.show()