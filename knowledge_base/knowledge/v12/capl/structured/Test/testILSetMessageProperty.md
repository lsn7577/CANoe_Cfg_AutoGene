# testILSetMessageProperty

> Category: `Test` | Type: `function`

## Syntax

```c
long testILSetMessageProperty( dbNode node, dbMessage msg, char propertyName[], long propertyValue);
```

## Description

Sets the internal property of a message, assigned to the node.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Success (property has been set successfully)

## Example

```c
if (testILSetMessageProperty(EBS, TSC1, "MessageCounterToContinue", 12) < 0)
{
  write("Can’t set message property ‘MessageCounterToContinue‘");
}
```

## Availability

| Since Version |
|---|
