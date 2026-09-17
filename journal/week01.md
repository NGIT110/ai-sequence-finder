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

5) 3, 6, 11, 18, 27 ; Due to my knowledge of quadratic sequences from GCSE, I was quickly able to identify that it was a sequence with n^2 as the second difference was 2 - meaning that by subtracting the square numbers from each of these terms, I was able to identify that the sequence was n^2 + 2.

6) 2, 3, 5, 7, 11, 13 ; I initially struggled with this sequence, expecting a very difficult solution, until I noticed that they were all primes - this is another pattern that doesnt follow a traditional rule - could a computer easily find this rule aswell?

## Experiment 2:
After briefly identifying a few simple sequences and their rules, I aimed to see if I could find alternate rules for sequence 2, in order to introduce a new question: Which rule best defines a specific sequence? Here was my thought process:
1) I was initially tunnel-visioned by idea of the differences between terms.
2) I then tried to think about recursive sequences (a sequence where each term is defined by applying a rule to one or more of the terms that came before it), but I still had no success despite 20 minutes of continuous testing.
3) In the end, I was unable to come up with any other rules, so I did some research.

## Research:
I found many other ways of expressing this sequence:
1) Adding consecutive odd numbers: start at 1, and then add the next consective odd number to get the next term; this is quite a unique rule, one that a computer might not easily be able to find.
2) Recursive Rule: a(n+1) = a(n) + 2n + 1 given a(1) = 1; This proved that my instinct of a recursive rule was correct.
3) Poynomial Interlacing rule: Uses the __Lagrange Polynomial interpolation__ to form a rule that fits the first 5 numbers but then diverges from the pattern in the 6th term. This is by far the most intriguing method, and most likely the method, I will be spending most time implementing in the future.

## Conclusion and New Question:
The moment I realised Lagrange interpolation could construct a function that "agrees" with n² for as many terms as I like, then diverges exactly where I choose — that's when the ambiguity problem stopped being abstract and became something I could actually build. It also opened the horizon to a new question: If infinitely many rules can fit the same data, how should an algorithm choose between them.