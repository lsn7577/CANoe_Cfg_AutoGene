# testILSetNodeProperty

> Category: `Test` | Type: `function`

## Syntax

```c
long testILSetNodeProperty( dbNode node, char propertyName[], long propertyValue);
```

## Description

Function field of J1939 NAME

## Return Values

0: Property has been set successfully

## Example

```c
if(testILSetNodeProperty(EBS, "BAM_DT_Interval", 100) < 0)
{
  write( "Can’t set node property ‘BAM_DT_Interval‘ " );
}
```

## Availability

| Since Version |
|---|
