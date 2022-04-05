#!/usr/bin/python3

import unittest, re
from napalm import get_network_driver
def ping_loopback(ip, user, passwd, loopback):
    driver = get_network_driver('ios')
    device = driver(ip, user, passwd)
    device.open()
    ping = device.device.send_command(f'ping {loopback} source loopback 0')
    m = re.search('(Success rate is)\s([\d]*)',ping)
    percent = int(m.group(2))
    device.close()
    return percent

def ospf_config(ip, user, passwd):
    driver = get_network_driver('ios')
    device = driver(ip, user, passwd)
    device.open() 
    iface = device.device.send_command(f'sh int loopback99')
    ip = re.search('[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}\/[\d]{2}',iface)
    loop_ip = ip.group(0)
    device.close()
    return loop_ip


def ospf_area(ip, user, passwd):
    driver = get_network_driver('ios')
    device = driver(ip, user, passwd)
    device.open() 
    iface = device.device.send_command(f'sh run  | i area')
    m = re.findall('area\s[\d]*',iface)
    length = len(m)
    device.close()
    return length


class TestStringMethods(unittest.TestCase):

    def test_loopback(self):
        loop_ip = ospf_config('198.51.100.15', 'netman', 'netman')
        self.assertEqual(loop_ip, '10.1.3.1/24')
		
    def test_ping(self):
        result = ping_loopback('198.51.100.12', 'netman', 'netman', '10.1.3.1')
        self.assertEqual(result, 100)

    def test_area(self):
        area = ospf_area('198.51.100.11', 'netman', 'netman')    
        self.assertEqual(area, 1)

if __name__ == '__main__':
    unittest.main()
