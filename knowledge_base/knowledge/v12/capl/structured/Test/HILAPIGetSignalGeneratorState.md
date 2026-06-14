# HILAPIGetSignalGeneratorState

> Category: `Test` | Type: `function`

## Syntax

```c
dword HILAPIGetSignalGeneratorState(dword handle);
```

## Description

Returns the state of a Signal Generator.

## Return Values

0: The handle of the Signal Generator is not valid

## Example

Gets the state of the Signal Generator:

```c
dword state;
state = HILAPIGetSignalGeneratorState( hGenerator);
```

## Availability

| Since Version |
|---|
