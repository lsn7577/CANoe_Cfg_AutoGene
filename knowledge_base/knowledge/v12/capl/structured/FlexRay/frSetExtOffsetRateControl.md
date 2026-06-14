# frSetExtOffsetRateControl

> Category: `FlexRay` | Type: `function`

## Syntax

```c
int frSetExtOffsetRateControl(int aChannel, int aRateCtrl, int anOffsetCtrl)
```

## Description

Applies the external rate and offset correction values from the FlexRay parameters for the next cycle. For a description and explanation of the external clock correction procedure please refer to the FlexRay specification and/or to the user manual for the E-Ray communication controller.

The function is used in the following sample configuration:

2 Cluster Gateway – FlexRay_2Cluster_Gateway.cfgDemonstrates a FlexRay-FlexRay gateway with manipulation of the routed data and the (optional) synchronization of both FlexRay clusters.

## Return Values

0: Success

## Availability

| Since Version |
|---|
