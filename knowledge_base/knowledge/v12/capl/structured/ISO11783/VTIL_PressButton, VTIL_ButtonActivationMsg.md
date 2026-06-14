# VTIL_PressButton, VTIL_ButtonActivationMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_PressButton(dword objectId, dword duration); // form 1
```

## Description

The VTIL_PressButton methods simulate the pressing of a Button and the releasing of it after the duration. As a result, the Button Activation Message is immediately sent with the key activation code = pressed/latched, then every 200 ms with the key activation code = still held and after the duration with the key activation code = released/unlatched.

For form 1 and 3 the button must be part of the active Data/Alarm/Window Mask. Otherwise, the function will return with an error code and no messages will be sent.

In contrast, forms 2, 4, 5 and 6 do not check whether the button belongs to the given Data/Alarm/Window mask or whether the button is active or visible.

The VTIL_ButtonActivationMsg methods send only the Button Activation Message (without triggering any event in the Virtual Terminal).

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_PressButton(VT, 3000, 400);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2102: TestStepFail("Invalid object!"); break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2115: TestStepFail("VT works in passive mode therefore you cannot press buttons!"); break;
  case -2120: TestStepFail("Button is currently disabled!"); break;
  case -2121: TestStepFail("Button is not available in the current  context!"); break;
  default:    TestStepFail("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
