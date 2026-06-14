# DiagInitEcuSimulation

> Category: `KLine` | Type: `function`

## Syntax

```c
long DiagInitEcuSimulation(char ecuQualifier[])
```

## Description

Initialize CAPL node to represent a diagnostics ECU simulation. From now on the ECU can interpret and use all diagnostic objects in the CAPL code of this node as defined by the respective diagnostic description.

CANoe will initialize the CAPL callback interface for diagnostics during the call.

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
on preStart
{
   char ecuQual[10] = "KLineECU";
   write( "DiagInitEcuSimulation( %s): %d", ecuQual, DiagInitEcuSimulation(ecuQual));
}
```

## Availability

| Since Version |
|---|
