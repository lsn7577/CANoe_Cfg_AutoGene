# VTIL_Touch, VTIL_PointingEventMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_Touch(dword x, dword y, dword duration); // form 1
```

## Description

Touches into the Data Mask.

The VTIL_Touch methods simulate a touch into the Data Mask and a release of the touch event after the duration. As a result, the Pointing Event Message is sent immediately with the touch state = pressed, then every 200 ms with the touch state = Held and after the duration with the touch state = Released.

If there is a button or input object at the specified position, the button or object is selected and pressed.

The VTIL_PointingEventMsg methods only send the Pointing Event Message (without influencing any button or input object and without triggering any event in the Virtual Terminal). You can use it to implement dragging operation.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_Touch(VT, 1, 2, 500);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2115: TestStepFail("VT works in passive mode. Therefore you cannot touch it!"); break;
  default:    TestStepFail("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
