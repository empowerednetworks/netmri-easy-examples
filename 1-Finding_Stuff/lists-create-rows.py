#!/usr/bin/env python3
"""An example of using the ConfigList broker to add a new row to a list with values."""

# Reference: 
# broker.create_row
# Create a row in a config list

# INPUTS
#  id: Optional Type: Integer
#        The internal NetMRI identifier for the list. Either id or name is required.

#  name: Optional Type: String
#        The name of the config list. Either id or name is required.

#  list_columns: Optional Type: String
#        Each list column to be updated should be included as a separate input, 
#        starting the name with $ (no actual input named list_columns is needed). 
#        For example, you can update the column 'foo' of a list to 'bar' by passing $foo 
#        as the input name, along with the value 'bar'.

# Important note for use in Python: This documentation is a bit inobvious, so I hope the code
# below more fully demonstrates what the library expects you to do.  In summary:
#    - create a dictonary
#    - include the list_id in the dictionary
#    - make the column names from the list the keys to your dictionary, adding leading "$" to each.
#    - pass everything over as **kwargs
#
# You can get the column names contained in the list by calling /config_lists/show with the id of the list
# you're operating on and then parsing through the json_columns collection on the name attribute.

# OUTPUTS
#  list_row Type: Hash (dict)
#        The config list row that was created.


import argparse
import configparser
from infoblox_netmri.client import InfobloxNetMRI as blox

# it's safe to ignore these two functions, they're just here for convenience.
def get_args(args=None):
    """Deal with command line arguments."""
    config_file = ""
    description = "An example of using the ConfigList broker to add a new row to a list with values."
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
    broker = client.get_broker("ConfigList")
    new_row_values = { 
                        "id" : 6, 
                        "$Name" : "Pebbles", 
                        "$Value1" : "Apples", 
                        "$Value2" : "Oranges", 
                        "$Value3" : "Potatoes" 
                    }
    row_results = broker.create_row(**new_row_values)
    
    print(row_results)
    
if __name__ == "__main__":
    main()
