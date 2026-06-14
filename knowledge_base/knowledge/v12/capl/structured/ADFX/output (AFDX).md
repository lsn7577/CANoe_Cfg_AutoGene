# output (AFDX)

> Category: `ADFX` | Type: `function`

## Syntax

```c
void output (a664Message aMessage) (1)
```

## Description

This function outputs the object from the program block of the analysis branch. Use output inside the appropriate event procedure in order to forward the event to the next block in the analysis branch. If the function is not called, then the event is not forwarded. Thus, events will be filtered by the CAPL program when omitting this function.

The function must not be used in the Simulation Setup branch. For transmitting an object of type a664Frame or a664Message use the functions A664TriggerFrame and A664TriggerMessage.

## Return Values

—

## Example

```c
on a664Message * {
  #if MEASUREMENT_SETUP
  output(this);
  #endif
}

// or on frame level

on a664Frame * {
  #if MEASUREMENT_SETUP
  output(this);
  #endif
}
```

## Availability

| Since Version |
|---|
