# coTfsSetSdoCANid

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSetSdoCANid( dword sdoClnRxId, dword sdoClnTxId );
```

## Description

With this function the internal the CAN identifiers to be used for the SDO tests are set. All test functions, which uses SDO access, will use the specified identifiers. This setting will override the application profile specific SDO id settings.

## Parameters

| Name | Description |
|---|---|
| sdoClnRxId | CAN-ID for receive SDOs. |
| sdoClnTxId | CAN-ID for send SDOs. |

## Return Values

Error code

## Example

```c
coTfsSetSdoCANid(0x580, 0x602); // set internal CAN-ID for Rx SDOs to 0x580 and for Tx SDOs to 0x602
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
