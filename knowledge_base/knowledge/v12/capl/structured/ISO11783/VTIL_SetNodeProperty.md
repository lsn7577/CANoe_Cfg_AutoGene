# VTIL_SetNodeProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_SetNodeProperty( char propertyName[], long propertyValue); // form 1
```

## Description

Changes an internal property of the node.

## Return Values

0: Property has been set successfully

## Example

```c
void SetNodeProperties()
{
  //Set language to English
  VTIL_SetNodeProperty(VT, "languageCode", 0x656E);
  // Object Pools have to be stored in the subdirectory "OP_VT1"
  VTIL_SetNodeProperty(VT, "locationOfStoredObjectPools", "OP_VT1");
}
```

## Availability

| Since Version |
|---|
