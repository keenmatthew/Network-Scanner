# Network Scanner
Python script to perform a ping sweep of a subnet to find all free addresses

```java
Enter the subnet (e.g., 192.168.1.0/24): 192.168.1.0/24
Enter the timeout per ping (default is 1 second): 0.5
Enter the number of threads (default is 50): 100
```

```java
Scanning for free IPs in subnet: 192.168.1.0/24 with timeout 0.5s and 100 threads.
Free IPs in subnet 192.168.1.0/24:
192.168.1.2
192.168.1.3
192.168.1.10
192.168.1.11
```

## To Run
```shell
# python -m venv myenv
# pip install -r requirements.txt
# python scanner.py
```

