# VPN rotate - www.redandgreen.co.uk

# close current tunnel and then modify conf file with next server ip address 
sudo service openvpn stop
sleep 4
sudo ifconfig tun0 down


server=$(cat '/etc/openvpn/privatvpn.conf' | grep remote -m1 | cut -d" " -f2)
nextserver=$(grep -A1 $server /etc/openvpn/list.txt|grep -v $server)

echo 'old server= ' $server

# clean line return
nextserver2=$(echo $nextserver | sed -e 's/\r/\n/g')

echo 'new server= ' $nextserver2

if [ -z "$nextserver2" ]; then
        nextserver=$(head -n1 /etc/openvpn/list.txt)
fi
sed -i "s!$server!$nextserver2!" /etc/openvpn/privatvpn.conf

# bring tunnel back up, connecting to the new server ip
sudo ifconfig tun0 up
sleep 3
sudo service openvpn start

