#!/usr/bin/env python3
"""An example of using the Event broker to get a list of events."""

# Reference:
# broker.find
# Lists the available events matching the input specification. This provides the most flexible search 
# specification of all the query mechanisms, enabling searching using comparison operations other than equality. 
# However, it is more complex to use and will not perform as efficiently as the index or search methods. 
# In the input descriptions below, 'field names' refers to the following fields: DataSourceID, EventCategory, 
# EventCategoryID, EventDetail, EventID, EventState, EventTimestamp, EventType.

# INPUTS
# op_DataSourceID: Optional Type: String
# The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, 
# not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for the collector NetMRI 
# that collected this data record. For the between operator the value will be treated as an Array if comma 
# delimited string is passed, and it must contain an even number of values.

# val_f_DataSourceID: Optional Type: String
# If op_DataSourceID is specified, the field named in this input will be compared to the value in DataSourceID 
# using the specified operator. That is, the value in this input will be treated as another field name, rather 
# than a constant value. Either this field or val_c_DataSourceID must be specified if op_DataSourceID is specified.

# val_c_DataSourceID: Optional Type: String
# If op_DataSourceID is specified, this value will be compared to the value in DataSourceID using the specified 
# operator. The value in this input will be treated as an explicit constant value. Either this field or 
# val_f_DataSourceID must be specified if op_DataSourceID is specified.

# op_EventCategory: Optional Type: String
# The operator to apply to the field EventCategory. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, 
# like, not like, is null, is not null, between. EventCategory: The category of an event. For the between operator 
# the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of 
# values.

# val_f_EventCategory: Optional Type: String
# If op_EventCategory is specified, the field named in this input will be compared to the value in EventCategory 
# using the specified operator. That is, the value in this input will be treated as another field name, rather 
# than a constant value. Either this field or val_c_EventCategory must be specified if op_EventCategory 
# is specified.

# val_c_EventCategory: Optional Type: String
# If op_EventCategory is specified, this value will be compared to the value in EventCategory using the 
# specified operator. The value in this input will be treated as an explicit constant value. Either this field 
# or val_f_EventCategory must be specified if op_EventCategory is specified.

# op_EventCategoryID: Optional Type: String
# The operator to apply to the field EventCategoryID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, 
# like, not like, is null, is not null, between. EventCategoryID: The internal NetMRI identifier of a category 
# in an event. For the between operator the value will be treated as an Array if comma delimited string is 
# passed, and it must contain an even number of values.

# val_f_EventCategoryID: Optional Type: String
# If op_EventCategoryID is specified, the field named in this input will be compared to the value in 
# EventCategoryID using the specified operator. That is, the value in this input will be treated as another 
# field name, rather than a constant value. Either this field or val_c_EventCategoryID must be specified if 
# op_EventCategoryID is specified.

# val_c_EventCategoryID: Optional Type: String
# If op_EventCategoryID is specified, this value will be compared to the value in EventCategoryID using 
# the specified operator. The value in this input will be treated as an explicit constant value. Either this 
# field or val_f_EventCategoryID must be specified if op_EventCategoryID is specified.

# op_EventDetail: Optional Type: String
# The operator to apply to the field EventDetail. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, 
# like, not like, is null, is not null, between. EventDetail: The detail of an event. For the between operator 
# the value will be treated as an Array if comma delimited string is passed, and it must contain an even number 
# of values.

# val_f_EventDetail: Optional Type: String
# If op_EventDetail is specified, the field named in this input will be compared to the value in EventDetail 
# using the specified operator. That is, the value in this input will be treated as another field name, rather 
# than a constant value. Either this field or val_c_EventDetail must be specified if op_EventDetail is specified.

# val_c_EventDetail: Optional Type: String
# If op_EventDetail is specified, this value will be compared to the value in EventDetail using the specified 
# operator. The value in this input will be treated as an explicit constant value. Either this field or 
# val_f_EventDetail must be specified if op_EventDetail is specified.

# op_EventID: Optional Type: String
# The operator to apply to the field EventID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, 
# not like, is null, is not null, between. EventID: The internal NetMRI identifier of an event. For the between 
# operator the value will be treated as an Array if comma delimited string is passed, and it must contain an 
# even number of values.

# val_f_EventID: Optional Type: String
# If op_EventID is specified, the field named in this input will be compared to the value in EventID using 
# the specified operator. That is, the value in this input will be treated as another field name, rather than 
# a constant value. Either this field or val_c_EventID must be specified if op_EventID is specified.

# val_c_EventID: Optional Type: String
# If op_EventID is specified, this value will be compared to the value in EventID using the specified operator. 
# The value in this input will be treated as an explicit constant value. Either this field or val_f_EventID 
# must be specified if op_EventID is specified.

# op_EventState: Optional Type: String
# The operator to apply to the field EventState. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, 
# not like, is null, is not null, between. EventState: The state of an event. For the between operator the 
# value will be treated as an Array if comma delimited string is passed, and it must contain an even number of 
# values.

# val_f_EventState: Optional Type: String
# If op_EventState is specified, the field named in this input will be compared to the value in EventState using 
# the specified operator. That is, the value in this input will be treated as another field name, rather than a 
# constant value. Either this field or val_c_EventState must be specified if op_EventState is specified.

# val_c_EventState: Optional Type: String
# If op_EventState is specified, this value will be compared to the value in EventState using the specified 
# operator. The value in this input will be treated as an explicit constant value. Either this field or 
# val_f_EventState must be specified if op_EventState is specified.

# op_EventTimestamp: Optional Type: String
# The operator to apply to the field EventTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, 
# not like, is null, is not null, between. EventTimestamp: The date and time this record was collected. 
# For the between operator the value will be treated as an Array if comma delimited string is passed, 
# and it must contain an even number of values.

# val_f_EventTimestamp: Optional Type: String
# If op_EventTimestamp is specified, the field named in this input will be compared to the value in 
# EventTimestamp using the specified operator. That is, the value in this input will be treated as another 
# field name, rather than a constant value. Either this field or val_c_EventTimestamp must be specified if 
# op_EventTimestamp is specified.

# val_c_EventTimestamp: Optional Type: String
# If op_EventTimestamp is specified, this value will be compared to the value in EventTimestamp using the 
# specified operator. The value in this input will be treated as an explicit constant value. Either this field or 
# val_f_EventTimestamp must be specified if op_EventTimestamp is specified.

# op_EventType: Optional Type: String
# The operator to apply to the field EventType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, 
# not like, is null, is not null, between. EventType: The type of an event. For the between operator the value 
# will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.

# val_f_EventType: Optional Type: String
# If op_EventType is specified, the field named in this input will be compared to the value in EventType 
# using the specified operator. That is, the value in this input will be treated as another field name, 
# rather than a constant value. Either this field or val_c_EventType must be specified if op_EventType is 
# specified.

# val_c_EventType: Optional Type: String
# If op_EventType is specified, this value will be compared to the value in EventType using the specified 
# operator. The value in this input will be treated as an explicit constant value. Either this field or 
# val_f_EventType must be specified if op_EventType is specified.

# DeviceGroupID: Optional Type: Array of Integer
# The internal NetMRI identifier of the device groups to which to limit the results.

# starttime: Optional Type: DateTime
# The data returned will represent the events with this date and time as lower boundary. If omitted, the result 
# will indicate the most recently collected data.

# endtime: Optional Type: DateTime
# The data returned will represent the events with this date and time as upper boundary. If omitted, the result 
# will indicate the most recently collected data.

# methods: Optional Type: Array of String
# A list of event methods. The listed methods will be called on each event returned and included in the output. 
# Available methods are: data_source.

# include: Optional Type: Array of String
# A list of associated object types to include in the output. The listed associations will be returned as 
# outputs named according to the association name (see outputs below). Available includes are: data_source.

# start: Optional Type: Integer
# The record number to return in the selected page of data. It will always appear, although it may not be the 
# first record. See the :limit for more information.

# limit: Optional Type: Integer
# The size of the page of data, that is, the maximum number of records returned. The limit size will be used 
# to break the data up into pages and the first page with the start record will be returned. So if you have 
# 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.

# sort: Optional Type: Array of String
# The data field(s) to use for sorting the output. Default is EventID. Valid values are EventID, DataSourceID, 
# EventCategory, EventCategoryID, EventType, EventTimestamp, EventState, EventDetail.

# dir: Optional Type: Array of String
# The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.

# select: Optional Type: Array
# The list of attributes to return for each Event. Valid values are EventID, DataSourceID, EventCategory, 
# EventCategoryID, EventType, EventTimestamp, EventState, EventDetail. If empty or omitted, 
# all attributes will be returned.

# goto_field: Optional Type: String
# The field name for NIOS GOTO that is used for locating a row position of records.

# goto_value: Optional Type: String
# The value of goto_field for NIOS GOTO that is used for locating a row position of records.

# xml_filter: Optional Type: String
# A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query 
# or field values, but before any limit options. The limit and pagination will be enforced after the filter. 
# Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.

# OUTPUTS
# events Type: Array of Event
# An array of the Event objects that match the specified input criteria.

import argparse
import configparser
from infoblox_netmri.client import InfobloxNetMRI as blox

# it's safe to ignore these two functions, they're just here for convenience.
def get_args(args=None):
    """Deal with command line arguments."""
    config_file = ""
    description = "An example of using the Event broker to get a list of events."
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
    broker = client.get_broker("Event")
    event_results = broker.find(op_EventCategory="=", val_c_EventCategory="SystemAlert") 
    # Important note on dereferencing: broker.search is going to return a List of NotificationRemote objects, 
    # so you'd probably want to iterate through the list and tweeze out the property(-ies) of interest
    # and stuff them into an interim structure.
    for thisresult in event_results:
        print(thisresult.EventCategory, thisresult.EventType, thisresult.EventTimestamp)

    
if __name__ == "__main__":
    main()
