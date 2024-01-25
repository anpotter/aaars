# default relation handlers
# for reenact and composition algorithms

import sys
def get_rel_name(argv):
    return sys._getframe(1).f_code.co_name

def adversative_antithesis(*argv): return get_rel_name(argv), argv
def adversative_concession(*argv): return get_rel_name(argv), argv
def adversative_contrast(*argv): return get_rel_name(argv), argv
def antithesis(*argv): return get_rel_name(argv), argv
def attribution(*argv): return get_rel_name(argv), argv
def attribution_negative(*argv): return get_rel_name(argv), argv
def attribution_positive(*argv): return get_rel_name(argv), argv
def background(*argv): return get_rel_name(argv), argv
def causal_cause(*argv): return get_rel_name(argv), argv
def causal_result(*argv): return get_rel_name(argv), argv
def cause(*argv): return get_rel_name(argv), argv
def circumstance(*argv): return get_rel_name(argv), argv
def concession(*argv): return get_rel_name(argv), argv
def condition(*argv): return get_rel_name(argv), argv
def conjunction(*argv): return get_rel_name(argv), argv
def context_background(*argv): return get_rel_name(argv), argv
def context_circumstance(*argv): return get_rel_name(argv), argv
def contingency_condition(*argv): return get_rel_name(argv), argv
def contrast(*argv): return get_rel_name(argv), argv
def convergence(*argv): return get_rel_name(argv), argv
def disjunction(*argv): return get_rel_name(argv), argv
def e_elaboration(*argv): return get_rel_name(argv), argv
def elaboration(*argv): return get_rel_name(argv), argv
def elaboration_additional(*argv): return get_rel_name(argv), argv
def elaboration_attribute(*argv): return get_rel_name(argv), argv
def elaboration_additional_e(*argv): return get_rel_name(argv), argv
def enablement(*argv): return get_rel_name(argv), argv
def evaluation(*argv): return get_rel_name(argv), argv
def evaluation_comment(*argv): return get_rel_name(argv), argv
def evaluation_n(*argv): return get_rel_name(argv), argv
def evaluation_s(*argv): return get_rel_name(argv), argv
def evidence(*argv): return get_rel_name(argv), argv
def explanation_evidence(*argv): return get_rel_name(argv), argv
def explanation_justify(*argv): return get_rel_name(argv), argv
def explanation_motivation(*argv): return get_rel_name(argv), argv
def interpretation(*argv): return get_rel_name(argv), argv
def joint(*argv): return get_rel_name(argv), argv
def joint_disjunction(*argv): return get_rel_name(argv), argv
def joint_list(*argv): return get_rel_name(argv), argv
def joint_other(*argv): return get_rel_name(argv), argv
def joint_sequence(*argv): return get_rel_name(argv), argv
def justify(*argv): return get_rel_name(argv), argv
def list_(*argv): return get_rel_name(argv), argv
def manner(*argv): return get_rel_name(argv), argv
def means(*argv): return get_rel_name(argv), argv
def mode_manner(*argv): return get_rel_name(argv), argv
def mode_means(*argv): return get_rel_name(argv), argv
def motivation(*argv): return get_rel_name(argv), argv
def nonvolitional_cause(*argv): return get_rel_name(argv), argv
def nonvolitional_result(*argv): return get_rel_name(argv), argv
def organization(*argv): return get_rel_name(argv), argv
def organization_heading(*argv): return get_rel_name(argv), argv
def organization_phatic(*argv): return get_rel_name(argv), argv
def organization_preparation(*argv): return get_rel_name(argv), argv
def otherwise(*argv): return get_rel_name(argv), argv
def preparation(*argv): return get_rel_name(argv), argv
def purpose(*argv): return get_rel_name(argv), argv
def purpose_attribute(*argv): return get_rel_name(argv), argv
def purpose_goal(*argv): return get_rel_name(argv), argv
def question(*argv): return get_rel_name(argv), argv
def reason(*argv): return get_rel_name(argv), argv
def restatement(*argv): return get_rel_name(argv), argv
def restatement_mn(*argv): return get_rel_name(argv), argv
def restatement_partial(*argv): return get_rel_name(argv), argv
def restatement_repetition(*argv): return get_rel_name(argv), argv
def result(*argv): return get_rel_name(argv), argv
def same_unit(*argv): return get_rel_name(argv), argv
def sequence(*argv): return get_rel_name(argv), argv
def solutionhood(*argv): return get_rel_name(argv), argv
def summary(*argv): return get_rel_name(argv), argv
def topic_question(*argv): return get_rel_name(argv), argv
def topic_solutionhood(*argv): return get_rel_name(argv), argv
def unconditional(*argv): return get_rel_name(argv), argv
def unless(*argv): return get_rel_name(argv), argv
def unstated(*argv): return get_rel_name(argv), argv
def unstated_relation(*argv): return get_rel_name(argv), argv
def volitional_cause(*argv): return get_rel_name(argv), argv
def volitional_result(*argv): return get_rel_name(argv), argv

if __name__ == "__main__":

    print(evidence(
        volitional_cause(
            circumstance(
                 2,3),4),1))
    
