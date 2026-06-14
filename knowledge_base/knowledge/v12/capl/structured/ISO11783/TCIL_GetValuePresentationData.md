# TCIL_GetValuePresentationData

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetValuePresentationData(dbNode client, dword ddi, dword elementNumber,dword idOfDVP, long offset, float scale, dword numberOfDecimals, dword designatorBufferSize, char designatorBuffer[]); // form 1
```

## Description

Returns all properties (id, offset, scale, numberDecimals, designator) of the ValuePresentation object referenced by the DeviceProcessData (DPD) or DeviceProperty (DPT) object defined by DDI/elementNumber.

Form 2 applicable in test module / test unit only.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
char designator[256];
dword idOfDVP, numOfDecimals;
long offset;
float scale;
// Retrieve all properties of the DVP object used by the DPD with DDI=17 and elementNumber=3
// from DDOP uploaded by Sprayer to TC
result = TCIL_GetValuePresentationData(TC, Sprayer, 17, 3, idOfDVP, offset, scale, numOfDecimals, 256, designator);
```

## Availability

| Since Version |
|---|
