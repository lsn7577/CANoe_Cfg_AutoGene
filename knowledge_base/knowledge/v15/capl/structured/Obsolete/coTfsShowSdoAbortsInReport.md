# coTfsShowSdoAbortsInReport

> Category: `Obsolete` | Type: `notes`

## Description

This function is replaced by coTfsSetReportBehaviour.

See Also

| Obsolete Function This function is replaced by coTfsSetReportBehaviour. |  |
|---|---|
| Function Syntax | long coTfsShowSdoAbortsInReport( dword enable ); |
| Function | Allows the report of SDO aborts in the test protocol. If the function is activated in the test module (default), each recognized SDO abort code is added to the test report. |
| Parameters | enable 0: SDO abort codes are not written to test report 1: SDO abort codes are written to test report |
| Return Values | Error code |
| Example coTfsShowSdoAbortsInReport(1); // enable SDO abort reports in test report |  |

| Version 15© Vector Informatik GmbH |
|---|
