import requests
import hashlib
import sys
import os

# Fix import paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.url_validator import validate_url, get_valid_url
from utils.hash_calculator import calculate_hash

def check_endpoint(url):
    """
    Check if a URL endpoint is valid and calculate hash of the response.
    
    Args:
        url (str): The URL to check
        
    Returns:
        tuple: (success_bool, status_code, hash_value)
    """
    # Get a properly formatted URL
    valid_url = get_valid_url(url)
    if not valid_url:
        return False, None, "Invalid URL format"
    
    # Try to connect to the URL
    try:
        response = requests.get(valid_url, timeout=10)
        status_code = response.status_code
        
        # Calculate hash of response content using our hash calculator
        hash_value = calculate_hash(response.content, algorithm='sha256')
        
        return True, status_code, hash_value
    
    except requests.exceptions.RequestException as e:
        return False, None, f"Connection error: {str(e)}"
    except Exception as e:
        return False, None, f"Error: {str(e)}"