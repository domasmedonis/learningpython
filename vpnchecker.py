import requests
import dns.resolver

# ---------- CONFIG ----------
HOME_IP = "YOUR_HOME_IP"  # Replace with your real home IP for comparison
DNS_SERVERS = ["8.8.8.8", "1.1.1.1"]  # Google & Cloudflare
# -----------------------------

def get_public_ip():
    """Fetch current public IP."""
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        ip = response.json().get("ip")
        return ip
    except Exception as e:
        return f"Error: {e}"

def check_dns():
    """Check DNS resolution using specified DNS servers."""
    results = {}
    for server in DNS_SERVERS:
        try:
            resolver = dns.resolver.Resolver()
            resolver.nameservers = [server]
            answer = resolver.resolve("example.com")
            ips = [a.to_text() for a in answer]
            results[server] = ips
        except Exception as e:
            results[server] = f"Error: {e}"
    return results

def analyze_vpn(ip):
    """Analyze if VPN is active based on IP comparison."""
    if ip == HOME_IP:
        return False
    else:
        return True

def main():
    print("=== VPN Checker ===\n")
    
    # Check public IP
    ip = get_public_ip()
    print(f"Public IP: {ip}")
    
    vpn_active = analyze_vpn(ip)
    if vpn_active:
        print("✅ VPN appears to be ACTIVE")
    else:
        print("❌ VPN appears to be INACTIVE")
    
    # Check DNS
    print("\nChecking DNS servers...")
    dns_results = check_dns()
    leak_found = False
    for server, ips in dns_results.items():
        print(f"DNS Server {server}: {ips}")
        if server not in DNS_SERVERS:
            leak_found = True
    
    if leak_found:
        print("\n⚠ DNS leak detected!")
    else:
        print("\n✅ No obvious DNS leaks detected")

if __name__ == "__main__":
    main()