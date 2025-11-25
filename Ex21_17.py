import requests

class SimpleAPIClient:
    def __init__(self):
        # Base URL of the JSONPlaceholder API
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_posts(self):
        """
        Fetch all posts using GET request
        """
        url = f"{self.base_url}/posts"
        response = requests.get(url)

        # Return posts only if request succeeded
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch posts")
            return None

    def create_post(self, title, body, user_id):
        """
        Create a new post using POST request
        """
        url = f"{self.base_url}/posts"
        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(url, json=data)

        # Return new post only if request succeeded
        if response.status_code == 201:
            return response.json()
        else:
            print("Failed to create post")
            return None


# ---------------------------
# Example usage
# ---------------------------

api = SimpleAPIClient()

# Fetch and print posts
posts = api.get_posts()
print("Fetched Posts:")
print(posts)

# Create a new post
new_post = api.create_post("My New Post", "This is the body of my post.", 1)
print("\nCreated Post:")
print(new_post)
