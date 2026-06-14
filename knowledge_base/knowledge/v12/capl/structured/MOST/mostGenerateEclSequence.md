# mostGenerateEclSequence

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateEclSequence (long channel, long startstop)
```

## Description

Starts the generation of the signal sequence on the ECL which was prepared by mostConfigureEclSequence. Dominant levels will be set actively whereas during recessive phases the generator is passive and other devices connected to the ECL may pull the line to dominant level.

## Return Values

See error codes

## Availability

| Since Version |
|---|
