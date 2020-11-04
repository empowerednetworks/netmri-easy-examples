# Finding Stuff in NetMRI

## The API Reference

The NetMRI API is documented as a living document collection on the appliance itself. The API docs are available after authenticating to the system by selecting the Tools menu (wrench) from the upper-right of the main pane, selecting Network and API Documentation.  Alternately, after authenticating, duplicate the tab the main pane is displayed in and change the URL to https://your-netmri-instance/api/ to view the docs. The Python and Perl libraries are available from this page as well.

## Query Operations

One of the biggest reasons to write external scripts in NetMRI is to leverage the rich collection of data that exists in the system to confirm or enrich data in other monitoring and management systems.  It follows that the general category of "finding stuff" will be high on the list of things to do for an integration developer.  The API represents the only programmatic way to access the data in the system (that is, there's no direct SQL interface available.)

Generally, all the objects in NetMRI expose the same three query methods for finding stuff of that particular class. They work the same in each class, differing only in the specific properties that can be used to delimit the searches or that are returned from the operations.  In order of performance (best to worst) the methods are:

index - Lists the available "whatevers". Any of the inputs listed may be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

search - Lists the available "whatevers" matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

find - Lists the available "whatevers" matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. Generally, the docs will provide a list of field_names that can be targeted for matching.

find() provides the ability to match either against a _field name_ or a _constant value_.  To do this, there is usually a op_FieldName parameter and then a val_f_FieldName and a val_c_FieldName parameter.  op_FieldName defines what sort of comparison operator to use, the valid operators being "=, <>, rlike, not rlike, >, >=, <, <=, like,  not like, is null, is not null, between".  Only one of val_f_ or val_c_ can be specified and one __must__ be specified if op_ is provided.  

val_f_ applies the comparison operator to another field name in the data model.  You might use this with the various timestamps on a record.  Consider the Device model as an example, which exposes the properties DeviceStartTime and DeviceEndTime.  If it were required to find all the devices where DeviceStartTime and DeviceEndTime were the same, op_DeviceStartTime could be set to "=" and then val_f_DeviceStartTime could be set to "DeviceEndTime" which would mean "give me all the records where DeviceStartTime = DeviceEndTime."

val_c_ applies the comparison operator to a user-specified value.  Say you wanted to find all the devices where the vendor was Juniper.  Set op_DeviceVendor to "like" and val_c_DeviceVendor to "Jun%" to provide the needed list.  Note in this example the use of the "%" as a wildcard; the API is a very thin wrapper over the internal database, so use SQL-style wildcards when required.

There will usually be a "show" method provided as well that will take an ID and return a specific record.

show - Shows the details for the specified "whatever."

## Limiting Results

When results are returned, the objects usually return all available fields.  This may be unnescessary if only a small set of the fields are needed for a particular operation, and in that case, best practice will be to limit the fields returned.  Generally, all the objects provide a select() operator that specifies what fields to return.

In spite of the docs assertion that select() takes an Array, in Python it's just a comma-delimited string.  As an example: 

```
device_results = broker.search(DeviceName=devices, select="DeviceID,DeviceName")
```

Note that when using the infoblox_netmri library, the returned object will be created with all of the properties (fields), not just the set that are specified in select(), however _only_ the fields specified will contain data, while all others will contain None.

## Pagination

Some of the collections in NetMRI are really big; Interface as an example has one record for each physicial interface on each device in the network.  Clearly in even a small network, this could be thousands or tens of thousands of records.  To handle large return sets, NetMRI implements pagination with the start() and limit() operators.

start Optional Integer, Default: 0
The record number to return in the selected page of data. It will always appear, although it may not be the first record.

limit Optional Integer, __Default: 1000__
The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. __The maximum limit is 10000.__

There is, unfortunately, not an operator to get the total number of entries that's native to library.  However, doing a raw GET on index() via requests will yield a JSON object that looks like this:

```
{
    "total": 510, 
    "start": 0, 
    "limit": 1000, 
    "current": 510, 
    "interfaces": [ . . . ]
}
```

The "total" value represents the total collection so with that, it's trivial to build a chunker to return results in whatever page sizes that are desired:

```
import requests

def chunker():
    params = {
                "op_DeviceVendor": "like",
                "val_c_DeviceVendor": "Jun%",
                "select": "DeviceID,DeviceName",
            }
    url = "https://my-netmri/api/3.5/interfaces/index"
    response = requests.get(url, params=params) # authentication, 
                                                # certificate validation
                                                # omitted for brevity.
    if response:
        total_records = response.json()["total"]
    limit = 100
    start = 0
    current = 0

    while current < total_records:
        current += limit # imcrement by limit on each pass.
        interfaces_results = broker.index(start=start, limit=limit)
        (do . . . stuff)
        start = current
```

## Sorting Results:

Results are returned in storage order (whatever order they are in the database, generally oldest to newest but order is not guaranteed.)  If it's desired to return them in a specific order, the API provides the sort() and dir() operators. The default sort field for a particular type is found in the docs for sort() for the type. Again in python even though the docs say "Array" they mean "comma-delimited string."

sort: Optional Type: Array of String
The data field(s) to use for sorting the output. 

dir: Optional Type: Array of String
The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.

## Worked Examples:

notifications-index.py - shows an example of using the index() method 
                         against Notifications (which are              
                         kinda misnamed.  They represent configurations for notifications to other systems
                         by email, SNMP trap or Syslog message.)

devices-search.py - shows an example of using the search() method to search 
                    for Devices by name.

events-find.py - shows an example of using the index() method to search for Events by type using the op_ and val_c_ 
                 operators.

devices-search-and-select.py - An example of using the Device broker to 
                               search for a device by name but limiting 
                               fields returned with select().

interfaces-paging.py - An example of using pagination.
