Feature: Solving quadratic equations

Scenario: Quadratic equation with two real roots
    Given coefficients a=1, b=-3, c=2
    When I solve the quadratic equation
    Then the solutions should be 2 and 1

Scenario: Quadratic equation with one real root
    Given coefficients a=1, b=-2, c=1
    When I solve the quadratic equation
    Then the solution should be 1

Scenario: Quadratic equation with no real roots
    Given coefficients a=1, b=2, c=5
    When I solve the quadratic equation
    Then there should be no real roots

Scenario: Quadratic equation with positive discriminant
    Given coefficients a=1, b=-1, c=-6
    When I solve the quadratic equation
    Then the solutions should be 3 and -2

Scenario: Quadratic equation with fractional roots
    Given coefficients a=2, b=7, c=3
    When I solve the quadratic equation
    Then the solutions should be -0.5 and -3