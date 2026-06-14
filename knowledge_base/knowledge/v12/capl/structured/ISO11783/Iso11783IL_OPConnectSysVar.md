# Iso11783IL_OPConnectSysVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPConnectSysVar( dword objectId, char sysVarNameWithPath[] );
```

## Description

Connects an object from the object pool (on implement side) to a system variable. Only the following objects are supported:

Input Boolean

Input Number

Input List

Input String

Output Number

Output List

Output Meter

Output Linear Bar Graph

Output Arched Bar Graph

Output String

Number Variable

String Variable

The connected system variable receives the value that was sent by the Virtual Terminal to the ECU via VT Change Numeric Value Message or VT Change String Value Message and modified the object value in the object pool on the implement side.

If the system variable in CANoe itself is modified (e.g., in CAPL or in a panel), the object value in the object pool on the implement side is modified and sent to the Virtual Terminal with the Change Numeric Value or Change String Value command.

To release connection between the system variable and an object from the object pool, just call the same method again, but with the empty string instead of the name of system variable.

## Return Values

0: Function has been executed successfully

## Example

```c
int ret;
ret = Iso11783IL_OPConnectSysVar(10100, "ConnectedSysVars::svIntVar");//connect
...
ret = Iso11783IL_OPConnectSysVar(10100, "");//release
```

## Availability

| Since Version |
|---|
