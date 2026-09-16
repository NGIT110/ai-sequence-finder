## Question: 
"How can you identify a mathematical pattern's rule?"
 
## Hypothesis:
I assumed most sequences would be obvious by looking at the differences between terms and others would have unique special cases.

## Experiment 1:
Working through 6 sequences by hand, I quickly found out the rules due to prior mathematical knowledge:
1) 2, 4, 6, 8, 10 ; This was clearly 2n, by using the difference between 2 consecutive terms = 2.

2) 1, 4, 9, 16, 25 ; This one was also simple - I quickly identified that they were square numbers, following the rule n^2.

3) 2, 4, 8, 16, 32 ; I quickly identified that the terms were powers of 2 which followed the rule 2^n.

4) 1, 1, 2, 3, 5, 8, 13 ; The fibonnacci pattern was relatively easy to spot. However, through this project, I aim to figure out how we as humans are able to identify such patterns and whether this recognition process is just as simple for a computer.

5) 3, 6, 11, 18, 27 ; Due to my knowledge of quadratic sequences from GCSE, I was quickly able to identify that it was a sequence with n^2 as the second difference was 2 - meaning that by subtracting the square numbers from each of these terms, I was abel to identify that the sequence was n^2 + 2.

6) 2, 3, 5, 7, 11, 13 ; I initially struggled with this sequence, expecting a very difficult solution, until I noticed that they were all primes - this is another pattern that doesnt follow a tradititional rule - could a computer easily find this rule aswell?

## Experiment 2:
After briefly identifying a few simple sequences and their rules, I aimed to see if I could find alternate rules for sequence 2, in order to introduce a new question: Which rule best defines a specific sequence? Here was my thought process:
1) I was initially tunnel-visioned by idea of the differences between terms.
2) I then tried to think about recursive sequences (a sequence where each term is defined by applying a rule to one or more of the terms that came before it), but I still had no success despite 20 minutes of continuous testing.