# VTIL_GetDwordValue, VTIL_GetDoubleValue, VTIL_GetStringValue

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetDwordValue(dbNode workingSetMaster, dword objectId, dword & value); // form 1
```

## Description

Returns the value of an object or of an object attribute.

You can use VTIL_GetDoubleValue or VTIL_GetDwordValue without attribute ID to get the numeric value of a Key object, Button object or an object that supports the Change Numeric Value command. You can use VTIL_GetStringValue the get the string value of a Input String, Output String, String Variable or a Input Attribute object.

## Return Values

0: Function has been executed successfully

## Example

```c
long result;
char buf[100];
result = VTIL_GetStringValue(VT, 205, buf, elCount(buf));
switch (result)
{
  case 0:
    write("Current value of object 205 is '%s'", buf);
    TestStepPass();
    break;
  case -2102: TestStepFail("Invalid object!"); break;
  case -2104: TestStepFail("Currently there is no active Working Set!"); break;
  case -2108: TestStepFail("Invalid variable reference!"); break;
  default:    TestStepFail("Unexpected error!"); break;
}
```

## Availability

| Since Version |
|---|
