# OnMostAsRegistry

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostAsRegistry();
```

## Description

When the Local FBlockList or Bus Registry is changed the event procedure OnMostAsRegistry() is called.

Causes for a change to the Local FBlockList:

Causes for a change to the Bus Registry:

Within this event procedure the functions mostEventChannel, mostEventTime and mostEventOrigTime can be used to call up supplemental information.

CAPL nodes are transparent to the controller events. Please use the Multibus Filter or MOST Filter, to filter these events in nodal sequences.

In the Simulation Setup event procedures are only called if the event occurs on the channel allocated to the CAPL node.

## Parameters

| Name | Description |
|---|---|
| regsel | 1: Changes in Local FBlockList2: Changes in Bus Registry |

## Return Values

—

## Example

Read-Out of the Registries

In the following example whenever a registry changes its contents are output to the Write Window.

```c
OnMostAsRegistry(long regsel)
{
   long size, i;
   long rxtxlog, fblockid, instid;
   // display registry type
   if(regsel == 1)
      write("Local 
 Registry:");
   else if(regsel == 2)
      write("Bus 
 Registry:");
   // get registry size
   size = mostAsRgGetSize(regsel);
   // print the whole registry
   write("Adr   FBlock InstID");
   for(i = 0; i < size; ++i)
   {
      rxtxlog = mostAsRgGetRxTxLog(regsel,i);
      fblockid = mostAsRgGetFBlockID(regsel,i);
      instid = 
 mostAsRgGetInstID(regsel,i);
      write("%04X 
  %02X     %02X", rxtxlog, fblockid, instid);
   }
}
Bus Registry:
Adr FBlock InstID
0100 02 00
0100 04 01
0100 C0 01
0101 C1 01
0101 C5 01
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
