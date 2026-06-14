# trigger

> Category: `Other` | Type: `function`

## Syntax

```c
void trigger();
```

## Description

Sends a trigger event to all CANoe Logging or Trigger Blocks.

For a Logging Block, the trigger event starts and stops logging, depending on

set in the Trigger Configuration dialog of this block.

For a trigger block, the trigger event starts and stops the data stream (like a filter) for the whole analysis branch or a single analysis window, depending also on trigger mode and trigger conditions in the Trigger Configuration dialog.

Please note in CANoe online help the Trigger Condition: CAPL

## Return Values

—

## Example

```c
on message 100 
{
  write("logging start");
  trigger(); // start logging
  setTimer(logging,1000); // for 1000 ms
}

on timer logging
{
  trigger(); // Stop logging
}
```

## Availability

| Since Version |
|---|
