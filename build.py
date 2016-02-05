import sys
import subprocess
import ansible.runner
from pynt import task

@task()
def run_playbook():
    print "running the playbook"
    subprocess.call(["ansible-playbook", "-i", "inventory", "site.yml"])

@task()
def get_roles():
    print "getting the roles"
    subprocess.call(["ansible-galaxy", "install", "-r", "requirements.yml", "-p", "roles/", "--force"])

@task()
def ping_hosts():
    print "pinging hosts"
    subprocess.call(["ansible", "-i", "inventory", "-m", "ping", "all"])

@task()
def display_host():
    print "storing host info"
    subprocess.call(["ansible", "-i", "inventory", "-m", "setup", "-t", "/tmp/facts",  "all"])


__DEFAULT__ = run_playbook
