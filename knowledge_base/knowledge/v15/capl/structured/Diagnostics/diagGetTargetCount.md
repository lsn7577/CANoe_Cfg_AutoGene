# diagGetTargetCount

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetTargetCount();
```

## Description

Returns the number /n/ of possible diagnostic targets configured. For indices /i/ with 0 ≤ i ≤ n you can retrieve the target qualifier with DiagGetTargetQualifier.

## Return Values

Error code or number of diagnostic targets.

## Example

```c
long i;
char ecuQual[100];
i = diagGetTargetCount();
while( i-- > 0)
{
   diagGetTargetQualifier( i, ecuQual, elcount(ecuQual));
   write( "Target %d: %s", i, ecuQual);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 7.5 | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
