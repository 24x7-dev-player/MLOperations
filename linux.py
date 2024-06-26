# Linux Basics

# Common Directories
root_directory = "/"            # Root directory
bin_directory = "/bin"          # Essential binary executables
etc_directory = "/etc"          # Configuration files
home_directory = "/home"        # User home directories
var_directory = "/var"          # Variable data files like logs
usr_directory = "/usr"          # User programs and data
tmp_directory = "/tmp"          # Temporary files

# File System Commands
ls_command = "ls"          # List directory contents
cd_command = "cd"          # Change directory
cp_command = "cp"          # Copy files or directories
mv_command = "mv"          # Move or rename files or directories
rm_command = "rm"          # Remove files or directories
mkdir_command = "mkdir"    # Create a new directory
pwd_command = "pwd"        # Print working directory
man_command = "man"        # Manual pages for commands

# Permissions
# Read (r), write (w), and execute (x) permissions for owner, group, and others
chmod_command = "chmod"    # Change file permissions
chown_command = "chown"    # Change file owner and group
chgrp_command = "chgrp"    # Change group ownership

# Example Permissions
read_permission = "r"      # Read permission
write_permission = "w"     # Write permission
execute_permission = "x"   # Execute permission

# Package Management Commands

# Debian-based (APT)
apt_update_command = "sudo apt-get update"     # Update package list
apt_install_command = "sudo apt-get install"   # Install package
apt_upgrade_command = "sudo apt-get upgrade"   # Upgrade all packages

# Red Hat-based (RPM)
yum_install_command = "sudo yum install"       # Install package
yum_update_command = "sudo yum update"         # Update all packages
yum_remove_command = "sudo yum remove"         # Remove package

# System Management Commands

# User Management
useradd_command = "sudo useradd"   # Add a new user
passwd_command = "sudo passwd"     # Change user password
usermod_command = "sudo usermod"   # Modify a user account
userdel_command = "sudo userdel"   # Delete a user account

# Process Management
ps_command = "ps"                  # Report process status
top_command = "top"                # Display all running processes
kill_command = "kill"              # Terminate a process by PID
killall_command = "killall"        # Terminate processes by name

# Disk Management
df_command = "df"                  # Report file system disk space usage
du_command = "du"                  # Estimate file space usage
fdisk_command = "sudo fdisk"       # Partition table manipulator for Linux
mkfs_command = "sudo mkfs"         # Build a Linux file system

# Networking Commands

# Configuration
ifconfig_command = "ifconfig"      # Configure network interfaces (deprecated)
ip_command = "ip"                  # Show/manipulate routing, devices, policy routing

# Tools
ping_command = "ping"              # Send ICMP ECHO_REQUEST to network hosts
netstat_command = "netstat"        # Network statistics
ssh_command = "ssh"                # OpenSSH SSH client (remote login program)

# Shell Scripting

# Example Script Structure
shebang = "#!/bin/bash"            # Shebang line for bash scripts
comment = "# This is a comment"    # Single line comment

# Variables
variable_assignment = "VAR_NAME=value"  # Assign a value to a variable
variable_access = "$VAR_NAME"           # Access the value of a variable

# Control Structures
if_structure = """
if [ condition ]; then
    # Commands
fi
"""

for_loop = """
for VAR in list; do
    # Commands
done
"""

while_loop = """
while [ condition ]; do
    # Commands
done
"""

# Functions
function_definition = """
function_name () {
    # Commands
}
"""

# Security Commands

# Firewall
iptables_command = "sudo iptables"  # Configure IP packet filter rules
ufw_command = "sudo ufw"            # Uncomplicated Firewall

# SELinux
selinux_command = "sestatus"        # Check SELinux status

# System Monitoring

# Log Files
log_directory = "/var/log"          # Directory containing log files
tail_command = "tail"               # View the end of a file
cat_command = "cat"                 # Concatenate and display files
less_command = "less"               # View file contents one screen at a time

# Monitoring Tools
htop_command = "htop"               # Interactive process viewer
vmstat_command = "vmstat"           # Report virtual memory statistics

# Example usage in Python (Note: These commands need to be run in a shell environment)
import os

# Running a basic command
os.system(ls_command)

# Example: Listing home directory contents
os.system(f"{ls_command} {home_directory}")
