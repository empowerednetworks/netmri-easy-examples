#!/usr/bin/env python3
"""An example of using pagination."""

# Reference:
# broker.index
# Lists the available interfaces. Any of the inputs listed may be be used to narrow the list; other inputs 
# will be ignored. Of the various ways to query lists, using this method is most efficient.

# INPUTS
# AggrInterfaceID: Optional Type: Array of Integer
# The internal NetMRI identifier for the 'owning' link aggregation interface for link aggregate members.

# DeviceID: Optional Type: Array of Integer
# The internal NetMRI identifier for the device containing this interface.

# InterfaceID: Optional Type: Array of Integer
# The internal NetMRI identifier for this interface.

# VirtualNetworkMemberID: Optional Type: Array of Integer
# The internal NetMRI identifier of the Virtual Network Member on which this interface is defined, 
# or blank if this cannot be determined.

# ifMAC: Optional Type: Array of String
# The interface Media Access Controller (MAC) address.

# ifName: Optional Type: Array of String
# The name of this interface. This is typically the short name of the interface as it is identified in the 
# console.

# ifNameSort: Optional Type: Array of String
# The internal NetMRI name of this interface for sorting purpose.

# ifTrunkStatus: Optional Type: Array of String
# If "on", then this interface is a VLAN trunk port.

# DeviceGroupID: Optional Type: Array of Integer
# The internal NetMRI identifier of the device groups to which to limit the results.

# timestamp: Optional Type: DateTime
# The data returned will represent the interfaces as of this date and time. 
# If omitted, the result will indicate the most recently collected data.

# methods: Optional Type: Array of String
# A list of interface methods. The listed methods will be called on each interface returned and included in 
# the output. Available methods are: cap_if_description_ind, cap_if_admin_status_ind, cap_if_vlan_assignment_ind, 
# cap_if_voice_vlan_ind, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, 
# cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, cap_itf_net_deprovisioning_ind, 
# cap_if_description_na_reason, cap_if_admin_status_na_reason, cap_if_vlan_assignment_na_reason, 
# cap_if_voice_vlan_na_reason, cap_if_net_provisioning_ipv4_na_reason, cap_if_net_provisioning_ipv6_na_reason, 
# cap_if_net_deprovisioning_ipv4_na_reason, cap_if_net_deprovisioning_ipv6_na_reason, 
# cap_itf_net_deprovisioning_na_reason, aggr_interface, infradevice, ifphysaddress, control_capabilities, 
# vrf_name, vrf_description, vrf_rd, network_id, aggr_interface_name, vpc_peer_ifname, vpc_peer_device_id, 
# meta, network_name, data_source, device, vlan.

# include: Optional Type: Array of String
# A list of associated object types to include in the output. The listed associations will be returned as 
# outputs named according to the association name (see outputs below). Available includes are: 
# aggr_interface, meta, data_source, device.

# start: Optional Type: Integer
# The record number to return in the selected page of data. It will always appear, although it may not be the 
# first record. See the :limit for more information.

# limit: Optional Type: Integer
# The size of the page of data, that is, the maximum number of records returned. The limit size will be used 
# to break the data up into pages and the first page with the start record will be returned. So if you have 100 
# records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.

# sort: Optional Type: Array of String
# The data field(s) to use for sorting the output. Default is InterfaceID. Valid values are DataSourceID, 
# DeviceID, InterfaceID, ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, 
# ifName, ifNameSort, ifDescr, ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, 
# ifAdminStatus, ifOperStatus, ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, 
# ifAggrMemberInd, ifArtificialInd, ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, 
# ifAdminDuplex, Slot, Port, PoEPower, PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, 
# ifEncapsulationTag, ifPortControlInd, ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, 
# DownstreamSwitchCount.

# dir: Optional Type: Array of String
# The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.

# select: Optional Type: Array
# The list of attributes to return for each Interface. Valid values are DataSourceID, DeviceID, InterfaceID, 
# ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, ifName, ifNameSort, ifDescr, 
# ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, ifAdminStatus, ifOperStatus, 
# ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, ifAggrMemberInd, ifArtificialInd, 
# ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, ifAdminDuplex, Slot, Port, PoEPower, 
# PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, ifEncapsulationTag, ifPortControlInd, 
# ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, DownstreamSwitchCount. 
# If empty or omitted, all attributes will be returned.

# goto_field: Optional Type: String
# The field name for NIOS GOTO that is used for locating a row position of records.

# goto_value: Optional Type: String
# The value of goto_field for NIOS GOTO that is used for locating a row position of records.

# NetworkID: Optional Type: Integer
# The network id to which results would be limited.

# OUTPUTS
# interfaces Type: Array of Interface
# An array of the Interface objects that match the specified input criteria.

import argparse
import configparser
from infoblox_netmri.client import InfobloxNetMRI as blox

# it's safe to ignore these two functions, they're just here for convenience.
def get_args(args=None):
    """Deal with command line arguments."""
    config_file = ""
    description = "An example of using pagination."
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
    broker = client.get_broker("Interface")
    interfaces_results = broker.index() # <-- Note that we're not limiting the return set at all here;
                                          #     the arguments to index() are all optional, so keep in mind
                                          #     there may be a need to use pagination on the results from
                                          #     large classes like Device or Interface.
    # Important note on dereferencing: broker.search is going to return a List of NotificationRemote objects, 
    # so you'd probably want to iterate through the list and tweeze out the property(-ies) of interest
    # and stuff them into an interim structure.
    print("==> Do index() on interfaces with no limits.")
    print("The total number of interfaces that NetMRI knows about is %s." %len(interfaces_results))
    interfaces_results = broker.index(start=0, limit=10)
    print("==> Same operation but now starting at 0 and limiting to 10 records.")
    print("The total number of interfaces that NetMRI knows about is %s." %len(interfaces_results))
    

    
if __name__ == "__main__":
    main()
