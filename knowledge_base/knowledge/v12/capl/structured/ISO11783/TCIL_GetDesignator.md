# TCIL_GetDesignator

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetDesignator(dbNode client, dword ddi, dword elementNumber, dword unitDesignatorBufferSize, char unitDesignatorBuffer[]); // form 1
```

## Description

Returns the designator of DeviceProcessData (DPD) or DeviceProperty (DPT) object defined by DDI/elementNumber.

Form 2 applicable in test module / test unit only.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
char designator[256];
// Retrieve the designator for the DPD with DDI=17 and elementNumber=3 from DDOP uploaded by Sprayer to TC
result = TCIL_GetDesignator(TC, Sprayer, 17 /*DDI*/, 3 /*elementNumber*/, 256 /*sizeOfBuffer*/, designator /*buffer*/);
```

## Availability

| Since Version |
|---|
