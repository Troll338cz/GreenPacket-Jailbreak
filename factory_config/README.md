
## /data/turin/etc/config/factory_conf

This file contains device information from factory and default logins.
```
config turin 'data'
        option macbr '2479EFXXXXXX'
        option sn 'H5SGSNNNNNNNNN'  
        option adminUser 'superadmin'
        option adminPasswd 'admin'
        option userUser 'admin'
        option userPasswd 'admin'
        option telnet '0'
        option timeZone '+0100'
        option gateWayIp '192.168.0.1'
        option dhcpStartIp '192.168.0.2'
        option dhcpEndIp '192.168.0.254'
        option algEnable 'true'
        option ftmMode '0'
        option syncflage '0'
        option f_pcb '16'
```

## /data/turin/factory/backup.tar

This is a .tar.gz file (yes with .tar name) containing default system backup file

File structure:
```
backup_folder/
backup_folder/hostapd.accept		<- Empty
backup_folder/mifi_config.sqlite	<- Default settings, mostly empty
backup_folder/dnsmasq.conf		<- Template for DHCP server
backup_folder/datas/
backup_folder/datas/README.md
backup_folder/datas/memohi.db		<- User + md5 passwords, SMS inbox/outbox
backup_folder/turin			<- Generic device info
backup_folder/time_config.conf		<- NTP Client settings
backup_folder/easycwmp			<- Default TR-069 settings
backup_folder/hostapd.conf		<- Template
backup_folder/hostapd.deny		<- Empty
backup_folder/dnshosts			<- DNS hosts for LAN portal
```

You can copy this file to the device /tmp folder and change settings as you want (or don't want) to apply after factory reset.

Clean one will be provided in this folder (TODO)

```sh
# Unpack
tar xvf backup.tar
# Repack
tar czvf backup.tar ./backup_folder
```
