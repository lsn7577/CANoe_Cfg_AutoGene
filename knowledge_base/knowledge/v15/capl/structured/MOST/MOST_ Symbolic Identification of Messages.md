# MOST: Symbolic Identification of Messages

> Category: `MOST` | Type: `notes`

## Description

For selected CAPL functions, e.g., mostAmsOutput, MOST messages can be described with the name used in the XML function catalog.

The symbolic definition of the message essentially follows the syntax that is used in the MOST specification. All variants are derived from the following basic form:

FBlock.Instance.Function.OpType(Parameter,Parameter,Parameter)

AudioAmplifier.1.Mute.Status(MuteOn)

Essentially it is possible to set raw data for the user data. Accordingly, the parameter bytes have to be set as hexadecimal values in curly brackets. This facilitates, for example, the sending of messages which do not comply with the definition in the function catalog.

Diagnosis.1.KeywordRec.Set({AABB11223344})

or pure numerical:

0x06.1.0x050.0x0({AABB11223344})

Press <Ctrl>+<M> or select Message input with MOST function catalog... from the shortcut menu to open an input assistant which displays a data entry field in the current program line listing a selection of all MOST messages described in the function catalog. The selection takes in all function catalogs assigned to the CAPL node.

In this context, the input assistant permits the description of messages up to OpType and adds the resulting description to the program text without quotation marks in the notation separated by period marks.

mostAMSOutput | mostMsgSet | Symbolic Identification of Parameters

| Example AudioAmplifier.1.Mute.Status(MuteOn) |
|---|

| Example Diagnosis.1.KeywordRec.Set({AABB11223344}) or pure numerical: 0x06.1.0x050.0x0({AABB11223344}) |
|---|

| Example Press <Ctrl>+<M> or select Message input with MOST function catalog... from the shortcut menu to open an input assistant which displays a data entry field in the current program line listing a selection of all MOST messages described in the function catalog. The selection takes in all function catalogs assigned to the CAPL node. In this context, the input assistant permits the description of messages up to OpType and adds the resulting description to the program text without quotation marks in the notation separated by period marks. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
