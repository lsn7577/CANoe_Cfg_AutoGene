# TestGetWaitPDUData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitPDUData (PDU * aPDU); // form 1
```

## Description

If a valid PDU is the last event that triggers a wait instruction, the PDU’s content can be called up with form 1.

Form 2 can only be used for joined events. The number of the joined event (return value of TestJoin...) is here being used as an index.

## Return Values

0: Data access successful.

## Availability

| Since Version |
|---|
