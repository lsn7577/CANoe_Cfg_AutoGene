# VTIL_EditNumericValue, VTIL_ChangeNumericValueMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_EditNumericValue(dword objectId, double value, dword duration); // form 1
```

## Description

Editing of an Input Number object.

The VTIL_EditNumericValue methods simulate the selection, opening, value modification and closing of the Input Number or Input List object. The corresponding VT messages are sent.

If the object is already selected or opened for input, then the steps Select, Open and Close (and corresponding VT messages) are skipped.

The VTIL_ChangeNumericValueMsg methods send only the VT Change Numeric Value message (without influencing any button or input object and without triggering any event in the Virtual Terminal).

## Return Values

0: Function has been executed successfully

## Example

Simulation of real time editing:

```c
//to simulate: Real Time Editing of the numeric object with ID=220

VTIL_SelectInputObject(VT, 220, 1); // open for editing
TestWaitForTimeout(200);
VTIL_EditNumericValue(VT, 220, 1, 0); //type „1“
TestWaitForTimeout(500);
VTIL_EditNumericValue(VT, 220, 12, 0); //type additionally „2“
TestWaitForTimeout(600);
VTIL_EditNumericValue(VT, 220, 123, 0);  //type additionally „3“
TestWaitForTimeout(400);
VTIL_SelectInputObject(VT, 220, 0);    //finish editing
```

## Availability

| Since Version |
|---|
