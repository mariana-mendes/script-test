import subprocess
import datetime
import time

servers = [
    "ping.online.net",
    "ping6.online.net",
    "ping-90ms.online.net",
    "ping6-90ms.online.net",
    "iperf3.moji.fr",
    "speedtest.milkywan.fr",
    "iperf.par2.as49434.net",
    "paris.bbr.iperf.bytel.fr",
    "paris.cubic.iperf.bytel.fr",
    "mrs.bbr.iperf.bytel.fr",
    "mrs.cubic.iperf.bytel.fr",
    "lyo.bbr.iperf.bytel.fr",
    "lyo.cubic.iperf.bytel.fr",
    "tls.bbr.iperf.bytel.fr",
    "tls.cubic.iperf.bytel.fr",
    "str.bbr.iperf.bytel.fr",
    "str.cubic.iperf.bytel.fr",
    "poi.bbr.iperf.bytel.fr",
    "poi.cubic.iperf.bytel.fr",
    "ren.bbr.iperf.bytel.fr",
    "ren.cubic.iperf.bytel.fr",
    "speedtest.serverius.net",
    "nl.iperf.014.fr",
    "ch.iperf.014.fr",
    "iperf.eenet.ee",
    "iperf.astra.in.ua",
    "iperf.volia.net",
    "iperf.angolacables.co.ao",
    "speedtest.uztelecom.uz",
    "iperf.biznetnetworks.com",
    "speedtest-iperf-akl.vetta.online",
    "iperf.he.net"
]


def run_iperf(server):
    time = 300
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"iperf_log_{server.replace('.', '_')}_{timestamp}.txt"
    command = ["iperf3", "-c", server, "-t", str(time)]  # Run 10s iperf test

    try:
        with open(log_filename, "w") as logfile:
            print(f"Running iperf test on {server}...")
            process = subprocess.run(command, stdout=logfile, stderr=subprocess.STDOUT, text=True, timeout=time+60)
            if process.returncode == 0:
                print(f"Test succeeded, output saved to {log_filename}")
                return True
            else:
                print(f"Test failed on {server} with return code {process.returncode}")
                return False
    except subprocess.TimeoutExpired:
        print(f"Test on {server} timed out.")
        return False
    except Exception as e:
        print(f"Error running iperf on {server}: {e}")
        return False

def main():
    for server in servers:
        success = run_iperf(server)
        if success:
            break 
        else:
            print(f"Trying next server...")
    else:
        print("All servers failed.")


if __name__ == "__main__":
    main()
