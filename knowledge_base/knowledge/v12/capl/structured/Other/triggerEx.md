# triggerEx

> Category: `Other` | Type: `function`

## Syntax

```c
void triggerEx(char name[]);
```

## Description

Sends a trigger event to a CANoe Logging or Trigger Block specified by name.

For a Logging Block, the trigger event starts and stops logging, depending on

set in the Trigger Configuration dialog of this block.

For a Trigger Block, the trigger event starts and stops the data stream (like a filter) for the whole analysis branch or a single analysis window, depending also on trigger mode and trigger conditions in the Trigger Configuration dialog.

If you enter no name, the event will be sent to all Trigger and Logging Blocks that are located behind the CAPL node with the CAPL function triggerEx() in the Measurement Setup. If you want the CAPL node to have effect on all Trigger Blocks, the CAPL node has to be placed directly after the online/offline switch.

Please note in CANoe online help the Trigger Condition: CAPL

## Parameters

| Name | Description |
|---|---|
| Note If you use the function in standalone mode with VN8900/CANoe RT and if you activated logging and Trigger Block in the standalone mode configuration settings you can address the (single) Trigger Block available in this case by passing an empty string as parameter. |  |

## Return Values

—

## Example

```c
on message 100 
{
  write("logging starts in Logging Block ""Logging""");
  triggerEx("Logging"); // start logging
  setTimer(logging,1000); // for 1000 ms
}

on timer logging
{
  triggerEx("Logging"); // Stop logging
}
```

## Availability

| Since Version |
|---|
