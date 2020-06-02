# Multi-Bracket Validation
[Table of Contents](../../../README.md)
## Challenge 13
Multi-Bracket Validation is a challenge to verify that an inputed string has balanced brackets. It will return a boolean representing whether or not the brackets in the string are balanced. There are three types of brackets:
- Round Brackets: `()`
- Square Brackets: `[]`
- Curly Brackets: `{}`

### Examples:
`multi_bracket_validation(input)`
|Input|Output|
|:-----:|:-----:|
|`{}`|`True`|
|`{}(){}`|`True`|
|`()[[Extra Characters]]`|`True`|
|`(){}[[]]`|`True`|
|`{}{Code}[Fellows](())`|`True`|
|`[({}]`|`False`|
|`(](`|`False`|
|`{(})`|`False`|

## Approach & Efficiency
I start off this challenge by strictly counting opening and closing brackets and ensure that there is an even number of these before diving deeper into the alogrithm. If they are not even we already know they are not balanced so return False. Once inside we will create a few lists utilizing two loops and two arrays. O(n) to make our first list which will be space of 0(1). Then we loop over that list if its an open bracket lets add it to another list, if its a closing , check the open bracket list last item pairs with the open bracket. If so, pop it off. So overall there are a few O(n) operations of efficiency and O(2) space used. I will ask how to truely calculate this in next lecture.

## Solution
![White Board Image](../../../assets/multi_bracket_validation.png)
