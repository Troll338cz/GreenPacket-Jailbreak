#!/bin/bash
# Interfaces are in DOWN status if you dont have more APNs configured

# APN 1
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 6969 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 7574 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 10001 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 12900 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 7574 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 12900 -j DROP
# APN 2
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 6969 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 7574 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 10001 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 12900 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 7574 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 12900 -j DROP
# APN 3
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 6969 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 7574 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 10001 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 12900 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 7574 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 12900 -j DROP
# APN 4
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 6969 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 7574 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 10001 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 12900 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 7574 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 12900 -j DROP

exit 0
