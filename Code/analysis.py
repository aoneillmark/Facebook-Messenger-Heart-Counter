import os
import json
import matplotlib.pyplot as plt

def analyze_json_file(file_path, aggregated_user_hearts, user_messages_count, x_num_heart_messages, x=5):
    heart_emoji = "\u00e2\u009d\u00a4"  # Define the unicode for the heart emoji reaction

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for message in data["messages"]:
        sender = message["sender_name"]
        # Update total messages sent by each user
        user_messages_count[sender] = user_messages_count.get(sender, 0) + 1
        
        # Count heart reactions for this message
        heart_count = sum(1 for reaction in message.get("reactions", []) if reaction["reaction"] == heart_emoji)
        if heart_count == x:
            # Save messages with exactly 5 heart reactions
            content = message.get("content", "Message with media or other content")
            x_num_heart_messages.append((sender, content))
        
        # Update heart counts for users based on reactions
        for reaction in message.get("reactions", []):
            if reaction["reaction"] == heart_emoji:
                actor = reaction["actor"]
                aggregated_user_hearts[actor] = aggregated_user_hearts.get(actor, 0) + 1


###########################################################
################# Performing Analysis #####################
###########################################################

# Initialize the data structures
aggregated_user_hearts = {}
user_messages_count = {}
x_num_heart_messages = []  # List to store messages with exactly X number of heart reactions

# Assuming you've already defined data_directory_path and json_files as before
data_directory_path = "./Data"
json_files = [f for f in os.listdir(data_directory_path) if f.endswith('.json')]

# Perform the analysis
for json_file in json_files:
    file_path = os.path.join(data_directory_path, json_file)
    analyze_json_file(file_path, aggregated_user_hearts, user_messages_count, x_num_heart_messages)


# Calculate the average number of heart reactions per message for each user
user_heart_averages = {user: aggregated_user_hearts[user] / user_messages_count[user] for user in aggregated_user_hearts}

# Sort users by their average heart reactions per message
users_ranked_by_average_hearts = sorted(user_heart_averages.items(), key=lambda x: x[1], reverse=True)

# Sort the aggregated user hearts count and print the results
users_ranked_aggregated = sorted(aggregated_user_hearts.items(), key=lambda x: x[1], reverse=True)

###########################################################
################# Printing the results ####################
###########################################################

print("\nAggregated Users Ranked by Heart Reactions:")
for user, total_hearts in users_ranked_aggregated:
    print(f"{user}: {total_hearts} total heart reactions")
# Save to results folder
with open('./Results/heart_reactions.txt', 'w') as f:
    for user, total_hearts in users_ranked_aggregated:
        f.write(f"{user}: {total_hearts} total heart reactions\n")

print("\n")

print("Users Ranked by Average Heart Reactions per Message:")
for user, avg_hearts in users_ranked_by_average_hearts:
    print(f"{user}: {avg_hearts:.2f} average heart reactions per message")

# Save to results folder
with open('./Results/average_heart_reactions.txt', 'w') as f:
    for user, avg_hearts in users_ranked_by_average_hearts:
        f.write(f"{user}: {avg_hearts:.2f} average heart reactions per message\n")

print("\n")

# # Print the messages with 6 hearts and the total count
# print(f"Total messages with exactly 5 heart reactions: {len(six_heart_messages)}")
# for sender, content in six_heart_messages:
#     print(f"Sender: {sender}, Message: {content}")

# # Save to results folder
# with open('./Results/six_heart_messages.txt', 'w') as f:
#     f.write(f"Total messages with exactly 5 heart reactions: {len(six_heart_messages)}\n")
#     for sender, content in six_heart_messages:
#         f.write(f"Sender: {sender}, Message: {content}\n")

###########################################################
################# Plotting the results ####################
###########################################################
######### Plotting Heart Reactions vs Sender ##############

# Sorting users by their name or total heart reactions if you want to sort by the number of reactions
users = list(aggregated_user_hearts.keys())
# Sort users by heart counts
users = [user for user, hearts in users_ranked_aggregated]
heart_reactions = [aggregated_user_hearts[user] for user in users]

# Creating the bar chart
plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
plt.bar(users, heart_reactions, color='skyblue')
plt.xlabel('Sender', fontsize=14)
plt.ylabel('Number of Heart Reactions', fontsize=14)
plt.title('Number of Heart Reactions vs Sender', fontsize=16)
plt.xticks(rotation=45)  # Rotate names to avoid overlap
plt.tight_layout()  # Adjust subplot parameters to give specified padding

# Save to results folder
plt.savefig('./Results/heart_reactions.png')

# Show the plot
plt.show()

###########################################################
######### Plotting Average Heart Reactions vs Sender ######

### Plotting Average Heart Reactions per Message for Each User
users = list(user_heart_averages.keys())
# Sort users by heart averages 
users = [user for user, avg in users_ranked_by_average_hearts]
average_heart_reactions = [user_heart_averages[user] for user in users]

# Creating the bar chart
plt.figure(figsize=(10, 8))  # Adjust the figure size as needed
plt.bar(users, average_heart_reactions, color='skyblue')
plt.xlabel('Sender', fontsize=14)
plt.ylabel('Average Heart Reactions per Message', fontsize=14)
plt.title('Average Heart Reactions per Message vs Sender', fontsize=16)
plt.xticks(rotation=45)  # Rotate names to avoid overlap
plt.tight_layout()  # Adjust subplot parameters to give specified padding

# Save to results folder
plt.savefig('./Results/average_heart_reactions.png')

# Show the plot
plt.show()
