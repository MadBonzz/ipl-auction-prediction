import pandas as pd
from rapidfuzz import process
from rapidfuzz.fuzz import token_sort_ratio

stats_df = pd.read_csv('statistics.csv')
auction_df = pd.read_csv('IPLPlayerAuctionData.csv')

stats_names = list(set(stats_df['player_name'].dropna().unique()))
auction_names = list(set(auction_df['Player'].dropna().unique()))

print(len(auction_names))
print(len(stats_names))

name_mapping = {}

found = []

for name in auction_names:
    if name in stats_names:
        name_mapping[name] = name
        found.append(name)

stats_names = [name for name in stats_names if name not in found]
auction_names = [name for name in auction_names if name not in found]
print(len(found))


for name in auction_names:
    pass
    match, score, _ = process.extractOne(
        name, 
        stats_names, 
        scorer=token_sort_ratio  # Corrected scorer reference
    )
    if score > 70:
        name_mapping[name] = match

mapping_df = pd.DataFrame({
    'Statistics_Name': name_mapping.values(),
    'Auction_Name': name_mapping.keys()
})

print(mapping_df)
mapping_df.to_csv('name_mapping.csv', index=False)
