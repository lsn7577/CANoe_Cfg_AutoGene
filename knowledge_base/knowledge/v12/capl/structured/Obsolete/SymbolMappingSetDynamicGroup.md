# SymbolMappingSetDynamicGroup

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void SymbolMappingSetDynamicGroup(char mappingSetName[]);
```

## Description

Changes the dynamic mapping set that will be used for mapping in the CANoe Symbol Mapping dialog. Only the mapping relations contained in the given dynamic mapping set and in the static mapping set are considered.

## Return Values

—

## Example

```c
on key '3'
{
  // Activate RT 3 and map RT 3
  SymbolMappingSetDynamicGroup("RT 3");
}

on key '4'
{
  // Activate RT 4 and map RT 4
  SymbolMappingSetDynamicGroup("RT 4");
}
```

## Availability

| Up to Version |
|---|
