# Iso11783IL_DelayRxMessage

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_DelayRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue, dword delay); // form 1
long Iso11783IL_DelayRxMessage(dword pgn, dword sourceAddress, qword filterMask, qword filterValue, dword delay, char sysVarNameWithPath[]); // form 2
long Iso11783IL_DelayRxMessage(dbNode node, dword pgn, dword sourceAddress, qword filterMask, qword filterValue, dword delay); // form 3
long Iso11783IL_DelayRxMessage(dbNode node, dword pgn, dword sourceAddress, qword filterMask, qword filterValue, dword delay, char sysVarNameWithPath[]); // form 4
```

## Description

A message described in the function is only forwarded to the simulation node after the defined delay. As a result, the simulated node reacts to the message only after this delay.

You can also define a system variable which is set if the specified message is received.

To revert this command you can use Iso11783IL_ResetDelayedRxMessage or Iso11783IL_ResetAllDelayedRxMessage.

## Parameters

| Name | Description |
|---|---|
| pgn | Parameter Group Number (with data page) of the message to be delayed. |
| sourceAddress | Source address of the message to be delayed (or 0xFFFFFFFF if the source address is to be ignored). |
| filterMask | Defines the bits of the first 8 Bytes of the message payload which shall be used to identify (filter) the message. Use value 0 if you don’t want to filter by message payload. |
| filterValue | Defines the value of the bits of the first 8 bytes of the message payload which shall be used to identify (filter) the message. If the value of the bits of a received message identified by filterMask is equal to this value, this message is delayed. |
| sysVarNameWithPath | Name of a system variable (all name spaces inclusive) which is set to 1 if the specified message is received. You can specify an empty string if no system variable shall be used. |
| delay | Delay in [ms]. After this delay the message is forwarded to the simulated node. If delay is 0 then the message is forwarded without any delay (e.g. if you only want to wait for the message using the specified system variable and the function testWaitForSysVar). |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
