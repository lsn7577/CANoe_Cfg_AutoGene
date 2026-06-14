# lookupFrFrame

> Category: `Other` | Type: `function`

## Syntax

```c
dbFrFrame * lookupFrFrame(char frameName[]);
```

## Description

Searches for a FlexRay frame definition in the database(s). If the frame is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid dbFrFrame.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact real-time performance.

## Return Values

The found unique frame definition or an invalid object.

## Availability

| Since Version |
|---|
