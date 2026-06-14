# HILAPIGetSignalGeneratorElapsedTime

> Category: `Test` | Type: `function`

## Syntax

```c
double HILAPIGetSignalGeneratorElaspedTime(dword handle);
```

## Description

Returns the elapsed time of a Signal Generator.

## Return Values

0: The handle of the Signal Generator is not valid. Note: If the Signal Generator has not been started at the time of this call 0 is returned as well.

## Example

Gets the elapsed time of the Signal Generator:

```c
double time;
time = HILAPIGetSignalGeneratorElaspedTime(hGenerator);
```

## Availability

| Since Version |
|---|
