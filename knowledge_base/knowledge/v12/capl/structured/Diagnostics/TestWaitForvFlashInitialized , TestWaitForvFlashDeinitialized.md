# TestWaitForvFlashInitialized , TestWaitForvFlashDeinitialized

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long TestWaitForvFlashInitialized();
```

## Description

Waits until the vFlash library is initialized/deinitialized. A call to TestWaitForvFlashDeinitialized is mandatory if any other call to a function of the vFlash API is made.

## Return Values

1: Success

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
