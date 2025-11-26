uci set easycwmp.@acs[0].periodic_enable='0'
uci set easycwmp.@local[0].enable='0'
uci set easycwmp.@acs[0].url='https://disabled/cwmp'
systemctl stop turin_easycwmpd.service
systemctl disable turin_easycwmpd.service
echo "TR69 disable ok" >> /tmp/status.txt
