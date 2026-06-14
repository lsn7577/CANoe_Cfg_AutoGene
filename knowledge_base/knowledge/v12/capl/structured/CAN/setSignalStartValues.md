# setSignalStartValues

> Category: `CAN` | Type: `function`

## Syntax

```c
setSignalStartValues(message msg); // form 1
```

## Description

Sets the values of the signals in the parameter to the start values defined in the database.

## Return Values

0: function was successful

## Example

```c
message LightState msg;
setSignalStartValues(msg);
```

## Availability

| Since Version |
|---|
