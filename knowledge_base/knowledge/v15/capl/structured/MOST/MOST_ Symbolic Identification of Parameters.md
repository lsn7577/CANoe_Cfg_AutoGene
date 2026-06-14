# MOST: Symbolic Identification of Parameters

> Category: `MOST` | Type: `notes`

## Description

For selected CAPL functions, e.g., mostParamGet, MOST messages can be described with the name used in the XML function catalog.

The current content of the message to which the CAPL function, e.g., mostParamSet, refers determines which definition in the function catalog the parameter description is compared with.

With simple parameters, the parameter name is sufficient for identification. With structured parameter types, the path to the elementary parameter must be specified.

Taking the AudioDiskPlayer(0x31) function block as an example, the parameter descriptions for a number of parameter types can be explained.

Property: DeckStatus (0x200)

Parameter name: DeckStatus

Property: TimePosition (0x201)

Parameter name: Data.TrackTime

The POS parameter that belongs to the record must be set so that the TrackTime parameter is part of the message. If this is the case, the parameter value is written to the correct place in the message, regardless of whether the entire record is a part of the message or only the record field: TrackTime.

Property: MediaInfo (0x413)

Parameter name: Data.Record[2].MediaType

The index of the array element is specified in square brackets and attached to the name of the array element. The associated POS parameter must be set so that the array element is part of the message. The parameter is MediaType irrespective of whether the entire array or only an element is part of the message.

As an alternative, the functions for accessing parameters permit the specification of the parameter index as an additional parameter inside the brackets of the parameter address instead (see the <arrayIndex> parameter in mostParamSet). This index declaration overwrites the indexing in the brackets of the parameter address.

mostAmsMessage AudioDiskPlayer.MediaInfo.Status msgmostParamSet(msg, "Data", 2); // sets the array size to 2mostParamSet(msg, "Data.Record[].MediaType", 2, 1); // sets the parameter 'MediaType' in the second array element to 1

Parameter name: Data

The size (number of elements) of arrays can be set or read with mostParamSet() and mostParamGet().

mostAmsMessage AudioDiskPlayer.MediaInfo.Status msgmostParamSet(msg, "Data", 3);

The "Data" parameter now contains 3 elements (here: 3 records).

Property: FBlockIDs (0x000) from function block NetBlock

Parameter name: FBlockIDList

The size (number of elements) of a sequence can also be set or read with mostParamSet() and mostParamGet().

mostAmsMessage NetBlock.FBlockIDs.Status msgmostParamSet(msg, "FBlockIDList", 3);

The "FBlockIDList" parameter now contains 3 elements (here: 3 entries with {FBlockID, InstID}).

The parameters can be set as follows:

mostParamSet(msg, "FBlockIDList.FBlockID[]", 1, 0x02);mostParamSet(msg, "FBlockIDList.InstID[]", 1, 0x00);mostParamSet(msg, "FBlockIDList.FBlockID[]", 2, 0x04);mostParamSet(msg, "FBlockIDList.InstID[]", 2, 0x01);

Press <Ctrl>+<W> or select Signal insertion from MOST function catalog... from the shortcut menu to open a selection dialog listing all messages and their parameters from the function catalog for selection.

In this context the parameter identification is inserted into the program text as a string enclosed inside quotation marks.

Test Feature Set: Symbolic Definition of MOST Messages | Symbolic Identification of Messages

| Note The POS parameter that belongs to the record must be set so that the TrackTime parameter is part of the message. If this is the case, the parameter value is written to the correct place in the message, regardless of whether the entire record is a part of the message or only the record field: TrackTime. |
|---|

| Example mostAmsMessage AudioDiskPlayer.MediaInfo.Status msgmostParamSet(msg, "Data", 2); // sets the array size to 2mostParamSet(msg, "Data.Record[].MediaType", 2, 1); // sets the parameter 'MediaType' in the second array element to 1 |
|---|

| Example mostAmsMessage AudioDiskPlayer.MediaInfo.Status msgmostParamSet(msg, "Data", 3); The "Data" parameter now contains 3 elements (here: 3 records). |
|---|

| Example mostAmsMessage NetBlock.FBlockIDs.Status msgmostParamSet(msg, "FBlockIDList", 3); The "FBlockIDList" parameter now contains 3 elements (here: 3 entries with {FBlockID, InstID}). The parameters can be set as follows: mostParamSet(msg, "FBlockIDList.FBlockID[]", 1, 0x02);mostParamSet(msg, "FBlockIDList.InstID[]", 1, 0x00);mostParamSet(msg, "FBlockIDList.FBlockID[]", 2, 0x04);mostParamSet(msg, "FBlockIDList.InstID[]", 2, 0x01); |
|---|

| Example Press <Ctrl>+<W> or select Signal insertion from MOST function catalog... from the shortcut menu to open a selection dialog listing all messages and their parameters from the function catalog for selection. In this context the parameter identification is inserted into the program text as a string enclosed inside quotation marks. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
