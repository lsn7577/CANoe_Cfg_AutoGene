# mostSetEclGlitchFilter

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetEclGlitchFilter (long channel, long durationus)
```

## Description

Configures the timing of the glitch filter for the ECL. For pulses which are shorter than the given time durations the callback <OnMostEcl> will not be called, neither will those pulses appear in a Trace Window.

## Return Values

See error codes

## Availability

| Since Version |
|---|
