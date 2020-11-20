# VPN rotate - www.redandgreen.co.uk

server=$(cat '/etc/openvpn/privatvpn.conf' | grep remote -m1 | cut -d" " -f2)
nextserver=$(grep -A1 $server /etc/openvpn/list.txt|grep -v $server)

echo 'old server= ' $server

# clean line return
nextserver2=$(echo $nextserver | sed -e 's/\r//g')

echo 'new server= ' $nextserver2

if [ -z "$nextserver2" ]; then
	nextserver=$(head -n1 /etc/openvpn/list.txt)
fi
sed -i "s!$server!$nextserver2!" /etc/openvpn/privatvpn.conf
