# vFlashActivateNetwork

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void vFlashActivateNetwork();
```

## Description

Activates the FlexRay network management, if required. The next API call is only allowed after the CAPL callback vFlashActivateNetworkCompleted was called!

Note: This event-driven API is only needed outside of test modules or test units.

## Return Values

—

## Example

```c
  // ...
  // Prepare flashing on FlexRay
  vFlashActivateNetwork();
}
void vFlashActivateNetworkCompleted(long vFlashStatusCode)
{
  write("FlexRay network management was activated");
}
```

## Availability

| Since Version |
|---|
