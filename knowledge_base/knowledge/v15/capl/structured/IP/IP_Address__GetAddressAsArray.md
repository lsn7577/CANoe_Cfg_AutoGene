# IP_Address::GetAddressAsArray

> Category: `IP` | Type: `method`

## Syntax

```c
long IP_Address::GetAddressAsArray(byte ipAddr[]); // form 1
long IP_Address::GetAddressAsArray(char ipAddr[]); // form 2
```

## Description

Copies the current IP address to the byte array whereas the byte array's size needs to fit the current IP address value.

## Example

```c
on start
{
  IP_Address FC00::0001 addr;
  byte addrData[16];

  if(addr.SetAddressAsArray( addrData ) == 0)
  {
    // do something with addrData
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 12.0 | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
