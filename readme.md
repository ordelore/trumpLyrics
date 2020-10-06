# About
This project is based on this [YouTube video](https://www.youtube.com/watch?v=1nsmzzAWLW0), which takes Trump's Covid announcement tweet and takes the letters to make some lyrics to Porter Robinson's [Mirror](https://www.youtube.com/watch?v=l0Jo-9aqhYc) directly from the tweet.
This code uses Python to automate this process. Given an arbitrary string, this script will find a Trump tweet that best fits this string. It can be song lyrics or anything else.
# Requirements
I have tested this with Python 3.8.5, but this should work with any Python3 distribution with access to the `json` module.
Getting the Trump tweets is a little more involved. I have included the tweets I have used in my repository (the tweets are accurate as of October 5th, 2020), but making your own Trump tweet database requires one to follow these steps. I used trumptwitterarchive.com, specifically [this filtered version](http://www.trumptwitterarchive.com/archive/none/ffff/none/Any%20time/Twitter%20for%20iPhone) to only include iPhone tweets, which I believe to most accurately capture his raw emotions, but your mileage may vary. it also filters out any non-original tweet. Therefore there are no retweets or replies. You can mess around witht he different settings to generate your own curated list of Trump tweets.
On the website, click the 'EXPORT' button and select the JSON option. Wait about a minute for the data to be processed before selecting the text in the above box and copy-pasting the text into a file named `tweets.json` in the same directory as `main.py`. You can use any website, or even other people as long as the tweets are formatted with a "text" field containing the text of an individual tweet, and an "id_str" field with that tweet's id.
# Usage
Run `python main.py <string>`
The output of this script is as follows:
The first line is the original input string
The second line is the text of the Trump tweet that comes closest to recreating the input string
The third, fourth, and fifth lines operate together to provide a judgement of how good this tweet is for recreating the string. If the fourth and fifth lines produce equal numbers, then the tweet is a perfect recreation.
The sixth line represents how many times you need to cycle through the tweet to recreate the original tweet. If you're trying to make a music video akin to the one I linked above, this is the number of individual frames required.
The seventh line is a direct link to the specified tweet.
![enter image description here](https://i.imgur.com/qo6Y5uK.png)

# Next steps
Tweak the algorithm to not allow words to run-on into a new repetition of the tweet.
Instead of hard-coding the name of the file, get the user to specify which file is the input JSON.
It would be really nice to automate the creation of frames like in the music video, but that goes a bit beyond the scope of what I'm trying to accomplish.
