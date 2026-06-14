# DoIP_SetLocalIPaddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long DoIP_SetLocalIPaddress(char ipAddress[]);
```

## Description

Set local IP address to bind to. In an ECU simulation, Vehicle Announcement Messages (VAM) will be sent from this IP address, in a tester node the Vehicle Identification Request (VIR) messages. If the tester node sets IP address in on prestart, it can receive VAMs even before it sends VIR messages itself. The target IP address is derived from this IP address: for an IPv4 address the broad-cast address is determined using the network mask, for an IPv6 address the multicast address is used.

If diagnostics communication is performed on a built-in channel (i.e. the tester node does not configure DoIP.DLL as a node-layer module), this function cannot be used. The address configured in the CANoe Vehicle Simulation Parameter area is used instead.

## Return Values

0: Success

## Example

```c
DoIP_SetLocalIPaddress( "10.10.10.222"); // Set an IPv4 address
...
DoIP_SetLocalIPaddress( "2001::2222");   // Set an IPv6 address
...
// retrieve the IP address configured for this simulation node's TCP/IP stack
ipGetAdapterAddressAsString( 1, localAddr, elcount(localAddr));
// and use it as local address
DoIP_SetLocalIPaddress( localAddr);
```

## Availability

| Since Version |
|---|
