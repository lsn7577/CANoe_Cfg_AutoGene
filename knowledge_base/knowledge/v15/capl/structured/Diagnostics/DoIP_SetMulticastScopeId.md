# DoIP_SetMulticastScopeId

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetMulticastScopeId(dword scopeId);
```

## Description

Sets an IPv6 address scope ID for multicast requests, sent by a tester. The scope ID is equal to an adapter index of the tester node. See ipGetAdapter functions for more information.

The function allows to select an appropriate adapter for IPv6 multicast address, to be able, for example, to send multicast requests with a given VLAN tag.

## Parameters

| Name | Description |
|---|---|
| scopeId | Scope ID for selection of a network adapter for IPv6 multicast requests. |

## Return Values

—

## Example

```c
// returns TCP/IP adapter index for the given IP address
dword GetTCPIPAdapterScopeId(char ipAddr[])
{
  dword adapterCount;
  dword adapterIndex;

  dword addressCount;
  dword addressIndex;

  IP_Address ipAddresses[16];
  char ipAddressString[256];

  adapterCount = ipGetAdapterCount();
  for(adapterIndex = 1; adapterIndex <= adapterCount; adapterIndex++)
  {
    ipGetAdapterAddress(adapterIndex, ipAddresses, addressCount);
    for(addressIndex = 0; addressIndex < addressCount; addressIndex++)
    {
      ipAddresses[addressIndex].PrintAddressToString(ipAddressString);
      if(strncmp(ipAddr, ipAddressString, strlen(ipAddr)) == 0)
        return adapterIndex;
    }
  }

return 0;
}

// identify the adapter scope ID for the tester IP address
// set it for sending multicast requests in corresponding network
dword scopeId;
scopeId = GetTCPIPAdapterScopeId(testerIPaddr);
DoIP_SetMulticastScopeId(scopeId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP2 | — | — | — | 4.0 SP2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
