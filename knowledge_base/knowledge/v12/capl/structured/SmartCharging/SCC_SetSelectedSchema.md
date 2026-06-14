# SCC_SetSelectedSchema

> Category: `SmartCharging` | Type: `function`

## Syntax

```c
long SCC_SetSelectedSchema ( long SchemaID )
```

## Description

Sets the ID of the schema to be selected in the SupportedAppProtocolRes message. This overrides the automatic selection done based on the vehicle’s priority values.

Due to technical reasons, the schema ID must belong to a schema actually offered by the vehicle (the charge point cannot continue with an undefined schema).

## Return Values

0: Not successful

## Availability

| Since Version |
|---|
