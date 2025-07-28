# network_optimizer.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. Load your latency data
df = pd.read_csv('network_latency.csv')

print("Loaded data:")
print(df)

# 2. Label the best route (the row with smallest AvgRTT)
df['BestRoute'] = 0
df.loc[df['AvgRTT'].idxmin(), 'BestRoute'] = 1

print("\nData with BestRoute label:")
print(df)

# 3. Prepare features and target
X = df[['MinRTT', 'AvgRTT', 'MaxRTT']]
y = df['BestRoute']

# 4. Fit Logistic Regression model
clf = LogisticRegression()
clf.fit(X, y)
y_pred = clf.predict(X)

print("\nPredicted Best Route labels:", y_pred)
print("Actual Best Route labels:   ", y.values)

# 5. Visualize the average RTTs for each path
plt.figure(figsize=(7,4))
plt.bar(df['Source'] + '→' + df['Destination'], df['AvgRTT'], color=['green' if b else 'gray' for b in df['BestRoute']])
plt.xlabel('Path')
plt.ylabel('Average RTT (ms)')
plt.title('Average Network Latency by Path')
plt.tight_layout()
plt.show()


