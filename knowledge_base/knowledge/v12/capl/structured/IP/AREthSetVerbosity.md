# AREthSetVerbosity

> Category: `IP` | Type: `function`

## Syntax

```c
long AREthSetVerbosity( long verbosity);
```

## Description

Sets the verbosity level of AUTOSAR Eth IL messages in the Write Window.

## Return Values

0: The function was successfully executed

## Example

```c
on key '0'
{
  char buffer[1024];
  // set verbosity level to "Silent" mode
  if(AREthSetVerbosity(0) == 0)
  {
    write("AUTOSAR Eth IL verbosity level was set to mode \"silent\"");
  } // if
  else
  {
    // check if last function was executed correct
    AREthGetLastErrorText(elcount(buffer),buffer);
    write("Error setting verbosity level if AUTOSAR Eth IL: %s", buffer);
  } // else
}
```

## Availability

| Since Version |
|---|
