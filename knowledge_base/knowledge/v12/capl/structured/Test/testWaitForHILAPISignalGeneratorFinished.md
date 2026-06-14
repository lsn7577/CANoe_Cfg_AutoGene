# testWaitForHILAPISignalGeneratorFinished

> Category: `Test` | Type: `function`

## Syntax

```c
long testWaitForHILAPISignalGeneratorFinished(dword handle);
```

## Description

Waits until a running generator has finished.

## Return Values

<0: An internal error occurred, e.g. a protocol error or a faulty configuration of the diagnostic layer.

## Example

```c
HILAPIStartSignalGenerator(hGenerator);
testWaitForHILAPISignalGeneratorFinished(hGenerator);
```

## Availability

| Since Version |
|---|
