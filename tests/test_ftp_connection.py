import pytest
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

class TestFTPConnection:
    def test_successful_connection(self):
        """Test successful FTP connection"""
        with patch('ftplib.FTP') as mock_ftp:
            # Setup mock FTP object
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            # Call the function
            connection, error = establish_ftp_connection(
                host='test.host.com', 
                username='testuser', 
                password='testpass'
            )
            
            # Assertions
            assert connection is not None
            assert error is None
            mock_instance.connect.assert_called_once_with(host='test.host.com', port=21)
            mock_instance.login.assert_called_once_with(user='testuser', passwd='testpass')

    def test_missing_parameters(self):
        """Test connection with missing parameters"""
        # Test with empty host
        connection, error = establish_ftp_connection(
            host='', 
            username='testuser', 
            password='testpass'
        )
        assert connection is None
        assert "Missing required connection parameters" in error

        # Test with empty username
        connection, error = establish_ftp_connection(
            host='test.host.com', 
            username='', 
            password='testpass'
        )
        assert connection is None
        assert "Missing required connection parameters" in error

        # Test with empty password
        connection, error = establish_ftp_connection(
            host='test.host.com', 
            username='testuser', 
            password=''
        )
        assert connection is None
        assert "Missing required connection parameters" in error

    def test_connection_failure(self):
        """Test FTP connection failure scenarios"""
        with patch('ftplib.FTP') as mock_ftp:
            # Simulate connection error
            mock_ftp.side_effect = ftplib.error_perm("550 Connection refused")
            
            connection, error = establish_ftp_connection(
                host='invalid.host.com', 
                username='testuser', 
                password='testpass'
            )
            
            assert connection is None
            assert "FTP Connection Error" in error

    def test_custom_port(self):
        """Test connection with custom port"""
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            connection, error = establish_ftp_connection(
                host='test.host.com', 
                username='testuser', 
                password='testpass', 
                port=2121
            )
            
            assert connection is not None
            assert error is None
            mock_instance.connect.assert_called_once_with(host='test.host.com', port=2121)

    def test_custom_timeout(self):
        """Test connection with custom timeout"""
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            connection, error = establish_ftp_connection(
                host='test.host.com', 
                username='testuser', 
                password='testpass', 
                timeout=10
            )
            
            assert connection is not None
            assert error is None
            # Verify timeout is set during FTP object creation
            mock_ftp.assert_called_once_with(timeout=10)