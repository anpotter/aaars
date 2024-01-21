# compression

import sys

def get_rel_name():
    return sys._getframe(1).f_code.co_name

def attribution(*argv): return compress(get_rel_name(),*argv)
def antithesis(*argv): return compress(get_rel_name(),*argv)
def background(*argv): return compress(get_rel_name(),*argv)
def circumstance(*argv): return compress(get_rel_name(),*argv)
def concession(*argv): return compress(get_rel_name(),*argv)
def condition(*argv): return compress(get_rel_name(),*argv)
def elaboration(*argv): return compress(get_rel_name(),*argv)
def enablement(*argv): return compress(get_rel_name(),*argv)
def evaluation(*argv): return compress(get_rel_name(),*argv)
def evidence(*argv): return compress(get_rel_name(), *argv)
def interpretation(*argv): return compress(get_rel_name(),*argv)
def justify(*argv): return compress(get_rel_name(),*argv)
def means(*argv): return compress(get_rel_name(),*argv)
def motivation(*argv): return compress(get_rel_name(),*argv)
def nonvolitional_cause(*argv): return compress(get_rel_name(),*argv)
def nonvolitional_result(*argv): return compress(get_rel_name(),*argv)
def otherwise(*argv): return compress(get_rel_name(),*argv)
def preparation(*argv): return compress(get_rel_name(),*argv)
def purpose(*argv): return compress(get_rel_name(),*argv)
def reason(*argv): return compress(get_rel_name(),*argv)
def restatement(*argv): return compress(get_rel_name(),*argv)
def solutionhood(*argv): return compress(get_rel_name(),*argv)
def summary(*argv): return compress(get_rel_name(),*argv)
def unconditional(*argv): return compress(get_rel_name(),*argv)
def unless(*argv): return compress(get_rel_name(),*argv)
def unstated_relation(*argv): return compress(get_rel_name(),*argv)
def volitional_cause(*argv): return compress(get_rel_name(),*argv)
def volitional_result(*argv): return compress(get_rel_name(),*argv)
def cause(*argv): return compress(get_rel_name(),*argv)
def result(*argv): return compress(get_rel_name(),*argv)

# irreducibles and multinuclear -- note argv not *arv
def attribution(*argv): return compress(get_rel_name(),argv)
def condition(*argv): return compress(get_rel_name(), argv)
def purpose(*argv): return compress(get_rel_name(), argv)
def unless(*argv): return compress(get_rel_name(), argv)
def otherwise(*argv): return compress(get_rel_name(), argv)

# for reducible condition
# def condition(*argv): return compress(get_rel_name(),*argv) 

# multinucs
def contrast(*argv): return compress(get_rel_name(), argv)
def disjunction(*argv): return compress(get_rel_name(), argv)
def joint(*argv): return compress(get_rel_name(), argv)
def list_(*argv): return compress(get_rel_name(), argv)
def restatement_mn(*argv): return compress(get_rel_name(), argv)
def sequence(*argv): return compress(get_rel_name(), argv)
def convergence(*argv): return compress(get_rel_name(), argv)
def conjunction(*argv): return compress(get_rel_name(), argv)

# GUM relations
def adversative_antithesis(*argv): return compress(get_rel_name(),*argv)
def adversative_concession(*argv): return compress(get_rel_name(),*argv)
def attribution_negative(*argv): return compress(get_rel_name(),*argv)
def attribution_positive(*argv): return compress(get_rel_name(),*argv)
def causal_cause(*argv): return compress(get_rel_name(),*argv)
def causal_result(*argv): return compress(get_rel_name(),*argv)
def context_background(*argv): return compress(get_rel_name(),*argv)
def context_circumstance(*argv): return compress(get_rel_name(),*argv)
def contingency_condition(*argv): return compress(get_rel_name(),*argv)
def elaboration_additional(*argv): return compress(get_rel_name(),*argv)
def elaboration_attribute(*argv): return compress(get_rel_name(),*argv)
def evaluation_comment(*argv): return compress(get_rel_name(),*argv)
def explanation_evidence(*argv): return compress(get_rel_name(),*argv)
def explanation_justify(*argv): return compress(get_rel_name(),*argv)
def explanation_motivation(*argv): return compress(get_rel_name(),*argv)
def mode_manner(*argv): return compress(get_rel_name(),*argv)
def mode_means(*argv): return compress(get_rel_name(),*argv)
def manner(*argv): return compress(get_rel_name(),*argv)
def organization_heading(*argv): return compress(get_rel_name(),*argv)
def organization_phatic(*argv): return compress(get_rel_name(),*argv)
def organization_preparation(*argv): return compress(get_rel_name(),*argv)
def purpose_attribute(*argv): return compress(get_rel_name(),*argv)
def purpose_goal(*argv): return compress(get_rel_name(),*argv)
def question(*argv): return compress(get_rel_name(),*argv)
def restatement_partial(*argv): return compress(get_rel_name(),*argv)
def topic_question(*argv): return compress(get_rel_name(),*argv)
def topic_solutionhood(*argv): return compress(get_rel_name(),*argv)


# Irreducibles
# note argv not *arv

def attribution_negative(*argv): return compress(get_rel_name(),argv)
def attribution_positive(*argv): return compress(get_rel_name(),argv)
def contingency_condition(*argv): return compress(get_rel_name(),argv)
def purpose_attribute(*argv): return compress(get_rel_name(),argv)
def purpose_goal(*argv): return compress(get_rel_name(),argv)

def adversative_contrast(*argv): return compress(get_rel_name(), argv)
def joint_disjunction(*argv): return compress(get_rel_name(), argv)
def joint_list(*argv): return compress(get_rel_name(), argv)
def joint_other(*argv): return compress(get_rel_name(), argv)
def joint_sequence(*argv): return compress(get_rel_name(), argv)
def restatement_repetition(*argv): return compress(get_rel_name(), argv)
def same_unit(*argv): return compress(get_rel_name(), argv)




# not lazy
exp = 'background(volitional_result(1,circumstance(3,2)),evidence(concession(5,antithesis(7,6)),4))'

# Das, RST Signalling Corpus
# exp = 'elaboration_additional_e(list_(attribution(2,list_(3,4)),5),1)'

# tax program v1
# exp = 'evidence(cause(2,3),1)'

# tax program v2
# exp = 'evidence(volitional_cause(circumstance(2,3),4),1)'

# cc letter
# exp = 'motivation(evidence(evidence(justify(10,antithesis(concession(11,12),13)),antithesis(evidence(condition(4,contrast(5,6)),concession(2,3)),elaboration(9,condition(8,7)))),1),14)'

# Lu, R., Attributed Rhetorical Structure Grammar 
#exp = 'concession(interpretation(elaboration(sequence(6,7),sequence(4,5)),elaboration(elaboration(3,2),1)),8)'

# New brochure time
# exp = 'justify(cause(1,2),otherwise(6,same_unit(condition(4,3),5)))'

# GUM_news_worship
# exp = 'preparation(attribution(1,2),circumstance(3,background(contrast(12,concession(14,13)),background(concession(attribution(10,11),9),background(background(8,result(7,6)),attribution(4,5))))))'

# GUM academic thrones
# exp = 'organization_heading(organization_preparation(1,2),joint_other(context_background(context_background(explanation_justify(context_background(explanation_evidence(24,same_unit(elaboration_attribute(22,21),23)),elaboration_attribute(26,25)),explanation_justify(context_background(explanation_evidence(context_background(context_circumstance(14,15),context_background(explanation_evidence(12,same_unit(elaboration_additional(10,9),11)),13)),adversative_antithesis(attribution_positive(3,4),elaboration_attribute(joint_sequence(6,elaboration_attribute(8,7)),5))),elaboration_attribute(purpose_goal(18,17),16)),elaboration_attribute(20,19))),mode_means(32,same_unit(elaboration_additional(28,27),elaboration_attribute(joint_list(30,31),29)))),context_circumstance(elaboration_attribute(35,34),33)),organization_heading(36,elaboration_additional(joint_sequence(context_background(context_background(context_background(same_unit(explanation_evidence(41,40),explanation_evidence(43,42)),adversative_contrast(44,45)),causal_cause(elaboration_additional(same_unit(restatement_partial(48,47),restatement_partial(50,49)),46),elaboration_additional(same_unit(elaboration_attribute(54,53),elaboration_attribute(56,55)),elaboration_attribute(52,51)))),mode_means(elaboration_attribute(explanation_evidence(62,61),60),joint_list(elaboration_additional(58,57),59))),elaboration_additional(organization_preparation(66,same_unit(restatement_partial(68,67),restatement_partial(70,69))),elaboration_additional(purpose_attribute(65,64),63)),purpose_attribute(72,71)),same_unit(elaboration_attribute(38,37),39))),organization_heading(73,evaluation_comment(87,elaboration_additional(joint_other(same_unit(elaboration_attribute(78,77),elaboration_additional(80,79)),mode_means(purpose_goal(84,83),elaboration_attribute(82,81)),elaboration_attribute(86,85)),elaboration_attribute(mode_manner(76,75),74))))))'

# GUM_speech_floyd
# exp = 'organization_heading(1,context_circumstance(2,organization_heading(3,context_circumstance(4,organization_preparation(context_background(5,6),attribution_positive(7,organization_phatic(joint_list(8,9,causal_cause(joint_list(11,elaboration_attribute(13,12)),10),14),organization_phatic(joint_list(restatement_repetition(146,147),148),restatement_partial(explanation_motivation(context_background(organization_preparation(context_background(103,elaboration_attribute(elaboration_attribute(102,101),100)),adversative_concession(causal_cause(105,104),joint_sequence(106,topic_question(organization_preparation(107,attribution_positive(108,attribution_positive(110,109))),attribution_positive(111,contingency_condition(112,113)))))),explanation_justify(organization_phatic(135,organization_preparation(elaboration_additional(topic_question(116,joint_list(117,causal_cause(same_unit(attribution_positive(119,120),purpose_goal(121,122)),118))),elaboration_additional(115,114)),context_circumstance(context_circumstance(123,attribution_positive(124,evaluation_comment(125,explanation_justify(127,126)))),elaboration_additional(elaboration_additional(explanation_evidence(132,joint_list(133,134)),evaluation_comment(restatement_repetition(130,131),129)),128)))),joint_list(attribution_positive(136,joint_list(same_unit(137,attribution_positive(138,139)),same_unit(140,attribution_positive(141,142)))),purpose_attribute(144,143)))),145),evaluation_comment(elaboration_additional(restatement_partial(attribution_positive(98,99),joint_list(attribution_positive(93,94),purpose_goal(joint_list(96,97),95))),attribution_positive(89,purpose_goal(elaboration_attribute(92,91),90))),explanation_justify(adversative_concession(adversative_antithesis(same_unit(elaboration_attribute(purpose_attribute(85,84),83),elaboration_attribute(87,86)),88),adversative_concession(58,explanation_justify(explanation_evidence(restatement_partial(66,adversative_concession(causal_cause(64,65),attribution_positive(context_background(explanation_evidence(joint_list(60,61),59),62),63))),causal_cause(organization_preparation(elaboration_additional(adversative_concession(69,70),68),context_circumstance(causal_cause(purpose_goal(joint_list(78,79),77),attribution_negative(organization_phatic(74,75),76)),context_circumstance(purpose_goal(73,72),71))),67)),attribution_positive(80,elaboration_attribute(82,81))))),evaluation_comment(elaboration_additional(adversative_concession(joint_list(45,same_unit(restatement_partial(47,46),elaboration_attribute(joint_disjunction(49,50),48))),joint_list(joint_disjunction(same_unit(51,organization_phatic(52,53)),54),55,elaboration_attribute(57,56))),44),organization_phatic(joint_list(elaboration_attribute(41,40),42,43),context_background(elaboration_additional(restatement_repetition(28,29),causal_result(adversative_concession(24,same_unit(25,adversative_concession(26,27))),elaboration_additional(mode_manner(joint_list(20,21,attribution_positive(22,23)),purpose_goal(19,18)),causal_cause(attribution_positive(15,16),17)))),explanation_justify(restatement_partial(context_circumstance(joint_list(organization_phatic(32,same_unit(elaboration_attribute(34,33),35)),36),31),30),purpose_goal(39,joint_sequence(37,38)))))))))))))))))'

# GUM_news_warhol
# exp = 'organization_heading(1,context_circumstance(2,joint_other(context_background(attribution_positive(organization_preparation(5,6),elaboration_attribute(4,3)),elaboration_additional(elaboration_additional(elaboration_additional(context_background(elaboration_additional(joint_list(29,30),28),elaboration_additional(27,26)),attribution_positive(25,24)),elaboration_attribute(23,22)),elaboration_additional(elaboration_additional(attribution_positive(21,20),19),elaboration_additional(elaboration_additional(18,17),elaboration_additional(16,elaboration_additional(joint_list(14,15),context_background(joint_list(12,13),context_background(elaboration_additional(attribution_positive(9,8),7),context_circumstance(10,11))))))))),organization_heading(31,context_background(attribution_positive(organization_preparation(34,35),elaboration_additional(33,32)),context_background(purpose_goal(37,36),context_background(attribution_positive(38,same_unit(elaboration_attribute(40,39),41)),organization_preparation(elaboration_additional(43,42),elaboration_additional(evaluation_comment(explanation_evidence(elaboration_additional(elaboration_attribute(elaboration_additional(elaboration_attribute(60,59),58),57),attribution_positive(56,context_circumstance(55,54))),53),restatement_partial(52,context_circumstance(50,51))),elaboration_additional(same_unit(attribution_positive(48,47),49),attribution_positive(44,joint_list(45,46))))))))),organization_heading(61,joint_other(elaboration_additional(elaboration_additional(attribution_positive(85,86),joint_list(elaboration_additional(82,81),elaboration_additional(84,83))),context_background(elaboration_additional(attribution_positive(80,adversative_contrast(77,elaboration_attribute(79,78))),attribution_positive(73,joint_sequence(context_circumstance(75,74),76))),context_background(joint_list(attribution_positive(66,attribution_positive(70,elaboration_additional(context_circumstance(69,68),67))),causal_cause(72,71)),elaboration_additional(65,same_unit(elaboration_attribute(63,62),64))))),evaluation_comment(attribution_positive(89,elaboration_additional(elaboration_attribute(92,91),90)),elaboration_attribute(88,87)))),organization_heading(93,joint_other(elaboration_attribute(elaboration_attribute(97,96),elaboration_additional(95,94)),explanation_justify(elaboration_additional(same_unit(105,explanation_evidence(106,107)),104),explanation_evidence(context_background(attribution_positive(100,99),contingency_condition(elaboration_attribute(103,102),101)),98)),attribution_positive(113,attribution_positive(108,restatement_repetition(109,causal_cause(112,elaboration_attribute(111,110))))),evaluation_comment(attribution_positive(117,118),attribution_positive(114,attribution_positive(115,116))),elaboration_additional(elaboration_additional(elaboration_additional(same_unit(elaboration_attribute(134,133),elaboration_attribute(136,135),137),attribution_positive(127,elaboration_attribute(purpose_goal(mode_means(joint_disjunction(131,132),130),129),128))),attribution_positive(125,126)),adversative_concession(adversative_concession(119,elaboration_additional(121,120)),attribution_positive(122,elaboration_attribute(124,123)))),restatement_partial(elaboration_additional(attribution_positive(148,causal_cause(145,purpose_goal(147,146))),144),attribution_positive(138,explanation_evidence(evaluation_comment(143,joint_sequence(140,joint_sequence(141,142))),139))))),organization_heading(149,joint_other(topic_question(context_background(attribution_positive(150,adversative_contrast(purpose_goal(152,151),153)),154),evaluation_comment(156,155)),joint_other(elaboration_additional(attribution_positive(158,explanation_justify(159,160)),157),evaluation_comment(elaboration_additional(169,attribution_positive(168,attribution_positive(166,167))),context_background(joint_list(elaboration_attribute(164,163),165),attribution_positive(161,162)))),elaboration_additional(joint_other(same_unit(elaboration_attribute(176,175),elaboration_additional(178,177)),179,elaboration_additional(joint_sequence(185,elaboration_additional(evaluation_comment(evaluation_comment(197,elaboration_additional(196,195)),context_circumstance(joint_list(191,purpose_goal(restatement_partial(194,193),192)),same_unit(elaboration_attribute(189,188),190))),elaboration_attribute(187,186))),same_unit(180,attribution_positive(181,elaboration_attribute(joint_list(183,184),182))))),organization_preparation(170,mode_manner(elaboration_attribute(174,elaboration_attribute(173,172)),171))))))))'

# GUM_academic_census
# exp ='organization_heading(1,context_background(context_background(context_background(elaboration_additional(3,2),adversative_concession(adversative_concession(17,18),explanation_evidence(joint_list(attribution_positive(7,mode_means(elaboration_attribute(13,12),same_unit(explanation_evidence(9,8),explanation_evidence(11,10)))),elaboration_attribute(16,explanation_evidence(15,14))),attribution_positive(4,elaboration_additional(6,5))))),explanation_justify(context_background(joint_other(adversative_contrast(context_background(adversative_contrast(explanation_evidence(32,elaboration_attribute(31,30)),elaboration_additional(36,same_unit(elaboration_additional(34,33),35))),evaluation_comment(adversative_concession(45,causal_result(47,46)),causal_cause(37,joint_list(same_unit(explanation_evidence(40,joint_list(38,39)),explanation_evidence(42,41)),explanation_evidence(44,43))))),evaluation_comment(adversative_contrast(explanation_evidence(52,51),causal_result(54,53)),explanation_evidence(50,elaboration_additional(49,48)))),evaluation_comment(organization_preparation(adversative_contrast(60,61),joint_list(explanation_evidence(64,elaboration_attribute(63,62)),explanation_evidence(causal_result(70,mode_means(69,68)),explanation_evidence(67,elaboration_additional(66,65))))),elaboration_additional(same_unit(restatement_partial(57,56),elaboration_additional(59,58)),55))),adversative_contrast(explanation_evidence(25,24),explanation_evidence(29,same_unit(26,context_circumstance(27,28))))),adversative_antithesis(joint_list(causal_result(22,21),23),purpose_attribute(20,19)))),elaboration_additional(organization_preparation(98,joint_sequence(mode_means(100,99),elaboration_additional(joint_sequence(mode_means(joint_sequence(103,elaboration_attribute(explanation_evidence(106,105),104)),102),elaboration_additional(purpose_goal(110,109),elaboration_attribute(108,107))),101))),evaluation_comment(97,elaboration_additional(joint_list(elaboration_additional(mode_means(84,adversative_antithesis(87,mode_means(86,85))),explanation_evidence(83,evaluation_comment(elaboration_attribute(purpose_goal(82,81),80),mode_means(79,78)))),evaluation_comment(purpose_goal(elaboration_attribute(92,91),90),purpose_goal(89,88)),adversative_contrast(93,context_circumstance(94,joint_list(95,96)))),evaluation_comment(joint_list(75,joint_list(76,77)),elaboration_attribute(mode_means(74,73),elaboration_attribute(72,71))))))))'


def strip(s): return ''.join(s.split())

exp_list = []
exp_list.append(strip(exp))

def compress(relname, *argv):
    
    if isinstance(argv[0], tuple):          # multinuclear
        mn = '{}{}'.format(relname,argv[0])
        mn = strip(mn)
        return mn

    sat = argv[0]                           # everything else
    nuc = argv[1]
    oldexp = '{}({},{})'.format(relname,sat,nuc)
    newexp = str(nuc)

    exp = exp_list[len(exp_list) - 1]
    exp = exp.replace(oldexp,newexp)
    exp_list.append(strip(exp))

    return nuc

eval(exp)

for e in exp_list:
    print(e)
