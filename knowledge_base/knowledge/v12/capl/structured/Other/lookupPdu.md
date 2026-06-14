# lookupPdu

> Category: `Other` | Type: `function`

## Syntax

```c
dbPDU * lookupPDU(char pduName[]);
```

## Description

Searches for a PDU definition in the database(s). If the PDU is not found or if the name is not unique, test modules/units report an error in test system while simulation/analysis nodes write a warning into the Write Window, and the function returns an invalid dbPDU.

It is recommended to use this function only in special cases or during measurement start, since searching for the database definition may impact realtime performance.

## Return Values

The found unique PDU definition or an invalid object.

## Availability

| Since Version |
|---|
