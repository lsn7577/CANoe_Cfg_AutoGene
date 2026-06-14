# Iso11783PDDOnStateChanged

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783PDDOnStateChanged( dword ecuHandle, dword state );
```

## Description

Is called up when the Node Layer changes its state.

## Return Values

—

## Example

```c
void Iso11783PDDOnStateChanged
 ( dword ecuHandle, dword state )
{
  switch(state) {
  case 0: // Uninitialized
    break;
  case 1: // Initialized
    break;
  case 2: // StartUpDelay
    break;
  case 3: // Wait For Task Controller 
 Status
    break;
  case 4: // Query Info
    break;
  case 5: // Transfer Object Pool
    break;
  case 6: // Activate Object Pool
    break;
  case 7: // Online
    break;
  case 8: // Task active
    break;
  }
}
```

## Availability

| Since Version |
|---|
