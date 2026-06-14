# HILAPICreateSignalGenerator

> Category: `Test` | Type: `function`

## Syntax

```c
dword HILAPICreateSignalGenerator(char filename[]);
```

## Description

Creates a Signal Generator from an ASAM HILAPI Signal Generator definition file.

## Return Values

0: The Signal Generator could not be created

## Example

Creates a ASAM HILAPI Signal Generator:

```c
dword hGenerator;
hGenerator = HILAPICreateSignalGenerator( “mygenerator.sti”);
```

## Availability

| Since Version |
|---|
