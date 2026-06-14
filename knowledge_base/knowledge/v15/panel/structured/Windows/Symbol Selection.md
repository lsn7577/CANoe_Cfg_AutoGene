# Symbol Selection

> Category: `Panel` | Subcategory: `Windows` | Type: `concept`

The Symbol Selection dialog displays the loaded databases as a tree view. You can select single symbol and assign it to the control.

Depending on the database this dialog contains branches for signals, messages, nodes, environment variables, application layer objects (CO, DO), system variables or diagnostic parameters and diagnostic services. These branches are divided into sub-branches until the symbols to be selected are reached. When selecting diagnostic parameters the services are listed and beneath the parameters transported in the primitives. The display is divided in classes and services . With you can select if the names (longname) or qualifiers (shortname) should be displayed.

Within the nodes you can differentiate between transmit/receive messages/signals and "transmit and receive" messages/signals.

This dialog offers various ways to reach the same symbol. For example, you can select a symbol directly from the signal or message list, or you can search for the symbol from a specific node.

With you can collapse the tree view.

The found symbols are selected by mouse or keyboard and are chosen by the [Accept] button or by [OK].

## Aggregations

For simplified usage the following elements are merged to form aggregations:

The following editors are available for selecting the elements to be included in an aggregation.

## List Editor

The List Editor can be used to select one or more elements. For networks and special arrays for selecting a point in time multiple elements can be selected.

For selecting a single element, click with the mouse on the desired element.

For selecting multiple elements, proceed as follows:

Example for List Editors

Network

Array

| Example for List Editors Network Array | Network | Array |
|---|---|---|
| Network | Array |  |

| Network | Array |
|---|---|

## Combined Array Selection

In addition to selecting individual or multiple arrays using the mouse button, you can also specify individual elements as text separated by a comma, specify several successive elements joined by a hyphen (e. g. 5-7), or you can use a combination of both options.

Example

| Example |
|---|

## Unspecified Array Selection

For Some/IP there are arrays whose number of elements is unknown when elements are selected. For these arrays, you can only determine the index via a text field and not via multi-selection. The arrays may be multi-dimensional as well. In this case, you can specify individual dimensions separated by a comma.

Example

| Example |
|---|

## Dynamic Arrays

For communication objects and distributed objects there are arrays whose number of elements can be dynamic. For these arrays, the length of the array is displayed as file in the tree view. This allows you to drag this property onto a panel and edit it.

Example

| Example |
|---|

## General

For arrays, you can click on [Collapse Items]/[Expand Items] to collapse/expand the aggregated view.

Aggregations can also be nested. This allows for selecting a comprehensive set of elements according to the individual needs.

Example

Drag and drop the selected elements:

The following elements are moved when using drag and drop:

| Example Drag and drop the selected elements: The following elements are moved when using drag and drop: StructVars/ArrayOfArrayStructVar[0]/arrayOfStructs[0]/floatMember StructVars/ArrayOfArrayStructVar[0]/arrayOfStructs[0]/shortMember StructVars/ArrayOfArrayStructVar[0]/arrayOfStructs[1]/floatMember StructVars/ArrayOfArrayStructVar[0]/arrayOfStructs[1]/shortMember StructVars/ArrayOfArrayStructVar[1]/arrayOfStructs[0]/floatMember StructVars/ArrayOfArrayStructVar[1]/arrayOfStructs[0]/shortMember StructVars/ArrayOfArrayStructVar[1]/arrayOfStructs[1]/floatMember StructVars/ArrayOfArrayStructVar[1]/arrayOfStructs[1]/shortMember |
|---|

## Search Options

You can search for a word or part of a word using the input field of the search . All existing texts in all columns are taken into account.

The tree view will be filtered by matches during entry. The filtered matches are highlighted in color. The tree view does not contain any entries if no match is found in it. You can delete the search entry using . The tree view will be shown completely.

The most recently used search terms can be selected again via a selection list.

The wildcards * and ? are supported. The texts will be searched for character strings.

## Partially Canceling the Search

When you search for an element in the Symbol Explorer, only the matches (Phase on the image) will be shown in the tree view.

If you would like to know which element is located Console_2 for example, you can use the context menu Suspend Search to partially cancel the search. That means all the sub-elements for Console_2 will now be displayed.

If you have partially canceled a search, the search term will no longer be highlighted. The element from which the search was canceled is marked with the symbol.

With the context menu Resume Search you can resume the partial search.

You can cancel and resume the partial search for several subtrees.

## Available Columns

In the according selection dialog there are columns available for a more detailed description of each object. These columns can be enabled/disabled by a right mouse click in the column title. In the following menu you can enable/disable the desired columns. You may sort the selectable objects by double-clicking the column title.

Symbol Explorer
