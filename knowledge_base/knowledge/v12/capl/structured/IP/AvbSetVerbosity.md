# AvbSetVerbosity

> Category: `IP` | Type: `function`

## Syntax

```c
dword AvbSetVerbosity(long verbosity);
```

## Description

Sets the verbosity level of AVB IL messages in the Write Window.

## Return Values

Number of copied characters.

## Example

```c
on key '0'
{
  char buffer[1024];
  // set verbosity level to "Silent" mode
  if (AvbSetVerbosity(0) == 0)
  {
    write("AVB IL verbosity level was set to mode
    \"silent\"");
  }
  else
  {
    // check if last function was successfully executed
    AvbGetLastErrorText(elcount(buffer), buffer);
    write("Error setting verbosity level if AVB IL: %s", buffer);
  }
}
```

## Availability

| Since Version |
|---|
