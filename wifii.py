import os
from wifi import Cell

def find_wifi_networks(interface_name, number_of_networks_to_show):
    cells = list(Cell.all(interface_name))
    return list(sorted(cells, key=lambda x: x.signal, reverse=True))[:number_of_networks_to_show]

def connect_to_wifi(interface_name, cell, passkey):
    cmd = f'nmcli d wifi connect "{cell.ssid}" password "{passkey}" iface "{interface_name}"'
    os.system(cmd + '>/dev/null 2>&1') 

if __name__ == '__main__':
    interface_name = "wlp1s0"
    number_of_networks_to_show = 3
    available_networks = find_wifi_networks(interface_name, number_of_networks_to_show)
    print(f"Your available wifi networks are:")
    for index in range(len(available_networks)):
        print(f"{[index+1]} {available_networks[index].ssid}")
    network_number = int(input("Your choice? "))
    password = input("Password: ")
    connect_to_wifi(interface_name, available_networks[network_number-1], password)
    print("connected!")