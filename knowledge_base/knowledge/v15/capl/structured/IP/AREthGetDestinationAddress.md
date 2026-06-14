# AREthGetDestinationAddress

> Category: `IP` | Type: `function`

## Syntax

```c
dword AREthGetDestinationAddress ( dword messageHandle ); // form 1
long AREthGetDestinationAddress ( dword messageHandle, byte ipv6Address[] ); // form 2
```

## Description

This function returns the IPv4 destination address.

## Parameters

| Name | Description |
|---|---|
| Note This function can only be called within the OnAREthMessage callback function. |  |
| ipv6Address | The parameter to which the IPv6 address will be written to. |

## Return Values

IPv4 destination address (Network Byte Order)
In the Event of an error, the function returns the value 0. The AREthGetLastError function can then be used to check whether the value is valid or an error has occurred.

## Example

```c
void OnAREthMessage( dword messageHandle )
{
  dword dstAddress    = 0;
  LONG  errorCode     = 0;
  LONG  errorOccured  = 0;
  char  buffer[100];

  // get data from SOME/IP message
  if((dstAddress = AREthGetDestinationAddress(messageHandle)) == 0)
  {
    // check if last function was executed correct
    if((errorCode = AREthGetLastError()) != 0)
    {
       write("AUTOSAR Eth IL error occured: Error code: %d", errorCode);
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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP2: form 1 10.0 SP4: form 2 | — | — | — | 2.1 SP3: form 1 2.2 SP4: form 2 |
| Restricted To | — | Ethernet | — | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
