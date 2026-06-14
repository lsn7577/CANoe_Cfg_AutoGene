# VTIL_SetResponseContent

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetResponseContent(dbNode workingSetMaster, byte vtFunction, pg VT12 pgWithNewContent); // form 1
```

## Description

The function changes the content of the next VT response VT12 sent by the VT IL to allow fault injection.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
pg VT12 vt12;
InitJ1939PGData(vt12);
vt12.VTFunctionVTtoECU = 168; // Change numeric value response
vt12.ObjectToChangeNumValueID = objectID;
vt12.byte(3)                  = errorCodes;
vt12.ValueOfTheObject         = value;
result = VTIL_SetResponseContent(VT, Sprayer, 168, vt12);
if (result < 0)
{
  TestStepFail("Failed to change Numeric Value response");
}
```

## Availability

| Since Version |
|---|
