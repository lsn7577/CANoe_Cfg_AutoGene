# mostAllocTableGetSize

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAllocTableGetSize(long channel)
```

## Return Values

>= 0: Number of entries.

## Example

List all connection labels in the Write Window on change of the allocation table.

```c
OnMostAllocTable()
{
   long numEntries, labelWidth, label, i;
   numEntries = mostAllocTableGetSize(mostEventChannel());
   write("%f s: OnMostAllocTable(): Number of allocated labels: %d", mostEventTimeNs()/1.0e9, numEntries);
   for(i = 0; i < numEntries; ++i)
   {
      write("  Label: %03X  Width: %d", mostAllocTableGetCL(mostEventChannel(), i), mostAllocTableGetWidth(mostEventChannel(), i));
   }
}
```

## Availability

| Since Version |
|---|
