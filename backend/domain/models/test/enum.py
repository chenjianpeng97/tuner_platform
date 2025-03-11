from enum import StrEnum

class TestRunScenarioStatusEnum(StrEnum):
    PASSED = "Passed"
    FAILED = "Failed"
    WORK_IN_PROGRESS = "Work in Progress"
    BLOCKED = "Blocked"
    RETEST = "Retest"
    SKIPPED = "Skipped"
    NOT_RUN = "Not Run"
class TestRunStepStatusEnum(StrEnum):
    PASSED = "passed"
    FAILED = "failed"
    UNDEFINED = "undefined"