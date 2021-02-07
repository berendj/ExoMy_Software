#!/usr/bin/env python

import rospy
# import subprocess // Neede for the second method that is commented out
from subprocess import call

class Raspberry():

    def shutdown(self):
        rospy.loginfo('Raspberry Pi shutting down')
        call("/sbin/shutdown -h now", shell=True)

#        This was an other way to shutdown the pay, but is also not working
#        command = "/usr/bin/sudo /sbin/shutdown -h now"
#        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#        output = process.communicate()[0]
#        return output

    def reboot(self):
        rospy.loginfo('Raspberry Pi rebooting')
        call("sbin/shutdown -r now", shell=True)

#        This was an other way to shutdown the pay, but is also not working
#        command = "/usr/bin/sudo /sbin/shutdown -r now"
#        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
#        output = process.communicate()[0]
#        return output
