# applILTxRequestPending

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
void applILTxRequestPending ( );
```

## Description

If the IL clamp 15 state (for ASR PDU ILIgnition state) is being enabled by ILActivateClamp15 (for ASR PDU IL ARILSetIgnitionState) or any wake-up-allowed signal is changed, then optionally this functions is called. Within this function the bus should be requested by the network management DLL.

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.0 SP2 | 14 | 14 | — | — |
| Restricted To | — | CAN Ethernet (since version 9.0) FlexRay (since version 9.0) | CAN Ethernet FlexRay | CAN Ethernet FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
