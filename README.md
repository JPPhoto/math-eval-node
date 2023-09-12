# math-eval-node
This is an InvokeAI 3.1-compatible node for performing arbitrary mathematical computations.
This InvokeAI node takes in four floating point numbers and lets you type in four equations that represent the output values. In addition to built-in mathematical operations (`+`, `-`, `*`, `/`, `min`, `max`) and nesting (with parentheses), you have full access to the `math` library from within your equations.

:warning: **This node uses the python function `eval()`**: This function can be exploited by malicious users. Always check the values if you're sent a workflow to use that uses this node. The author claims no responsibility for any consequences.
