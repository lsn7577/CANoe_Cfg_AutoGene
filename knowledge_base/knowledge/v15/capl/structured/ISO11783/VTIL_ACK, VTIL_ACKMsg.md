# VTIL_ACK, VTIL_ACKMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_ACK(dword duration ); // form 1
long VTIL_ACK(dbNode vt, dword duration); // form 2
long VTIL_ACKMsg(dword objectId, dword keyActivationCode); // form 3
long VTIL_ACKMsg (dbNode vt, dword objectId, dword keyActivationCode); // form 4
```

## Description

Simulates the press of the ACK means of the Virtual Terminal. As a result, the Soft Key Activation message is immediately sent to the active Working Set with key activation code = pressed, then every 200 ms with the key activation code = still held and after the duration with the key activation code = released.

The VTIL_ACKMsg methods only send the Soft Key Activation message to the active Working Set (without triggering any event in the Virtual Terminal). In the sent Soft Key Activation messages the object ID of the Key object is always 0xFFFF and the key number is always 0.

## Parameters

| Name | Description |
|---|---|
| vt | VT simulation node to apply the function. |
| objectId | Object ID of visible Data Mask or Alarm Mask. |
| duration | Time while the ACK is held [ms]. If duration is < 200 ms then the commands Key has been pressed and Key has been released are sent. Else the command Key is still pressed is sent too. |
| keyActivationCode | 0: Key has been released (state change) 1: Key has been pressed (state change) 2: Key is still pressed 3: Key press aborted |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP5 | 13.0 | — | — | 2.2 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 3) | ✔ (form 1, 3) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2, 4) | ✔ (form 2, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
