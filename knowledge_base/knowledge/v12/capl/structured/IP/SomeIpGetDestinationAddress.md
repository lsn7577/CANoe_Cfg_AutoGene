# SomeIpGetDestinationAddress

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetDestinationAddress ( dword messageHandle ); // form 1
```

## Description

This function returns the IPv4 destination address.

## Parameters

| Name | Description |
|---|---|
| Note This function can only be called within the OnSomeIpMessage callback function. |  |

## Return Values

IPv4 destination address (Network Byte Order)
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.
Note
The IpGetAddressAsString function can be used to convert the numerical return value to a character string in shorthand notation.

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD dstAddress    = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;
  char  buffer[100];

  // get data from SOME/IP message
  if((dstAddress = SomeIpGetDestinationAddress(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = SomeIpGetLastError()) != 0)
    {
       write("SOME/IP IL error occured: Error code: %d", errorCode);
       errorOccured = 1;
    } // if
  } // if

  if(errorOccured == 0)
  {
    IpGetAddressAsString(dstAddress, buffer, elcount(buffer));
    write("SOME/IP message received. Destination address: %s",buffer);
  } // if
}
```

## Availability

| Since Version |
|---|
