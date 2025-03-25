import psutil
import sounddevice as sd
import socket

def check_network():
    print("=== 網卡狀況檢測 ===")
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    for interface, addrs in interfaces.items():
        print(f"網卡名稱: {interface}")
        for addr in addrs:
            print(f"  {addr.family.name}: {addr.address}")
        if interface in stats:
            status = "已啟用" if stats[interface].isup else "已停用"
            print(f"  狀態: {status}")
        print()

def check_internet():
    print("=== 網路連線檢測 ===")
    try:
        socket.create_connection(("www.google.com", 80), timeout=2)
        print("網路連線：成功")
    except OSError:
        print("網路連線：失敗")
    print()

def check_microphone():
    print("=== 麥克風檢測 ===")
    try:
        devices = sd.query_devices()
        for device in devices:
            if device['max_input_channels'] > 0:
                print(f"麥克風裝置：{device['name']} (輸入通道：{device['max_input_channels']})")
    except Exception as e:
        print(f"檢測失敗：{str(e)}")
    print()

def check_speaker():
    print("=== 喇叭檢測 ===")
    try:
        devices = sd.query_devices()
        for device in devices:
            if device['max_output_channels'] > 0:
                print(f"喇叭裝置：{device['name']} (輸出通道：{device['max_output_channels']})")
    except Exception as e:
        print(f"檢測失敗：{str(e)}")
    print()

def main():
    check_network()
    check_internet()
    check_microphone()
    check_speaker()

if __name__ == "__main__":
    main()
