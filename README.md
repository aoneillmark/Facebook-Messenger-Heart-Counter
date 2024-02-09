# Facebook Messenger Heart Counter

This repository provides a fun and interactive way to analyze the distribution of "heart" reactions in a Facebook Messenger group chat. It calculates the total number of hearts per user and the average hearts per message for each user (e.g., Mark gets 0.48 hearts per message). 

To make the results more digestible, it also generates bar charts, perfect for those who prefer visual data over raw numbers. This project is a light-hearted way to rank friends in a group chat based on their "heart" popularity.

## Example of Results

Here are some examples of the results you can expect:

1. Total Heart Reactions:
![Total Heart Reactions](https://github.com/aoneillmark/Facebook-Messenger-Heart-Counter/blob/main/Results/heart_reactions.png?raw=true)

2. Average Heart Reactions:
![Average Heart Reactions](https://github.com/aoneillmark/Facebook-Messenger-Heart-Counter/blob/main/Results/average_heart_reactions.png?raw=true)

3. Messages vs Heart Reactions:
![Messages vs Heart Reactions](https://github.com/aoneillmark/Facebook-Messenger-Heart-Counter/blob/main/Results/messages_vs_heart_reactions.png?raw=true)

The last chart is particularly interesting as it shows that all members in the group chat receive "heart" reactions at a similar rate. The difference in total hearts is mainly due to the frequency of messages sent by each user.

## How to Use

Follow these steps to use this tool:

1. Download your Messenger history from Facebook as JSON files. You can find instructions on how to do this [here](https://www.facebook.com/help/messenger-app/677912386869109).
2. Import the downloaded JSON files into the `Data` folder.
3. Run `analysis.py`.

The results will be saved in the `Results` folder.