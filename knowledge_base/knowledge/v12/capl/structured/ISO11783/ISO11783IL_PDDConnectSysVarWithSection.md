# ISO11783IL_PDDConnectSysVarWithSection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long ISO11783IL_PDDConnectSysVarWithSection(dword ddiOfCondensedState, dword elementNumber, dword sectionNumber, char[] sysVarNameWithPath); // form 1
```

## Description

Connects a single section state to a system variable.

If a section state is changed the new value is put into the system variable.

To release connection between the system variable and the condensed state, just call the same method again, but with the empty string instead of the name of system variable.

## Return Values

0: function has been executed successfully

## Example

```c
long result;
char text[256];
result = Iso11783IL_PDDConnectSysVarWithSection(290, 10, 1, "ConnectedSysVars::svSection1");
if (result < 0)
{
  Iso11783IL_GetLastErrorText ( elCount(text), text );
  write( "ERROR: %s", text);
}
```

## Availability

| Since Version |
|---|
