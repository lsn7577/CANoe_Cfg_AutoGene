# GetBusNameContext

> Category: `Other` | Type: `function`

## Syntax

```c
dword GetBusNameContext(char name[]); // form 1
dword GetBusNameContext(dword busType, dword channelNumber); // form 2
```

## Description

Returns the context of the specified bus.

## Parameters

| Name | Description |
|---|---|
| name | The name of the bus.The bus name can be taken from the CANoeSimulation Setup: Open the System View Select a network Select the Rename... shortcut menu command Copy the name from the dialog |
| busType | Bus Type of the bus. The predefined enum BusType should be used for the value of this parameter. |
| channelNumer | Number of the channel for the specified bus. Channel numbering starts with 1. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 3.2 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
