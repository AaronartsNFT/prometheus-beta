import lzma
import os
from typing import Union

def xz_compress(data: Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress input data using XZ (LZMA2) compression algorithm.

    Args:
        data (Union[str, bytes]): The input data to compress. 
                                  Can be either a string or bytes.
        compression_level (int, optional): Compression level from 0-9. 
                                           Defaults to 6 (recommended).

    Returns:
        bytes: Compressed data in XZ format.

    Raises:
        ValueError: If compression level is not between 0 and 9.
        TypeError: If input data is not str or bytes.
    """
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Convert string to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, bytes):
        raise TypeError("Input must be a string or bytes")

    # Compress using LZMA with specified compression level
    try:
        compressed_data = lzma.compress(data, preset=compression_level)
        return compressed_data
    except Exception as e:
        raise RuntimeError(f"Compression failed: {str(e)}")

def xz_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress XZ (LZMA2) compressed data.

    Args:
        compressed_data (bytes): XZ compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        lzma.LZMAError: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Decompress using LZMA
    try:
        decompressed_data = lzma.decompress(compressed_data)
        return decompressed_data
    except lzma.LZMAError as e:
        raise RuntimeError(f"Decompression failed: {str(e)}")