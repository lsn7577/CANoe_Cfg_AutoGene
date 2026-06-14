# lookupNode

> Category: `Other` | Type: `function`

## Syntax

```c
dbNode * lookupNode(char nodeName[]);
```

## Description

Searches for a node definition in the database(s). If the node is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid dbNode.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact real-time performance.

## Return Values

The found unique node definition or an invalid object.

## Availability

| Since Version |
|---|
