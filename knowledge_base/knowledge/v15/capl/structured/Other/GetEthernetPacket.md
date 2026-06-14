# GetEthernetPacket

> Category: `Other` | Type: `function`

## Syntax

```c
long GetEthernetPacket(this, ethernetPacket packet);
```

## Description

This function can only be called inside of an on PDU handler. The function will return in its second parameter the Ethernet packet, the PDU was contained.

## Parameters

| Name | Description |
|---|---|
| this | Handle to the currently handled (received) PDU object. |
| packet | Reference to an Ethernet Packet object that will contain the overall received packet data and information. |

## Example

```c
on PDU PDU_B
{
  ethernetPacket aPacket_01;
  long result;
  result = GetEthernetPacket(this, aPacket_01); // PDU is assumed to be sent on ETH
  if (result == 0)
  {
    write("Received PDU 'PDU_B' in ETH packet with FCS %lu", aPacket_01.FCS);
  }
  else
  {
    write("Error accessing PDU!");
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP2 | 9.0 SP2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
