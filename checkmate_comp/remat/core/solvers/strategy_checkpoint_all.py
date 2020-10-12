from remat.core.dfgraph import DFGraph
from remat.core.schedule import ScheduledResult
from remat.core.utils.solver_common import gen_s_matrix_fixed_checkpoints, solve_r_opt
from remat.core.enum_strategy import SolveStrategy
from remat.core.utils.scheduler import schedule_from_rs
from remat.core.utils.timer import Timer


def solve_checkpoint_all(g: DFGraph):
    with Timer('solve_checkpoint_all') as timer_solve:
        s = gen_s_matrix_fixed_checkpoints(g, g.vfwd)
        r = solve_r_opt(g, s)
    schedule, aux_data = schedule_from_rs(g, r, s)
    return ScheduledResult(
        solve_strategy=SolveStrategy.CHECKPOINT_ALL,
        solver_budget=0,
        feasible=True,
        schedule=schedule,
        schedule_aux_data=aux_data,
        solve_time_s=timer_solve.elapsed
    )


def solve_checkpoint_all_ap(g: DFGraph):
    with Timer('solve_checkpoint_all') as timer_solve:
        s = gen_s_matrix_fixed_checkpoints(g, g.checkpoint_set)
        r = solve_r_opt(g, s)
    schedule, aux_data = schedule_from_rs(g, r, s)
    return ScheduledResult(
        solve_strategy=SolveStrategy.CHECKPOINT_ALL_AP,
        solver_budget=0,
        feasible=True,
        schedule=schedule,
        schedule_aux_data=aux_data,
        solve_time_s=timer_solve.elapsed
    )
