from urllib.parse import urlparse

def validate_url(url):
    """
    Validate if a string is a properly formatted URL.
    
    Args:
        url (str): The URL to validate
        
    Returns:
        bool: True if the URL is valid, False otherwise
    """
    if not url:
        return False
    
    # Check if URL has a scheme, if not add https://
    if not url.startswith(('http://', 'https://', 'ftp://', 'ftps://')):
        url = 'https://' + url
        
    try:
        result = urlparse(url)
        # Check if scheme and netloc exist
        valid_scheme = result.scheme in ('http', 'https', 'ftp', 'ftps')
        return valid_scheme and bool(result.netloc)
    except Exception:
        return False

def get_valid_url(url):
    """
    Get a valid URL with proper protocol.
    If URL is invalid, returns None.
    
    Args:
        url (str): The URL to validate and format
        
    Returns:
        str or None: Properly formatted URL or None if invalid
    """
    if not url:
        return None
        
    # Add https:// if no protocol specified
    if not url.startswith(('http://', 'https://', 'ftp://', 'ftps://')):
        url = 'https://' + url
        
    if validate_url(url):
        return url
    else:
        return None