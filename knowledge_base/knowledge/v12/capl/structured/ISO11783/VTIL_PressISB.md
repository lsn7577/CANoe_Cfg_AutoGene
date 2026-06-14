# VTIL_PressISB

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_PressISB(dword duration); // form 1
```

## Description

The VTIL_PressButton methods simulates pressing the ISOBUS Shortcut Button [ISB] of the Virtual Terminal and the releasing of it after the duration. As a result, the All Implements Stop Operations Switch State Message is sent with the value Stop implement operations until the ISB is released.

Every time the function is called the Number of transitions from Permit to Stop is incremented.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_PressISB(VT,  300);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2115: TestStepFail("VT works in passive mode therefore you cannot 
press the ISB button!"); break;
  case -2121: TestStepFail("ISB Button is not available because property ‚isbServer‘ is not set!"); break;
  default: TestStepFail("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
