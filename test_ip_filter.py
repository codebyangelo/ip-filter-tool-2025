import os
import shutil
import subprocess
import unittest
import tempfile

class TestIPFilter(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.original_dir = os.getcwd()
        # Copy script to test dir
        shutil.copy(os.path.join(self.original_dir, "ip_filter_tool.py"), os.path.join(self.test_dir, "ip_filter_tool.py"))
        
        os.chdir(self.test_dir)
        
        # Create a dummy allow_list.txt
        with open("allow_list.txt", "w") as f:
            f.write("192.168.97.225\n192.168.1.1\n192.168.158.170\n192.168.2.2\n")
            
    def tearDown(self):
        os.chdir(self.original_dir)
        shutil.rmtree(self.test_dir)

    def test_filter(self):
        # Run the script
        subprocess.run(["python3", "ip_filter_tool.py"], check=True)
        
        # Read the resulting file
        with open("allow_list.txt", "r") as f:
            content = f.read()
            
        ips = content.split()
        
        # IPs that are in the remove_list should be removed
        self.assertNotIn("192.168.97.225", ips)
        self.assertNotIn("192.168.158.170", ips)
        
        # IPs not in the remove_list should remain
        self.assertIn("192.168.1.1", ips)
        self.assertIn("192.168.2.2", ips)

if __name__ == '__main__':
    unittest.main()
