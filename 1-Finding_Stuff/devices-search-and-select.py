#!/usr/bin/env python3
"""An example of using the Device broker to search for a device by name but limiting fields returned with select()."""

# Reference:
# broker.search
# Lists the available devices matching the input criteria. This method provides a more flexible search 
# interface than the index method, but searching using this method is more demanding on the system and 
# will not perform to the same level as the index method. The input fields listed below will be used 
# as in the index method, to filter the result, along with the optional query string and XML filter 
# described below.

# INPUTS
# DataSourceID: Optional Type: Array of Integer
# The internal NetMRI identifier for the collector NetMRI that collected this data record.

# DeviceAddlInfo: Optional Type: Array of String
# Additional information about the device; IP phones will contain the extension in this field.

# DeviceAssurance: Optional Type: Array of Integer
# The assurance level of the device type value.

# DeviceChangedCols: Optional Type: Array of String
# The fields that changed between this revision of the record and the previous revision.

# DeviceDNSName: Optional Type: Array of String
# The device name as reported by DNS.

# DeviceEndTime: Optional Type: Array of DateTime
# The ending effective time of this record, or empty if still in effect.

# DeviceFirstOccurrenceTime: Optional Type: Array of DateTime
# The date/time that this device was first seen on the network.

# DeviceID: Optional Type: Array of Integer
# An internal NetMRI identifier for the device.

# DeviceIPDotted: Optional Type: Array of String
# The management IP address of the device, in dotted (or colon-delimited for IPv6) format.

# DeviceIPNumeric: Optional Type: Array of Integer
# The numerical value of the device IP address.

# DeviceMAC: Optional Type: Array of String
# The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest 
# numbered non-zero MAC for any interface on the device. If no interface records are available for the device, 
# the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table 
# will be used.

# DeviceModel: Optional Type: Array of String
# The device model name.

# DeviceName: Optional Type: Array of String
# The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, 
# depending on your NetMRI configuration.

# DeviceNetBIOSName: Optional Type: Array of String
# The NetBIOS name of the device.

# DeviceOUI: Optional Type: Array of String
# The NetMRI-determined device vendor using OUI.

# DeviceStartTime: Optional Type: Array of DateTime
# The starting effective time of this revision of the record.

# DeviceSysContact: Optional Type: Array of String
# The contact information of a device.

# DeviceSysDescr: Optional Type: Array of String
# The device sysDescr as reported by SNMP.

# DeviceSysLocation: Optional Type: Array of String
# The device sysLocation as reported by SNMP.

# DeviceSysName: Optional Type: Array of String
# The device name as reported by SNMP.

# DeviceTimestamp: Optional Type: Array of DateTime
# The date and time this record was collected.

# DeviceType: Optional Type: Array of String
# The NetMRI-determined device type.

# DeviceUniqueKey: Optional Type: Array of String
# Unique key which allows duplicates detecting over different Virtual Networks.

# DeviceVendor: Optional Type: Array of String
# The device vendor name.

# DeviceVersion: Optional Type: Array of String
# The device OS version.

# InfraDeviceInd: Optional Type: Array of Boolean
# A flag indicating whether this device is an infrastructure device or not.

# MgmtServerDeviceID: Optional Type: Array of Integer
# The Device ID of the management server for the device

# NetworkDeviceInd: Optional Type: Array of Boolean
# A flag indicating whether this device is a network device or an end host.

# ParentDeviceID: Optional Type: Array of Integer
# The internal NetMRI identifier for the device containing this virtual device.

# VirtualInd: Optional Type: Array of Boolean
# A flag indicating if the source device is a virtual device.

# VirtualNetworkID: Optional Type: Array of Integer
# The internal NetMRI identifier of the Virtual Network on which this device is defined, or blank if this 
# cannot be determined.

# DeviceGroupID: Optional Type: Array of Integer
# The internal NetMRI identifier of the device groups to which to limit the results.

#timestamp: Optional Type: DateTime
# The data returned will represent the devices as of this date and time. If omitted, the result will 
# indicate the most recently collected data.

# methods: Optional Type: Array of String
# A list of device methods. The listed methods will be called on each device returned and included 
# in the output. Available methods are: SwitchingInd, RoutingInd, DeviceSAAVersion, DeviceRebootTime, 
# DeviceContextName, DeviceCommunitySecure, DeviceRank, DeviceCommunity, DeviceFirstOccurrence, group, 
# parent_device, gateway_device, running_config, running_config_text, saved_config, saved_config_text, 
# running_config_diff, saved_config_diff, virtual_child_count, asset_type, device_setting, 
# data_collection_status, control_capabilities, network_name, interfaces, issue_details, device_routes, 
# device_physicals, if_addrs, config_revisions, detected_changes, device_ports, privileged_polling, 
# cap_description_ind, cap_admin_status_ind, cap_vlan_assignment_ind, cap_voice_vlan_ind, 
# cap_net_provisioning_ind, cap_net_vlan_provisioning_ind, cap_net_deprovisioning_ind, 
# cap_description_na_reason, cap_admin_status_na_reason, cap_vlan_assignment_na_reason, 
# cap_voice_vlan_na_reason, cap_net_provisioning_na_reason, cap_net_vlan_provisioning_na_reason, 
# cap_net_deprovisioning_na_reason, meta, data_source.

# include: Optional Type: Array of String
# A list of associated object types to include in the output. The listed associations will be returned 
# as outputs named according to the association name (see outputs below). Available includes are: parent_device, 
# device_setting, data_collection_status, interfaces, issue_details, device_routes, device_physicals, 
# if_addrs, config_revisions, detected_changes, device_ports, meta, data_source.

# start: Optional Type: Integer
# The record number to return in the selected page of data. It will always appear, although it may 
# not be the first record. See the :limit for more information.

# limit: Optional Type: Integer
# The size of the page of data, that is, the maximum number of records returned. The limit size will be used 
# to break the data up into pages and the first page with the start record will be returned. 
# So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. 
# The maximum limit is 10000.

# sort: Optional Type: Array of String
# The data field(s) to use for sorting the output. Default is DeviceID. Valid values are 
# DataSourceID, DeviceID, DeviceStartTime, DeviceEndTime, DeviceChangedCols, DeviceIPDotted, 
# DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, 
# DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceFirstOccurrenceTime, 
# DeviceTimestamp, DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceNetBIOSName, DeviceOUI, 
# MgmtServerDeviceID, InfraDeviceInd, NetworkDeviceInd, VirtualInd, VirtualNetworkID, DeviceUniqueKey.

# dir: Optional Type: Array of String
# The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.

# select: Optional Type: Array
# The list of attributes to return for each Device. Valid values are DataSourceID, DeviceID, 
# DeviceStartTime, DeviceEndTime, DeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, 
# DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceSysName, DeviceSysDescr, 
# DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceFirstOccurrenceTime, DeviceTimestamp, 
# DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceNetBIOSName, DeviceOUI, MgmtServerDeviceID, 
# InfraDeviceInd, NetworkDeviceInd, VirtualInd, VirtualNetworkID, DeviceUniqueKey. 
# If empty or omitted, all attributes will be returned.

# goto_field: Optional Type: String
# The field name for NIOS GOTO that is used for locating a row position of records.

# goto_value: Optional Type: String
# The value of goto_field for NIOS GOTO that is used for locating a row position of records.

# NetworkID: Optional Type: Integer
# The network id to which results would be limited.

# query: Optional Type: String
# This value will be matched against devices, looking to see if one or more of the listed attributes contain 
# the passed value. You may also surround the value with '/' and '/' to perform a regular expression 
# search rather than a containment operation. Any record that matches will be returned. 
# The attributes searched are: DataSourceID, DeviceAddlInfo, DeviceAssurance, DeviceChangedCols, 
# DeviceDNSName, DeviceEndTime, DeviceFirstOccurrenceTime, DeviceID, DeviceIPDotted, DeviceIPNumeric, 
# DeviceMAC, DeviceModel, DeviceName, DeviceNetBIOSName, DeviceOUI, DeviceStartTime, DeviceSysContact, 
# DeviceSysDescr, DeviceSysLocation, DeviceSysName, DeviceTimestamp, DeviceType, DeviceUniqueKey, 
# DeviceVendor, DeviceVersion, InfraDeviceInd, MgmtServerDeviceID, NetworkDeviceInd, ParentDeviceID, 
# VirtualInd, VirtualNetworkID.

# xml_filter: Optional Type: String
# A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.

# OUTPUTS
# devices Type: Array of Device
# An array of the Device objects that match the specified input criteria.
# Python: Returns an instance of the DeviceRemote object.

import argparse
import configparser
import pprint
from infoblox_netmri.client import InfobloxNetMRI as blox

# it's safe to ignore these two functions, they're just here for convenience.
def get_args(args=None):
    """Deal with command line arguments."""
    config_file = ""
    description = "An example of using the Device broker to search for a device by name but limiting fields returned with select()."
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
    broker = client.get_broker("Device")
    devices = ["nas01", "nas02"] # <-- Specify a list of device names that's valid in your environment here.
    device_results = broker.search(DeviceName=devices)
    # Important note on dereferencing: broker.search is going to return a List of DeviceRemote objects, 
    # so you'd probably want to iterate through the list and tweeze out the property(-ies) of interest
    # and stuff them into an interim structure.
    print("Showing DeviceMAC on results with no select() clause.")
    for thisresult in device_results: 
        print(thisresult.DeviceMAC)
    device_results = ""
    device_results = broker.search(DeviceName=devices, select="DeviceID,DeviceName")
    # Note that the object will retain all properties (e.g. fields) but only the fields specified in 
    # select() will have data published on them.
    print("These results have been limited to DeviceID and DeviceName, so printing DeviceMAC returns None.")
    for thisresult in device_results: 
        print(thisresult.DeviceMAC)
    
if __name__ == "__main__":
    main()
