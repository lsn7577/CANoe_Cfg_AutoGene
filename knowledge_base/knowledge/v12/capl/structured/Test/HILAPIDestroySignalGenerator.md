# HILAPIDestroySignalGenerator

> Category: `Test` | Type: `function`

## Syntax

```c
dword HILAPIDestroySignalGenerator(dword handle);
```

## Description

Destroys an instance of a Signal Generator.

## Return Values

0: The handle of the Signal Generator is not valid

## Example

Destroys an instance of a ASAM HILAPI Signal Generator:

```c
HILAPIDestroySignalGenerator( hGenerator);
```

## Availability

| Since Version |
|---|
