# VTIL_EditStringValue, VTIL_ChangeStringValueMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_EditStringValue(dword objectId, char value[], dword duration); // form 1
```

## Description

Editing of an Input String object.

The VTIL_EditStringValue methods simulate the selection, opening, value modification and closing of the Input String object. The corresponding VT messages are sent. If the object is already selected or opened for input, then the steps Select, Open and Close are skipped.

The VTIL_ChangeStringValueMsg methods send only the VT Change String Value message (without influencing any button or input object and without triggering any event in the Virtual Terminal).

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_EditStringValue (VT, 301, "text", 2000);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2102: TestStepFail("Invalid object!"); break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2106: TestStepFail("Currently there is no active Data or Alarm mask!"); break;
  case -2115: TestStepFail("VT works in passiv mode therefore you cannot select objects!"); break;
  case -2117: TestStepFail("Failed to open object for editing!"); break;
  case -2118: TestStepFail("Object is no Input String object!"); break;
  case -2120: TestStepFail("Failed to edit object because it is disabled!"); break;
  case -2121: TestStepFail("Button is not available in the current  context!"); break;
  default: TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
