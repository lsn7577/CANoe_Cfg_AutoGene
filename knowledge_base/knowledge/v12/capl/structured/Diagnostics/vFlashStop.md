# vFlashStop

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashActivateNetwork();
```

## Description

Stops the flashing procedure. The completion of the stopping is indicated by a call to the CAPL function vFlashStopCompleted.

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

—

## Example

```c
  //...
  vFlashStop();
}

void vFlashStopCompleted(long statusCode)
{
  write("Stopping flashing completed with status %d", status);
  // Unload the project to be able to load a different one
  vFlashUnloadProject();
}
```

## Availability

| Since Version |
|---|
