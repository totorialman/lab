from behave import given, when, then
from main import solving

@given('coefficients a={a}, b={b}, c={c}')
def set_coefficients(context, a, b, c):
    context.coefficients = (int(a), int(b), int(c))

@when('I solve the quadratic equation')
def solve_quadratic(context):
    context.result = solving(*context.coefficients)

@then('the solutions should be {x1} and {x2}')
def check_solutions(context, x1, x2):
    expected_result = (float(x1), float(x2))
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"

@then('the solution should be {x}')
def check_solution(context, x):
    expected_result = float(x)
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"

@then('there should be no real roots')
def check_no_real_roots(context):
    assert context.result == "No real roots", f"Expected 'Нет действительных корней', but got {context.result}"