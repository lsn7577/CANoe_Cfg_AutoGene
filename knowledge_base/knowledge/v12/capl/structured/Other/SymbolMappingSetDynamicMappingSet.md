# SymbolMappingSetDynamicMappingSet

> Category: `Other` | Type: `function`

## Syntax

```c
void SymbolMappingSetDynamicMappingSet(char mappingSetName[]);
```

## Description

Changes the dynamic mapping set that will be used for mapping in the CANoe Symbol Mapping dialog. Only the mapping relations contained in the given dynamic mapping set and in the static mapping set are considered.

## Return Values

-1, if no mapping set with the given name is found.

## Example

```c
on key '1'
{
  // Activate DataSet1 and map its contained mapping relations
  SymbolMappingSetDynamicMappingSet ("DataSet1");
}
```

## Availability

| Since Version |
|---|
