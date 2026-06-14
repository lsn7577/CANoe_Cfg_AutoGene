# VTIL_SelectInputObject, VTIL_SelectInputObjectMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SelectInputObject(dword objectId); // form 1
```

## Description

Select an input filed, Button of Key object.

The VTIL_SelectInputObject methods simulate the selection of an input field, button or key object by user. As a result:

The VTIL_SelectInputObjectMsg methods send only the VT Select Input Object message (without influencing any button or input object and without triggering any event in the Virtual Terminal). You can use it to implement fault injection.

If an input object is open for data input, the value of the object can be modified with VTIL_EditNumericValue or VTIL_EditStringValue. To close an input object which is open for data input, you have to use this command with openMode 0.

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
