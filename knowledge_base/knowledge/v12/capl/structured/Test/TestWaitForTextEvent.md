# TestWaitForTextEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForTextEvent(char aText[], dword aTimeout);
```

## Description

Waits for the signaling of the specified textual event from the individual test module. A signaling from another test module does not effect this wait instruction.

Should this event not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

## Return Values

-2: Resume due to constraint violation

## Example

```c
// waits for the occurrence of text event „ErrorFrame occurred!“
long result;
result = TestWaitForTextEvent("ErrorFrame occurred!", 3000);

// handler ‘on errorFrame’ signals event
on errorFrame
{
   TestSupplyTextEvent("ErrorFrame occurred!");
}
```

## Availability

| Since Version |
|---|
