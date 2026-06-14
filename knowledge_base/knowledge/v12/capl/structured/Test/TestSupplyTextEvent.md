# TestSupplyTextEvent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestSupplyTextEvent(char aText[]);
```

## Description

Signals the specified event.

Consequently resolves a possibly-active wait condition on this event.

## Return Values

0: Event was signaled successfully

## Example

```c
// Signals the occurrence of an Error Frame as a text event
on errorFrame
{
 TestSupplyTextEvent("ErrorFrame occurred!")
}
```

## Availability

| Since Version |
|---|
