# ChkCreate_UBObservationAsrPDU, ChkStart_UBObservationAsrPDU, ChkCreate_UBObservationAsrSignal, ChkStart_UBObservationAsrSignal

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_UBObservationAsrPDU(PDU aPDU, dword maxNoOfConsUnchangedDataWithSetUB);
```

## Description

Monitors the UB of a PDU, a single signal group of a PDU or a single signal of a PDU. The check condition is violated if the UB of an signal is set and the matching signal is not changed in the PDU or signal group. The check can be set up for a single PDU, a single signal group within a PDU or a single signal with a PDU.

The functions/constructors without the parameter signalGroup monitors all specified UB's within the given PDU.

The numeric functions/constructors with the parameter aHeaderId cannot be used for FlexRay.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

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

| Since Version |
|---|
