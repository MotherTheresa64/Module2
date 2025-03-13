# ====================
# Engage & Apply: Extract Hashtags from Tweets
# ====================

import re

# List of tweets
tweets = [
    "Loving the #sunset! So peaceful #nature #blessed",
    "Had a great day! #happy #friends #goodvibes",
    "Can't wait for the #weekend! #fun #relax"
]

# Extracting hashtags using re.findall()
hashtags = []
for tweet in tweets:
    hashtags += re.findall(r"#\w+", tweet)

# Printing out the hashtags
print("Hashtags found in tweets:", hashtags)


# ====================
# My Version of the Engage & Apply Challenge
# ====================

# List of tweets
tweets = [
    "Enjoying the #sunshine today! #beautifulweather",
    "Feeling #excited about the #future",
    "Had a blast at the #party last night! #goodtimes"
]

# Extracting hashtags using re.findall()
hashtags = []
for tweet in tweets:
    hashtags += re.findall(r"#\w+", tweet)

# Printing out the hashtags
print("Hashtags found in tweets:", hashtags)


# ====================
# Final Challenge: Email Validation Program
# ====================

import re

# List of email addresses
emails = [
    "correct.email@example.com",
    "incorrect-email-at-example.com",
    "another.correct.email@example.org"
]

# Validating each email using re.search()
for email in emails:
    # Regex pattern for a valid email
    pattern = r"[\w.-]+@[\w-]+\.[a-z]{2,3}"
    if re.search(pattern, email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")


# ====================
# My Version of the Final Challenge
# ====================

# List of email addresses
emails = [
    "john.doe@example.com",
    "jane_doe123@codingplatform.net",
    "invalid-email.com"
]

# Validating each email using re.search()
for email in emails:
    # Regex pattern for a valid email
    pattern = r"[\w.-]+@[\w-]+\.[a-z]{2,3}"
    if re.search(pattern, email):
        print(f"{email} is valid")
    else:
        print(f"{email} is invalid")
