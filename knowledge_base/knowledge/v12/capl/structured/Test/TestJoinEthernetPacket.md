# TestJoinEthernetPacket

> Category: `Test` | Type: `function`

## Syntax

```c
long TestJoinEthernetPacket(qword sMAC, qword dMAC, word vlanID, word etherType, dword flags, dword aTimeout); // form 1
```

## Description

Completes the current set of "joined events" with the transmitted event. This function does not wait.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

## Return Values

0: Data access successful

## Availability

| Since Version |
|---|
