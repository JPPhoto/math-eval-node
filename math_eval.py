# Copyright (c) 2023 Jonathan S. Pollack (https://github.com/JPPhoto)

import math

from invokeai.app.invocations.baseinvocation import (
    BaseInvocation,
    BaseInvocationOutput,
    InputField,
    InvocationContext,
    OutputField,
    invocation,
    invocation_output,
)


@invocation_output("math_eval_output")
class MathEvalOutput(BaseInvocationOutput):
    """Base class for math output"""

    a: float = OutputField(description="Output a")
    b: float = OutputField(description="Output b")
    c: float = OutputField(description="Output c")
    d: float = OutputField(description="Output d")


@invocation("math_eval", title="MathEval", tags=["math_eval"], version="1.0.0")
class MathEvalInvocation(BaseInvocation):
    """Performs arbitrary user-defined calculations on x, y, z, and w variables"""

    x: float = InputField(default=0.0, description="Input x")
    y: float = InputField(default=0.0, description="Input y")
    z: float = InputField(default=0.0, description="Input z")
    w: float = InputField(default=0.0, description="Input w")
    equation_a: str = InputField(
        default="math.sin(x)", description="A basic mathematical equation for a involving x, y, z, and w"
    )
    equation_b: str = InputField(
        default="1+(x*y)", description="A basic mathematical equation for b involving x, y, z, and w"
    )
    equation_c: str = InputField(default="", description="A basic mathematical equation for c involving x, y, z, and w")
    equation_d: str = InputField(default="", description="A basic mathematical equation for d involving x, y, z, and w")

    def safe_eval(self, equation):
        result = 0
        if len(equation) > 0:
            my_dict = {}
            my_dict["math"] = math
            my_dict["min"] = min
            my_dict["max"] = max
            my_dict["x"] = self.x
            my_dict["y"] = self.y
            my_dict["z"] = self.z
            my_dict["w"] = self.w
            result = eval(equation, {"__builtins__": None}, my_dict)
        return result

    def invoke(self, context: InvocationContext) -> MathEvalOutput:
        return MathEvalOutput(
            a=self.safe_eval(self.equation_a),
            b=self.safe_eval(self.equation_b),
            c=self.safe_eval(self.equation_c),
            d=self.safe_eval(self.equation_d),
        )
