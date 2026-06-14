# Iso11783IL_EnableAddressViolationDetection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_EnableAddressViolationDetection( dword numberOfDM1Transmissions); // form 1
long Iso11783IL_EnableAddressViolationDetection( dbNode node, dword numberOfDM1Transmissions); // form 2
```

## Description

Activates detection of address violations by other nodes.

Address violation means that a message is registered on the bus with the source address of the simulated node that was not sent by the simulated node itself.

If an address violation is detected, the simulated node sends an Address Claimed message. If diagnostics support is activated (via ISO11783IL_ActivateDiagnosticsSupport) then the node also sends DM1 with SPN=2000+nodeAddress, FMI=31 and OC=1.

This behavior can be influenced by implementing the function Iso11783IL_OnAddressViolation.

## Parameters

| Name | Description |
|---|---|
| numberOfDM1Transmissions | 0..0xFFFFFFFF: activates the detection of address violations 0: deactivates detection of address violations If value is >0 and an address violation is detected and diagnostics support is activated then message DM1 is sent numberOfDM1Transmissions times. If numberOfDM1Transmissions is 0xFFFFFFFF then sending of DM1 is not stopped. |
| node | Simulation node to apply the function. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 SP4 | 13.0 | — | — | 4.0 SP4 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
