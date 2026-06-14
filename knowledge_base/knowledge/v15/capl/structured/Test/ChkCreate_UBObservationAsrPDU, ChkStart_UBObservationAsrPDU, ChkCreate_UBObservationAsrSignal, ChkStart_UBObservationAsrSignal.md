# ChkCreate_UBObservationAsrPDU, ChkStart_UBObservationAsrPDU, ChkCreate_UBObservationAsrSignal, ChkStart_UBObservationAsrSignal

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_UBObservationAsrPDU(PDU aPDU, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkStart_UBObservationAsrPDU(PDU aPDU, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkCreate_UBObservationAsrPDU(PDU aPDU, char [] signalGroup, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkStart_UBObservationAsrPDU(PDU aPDU, char [] signalGroup, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkCreate_UBObservationAsrPDU(long aHeaderId, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkStart_UBObservationAsrPDU(long aHeaderId, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkCreate_UBObservationAsrPDU(long aHeaderId, char [] signalGroup, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkStart_UBObservationAsrPDU(long aHeaderId, char [] signalGroup, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkCreate_UBObservationAsrSignal(long aHeaderId, char [] signalName, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkStart_UBObservationAsrSignal(long aHeaderId, char [] signalName, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkCreate_UBObservationAsrSignal(PDU aPDU, char [] signalName, dword maxNoOfConsUnchangedDataWithSetUB);
dword ChkStart_UBObservationAsrSignal(PDU aPDU, char [] signalName, dword maxNoOfConsUnchangedDataWithSetUB);
```

## Description

Monitors the UB of a PDU, a single signal group of a PDU or a single signal of a PDU. The check condition is violated if the UB of an signal is set and the matching signal is not changed in the PDU or signal group. The check can be set up for a single PDU, a single signal group within a PDU or a single signal with a PDU.

The functions/constructors without the parameter signalGroup monitors all specified UB's within the given PDU.

The numeric functions/constructors with the parameter aHeaderId cannot be used for FlexRay.

## Parameters

| Name | Description |
|---|---|
| aPDU | Must exist in DB |
| aHeaderId | PDU header ID to be observed. The corresponding PDU shall be defined in the database. |
| signalGroup | Signal group with SQC to be observed. |
| signalName | Signal with UB to be observed. |
| maxNoOfConsUnchangedDataWithSetUB | > 0: Maximal number of constant unchanged data with set UB= 0: Unchanged data with set UB not allowed-1: Unchanged data with set UB allowed infinite |

## Example

```c
// checks the payload gaps of the message
checkId = ChkStart_UBObservationAsrPDU (PDUToObserve, “signalGroup1”);
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
