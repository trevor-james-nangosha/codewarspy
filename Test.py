from ast import Pass


class Test:
    def __init__(self):
        self.testedValue = 0
        self.expectedValue= 0
        self.passedTests = 0
        self.failedTests = 0

    def expect(self, testedValue, expectedValue):
        """The arguments that we want to test."""
        self.testedValue = testedValue
        self.expectedValue = expectedValue
        if self.testedValue == self.expectedValue:
            self.passedTests += 1
            print(f"{self.passedTests} test(s) passed......")
        elif not self.testedValue == self.expectedValue:
            self.failedTests += 1
            print(f"""
                {self.failedTests} test(s) failed.......
                expected {expectedValue} but got {testedValue}
            """)
 
    def toBe(self, argument):
        """The value we expect after executing the function."""
        pass