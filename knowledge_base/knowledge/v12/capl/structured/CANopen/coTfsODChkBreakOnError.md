# coTfsODChkBreakOnError

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsODChkBreakOnError( dword enable );
```

## Description

The function controls the behavior of the test module while executing coTfsODChk and coTfsODChkNotExist. It can called before the two test sequences and define the behavior in an error case. It can be defined if the tests should stop in an error occurrence to execute the next command (breakOnError=1) or if the error should be ignored (breakOnError=0).

## Return Values

Error code

## Example

```c
coTfsODChkBreakOnError(1); // break on error
coTfsOdRunHiddenObjUserTest();
```
