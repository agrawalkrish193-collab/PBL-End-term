import pandas as pd

df = pd.read_csv('data2.csv', sep='\t', usecols=[
    'id','gender','articleType','baseColour',
    'season','usage','productDisplayName'
], on_bad_lines='skip')

print("Original Shape:", df.shape)

# Missing values
df = df.dropna(subset=['usage', 'season'])
df['baseColour'] = df['baseColour'].fillna('unknown')

# Remove duplicates
df = df.drop_duplicates(subset=['id'])

# Text cleaning
for col in ['usage', 'season', 'baseColour', 'articleType', 'gender']:
    df[col] = df[col].str.lower().str.strip()

# Weather mapping
weather_map = {
    'summer': 'hot',
    'winter': 'cold',
    'spring': 'mild',
    'fall': 'mild',
    'autumn': 'mild',
    'all season': 'all'
}
df['weather'] = df['season'].map(weather_map)

# Occasion mapping
occasion_map = {
    'casual': 'casual',
    'formal': 'formal',
    'sports': 'sports',
    'ethnic': 'ethnic',
    'party': 'party',
    'travel': 'casual'
}
df['occasion'] = df['usage'].map(occasion_map)

df = df.dropna(subset=['occasion'])


print("Final Shape:", df.shape)
print(df.isnull().sum())


df.to_csv('cleaned_fashion_data.csv', index=False)

print("Cleaned data saved successfully!")
