#!/bin/bash
# APN 1
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data0 -p udp -m udp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data0 -p udp -m udp --dport 10001 -j DROP
# APN 2
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data1 -p udp -m udp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data1 -p udp -m udp --dport 10001 -j DROP
# APN 3
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data2 -p udp -m udp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data2 -p udp -m udp --dport 10001 -j DROP
# APN 4
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 23 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 80 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 443 -j DROP
iptables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 2222 -j DROP
iptables -A  INPUT -i rmnet_data3 -p udp -m udp --dport 10001 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 23 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 80 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 443 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p tcp -m tcp --dport 2222 -j DROP
ip6tables -A  INPUT -i rmnet_data3 -p udp -m udp --dport 10001 -j DROP
exit 0
