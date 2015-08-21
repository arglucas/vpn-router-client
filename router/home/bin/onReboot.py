#!/usr/bin/env python
# Send SNS Notification of reboot and new IP Address
# Add to crontab for informing post reboot...
#   @reboot sleep 20 && /home/USERNAME/bin/onReboot.py
import boto.sns
import logging


import json
import netifaces

i = [{ifname: netifaces.ifaddresses(ifname)} for ifname in netifaces.interfaces()]
i_json = json.dumps(i, indent=2);


logging.basicConfig(filename="onReboot.log", level=logging.DEBUG)

s = boto.sns.connect_to_region("eu-west-1")

topic = "arn:aws:sns:eu-west-1:817794132868:HostAddress"
message = "RPI2 Rebooted.\n\n" + i_json
subject = "[NOTIFICATION] RPI2 Rebooted"

pub = s.publish(topic, message, subject=subject)

print pub 
