# frConfiguration

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frConfiguration <configuration var>;
```

## Description

Can be used to create a FlexRay parameter object. The data content of this object is all protocol parameters relevant to FlexRay in the context of initializing a FlexRay Communication Controller. The object data can be manipulated or read out by selectors associated with this object.

Initially, all protocol parameters are set to a value of 0.

The frGetConfiguration or frSetConfiguration functions are used to read or set parameters from or in the FlexRay interface’s Communication Controller.

## Availability

| Since Version |
|---|
