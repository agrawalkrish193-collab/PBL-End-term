import pandas as pd

df = pd.read_csv('cleaned_fashion_data.csv')

print("Welcome to Wardrobe Recommender")

gender_input = input("Enter gender (men/women): ").lower()
color_input = input("Enter color: ").lower()
weather_input = input("Enter weather (hot/cold/mild): ").lower()
occasion_input = input("Enter occasion (casual/formal/party/etc): ").lower()

filtered = df[
    (df['gender'] == gender_input) &
    (df['baseColour'] == color_input) &
    (df['weather'] == weather_input) &
    (df['occasion'] == occasion_input)
]

if len(filtered) > 0:
    print("\nRecommended Outfits:\n")
    print(filtered[['productDisplayName', 'articleType']].head(10))
else:
    print("\nNo exact match found, showing similar results...\n")

    fallback = df[
        (df['gender'] == gender_input) &
        (df['occasion'] == occasion_input)
    ]

    print(fallback[['productDisplayName', 'articleType']].head(10))
