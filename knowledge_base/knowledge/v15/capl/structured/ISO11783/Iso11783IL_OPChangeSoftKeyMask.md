# Iso11783IL_OPChangeSoftKeyMask

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangeSoftKeyMask( dword maskID, dword softKeyMaskID ); // form 1
long Iso11783IL_OPChangeSoftKeyMask( dword maskType, dword maskID, dword softKeyMaskID ); // form 2
long Iso11783IL_OPChangeSoftKeyMask( dbNode implement, dword maskType, dword maskID, dword softKeyMaskID ); // form 3
```

## Description

The function changes the soft key mask of a data mask. A Change Soft Key Mask command is sent to the Virtual Terminal.

If parameter maskType is not used the mask type is determined by the mask object.

## Parameters

| Name | Description |
|---|---|
| maskID | object ID of the data mask |
| softkeyMaskID | object ID of the data mask |
| maskType | type of mask 1: data mask 2: alarm mask |
| implement | Simulation node to apply the function. |

## Example

```c
Iso11783IL_OPChangeSoftKeyMask( 1000, 1050 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0: form 1 8.5 SP3: form 2 9.0: form 3 | 13.0 | — | — | 2.1 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 3 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1, 2) | ✔ (form 1, 2) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 3) | ✔ (form 3) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 3) | ✔ (form 3) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
