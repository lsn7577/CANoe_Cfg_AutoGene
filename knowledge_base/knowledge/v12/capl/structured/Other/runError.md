# runError

> Category: `Other` | Type: `function`

## Syntax

```c
void runError(long err, long);
```

## Description

Triggers a run error. Outputs the error number to the Write Window indicating the error number and the passed number, and then terminates the measurement.

## Return Values

—

## Example

```c
...
if(rpm < 0) runError(1001,1);
...
```

## Availability

| Since Version |
|---|
