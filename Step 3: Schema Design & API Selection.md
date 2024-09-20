# Schema Design

## User: Stores user credentials and profile information.

id (Primary Key)
username (Unique)
email (Unique)
password_hash


## RecipientProfile: Represents a profile created by a user for a gift recipient.

id (Primary Key)
user_id (Foreign Key referencing User)
name
birthday
gender
relationship (e.g., friend, family)
interests (Text field to store a list or JSON)
occasion
budget
additional_details (Text field)
created_at (Timestamp)


## GiftIdea: Stores suggestions linked to recipient profiles.

id (Primary Key)
recipient_profile_id (Foreign Key referencing RecipientProfile)
suggestion_text
created_at (Timestamp)
extrenal_link (URL to product/search result) 

# API Selection

OpenAI API: Using this for generating gift ideas based on recipient profile descriptions.

Amazon Product Advertising API or Google Shopping API: Using one of these for linking gift suggestions to actual products. These APIs will provide real-time prices, product details, and possibly affiliate links.