#!/usr/bin/env python3
"""An example of using the Notification broker to get a list of notifications."""

# Reference:
# broker.index
# Lists the available notifications. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

# INPUTS
# id: Optional Type: Array of Integer
# The internal NetMRI identifier for the notification.

# start: Optional Type: Integer
# The record number to return in the selected page of data. It will always appear, although it may not be the 
# first record. See the :limit for more information.

# limit: Optional Type: Integer
# The size of the page of data, that is, the maximum number of records returned. The limit size will 
# be used to break the data up into pages and the first page with the start record will be returned. 
# So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. 
# The maximum limit is 10000.

# sort: Optional Type: Array of String
# The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_user_id, category, 
# delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, 
# from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, 
# event_type, send_clearing_ind, cron, last_run.

# dir: Optional Type: Array of String
# The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.

# select: Optional Type: Array
# The list of attributes to return for each Notification. Valid values are id, auth_user_id, category, 
# delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, 
# from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, 
# event_type, send_clearing_ind, cron, last_run. If empty or omitted, all attributes will be returned.

# goto_field: Optional Type: String
# The field name for NIOS GOTO that is used for locating a row position of records.

# goto_value: Optional Type: String
# The value of goto_field for NIOS GOTO that is used for locating a row position of records.

# OUTPUTS
# notifications Type: Array of Notification
# An array of the Notification objects that match the specified input criteria.

import argparse
import configparser
from infoblox_netmri.client import InfobloxNetMRI as blox

# it's safe to ignore these two functions, they're just here for convenience.
def get_args(args=None):
    """Deal with command line arguments."""
    config_file = ""
    description = "An example of using the Device broker to search for a device by name."
    try:
        with open("../examples.local") as dev_f:
            print("Using local config " + dev_f.name + ".")
            config_file = "../examples.local"
    except IOError:
        config_file = "../examples.conf"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-c", "--configfile",
                        help="/path/to/configfile",
                        default=config_file)
    results = parser.parse_args(args)
    return {"configfile": results.configfile}

def get_config(args):
    """Read our config file for local settings."""
    config = configparser.ConfigParser()
    thisconfig = config.read(args["configfile"])
    if len(thisconfig) == 0: # length of thisconfig will be zero if the config file doesn't exist.
        return None
    return config
# it's safe to ignore these two functions, they're just here for convenience.

def main():
    """The Main Event!"""
    args = get_args()
    config = get_config(args)
    creds = {"host" : config["netmri-settings"]["netmri-api-hostname"],
             "username" : config["netmri-settings"]["netmri-user"],
             "password" : config["netmri-settings"]["netmri-password"]}
    client = blox(**creds)
    broker = client.get_broker("Notification")
    notification_results = broker.index() # <-- Note that we're not limiting the return set at all here;
                                          #     the arguments to index() are all optional, so keep in mind
                                          #     there may be a need to use pagination on the results from
                                          #     large classes like Device or Interface.
    # Important note on dereferencing: broker.search is going to return a List of NotificationRemote objects, 
    # so you'd probably want to iterate through the list and tweeze out the property(-ies) of interest
    # and stuff them into an interim structure.
    for thisresult in notification_results:
        print(thisresult.id, thisresult.category, thisresult.delivery_method)

    
if __name__ == "__main__":
    main()
