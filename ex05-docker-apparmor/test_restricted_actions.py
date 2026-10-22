import time
import docker

client = docker.from_env()

container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)
print(f"Container started: {container.short_id}")
time.sleep(2)

def attempt(label, cmd):
    try:
        exit_code, output = container.exec_run(cmd)
        print(f"{label}: Exit Code {exit_code}, Output: {output.decode(errors='replace').strip()}")
    except docker.errors.APIError as e:
        print(f"{label}: BLOCKED -> {e}")

attempt("Attempt to run cat /etc/passwd", "cat /etc/passwd")
attempt("Attempt to execute /bin/bash", "/bin/bash")
attempt("Attempt to read /etc/passwd using Python",
        ["python", "-c", "print(open('/etc/passwd').read())"])

container.stop()
container.remove()
print("Container stopped")
