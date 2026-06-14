# VTIL_PressSoftKey, VTIL_SoftKeyActivationMsg

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_PressSoftKey(dword objectId, dword duration); // form 1
```

## Description

The VTIL_PressSoftKey methods simulate the pressing of a Soft Key and the releasing of it after the duration. As a result, the Soft Key Activation Message is immediately sent with the key activation code = pressed, then every 200 ms with the key activation code = still held and after the duration with the key activation code = released.

For form 1 and 3 the Soft Key must be part of the active Soft Key Mask. Otherwise, the function will return with an error code and no messages will be sent.

In contrast, forms 2, 4, 5 and 6 do not check whether the Soft Key belongs to the given Soft Key mask or whether the Soft Key is active or visible.

The VTIL_SoftKeyActivationMsg methods only send the Soft Key Activation message (without triggering any event in the Virtual Terminal).

You can also use these methods to simulate the press of the ACK means of the Virtual Terminal to acknowledge an alarm mask. For this the objectId must be 0xFFFF and parentId has to be equal to the ID of the current alarm mask.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
result = VTIL_PressSoftKey(VT, 6011, 250);
switch (result)
{
  case 0: TestStepPass(); break;
  case -2102: TestStepFail("Invalid object!"); break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2107: TestStepFail("Currently there is no active Soft Key Mask!"); break;
  case -2115: TestStepFail("VT works in passive mode therefore you cannot press keys!"); break;
  default: TestStepFail("Unexpected error"); break;
}
```

## Availability

| Since Version |
|---|
