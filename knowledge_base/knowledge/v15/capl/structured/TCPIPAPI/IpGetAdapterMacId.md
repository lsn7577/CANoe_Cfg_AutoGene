# IpGetAdapterMacId

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetAdapterMacId( dword ifIndex, byte macId[]); // form 1
qword IpGetAdapterMacId( dword ifIndex ); // form 2
```

## Description

The function returns the MAC ID of the given interface.

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. All adapter addresses including the local loopback address are taken into account in the stack of the operating system. The order depends on how the operating system lists the adapters.All assigned addresses including the VLAN addresses are taken into account in the CANoe stack. |
| macId | A byte array of 6 bytes size to return the MAC ID. |

## Example

```c
on start
{
  long result;
  long ifIndex;
  char adapterDesc[255];
  byte macId[6];

  ifIndex = 1;

  result = ipGetAdapterDescription(ifIndex, adapterDesc, elcount(adapterDesc));
  if( result != 0 )
  {
    writeLineEx(1, 3, "Failed to get the adapter description. Result: %d", result);
  }

  result = IpGetAdapterMacId(ifIndex, macId);
  if( result != 0 )
  {
    writeLineEx(1, 3, "Failed to get the adapter MAC ID. Result: %d", result);
  }
  else
  {
    writeLineEx(1, 0, "The Mac Id of Adapter %s is %02x:%02x:%02x:%02x:%02x:%02x",
    adapterDesc, macId[0], macId[1], macId[2], macId[3], macId[4], macId[5]);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5: form 1 12.0: form 2 | 8.2 SP2: form 1 12.0: form 2 | 13.0 | 13.0: form 2 | — | 2.0 SP2: form 1 4.0: form 2 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
