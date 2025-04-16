import joblib
import pandas as pd

df = pd.read_csv('final_data.csv')
df.drop(columns=['Amount', 'Unnamed: 0'], inplace=True)
players = df['Player'].unique().tolist()

player = 'Aaron Finch'
year = 2015

loaded_pipeline = joblib.load('model_pipeline.pkl')
encoder = loaded_pipeline['encoder']
model = loaded_pipeline['model']

cols = ['battingstyle', 'bowlingstyle', 'position', 'Player Origin']
test_sample = df[(df['Player'] == player) & (df['Year'] == year)].copy()
test_sample.drop(columns=['Player', 'player_name'], inplace=True)
test_sample[cols] = encoder.transform(test_sample[cols])

prediction = round(model.predict(test_sample)[0], 2)

print(f"The predicted auction price for {player} in {year} is {prediction}")