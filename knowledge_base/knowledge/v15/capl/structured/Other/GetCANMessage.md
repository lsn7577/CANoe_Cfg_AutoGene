# GetCANMessage

> Category: `Other` | Type: `function`

## Syntax

```c
long GetCANMessage(this, message * msg);
```

## Description

This function can only be called inside of an on PDU handler. The function will return in its second parameter the CAN (or CAN-FD) frame, the PDU was contained.

## Parameters

| Name | Description |
|---|---|
| this | Handle to the currently handled (received) PDU object. |
| msg | Reference to a message object that will contain the overall received message data and information. |

## Example

```c
on PDU PDU_A
{
  message * aMsg_01;
  long result;
  result = GetCANMessage(this, aMsg_01); // PDU is assumed to be sent on CAN
  if (result == 0)
  {
    write("Received PDU 'PDU_A' in message with CAN ID %lu", aMsg_01.ID);
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
