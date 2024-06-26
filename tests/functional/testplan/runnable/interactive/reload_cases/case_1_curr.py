from testplan.runners.pools.tasks.base import task_target
from testplan.testing.multitest import MultiTest, testcase, testsuite


@task_target
def dummy_test():
    return MultiTest(name="dummy_test", suites=[Suite()])


@testsuite
class Suite:
    @testcase(parameters=range(3))
    def case_1(self, env, result, arg):
        result.true(True)
