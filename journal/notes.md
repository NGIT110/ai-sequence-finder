### Newton's Forward Difference Formula
Newton's forward difference formula is used to estimate intermediate values of a function when the given data points are equally spaced. It is optimized for interpolating values near the beginning of a data table.

Think of this formula as a highly accurate way to fill in the blanks of a data table. If you have a list of matching (x) and (y) numbers (like years and population sizes), this formula helps you guess the exact (y) value for an (x) value that sits somewhere in between your data points.

Instead of just guessing a straight line between two points, Newton's formula looks at how the trends change over time. It calculates differences:
1. First Differences (\(\Delta y\)): How much does \(y\) change from one step to the next? (e.g., \(y_2 - y_1\))
2. Second Differences (\(\Delta ^{2}y\)): How much does the rate of change itself accelerate or slow down? (Like tracking if a car is speeding up or braking).
3. Higher Differences: Looking at deeper and deeper patterns in the numbers.

## Trees
A tree is a foundational, non-linear, hierarchical data structure composed of collection entities called nodes that are connected by edges. Unlike linear structures like arrays, stacks, or linked lists, trees store data in a structural parent-child hierarchy with no loops or cycles.

• Root: The single topmost node in a tree that has no incoming edges (no parent). Every traversal starts here.
• Edge: The link or pointer connecting one node to another, representing their relationship.
• Parent / Child: A node directly above another is its parent; the node below it is its child.
• Leaf: Nodes located at the absolute bottom of a tree that have zero outgoing edges (no children).
• Subtree: A standalone tree structure nested within a larger tree, consisting of a node and all of its descendants.
• Height: The maximum number of edges from a specific node down to the furthest leaf. The height of the entire tree is the height of its root.
• Depth: The number of edges from the root node to a specific node.

