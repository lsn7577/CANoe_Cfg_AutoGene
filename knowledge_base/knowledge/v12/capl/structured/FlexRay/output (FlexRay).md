# output (FlexRay)

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void output(flexraymessage msg); // form 1
```

## Description

Outputs the object from the program block of the analysis branch. This function must be used inside the appropriate event procedure in order to forward the event to the next block in the analysis branch. If the function is not called, then the event is not forwarded. Thus, events will be filtered by the CAPL program when omitting this function.

The function must not be used in the Simulation Setup or transmit branch.

## Parameters

| Name | Description |
|---|---|
| flexraymessage | List of available selectors for this type of objects can be found under on frFrame selectors, on frSlot selectors, on frNullFrame selectors, and on frFrameError selectors. |
| flexraystartcycle | List of available selectors for this type of objects can be found under on frStartCycle selectors. |
| flexraysymbol | List of available selectors for this type of objects can be found under on frSymbol selectors. |
| flexraypocstate | List of available selectors for this type of objects can be found under on frPocState selectors. |
| flexrayerror | List of available selectors for this type of objects can be found under on frRError selectors. |

## Return Values

—

## Example

If you react on start of cycle, frame, Null Frame or frame error events, then you must forward the event explicitly to the next node in the Measurement Setup. Otherwise the successor node will not receive that event!

```c
on frFrame *
{
   // do something ...
   // forward event to next node in Measurement Setup:
   output(this);
}
```

## Availability

| Since Version |
|---|
