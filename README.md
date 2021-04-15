# Roll the Dice

> Plover text macros to roll dice, flip a coin, and take chances.

## Installation

Install from the Plover plugins manager.

## Usage

| Meta / Macro Name | Description |
| ---- | ---- |
| `{:roll:range:0:100}` | Get a random integer in the provided range. |
| `{:roll:choice:option1:option2:etc}` | Randomly select a choice from the options provided. |
| `{:roll:d6}` | Roll a six-sided die. You can replace "6" with any positive whole number. Equivalent to `{:roll:range:1:6}`. |
| `{:roll:d10}` | Roll a 10-sided die. Equivalent to `{:roll:range:0:9}`. |
| `{:roll:d20}` | Roll a 20-sided die. Equivalent to `{:roll:range:1:20}`. |
| `{:roll:coin}` | Flip a coin. Equivalent to `{:roll:choice:heads:tails}`. |
| `{:roll:8ball}` | Ask the Magic 8-Ball a question. |

## Examples

You can mix these metas into your text.

```json
{
  "RO*L": "I roll a d20... the result is {:roll:d20}",
  "KO*EUPB": "Heads or tails{?}{:roll:coin}{!}",
  "SAO*UR": "{:roll:choice:yep:sure:okay:fine by me}"
}
```
