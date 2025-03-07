class LZ77Compressor:
    """
    Implementation of the LZ77 compression algorithm.
    
    LZ77 works by replacing repeated occurrences of data with references 
    to a single copy of that data existing earlier in the input stream.
    """
    
    def __init__(self, window_size=1024, look_ahead_buffer_size=16):
        """
        Initialize the LZ77 compressor.
        
        :param window_size: Size of the sliding window for searching previous matches
        :param look_ahead_buffer_size: Size of the look-ahead buffer for finding matches
        """
        self.window_size = window_size
        self.look_ahead_buffer_size = look_ahead_buffer_size
    
    def compress(self, data):
        """
        Compress the input data using LZ77 algorithm.
        
        :param data: Input string or bytes to compress
        :return: List of tuples representing compressed tokens
        """
        # Convert input to bytes if it's a string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Validate input
        if not data:
            return []
        
        compressed = []
        current_pos = 0
        
        while current_pos < len(data):
            # Determine search window boundaries
            search_start = max(0, current_pos - self.window_size)
            search_end = current_pos
            
            # Determine look-ahead buffer boundaries
            look_ahead_start = current_pos
            look_ahead_end = min(current_pos + self.look_ahead_buffer_size, len(data))
            
            # Search for the longest match in the search window
            best_length = 0
            best_offset = 0
            
            for offset in range(search_end - search_start):
                match_length = 0
                
                while (match_length < look_ahead_end - look_ahead_start and
                       search_start + offset + match_length < search_end and
                       data[search_start + offset + match_length] == 
                       data[look_ahead_start + match_length]):
                    match_length += 1
                
                # Update best match if current match is longer
                if match_length > best_length:
                    best_length = match_length
                    best_offset = search_end - (search_start + offset)
            
            # Add compressed token
            if best_length > 0:
                # (offset, length, next_symbol)
                compressed.append((best_offset, best_length, 
                                   data[look_ahead_start + best_length] 
                                   if look_ahead_start + best_length < len(data) 
                                   else None))
                current_pos += best_length + 1
            else:
                # No match found, output literal symbol
                compressed.append((0, 0, data[current_pos]))
                current_pos += 1
        
        return compressed
    
    def decompress(self, compressed_data):
        """
        Decompress data compressed with LZ77 algorithm.
        
        :param compressed_data: List of tuples from compression
        :return: Decompressed bytes
        """
        # Validate input
        if not compressed_data:
            return b''
        
        decompressed = bytearray()
        
        for token in compressed_data:
            offset, length, symbol = token
            
            # Handle literal symbol
            if length == 0:
                decompressed.append(symbol)
            else:
                # Reconstruct repeated sequence
                start = len(decompressed) - offset
                for i in range(length):
                    decompressed.append(decompressed[start + i])
                
                # Add next symbol if exists
                if symbol is not None:
                    decompressed.append(symbol)
        
        return bytes(decompressed)