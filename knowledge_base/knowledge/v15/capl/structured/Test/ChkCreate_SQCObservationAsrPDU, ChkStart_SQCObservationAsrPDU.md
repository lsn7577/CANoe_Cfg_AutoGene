# ChkCreate_SQCObservationAsrPDU, ChkStart_SQCObservationAsrPDU

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_SQCObservationAsrPDU(PDU aPDU);
dword ChkStart_SQCObservationAsrPDU(PDU aPDU);
dword ChkCreate_SQCObservationAsrPDU(PDU aPDU, char [] signalGroup);
dword ChkStart_SQCObservationAsrPDU(PDU aPDU, char [] signalGroup);
dword ChkCreate_SQCObservationAsrPDU(long aHeaderId);
dword ChkStart_SQCObservationAsrPDU(long aHeaderId);
dword ChkCreate_SQCObservationAsrPDU(long aHeaderId, char [] signalGroup);
dword ChkStart_SQCObservationAsrPDU(long aHeaderId, char [] signalGroup);
```

## Description

Monitors the SQC of a PDU or a single signal group of a PDU. The check condition is violated if the last SQC does not match to the current contained in the PDU or signal group. The check can be set up for a single PDU or a single signal group within a PDU.

The functions/constructors without the parameter signalGroup monitors all specified SQC's within the given PDU.

The numeric functions/constructors with the parameter aHeaderId cannot be used for FlexRay.

## Parameters

| Name | Description |
|---|---|
| aPDU | Must exist in DB |
| aHeaderId | PDU header ID to be observed. The corresponding PDU shall be defined in the database. |
| signalGroup | Signal group with SQC to be observed. |

## Example

```c
// checks the payload gaps of the message
checkId = ChkStart_SQCObservationAsrPDU (PDUToObserve, “signalGroup1”);
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 SP2 | 13.0 | — | 14 | 3.0 SP2 |
| Restricted To | — | PDU network | PDU network | — | PDU network | PDU network |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
