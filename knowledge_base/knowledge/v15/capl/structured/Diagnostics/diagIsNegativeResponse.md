# diagIsNegativeResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagIsNegativeResponse (diagResponse obj)
```

## Description

Returns value <> 0 if the object is a negative response to a request.

## Parameters

| Name | Description |
|---|---|
| obj | Diagnostics object |

## Return Values

0 or <>0

## Example

```c
on diagResponse *
{
  // Handle the ambiguity of neg responses by treating them as '*'
  if( diagIsNegativeResponse ( this ) )
  {
    write( "Received negative response for service 0x%x, code 0x%x",
    (long) diagGetParameter( this, "SIDRQ_NR" ),
    (long) diagGetParameter( this, "NRC" ) );
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.5 SP2 | 5.0 7.0 SP5: methods | — | — | — | 1.0 |
| Restricted To | Online mode | Online mode | — | — | — | Online mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ (since 9.0) | ✔ (since 9.0) | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
