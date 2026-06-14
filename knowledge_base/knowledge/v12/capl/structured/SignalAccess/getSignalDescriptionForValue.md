# getSignalDescriptionForValue

> Category: `SignalAccess` | Type: `function`

## Syntax

```c
long getSignalDescriptionForValue(Signal signal, int64 rawValue, char buffer[], long bufferSize); // form 1
```

## Description

Retrieves the description for the value of a database signal. In this way, you can access the value table of the signal.

## Return Values

0: No error, function successful.

## Example

```c
char buffer[100]; long ret;
ret = getSignalDescriptionForValue(PowerTrain::Engine::GearBoxInfo::Gear, 1, buffer, elcount(buffer));
if (ret == 0) write("Description for value 1 is '%s'", buffer);
else write("Error getting description for value 1: %d", ret);
```

## Availability

| Since Version |
|---|
