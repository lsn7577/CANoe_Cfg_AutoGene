# testWaitForHILAPISignalGeneratorLoaded

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForHILAPISignalGeneratorLoaded(dword handle);
```

## Description

Waits until a signal generator created with HILAPICreateSignalGenerator is fully loaded and ready to start.

## Return Values

<0: An internal error occurred, e.g. a protocol error or a faulty configuration of the diagnostic layer.

## Example

```c
hGenerator = HILAPICreateSignalGenerator("Example.sti");
testWaitForHILAPISignalGeneratorLoaded(hGenerator);
```

## Availability

| Since Version |
|---|
