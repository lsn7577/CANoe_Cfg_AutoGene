# a429InitPayload

> Category: `A429` | Type: `function`

## Syntax

```c
long a429InitPayload (a429Word myA429word)
```

## Description

Initialize the payload of an existing a429word using the current values of corresponding signals from SignalServer.

This can be used to initialize a message from scratch to the StartValues of the StartValue-table in the Init-section, or to assign the current signal values to the payload during any time of measurement.

## Example

```c
variables
{
  a429Word *msg = { msgChannel = 1};
}
on key '1'
{
  a429InitPayload(msg);
}
```

## Availability

| Since Version |
|---|
