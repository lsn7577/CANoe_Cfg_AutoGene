# GetBusNameContext

> Category: `Other` | Type: `function`

## Syntax

```c
dword GetBusNameContext(char name[])
```

## Description

Returns the context of the specified bus.

## Return Values

In the case of success, the context of the specified bus is returned.
If the specified bus does not exist, 0 is returned.

## Example

This is an example for a simulation node.Test nodes should copy the bus context to a CAPL variable in the Main() function because all global variables are cleared when a test module is started.

```c
variables
{
char ibus[32] = "ibus";
char motbus[32] = "motbus";

dword ibus_context = 0;
dword motbus_context = 0;
}
on preStart
{
ibus_context = GetBusNameContext( ibus);
motbus_context = GetBusNameContext( motbus);

if ( 0 == ibus_context)
{
writeex( 0, 3, "Error: Cannot determine context for bus: %s", ibus);
}
if ( 0 == motbus_context)
{
writeex( 0, 3, "Error: Cannot determine context for bus: %s", motbus);
}
}
```

## Availability

| Since Version |
|---|
