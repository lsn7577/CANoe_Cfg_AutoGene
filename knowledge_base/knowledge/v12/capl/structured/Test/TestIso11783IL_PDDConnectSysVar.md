# TestIso11783IL_PDDConnectSysVar

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDConnectSysVar( dbNode node, dword ddi, dword elementNumber, char sysVarNameWithPath[] );
```

## Description

Connects an object from the loaded Process Data Descripton (PDD) (on Implement side) with a system variable.

The connected system variable receives the value that was sent by the Task Controller to the ECU via Set Value and Acknowledge command or Set Value command and modified the object value in the object pool on the implement side.

If the system variable in CANoe itself is modified (e.g., in CAPL or in a panel), the value of the process variable in the PDD on implement side is modified. This value can then be requested by the Task Controller with a Request Value command or transferred to the Task Controller by the implement itself as logging.

To release connection between the system variable and an object from the PDD, just call the same method again, but with the empty string instead of the name of system variable.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: function has been executed successfully

## Example

```c
int ret;
ret = TestIso11783IL_PDDConnectSysVar(Sprayer, 0x6, 0x1, "ConnectedSysVars::svIntVar"); //connect
...
ret = TestIso11783IL_PDDConnectSysVar(Sprayer, 0x6, 0x1, ""); //release
```

## Availability

| Since Version |
|---|
