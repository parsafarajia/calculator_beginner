from main import evaluate_infix, prefix_evaluator, postfix_evaluator, determine_expression_type
def test_evaluate_infix():
    """Test the infix evaluator."""
    assert evaluate_infix("3 + 5") == 8
    assert evaluate_infix("10 - 2 * 3") == 4
    assert evaluate_infix("2 ^ 3 + 1") == 9
    assert evaluate_infix("4 / 2 - 1") == 1.0
    assert evaluate_infix("5 + -6 * 2 + 3") == 19
    assert evaluate_infix("10 + -2") == 8
    assert evaluate_infix("10 * -2 + 3") == -17
    print("All tests passed!")
def test_prefix_evaluator():
    """Test the prefix evaluator."""
    assert prefix_evaluator("+ 3 5") == 8
    assert prefix_evaluator("- 10 * 2 3") == 4
    assert prefix_evaluator("+ ^ 2 3 1") == 9
    assert prefix_evaluator("- / 4 2 1") == 1.0
    assert prefix_evaluator("+ 5 * -6 2 3") == 19
    assert prefix_evaluator("+ 10 -2") == 8
    assert prefix_evaluator("+ 10 * -2 3") == -17
    print("All tests passed!")
def test_postfix_evaluator():
    """Test the postfix evaluator."""
    assert postfix_evaluator("3 5 +") == 8
    assert postfix_evaluator("10 2 3 * -") == 4
    assert postfix_evaluator("2 3 ^ 1 +") == 9
    assert postfix_evaluator("4 2 / 1 -") == 1.0
    assert postfix_evaluator("5 -6 2 * 3 +") == 19
    assert postfix_evaluator("10 -2 +") == 8
    assert postfix_evaluator("10 -2 * 3 +") == -17
    print("All tests passed!")
def test_determine_expression_type():
    """Test the expression type determination."""
    assert determine_expression_type("+ 3 5") == 'prefix'
    assert determine_expression_type("3 5 +") == 'postfix'
    assert determine_expression_type("3 + 5") == 'infix'
    assert determine_expression_type("- 10 * 2 3") == 'prefix'
    assert determine_expression_type("10 2 3 * -") == 'postfix'
    assert determine_expression_type("10 - 2") == 'infix'
    print("All tests passed!")
if __name__ == "__main__":
    test_evaluate_infix()
    test_prefix_evaluator()
    test_postfix_evaluator()
    test_determine_expression_type()
    print("All tests completed successfully!")
    # Ensure all tests pass before running the main function
    from main import main
    main()
# Ensure all tests pass before running the main function    

