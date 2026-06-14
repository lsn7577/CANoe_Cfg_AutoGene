# mostSetMasterMode, mostGetMasterMode

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetMasterMode(long channel, long mode)
```

## Description

Configures the timing master as static or non-static master. A non-static master shuts the network down if there is for example no signal at its optical input, whereas a static master keeps the network running independently from the input signal.

mostSetMasterMode becomes operative with the next call of mostSetTimingMode.

## Return Values

mostSetMasterMode: See error codes

## Example

```c
// configure bus interface as non-static timing master
mostSetMasterMode(1, 1);
mostSetTimingMode(1, 1);
```

## Availability

| Since Version |
|---|
