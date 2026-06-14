# OnIpAddressAdded

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
void OnIpAddressAdded(dword ifIndex, ip_address address, dword prefix, dword origin);
```

## Description

If the CAPL program implements this callback it is called when a new address is added to a network interface.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. |
| address | The added IP address. |
| prefix | The prefix of the added address. It defines the number of bits belonging to the network part of the address. |
| origin | Defines the initiator for adding this address. Possible values are: ORIGIN_UNKNOWN = 0, ORIGIN_USER = 1, ORIGIN_SYSTEM = 2, ORIGIN_DHCPv4CLIENT = 3, ORIGIN_DHCPv6CLIENT = 4, ORIGIN_RFC3927CLIENT = 5 |

## Return Values

—

## Example

```c
void OnIpAddressAdded(dword ifIndex, ip_Address address, dword prefix, dword origin)
{
  char addrString[50];
  char originNames[6][25] = {"ORIGIN_UNKNOWN", "ORIGIN_USER", "ORIGIN_SYSTEM", "ORIGIN_DHCPv4CLIENT", "ORIGIN_DHCPv6CLIENT", "ORIGIN_RFC3927CLIENT"};
  address.PrintAddressToString(addrString);
  snprintf(addrString, elcount(addrString), "%s/%d", addrString, prefix);
  write("added ip address: %s to adapter nr: %d. Origin: %s", addrString, ifIndex, originNames[origin]);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
