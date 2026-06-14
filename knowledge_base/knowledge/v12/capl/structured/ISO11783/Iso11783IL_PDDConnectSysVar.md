# Iso11783IL_PDDConnectSysVar

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDConnectSysVar( dword ddi, dword elementNumber, char sysVarNameWithPath[] ); // form 1
```

## Description

Connects an object from the loaded Process Data Descripton (PDD) (on Implement side) with a system variable.

The connected system variable receives the value that was sent by the Task Controller to the ECU via Set Value and Acknowledge command or Set Value command and modified the object value in the object pool on the implement side.

If the system variable in CANoe itself is modified (e.g., in CAPL or in a panel), the value of the process variable in the PDD on implement side is modified. This value can then be requested by the Task Controller with a Request Value command or transferred to the Task Controller by the implement itself as logging.

To release connection between the system variable and an object from the PDD, just call the same method again, but with the empty string instead of the name of system variable.

## Return Values

0: function has been executed successfully

## Example

```c
int ret;
ret = Iso11783IL_PDDConnectSysVar(0x6, 0x1, "ConnectedSysVars::svIntVar");//connect
...
ret = Iso11783IL_PDDConnectSysVar(0x6, 0x1, "");//release
```

## Availability

| Since Version |
|---|
