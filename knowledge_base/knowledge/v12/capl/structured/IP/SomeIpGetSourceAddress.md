# SomeIpGetSourceAddress

> Category: `IP` | Type: `function`

## Syntax

```c
dword SomeIpGetSourceAddress ( dword messageHandle ); // form 1
```

## Description

This function returns the IPv4 sender address.

## Parameters

| Name | Description |
|---|---|
| Note This function can only be called within the OnSomeIpMessage callback function. |  |

## Return Values

IPv4 sender address (Network Byte Order) as numeric value.
In the Event of an error, the function returns the value 0. The SomeIpGetLastError function can then be used to check whether the value is valid or an error has occurred.
Note
The IpGetAddressAsString function can be used to convert the numerical return value to a character string in shorthand notation.

## Example

```c
void OnSomeIpMessage( DWORD messageHandle )
{
  DWORD srcAddress    = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;
  char  buffer[100];

  // get data from SOME/IP message
  if((srcAddress = SomeIpGetSourceAddress(messageHandle)) == 0)
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
    IpGetAddressAsString(srcAddress, buffer, elcount(buffer));
    write("SOME/IP message from source address %s received",buffer);
  } // if
}
```

## Availability

| Since Version |
|---|
