from behave import given, when, then
from Donation_System import DonationSystem


@given('the donation system is running')
def step_system_running(context):
    context.system = DonationSystem()
    context.error_message = None


@when('a donor named "{donor_name}" contributes {amount:d}')
def step_donor_contributes(context, donor_name, amount):
    try:
        context.system.add_donation(donor_name, amount)
    except ValueError as error:
        context.error_message = str(error)


@then('the total donations should be {expected_total:d}')
def step_total_should_be(context, expected_total):
    actual_total = context.system.get_total_donations()
    assert actual_total == expected_total, (
        f"Expected total {expected_total}, but got {actual_total}"
    )


@then('the donation count should be {expected_count:d}')
def step_count_should_be(context, expected_count):
    actual_count = context.system.get_donation_count()
    assert actual_count == expected_count, (
        f"Expected count {expected_count}, but got {actual_count}"
    )


@then('an error message should be displayed')
def step_error_should_display(context):
    assert context.error_message is not None
    assert context.error_message == "Donation amount must be greater than zero"