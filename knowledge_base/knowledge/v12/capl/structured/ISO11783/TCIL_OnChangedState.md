# TCIL_OnChangedState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void TCIL_OnChangedState( long state );
```

## Description

This callback function is called from the TC IL if it has changed its state.

## Return Values

—

## Example

```c
void TCIL_OnChangedState( long state )
{
  switch(state) {
    case 1: // Claiming
      break;
    case 2: // Active
      break;
    case 3: // Stopped
      break;
    case 4: // Suspended
      break;
  }
}
```

## Availability

| Since Version |
|---|
