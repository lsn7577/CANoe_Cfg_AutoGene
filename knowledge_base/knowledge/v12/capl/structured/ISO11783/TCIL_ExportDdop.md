# TCIL_ExportDdop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_ExportDdop(dbNode client, char[] ddopPath[]); // form 1
```

## Description

Exports the device descriptor object pool of the Task Controller client into a file.

## Return Values

0: Function has been executed successfully

## Example

```c
Example (*)
long result;
result =  TCIL_ExportDdop( TC, "xml\\sprayerV1.xml");
if (result < 0)
{
  TestStepFail("Failed to export DDOP!");
}
```

## Availability

| Since Version |
|---|
