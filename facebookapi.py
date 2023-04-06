import facebook

# Replace ACCESS_TOKEN with your generated access token
ACCESS_TOKEN = 'EAACotIUed5ABAGdy3yydZBZBpyrVulxX3BdfiNeQBLF5WundxHWYjuvG5sZBkJqxcL4ZC37obJE8IUCZAZAJMN5Rh9VpwRQ0E3vsgAPIDtPuy3BR9w6qvCO8DlbvCqCwXXdqrik17Uk8JT7voqhTiDNPZC4ddKmi3madsgVeC0PShb4cIUc1mwe4ZC8HcHU6f7oLxQSX16B0RswMP0MgHMZBQjZBmXEOSkHm0LyZCbzWHe7dQZAfndE8Oldd'

# Initialize the Facebook Graph API object with the access token
graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version='3.0')

try:
    # Make a request to the Graph API to get your friend list
    friends = graph.get_object('/me/friends')
    print(friends)
    if friends:
        # Print the name of each friend
        for friend in friends['data']:
            print(friend['name'])
    else:
        print("No friends found.")
except facebook.GraphAPIError as e:
    print(f"Error: {e}")
