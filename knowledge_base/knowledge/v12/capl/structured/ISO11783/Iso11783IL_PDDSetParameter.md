# Iso11783IL_PDDSetParameter

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_PDDSetParameter( char paramName[], float paramValue ); // form 1
```

## Description

Changes an internal parameter of the PDD API.

## Parameters

| Name | Description |
|---|---|
| Value | Description |
| debug | activates debug outputs in the Write Window 1: on 0: off |
| autoUpdateVariable | process variable is updated if value command is received 1: auto update 0: process variable have to be updated manually by Iso11783IL_PDDSetValue e.g. in callback function Iso11783IL_PDDOnDataChanged |
| Note Using version the version value obtained from the database (node attribute ISO11783PDDVersion) is overwritten. |  |

## Example

```c
if (Iso11783IL_PDDSetParameter( "debug", 1 ) == 0) {
  write( "Debug mode activated" );
}
```

## Availability

| Since Version |
|---|
