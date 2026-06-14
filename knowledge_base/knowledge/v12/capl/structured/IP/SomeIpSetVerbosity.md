# SomeIpSetVerbosity

> Category: `IP` | Type: `function`

## Syntax

```c
long SomeIpSetVerbosity( long verbosity);
```

## Description

Sets the verbosity level of SOME/IP IL messages in the Write Window.

## Return Values

0: The function was successfully executed

## Example

```c
on key '0'
{
  char buffer[1024];
  // set verbosity level to "Silent" mode
  if(SomeIpSetVerbosity(0) == 0)
  {
    write("SOME/IP IL verbosity level was set to mode \"silent\"");
  } // if
  else
  {
    // check if last function was executed correct
    SomeIpGetLastErrorText(elcount(buffer),buffer);
    write("Error setting verbosity level if SOME/IP IL: %s", buffer);
  } // else
}
```

## Availability

| Since Version |
|---|
