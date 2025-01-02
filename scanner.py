from ping3 import ping
from ipaddress import ip_network, ip_address
from concurrent.futures import ThreadPoolExecutor, as_completed

def is_ip_free(ip, timeout=1):
    """
    Check if an IP address is free by pinging it.
    Uses a timeout to avoid long waits for unreachable hosts.
    """
    try:
        response = ping(ip, timeout=timeout)
        return ip if response is None else None
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        return None

def find_free_ips(subnet, timeout=1, max_threads=50):
    """
    Find free IP addresses in a given subnet using multithreading.
    """
    free_ips = []
    with ThreadPoolExecutor(max_threads) as executor:
        future_to_ip = {executor.submit(is_ip_free, str(ip), timeout): ip for ip in ip_network(subnet, strict=False).hosts()}
        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                result = future.result()
                if result:
                    free_ips.append(ip_address(result))  # Convert to ip_address for proper sorting
            except Exception as e:
                print(f"Error checking IP {ip}: {e}")
    return free_ips

if __name__ == "__main__":
    # Specify the subnet to scan (e.g., "192.168.1.0/24")
    subnet = input("Enter the subnet (e.g., 192.168.1.0/24): ").strip()
    timeout = input("Enter the timeout per ping (default is 1 second): ").strip()
    timeout = float(timeout) if timeout else 1
    max_threads = input("Enter the number of threads (default is 50): ").strip()
    max_threads = int(max_threads) if max_threads else 50

    print(f"Scanning for free IPs in subnet: {subnet} with timeout {timeout}s and {max_threads} threads.")
    free_ips = find_free_ips(subnet, timeout, max_threads)

    if free_ips:
        free_ips.sort()  # Sort IPs numerically
        print(f"Free IPs in subnet {subnet}:")
        for ip in free_ips:
            print(ip)
    else:
        print("No free IPs found.")
