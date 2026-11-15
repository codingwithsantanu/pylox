from .expr import *

class AstPrinter(ExprVisitor):
    def expression(self, expr: Expr) -> str:
        return expr.visit(self)

    def visit_binary_expr(self, expr: BinaryExpr) -> str:
        left: str = self.expression(expr.left)
        operator: str = expr.operator.lexeme
        right: str = self.expression(expr.right)

        return f"(binary {left} {operator} {right})"

    def visit_grouping_expr(self, expr: GroupingExpr) -> str:
        value: str = self.expression(expr.expression)
        return f"(group {value})"

    def visit_unary_expr(self, expr: UnaryExpr) -> str:
        value: str = self.expression(expr.expression)
        operator: str = expr.operator.lexeme
        return f"(unary {operator} {value})"

    def visit_literal_expr(self, expr: LiteralExpr) -> str:
        match expr.value:
            case float():
                return f"(literal {str(expr.value)})"
            case bool():
                return f"(literal {str(expr.value).lower()})"
            case str():
                return f"(literal \"{expr.value}\")"
            case None:
                return f"(literal nil)"
            case _:
                raise TypeError("Literals must be of type float, bool, str, or None.")
                return "ERROR" # Unnecessary, but for some linters.

