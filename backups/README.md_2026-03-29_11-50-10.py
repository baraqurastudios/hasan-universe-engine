import subprocess

class ServiceMonitor:
    def get_active_services(self):
        # v2.2: Real-time service status check
        output = subprocess.getoutput("docker ps --format '{{.Names}}'")
        return output.split("\n")

    def is_healthy(self, service_name):
        status = subprocess.getoutput(f"docker inspect -f '{{{{.State.Running}}}}' {service_name}")
        return status == "true"