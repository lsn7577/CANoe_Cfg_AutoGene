# VTIL_GetChildObjectId

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long VTIL_GetChildObjectId(dbNode workingSetMaster, dword objectId, dword index, long & childObjectId); // form 1
```

## Description

Returns the ID of an object which is contained by a parent object.

You can obtain the number of child objects with method VTIL_GetNumberOfChildObjects.

## Return Values

0: Function has been executed successfully

## Example

```c
dword index, numberOfChildObjects;
long childObjectId;

//iterate over all children of the object with objectId = 1000
if (VTIL_GetNumberOfChildObjects(VT, Loader, 1000, numberOfChildObjects) == 0)
{
  for (index = 0; index < numberOfChildObjects; ++index)
  {
    if (VTIL_GetChildObjectId(VT, Loader, 1000, index, childObjectId) == 0)
    {
      Write("ID of child object at index %u is %i", index, childObjectId);
    }
  }
}
```

## Availability

| Since Version |
|---|
