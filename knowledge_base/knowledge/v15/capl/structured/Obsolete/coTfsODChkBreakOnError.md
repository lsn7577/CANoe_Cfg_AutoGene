# coTfsODChkBreakOnError

> Category: `Obsolete` | Type: `notes`

## Description

This function is replaced by coTfsODSetErrorHandling.

| Obsolete Function This function is replaced by coTfsODSetErrorHandling. |  |
|---|---|
| Function Syntax | long coTfsODChkBreakOnError( dword enable ); |
| Function | The function controls the behavior of the test module while executing coTfsODChk and coTfsODChkNotExist. It can called before the two test sequences and define the behavior in an error case. It can be defined if the tests should stop in an error occurrence to execute the next command (breakOnError=1) or if the error should be ignored (breakOnError=0). |
| Parameters | enable 0: test goes on after an error, all objects of the internal list are checked in the test 1: test is stopped |
| Return Values | Error code |
| Example coTfsODChkBreakOnError(1); // break on errorcoTfsOdRunHiddenObjUserTest(); |  |

| Version 15© Vector Informatik GmbH |
|---|
