import importlib
import cProfile
import pstats
import problems
import pkgutil
import datetime
import logging

from common.primedb import PRIME_DB

from common.api import ProblemInfo
from time import perf_counter

from common.sequences import *
from common.tests import *
from common.theorems import *
from common.permutator import *
from common.fraction import *

class EulerManager():
    SLOW_TIME = 60
    OK_TIME = 10
    FAST_TIME = 1
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.problem_info = ProblemInfo()
        self.prime_load_time = perf_counter()
        self.PRIME_DB = PRIME_DB
        self.prime_load_time = perf_counter() - self.prime_load_time
        self.prof_timers = dict()
    
    def solve_all(self,start_from=None,stop_at=None):
        importlib.reload(problems)
        problems_answered = []
        for importer, modname, ispkg in pkgutil.iter_modules(problems.__path__):
            try:
                problems_answered.append(int(modname[-3:]))
            except ValueError:
                continue
            
        for p in sorted(problems_answered):
            if start_from and p < start_from:
                continue
            if stop_at and p > stop_at:
                break
            self.solve(p,False)
        
    def solve(self,n,silent=True):
        _locals = locals()
        _globals = globals()
        _globals["PRIME_DB"] = self.PRIME_DB
        load_time = perf_counter()
        exec(open("problems/euler{:03d}.py".format(n)).read(),_globals,_locals)
        load_time = perf_counter() - load_time
        with cProfile.Profile() as pr:
            exec_time = perf_counter()
            exec("r = euler{:03d}()".format(n),_globals,_locals)
            exec_time = perf_counter() - exec_time
        if exec_time > self.OK_TIME:
            pstats.Stats(pr).sort_stats(pstats.SortKey.TIME).dump_stats("prof/euler{:03d}.prof".format(n))
        if not "r" in _locals:
            _locals["r"] = None
            _locals["r_correct"] = False
        else:
            resp = self.problem_info.get_answer(n)
            if resp:
                _locals["r_correct"] = _locals["r"] == resp
            else:
                _locals["r_correct"] = None
        self.prof_timers[n] = (load_time,exec_time,_locals["r"],_locals["r_correct"],pstats.Stats(pr).sort_stats(pstats.SortKey.TIME))
        
        if not silent:
            self.print_summary(n)
        return _locals["r"]
    def print_summary(self,i):
        try:
            if not i in self.prof_timers:
                self.log.warning("Tried to get summary for problem %i, which wasn't calculated" % i)
                self.log.warning("executing solve(%i)" % i)
                self.solve(i)
            p = self.prof_timers[i]
            print("[{:03d}] Load: {: <10.6f}  Exec: {: <10.6f}  Answer: {!s:20}  Correct: {!s:6}".format(i,*p[:4]))
        except TypeError as t:
            self.log.error("TypeError: %s" % str(p))
        except Exception as e:
            raise e