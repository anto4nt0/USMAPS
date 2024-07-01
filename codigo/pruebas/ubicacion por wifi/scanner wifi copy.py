import pywifi
from pywifi import const
import time

def scan_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(5)  # Espera un poco para que se complete el escaneo

    scan_results = iface.scan_results()
    networks = {}
    for network in scan_results:
        ssid = network.ssid
        bssid = network.bssid
        signal = network.signal  # Intensidad de la señal
        if ssid not in networks:
            networks[ssid]={}
            networks[ssid][bssid]= {'señal': signal}
        elif ssid in networks:
            networks[ssid][bssid]= {'señal': signal}
    return networks
wifis= scan_networks()
print(wifis)


def mayor_intensidad():
    mayor= []
    cont=True
    for i in wifis:
        if cont==True:
            mayor.append(i)
            mayor.append(wifis['Estudiantes_USM'][i]['señal'])
            cont=False
        if wifis['Estudiantes_USM'][i]['señal']>mayor[1]:
            mayor[0]=i
            mayor[1]= wifis['Estudiantes_USM'][i]['señal']
    return mayor
                

            
        
def main():
    networks = scan_networks()
    for ssid, bssid, signal in networks:
        print(f"SSID: {ssid}")
        print(f"MAC Address: {bssid}")
        print(f"Signal: {signal} dBm")  # Muestra la intensidad de la señal en dBm
        print("---------------------------")
