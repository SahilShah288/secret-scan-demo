import os

API_KEY = os.getenv("ACME_API_KEY", "not-set")
print("App started. Key loaded from environment:", API_KEY != "not-set")