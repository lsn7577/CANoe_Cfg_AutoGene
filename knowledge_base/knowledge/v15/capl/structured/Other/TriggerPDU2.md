# TriggerPDU2

> Category: `Other` | Type: `function`

## Syntax

```c
long triggerPDU2(pdu PDUObject, dword DestBusContext, char[] DBName,char[] TXNode, char[] PDUName, dword ShortHeaderID, dword LongHeaderID, dword Flags, dword PayloadLen);
```

## Description

This function forwards a received PDU to another Network. The destination PDU can be changed. For gateway applications this function can be useful.

## Parameters

| Name | Description |
|---|---|
| PDUObject | PDU object to be transmitted. |
| DestBusContext | bus context of the destination network where the pdu is to be sent |
| DBName | Name of the cluster in the database |
| TXNode | Name of the transmitter node, can be used with empty string also |
| PDUName | Name of the PDU to be transmitted. |
| ShortHeaderID | ID of the PDU to be transmitted. 0 means not configured |
| LongHeaderID | ID of the PDU to be transmitted. 0 means not configured |
| Flags | reserved, 0 means not configured |
| PayloadLen | Length of Payload in Byte |

## Example

```c
variables
{
  dword dstBusContext;
}
on preStart
{
  dstBusContext = GetBusNameContext("GWout");
  write("GWout = %d", dstBusContext);
  write("GWin  = %d", GetBusNameContext("GWin"));
}
on PDU msgchannel1.*
{
  long result;
  pdu * out;

if((this.MsgChannel == 1) && (this.BusType == 1 /* CAN */))
  {
    result = TriggerPDU2(this, dstBusContext, "BODY3" /* DBName */, "" /* TXNode */, this.Name /* PDUName */, this.ShortHeaderID, this.LongHeaderID, 0, this.PduLength);
    writeLineEx(-3, 1, "Trigger (bridge) PDU '%s' onto bus (Channel %d, BusType %d) returned %d.", this.Name (dstBusContext & 0xFFFF), (dstBusContext >> 16), result);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 SP2 | 10.0 SP2 | 13.0 | — | — | 2.2 SP1 |
| Restricted To | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs FlexRay AUTOSAR PDUs | — | — | CAN AUTOSAR PDUs Ethernet AUTOSAR PDUs |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ (CAN) — (Ethernet) | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
