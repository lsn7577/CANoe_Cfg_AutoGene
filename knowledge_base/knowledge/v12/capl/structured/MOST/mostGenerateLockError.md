# mostGenerateLockError

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateLockError(long channel, long unmodtime, long modtime, long repeat)
```

## Description

Starts (repeat > 0) or stops (repeat = 0) generation of Light Unmodulated-Modulated transitions.

For OptoLyzerOL3150o: The stress network interface controller (NIC) must have its bypass opened (see mostSetStressNodeParameter).

## Return Values

See error codes

## Availability

| Since Version |
|---|
