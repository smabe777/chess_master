
class Test:
    failures = 0
    def t_assert(self, stmt, result):
        if result : print(stmt, ": PASSED")
        else: 
            print(stmt, ": FAILED")
            self.failures += 1
    def test(self):
        pass
    def result(self):
        self.test()
  
        if self.failures > 0:
                print(f'Test {type(self).__name__} failed : {self.failures} failure(s)')
        else:
            print(f'Test {type(self).__name__} passed')

