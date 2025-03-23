import hashlib

def calculate_hash(data, algorithm='md5'):
    """
    Calculate hash value of input data
    
    Args:
        data (str or bytes): Data to be hashed
        algorithm (str): Hash algorithm to use (default: md5)
        
    Returns:
        str: Hexadecimal hash value
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if algorithm.lower() == 'md5':
        hash_obj = hashlib.md5(data)
    elif algorithm.lower() == 'sha256':
        hash_obj = hashlib.sha256(data)
    elif algorithm.lower() == 'sha1':
        hash_obj = hashlib.sha1(data)
    else:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        
    return hash_obj.hexdigest()