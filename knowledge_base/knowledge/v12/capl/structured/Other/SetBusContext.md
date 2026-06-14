# SetBusContext

> Category: `Other` | Type: `function`

## Syntax

```c
dword SetBusContext( dword context)
```

## Description

Sets the bus context of the CAPL block.

## Return Values

The bus context that was valid before the call was made is returned.

## Example

This is an example for a simulation node. Test nodes should copy the bus context to a CAPL variable in the Main() function because all global variables are cleared when the test module is started.

```c
variables
{
dword ibus_context = 0;
dword motbus_context = 0;
}
on preStart
{
ibus_context = GetBusNameContext( "ibus");
motbus_context = GetBusNameContext( "motbus");
}
void apCanOn()
{
dword context;
// activate the CAN channel on the "current" context
CanOnline();
// determine the "other" context
context = ibus_context == GetBusContext() ? motbus_context : ibus_context;
// set the context to the "other" bus...
SetBusContext( context);
// ...and activate its CAN chip as well
CanOnline();
}
```

## Availability

| Since Version |
|---|
