# test_nftmarketplacebuilder.py
"""
Tests for NftMarketplaceBuilder module.
"""

import unittest
from nftmarketplacebuilder import NftMarketplaceBuilder

class TestNftMarketplaceBuilder(unittest.TestCase):
    """Test cases for NftMarketplaceBuilder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMarketplaceBuilder()
        self.assertIsInstance(instance, NftMarketplaceBuilder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMarketplaceBuilder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
