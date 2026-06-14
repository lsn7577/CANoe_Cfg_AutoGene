# FSIL_SetNodeProperty

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_SetNodeProperty( char propertyName[], long propertyValue); // form 1
```

## Description

Changes an internal property of the File Server node.

## Return Values

0: Property has been set successfully

## Example

```c
void SetNodeProperties()
{
  // Set File Server version 3
  FSIL_SetNodeProperty(FS, "fsVersion", 3);
  // Set root directory for file server volumes
  FSIL_SetNodeProperty (FS, "rootDirectory", "ISOBUS_FSRootDir");
}
```

## Availability

| Since Version |
|---|
