import pandas as pd
import numpy as np

# Simulated engagement data
np.random.seed(42)
data = {
    'user_id': np.arange(1, 501),
    'posts_per_month': np.random.poisson(1.5, 500),
    'likes_received': np.random.randint(0, 50, 500),
    'comments_written': np.random.randint(0, 20, 500),
    'is_active_user': np.random.choice([0, 1], 500, p=[0.4, 0.6])
}

df = pd.DataFrame(data)
df['engagement_score'] = (
    df['posts_per_month'] * 0.5 +
    df['likes_received'] * 0.3 +
    df['comments_written'] * 0.2
)
df.to_csv('data/engagement_metrics_sample.csv', index=False)
print(df.head())
