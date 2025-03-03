""""""

from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex("\\frac{d}{dx}f(x)g(x)=", "f(x)\\frac{d}{dx}g(x)", "+", "g(x)\\frac{d}{dx}f(x)")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait()


## LOGARITHMS ##

# Quotient Rule

class LogarithmQuotientRule(Scene):
    def construct(self):
        text=MathTex("\\log_{b}\\left(\\frac{a}{c}\\right)=", "\\log_{b}(a)", "-", "\\log_{b}(c)")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait()


# Product Rule

class LogarithmProductRule(Scene):
    def construct(self):
        text=MathTex("\\log_{b}(a \\cdot c)=", "\\log_{b}(a)", "+", "\\log_{b}(c)")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait()


# Power Rule

class LogarithmPowerRule(Scene):
    def construct(self):
        text=MathTex("\\log_{b}(a^{c})=", "c\\log_{b}(a)")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        self.play(Create(framebox1))
        self.wait()


# log5(9) - log5(11) = log5(x).

class LogarithmEquation1(Scene):
    def construct(self):
        text=MathTex("\\log_{5}(9)", "-", "\\log_{5}(11)", "=", "\\log_{5}(x)")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[0], buff = .1)
        framebox2 = SurroundingRectangle(text[2], buff = .1)
        framebox3 = SurroundingRectangle(text[4], buff = .1)
        self.play(Create(framebox1))
        self.wait()
        self.play(Create(framebox2))
        self.wait()
        self.play(Create(framebox3))
        self.wait()


# log2(x) + log2(11) = log2(55).

class LogarithmEquation2(Scene):
    def construct(self):
        text=MathTex("\\log_{2}(x)", "+", "\\log_{2}(11)", "=", "\\log_{2}(55)")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[0], buff = .1)
        framebox2 = SurroundingRectangle(text[2], buff = .1)
        framebox3 = SurroundingRectangle(text[4], buff = .1)
        self.play(Create(framebox1))
        self.wait()
        self.play(Create(framebox2))
        self.wait()
        self.play(Create(framebox3))
        self.wait()


# 2log9(5) = log9(x).

class LogarithmEquation3(Scene):
    def construct(self):
        text=MathTex("2\\log_{9}(5)", "=", "\\log_{9}(x)")
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[2], buff = .1)
        self.play(Create(framebox1))
        self.wait()
        self.play(Create(framebox2))
        self.wait()


class LogQuotientRuleAndExample(Scene):
    def construct(self):
        # 1) INTRO: Display the general Quotient Rule: log_b(a/c) = log_b(a) - log_b(c)
        title = Text("Quotient Rule for Logarithms", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait()

        quotient_rule = MathTex("\\log_{b}\\bigl(\\tfrac{a}{c}\\bigr)", "=", "\\log_{b}(a)", "-", "\\log_{b}(c)").shift(UP*1)

        self.play(Write(quotient_rule))
        self.wait()

        # Highlight the log_b(a) part
        frame_a = SurroundingRectangle(quotient_rule[2], buff = 0.1, color=YELLOW)
        self.play(Create(frame_a))
        self.wait()

        # Transform highlight to the log_b(c) part
        frame_c = SurroundingRectangle(quotient_rule[4], buff = 0.1, color=RED)
        self.play(ReplacementTransform(frame_a, frame_c))
        self.wait()

        # Fade out highlights
        self.play(FadeOut(frame_c))
        self.wait()

        # 2) EXAMPLE PROBLEM: log_5(9) - log_5(11) = log_5(x)
        example_title = Text("Apply to Example", font_size=36).next_to(title, DOWN, buff=0.8)
        self.play(Write(example_title))
        self.wait()

        # Write the expression: log_5(9) - log_5(11) = log_5(x)
        expr = MathTex("\\log_{5}(9)", "-", "\\log_{5}(11)", "=", "\\log_{5}(x)")
        expr.shift(DOWN*0.5)

        self.play(Write(expr))
        self.wait()

        # 3) Show how the left side can be combined via the Quotient Rule
        #    We'll highlight the left terms and then transform them
        left_side_brace = Brace(expr[:3], DOWN)
        left_side_text = left_side_brace.get_text("Combine via Quotient Rule")

        self.play(Create(left_side_brace), Write(left_side_text))
        self.wait()

        # Create a 'target' expression: log_5(9/11)
        combined_expr = MathTex("\\log_{5}\\bigl(\\frac{9}{11}\\bigr)")
        combined_expr.move_to(expr[:3].get_center())  # place it where the left side is

        # We'll transform log_5(9) - log_5(11) into log_5(9/11)
        self.play(
            ReplacementTransform(expr[:3].copy(), combined_expr),
            FadeOut(left_side_brace),
            FadeOut(left_side_text)
        )
        self.wait()

        # 4) So the entire equation becomes: log_5(9/11) = log_5(x)
        #    We'll replace the left side with the combined version.
        new_equation = MathTex("\\log_{5}\\bigl(\\tfrac{9}{11}\\bigr)", "=", "\\log_{5}(x)")
        new_equation.move_to(expr.get_center())

        self.play(
            ReplacementTransform(expr[:3], new_equation[0]),
            ReplacementTransform(expr[3], new_equation[1]),
            ReplacementTransform(expr[4], new_equation[2])
        )
        self.wait()

        # 5) Final step: Because log_5( A ) = log_5( x ), we deduce x = A
        #    In this case, A = 9/11

        conclude_text = Text("Hence, x = 9/11", font_size=36, color=GREEN).next_to(new_equation, DOWN, buff=0.5)
        self.play(Write(conclude_text))
        self.wait()

        # 6) Fade out everything if desired
        self.play(FadeOut(new_equation), FadeOut(conclude_text), FadeOut(title), FadeOut(example_title), FadeOut(quotient_rule))
        self.wait()


class LogProductRuleAndExample(Scene):
    def construct(self):
        # 1) INTRO: Display the general Product Rule: log_b(a*c) = log_b(a) + log_b(c)
        title = Text("Product Rule for Logarithms", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait()

        product_rule = MathTex(
            "\\log_{b}(a \\cdot c)", "=", "\\log_{b}(a)", "+", "\\log_{b}(c)"
        ).shift(UP)

        self.play(Write(product_rule))
        self.wait()

        # Highlight the log_b(a) part
        frame_a = SurroundingRectangle(product_rule[2], buff=0.1, color=YELLOW)
        self.play(Create(frame_a))
        self.wait()

        # Transform highlight to the log_b(c) part
        frame_c = SurroundingRectangle(product_rule[4], buff=0.1, color=RED)
        self.play(ReplacementTransform(frame_a, frame_c))
        self.wait()

        # Fade out the highlights
        self.play(FadeOut(frame_c))
        self.wait()

        # 2) EXAMPLE PROBLEM: log_2(x) + log_2(11) = log_2(55)
        example_title = Text("Apply to Example", font_size=36).next_to(title, DOWN, buff=0.8)
        self.play(Write(example_title))
        self.wait()

        expr = MathTex("\\log_{2}(x)", "+", "\\log_{2}(11)", "=", "\\log_{2}(55)")
        expr.shift(DOWN*0.5)

        self.play(Write(expr))
        self.wait()

        # 3) Show how the left side can be combined via the Product Rule
        left_brace = Brace(expr[:3], DOWN)
        left_text = left_brace.get_text("Combine via Product Rule")

        self.play(Create(left_brace), Write(left_text))
        self.wait()

        # We'll transform log_2(x) + log_2(11) into log_2(11x)
        combined_expr = MathTex("\\log_{2}(11x)")
        combined_expr.move_to(expr[:3].get_center())

        self.play(
            ReplacementTransform(expr[:3].copy(), combined_expr),
            FadeOut(left_brace),
            FadeOut(left_text)
        )
        self.wait()

        # 4) So the entire equation becomes: log_2(11x) = log_2(55)
        new_equation = MathTex("\\log_{2}(11x)", "=", "\\log_{2}(55)")
        new_equation.move_to(expr.get_center())

        self.play(
            ReplacementTransform(expr[:3], new_equation[0]),
            ReplacementTransform(expr[3], new_equation[1]),
            ReplacementTransform(expr[4], new_equation[2]),
        )
        self.wait()

        # 5) Final step: By one-to-one property, 11x = 55 => x = 5
        conclusion = Text("Hence, x = 5", font_size=36, color=GREEN).next_to(new_equation, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait()

        # Optional: Fade everything out to finish
        self.play(
            FadeOut(new_equation),
            FadeOut(conclusion),
            FadeOut(title),
            FadeOut(example_title),
            FadeOut(product_rule)
        )
        self.wait()


class LogPowerRuleAndExample(Scene):
    def construct(self):
        # 1) INTRO: Display the general Power Rule: log_b(a^c) = c log_b(a)
        title = Text("Power Rule for Logarithms", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait()

        power_rule = MathTex("\\log_{b}(a^{c})", "=", "c\\log_{b}(a)").shift(UP*1)
        self.play(Write(power_rule))
        self.wait()

        # Highlight the c log_b(a) part
        highlight_power = SurroundingRectangle(power_rule[2], buff=0.1, color=YELLOW)
        self.play(Create(highlight_power))
        self.wait()

        # Fade out the highlight
        self.play(FadeOut(highlight_power))
        self.wait()

        # 2) EXAMPLE PROBLEM: 2 log_9(5) = log_9(x)
        example_title = Text("Apply to Example", font_size=36).next_to(title, DOWN, buff=0.8)
        self.play(Write(example_title))
        self.wait()

        expr = MathTex("2\\log_{9}(5)", "=", "\\log_{9}(x)")
        expr.shift(DOWN*0.5)

        self.play(Write(expr))
        self.wait()

        # 3) Show how to rewrite 2 log_9(5) using the Power Rule => log_9(5^2)
        left_brace = Brace(expr[0], DOWN)
        left_text = left_brace.get_text("Use Power Rule").scale(0.8)

        self.play(Create(left_brace), Write(left_text))
        self.wait()

        # We'll transform 2 log_9(5) into log_9(5^2)
        combined_expr = MathTex("\\log_{9}(5^2)")
        combined_expr.move_to(expr[0].get_center())

        self.play(
            ReplacementTransform(expr[0].copy(), combined_expr),
            FadeOut(left_brace), FadeOut(left_text)
        )
        self.wait()

        # 4) Now the equation is log_9(5^2) = log_9(x)
        new_equation = MathTex("\\log_{9}(5^2)", "=", "\\log_{9}(x)")
        new_equation.move_to(expr.get_center())

        self.play(
            ReplacementTransform(expr[0], new_equation[0]),
            ReplacementTransform(expr[1], new_equation[1]),
            ReplacementTransform(expr[2], new_equation[2]),
        )
        self.wait()

        # 5) By the one-to-one property, 5^2 = x => x=25
        conclusion = Text("Hence, x = 25", font_size=36, color=GREEN).next_to(new_equation, DOWN, buff=0.5)
        self.play(Write(conclusion))
        self.wait()

        # Optional: Fade everything out
        self.play(
            FadeOut(new_equation),
            FadeOut(conclusion),
            FadeOut(power_rule),
            FadeOut(title),
            FadeOut(example_title)
        )
        self.wait()

