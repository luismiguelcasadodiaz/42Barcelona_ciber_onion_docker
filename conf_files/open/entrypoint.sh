#!/bin/sh


# Start NGINX Service
/usr/sbin/nginx -g 'daemon off;' &


# Start SSH service

ssh-keygen -A
/usr/sbin/sshd -D -e "$@"

# "-D": This flag tells the SSH daemon to run in the foreground and stay attached to the terminal.
# Normally, sshd detaches itself from the terminal and runs as a background process, but using 
# this flag keeps it in the foreground. This can be useful for debugging purposes or when you want 
# to monitor the SSH daemon's activity in real-time.

# "-e": This flag instructs the SSH daemon to send its debug output to the standard error (stderr)
# instead of the system log files. By default, sshd logs its debug information to the system log, 
# but using this flag redirects the output to stderr. This can be helpful when troubleshooting 
# SSH connection issues or investigating problems with the SSH daemon.

