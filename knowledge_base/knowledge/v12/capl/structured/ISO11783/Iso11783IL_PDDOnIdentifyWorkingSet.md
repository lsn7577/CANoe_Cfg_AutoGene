# Iso11783IL_PDDOnIdentifyWorkingSet

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDOnIdentifyWorkingSet( );
```

## Description

The function is called by the ISO11783 interaction layer to determine if the interaction layer is responsible for sending of the Working Set Master message after the Task Controller starts to send his status messages.

If this callback function is not implemented or it returns the value 1, the Working Set Master message is sent by the ISO11783 interaction layer. The transmitted number of Working Set members is 1. If the return value of the function is 0, the ISO11783 interaction layer doesn’t send the Working Set Master message. Instead, the CAPL application sends the Working Set Master message.

## Example

```c
LONG Iso11783IL_PDDOnIdentifyWorkingSet( )
{
  return 1;
}
```

## Availability

| Since Version |
|---|
