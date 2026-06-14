# SysGetVariableIntArray

> Category: `Obsolete` | Type: `notes`

| Deprecated Function Replaced by SysGetVariableLongArray. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long SysGetVariableIntArray(char namespace[], char variable[], int values[], long arraySize); // form 1 |  |  |  |
| long SysGetVariableIntArray(SysVarName, int values[], long arraySize); // form 2 |  |  |  |  |
| Function | Returns the value of a variable of the int[] type. |  |  |  |
| Parameters | namespace Name of the name space (form 1) |  |  |  |
| variable Name of the variable (form 1) |  |  |  |  |
| values Gets the values of the variable (both forms) |  |  |  |  |
| arraySize Size of the array (both forms) |  |  |  |  |
| SysVarName Name of the fully qualified name of the system variable, including all name spaces, separated by "::". The name must be preceded by "sysVar::". (form 2) |  |  |  |  |
| Return Values | 0: no error, function successful |  |  |  |
| 1: name space was not found or second try to define the same name space |  |  |  |  |
| 2: variable was not found or second try to define the same variable |  |  |  |  |
| 3: no writing right for the name space available |  |  |  |  |
| 4: the variable has no suitable type for the function |  |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 5.1 | — | — | • |  |
| 7.0 | — | • | • |  |
| Example — |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
