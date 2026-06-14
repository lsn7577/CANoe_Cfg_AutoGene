# TCIL_AssignTransmitter

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_AssignTransmitter(dword ddi, dbNode user, dword elementNumberUser, dbNode source, dword elementNumberSource) // form 1
long TCIL_AssignTransmitter(dword ddi, dword addressUser, dword elementNumberUser, dword addressSource, dword elementNumberSource) // form 2
long TCIL_AssignTransmitter(dbNode tc, dword ddi, dbNode user, dword elementNumberUser, dbNode source, dword elementNumberSource) // form 3
long TCIL_AssignTransmitter(dbNode tc, dword ddi, dword addressUser, dword elementNumberUser, dword addressSource, dword elementNumberSource) // form 4
```

## Description

The functions sends an Assign Transmitter message to the setpoint value source device.

## Parameters

| Name | Description |
|---|---|
| ddi | This DDI and the element number specify the setpoint value user. |
| user | Peer control capable device which acts as a setpoint value user. |
| addressUser | Address of the peer control capable device which acts as a setpoint value user. |
| elementNumberUser | The combination of this element number and the DDI receives data from the setpoint value source. |
| source | Peer control capable device which acts as a setpoint value source. |
| addressSource | Address of the peer control capable device which acts as a setpoint value source. |
| elementNumberSource | The value of the process variable specified by combination of this element number and the DDI has to be sent to the setpoint value user. |
| tc | Task Controller simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 9.0 SP4: form 1, 3 13.0: form 2, 4 | 13.0 | — | — | 2.1 SP4: form 3 5.0: form 4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3, 4 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3, 4) | ✔ (form 3, 4) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
