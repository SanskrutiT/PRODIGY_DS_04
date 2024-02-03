import subprocess
import sys

# Check if textblob is installed
try:
    import textblob
except ImportError:
    print("textblob is not installed. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "textblob"])
    import textblob

# Now that textblob is installed or imported, you can use it in your code
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Step 2: Load the dataset
# Provide the full path to the CSV file
# Specify encoding as 'ISO-8859-1' (latin1) or 'Windows-1252'
twitter_data = pd.read_csv("C:/Users/Sanskruti_Thakur/Desktop/SANS_INTERNSHIPS/twitter_training.csv (3).zip")

# Step 3: Explore the dataset
print(twitter_data.head())  # Print the first few rows
print(twitter_data.info())  # Get information about the dataset

# Step 4: Preprocess the data (if needed)
# For example, remove special characters, stopwords, URLs, etc.

# Step 5: Sentiment analysis
# Use TextBlob to analyze sentiment of each tweet
twitter_data['polarity'] = twitter_data['Tweet'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

# Step 6: Visualize sentiment patterns
# Plot histogram of sentiment polarity using RGB or hex values

# Normalize RGB values to the range of 0 to 1
color_rgb = (0, 0, 128)  # Dark blue color
color_normalized = (color_rgb[0] / 255, color_rgb[1] / 255, color_rgb[2] / 255)
import matplotlib.pyplot as plt

# Normalize RGB values to the range of 0 to 1
color_rgb = (0, 0, 128)  # Dark blue color
color_normalized = (color_rgb[0] / 255, color_rgb[1] / 255, color_rgb[2] / 255)
# Plot histogram of sentiment polarity using normalized RGB values
plt.hist(twitter_data['polarity'], bins=50, color=color_normalized, edgecolor='white')
plt.xlabel('Response')
plt.ylabel('Population')
plt.title('Sentiment Polarity Distribution')
plt.show()

# Step 7: Interpret the results
# Analyze the sentiment polarity distribution to understand public opinion and attitudes

# Step 8: Summarize findings
# Write a summary of key findings from the sentiment analysis and visualization
