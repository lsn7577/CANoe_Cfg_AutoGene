# getSignalValueForDescription

> Category: `SignalAccess` | Type: `function`

## Syntax

```c
long getSignalValueForDescription(Signal signal, char description[], int64& rawValue); // form 1
```

## Description

Retrieves the value for a value description of a database signal. In this way, you can access the value table of the signal.

## Return Values

0: No error, function successful.

## Example

```c
int64 val; long ret;
ret = getSignalValueForDescription(PowerTrain::Engine::GearBoxInfo::Gear, "Gear_2", val);
if (ret == 0) write("Value for description 'Gear_2' is %I64d", val);
else write("Error getting value for description 'Gear_2': %d", ret);
```

## Availability

| Since Version |
|---|
