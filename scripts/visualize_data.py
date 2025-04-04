import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
data = pd.read_csv('../data/chat_data.csv')

# Plot sentiment distribution
sns.countplot(x='sentiment', data=data)
plt.title('Sentiment Distribution')
plt.savefig('../visualizations/sentiment_distribution.png')
plt.show()