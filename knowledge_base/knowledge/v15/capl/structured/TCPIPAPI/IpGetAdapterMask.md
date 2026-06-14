# IpGetAdapterMask

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterMask( dword ifIndex, dword mask[], dword maskSize); // form 1
long IpGetAdapterMask( dword ifIndex, IP_Address addressMasks[], dword &count); // form 2
```

## Description

The function retrieves the address masks (subnet masks) associated with the specified network interface.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| maskSize | The size of the mask array. |
| count | The size of the mask array. |
| mask | The array used to store the numerical IPv4 address masks. |
| addressMasks | Address masks are copied to this array. |

## Example

```c
on start
{
  IP_Address addresses[10];
  dword addressesCount;
  IP_Address addrMasks[10];
  dword addrMasksCount;
  long addrIdx;
  long ifIdx;

  write( "IP Configuration" );

  for( ifIdx = 1; ifIdx <= ipGetAdapterCount(); ifIdx++)
  {
    ipGetAdapterAddress( ifIdx, addresses, addressesCount );
    ipGetAdapterMask( ifIdx, addrMasks, addrMasksCount );

    for( addrIdx = 0; addrIdx < addressesCount; addrIdx++ )
    {
      char addrStr[30];
      char maskStr[30];
      addresses[addrIdx].PrintAddressToString( addrStr );
      addrMasks[addrIdx].PrintAddressToString( maskStr );

      write( "  %d. %s | %s", addrIdx+1, addrStr, maskStr );
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1 12.0: form 2 | 7.0: form 1 12.0: form 2 | 13.0 | 13.0: form 2 | — | 2.0 SP2: form 1 4.0: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
