# lookupFrPDU

> Category: `Other` | Type: `function`

## Syntax

```c
dbFrPDU * lookupFrPDU(char pduName[]);
```

## Description

Searches for a FlexRay PDU definition in the database(s). If the PDU is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid dbFrPDU.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact real-time performance.

## Return Values

The found unique PDU definition or an invalid object.

## Availability

| Since Version |
|---|
