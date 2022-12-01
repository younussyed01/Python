import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("Coding_projects_cs/games-analysis/game-ratings-by-release-dates.csv")

# Clean up fields.
df["first_release_date"] = pd.to_datetime(df["first_release_date"]) 

# Analyze data.
plt.scatter(df["first_release_date"], df["critic_rating_value"], color = "blue", label = "Critic Ratings")
plt.scatter(df["first_release_date"], df["user_rating_value"], color = "red", label = "User Ratings")

plt.legend(loc = "upper left")

plt.show()