"""
helper functions
"""

def build_url(endpoint):
    # in deployment
    # return 'https://thepointistochangeit.com/' + endpoint
    # in development
    return 'http://127.0.0.1:8080/' + endpoint
