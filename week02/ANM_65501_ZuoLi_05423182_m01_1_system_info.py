import time
import sys
import platform

# Define data
current_time = time.asctime()
current_date = '{} {},{}'.format(current_time.split(' ')[1],
                                 current_time.split(' ')[3],
                                 current_time.split(' ')[5])
current_clock = current_time.split(' ')[4]
operating_system = "{} {}".format(platform.system(), platform.release())
python_version = sys.version.split(' ')[0]
title = 'System Report'

# Process data
output_string = '{}\n \
    Time: {}\n \
    Date:{}\n \
    Operating Systerm: {}\n \
    Python Version: {}'.format(
                            title,
                            current_clock,
                            current_date,
                            operating_system,
                            python_version) 

print (output_string)