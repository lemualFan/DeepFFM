# -*- coding: utf-8 -*-
RANDOM_SEED = 3

TRAIN_PATH = './data/train.csv'
TEST_PATH = './data/test.csv'



LABEL_NAME = 'y'
NUM_CLASS = 2

ID_COL = []

NUMERIC_COL = ['x_62*x_69', 'x_2+x_58', 'x_72-x_80', 'x_80+x_82', 'x_40/x_63',
               'x_2+x_99', 'x_80+x_142', 'x_43/x_68', 'x_54/x_63', 'x_2_new_all',
               'x_50-x_93', 'x_42*x_95', 'x_80+x_81', 'x_52+x_83', 'x_81+x_97',
               'x_80-x_154', 'x_1_new_all', 'x_2//x_153', 'x_2+x_84', 'x_93_new_all',
               'x_81-x_144', 'x_1+x_93', 'x_2+x_156', 'x_52-x_63', 'x_2+x_91',
               'x_14-x_80', 'x_1+x_79', 'x_36/x_52', 'x_78_new_all', 'x_63/x_68',
               'x_43*x_157', 'x_2+x_97', 'x_1+x_78', 'x_45-x_81', 'x_51/x_66',
               'x_42+x_46', 'x_7-x_80', 'x_2/x_45', 'x_48/x_156', 'x_61-x_95',
               'x_80+x_156', 'x_83*x_84', 'x_95+x_156', 'x_80+x_97', 'x_72+x_95',
               'x_66//x_95', 'x_38+x_56', 'x_2+x_61', 'x_61-x_80', 'x_54/x_62',
               'x_50/x_61', 'x_62*x_141', 'x_54/x_60', 'x_1*x_49', 'x_2*x_51',
               'x_40/x_43', 'x_44/x_157', 'x_24/x_80', 'x_14*x_55', 'x_78/x_97',
               'x_156_new_all', 'x_46-x_95', 'x_63-x_93', 'x_142_new_all', 'x_80+x_85',
               'x_58+x_95', 'x_47*x_55', 'x_30*x_80', 'x_4+x_80', 'x_40*x_84',
               'x_62+x_157', 'x_35/x_79',
               'x_1', 'x_10', 'x_100', 'x_101', 'x_102', 'x_103', 'x_104', 'x_105', 
               'x_106', 'x_107', 'x_108', 'x_109', 'x_11', 'x_110', 'x_111', 'x_112', 
               'x_113', 'x_114', 'x_115', 'x_116', 'x_117', 'x_118', 'x_119', 'x_12', 
               'x_120', 'x_121', 'x_122', 'x_123', 'x_124', 'x_125', 'x_126', 'x_127', 
               'x_128', 'x_129', 'x_13', 'x_130', 'x_131', 'x_132', 'x_133', 'x_134', 
               'x_135', 'x_136', 'x_137', 'x_138', 'x_139', 'x_14', 'x_140', 'x_141', 
               'x_142', 'x_143', 'x_144', 'x_145', 'x_146', 'x_147', 'x_148', 'x_149', 
               'x_15', 'x_150', 'x_151', 'x_152', 'x_153', 'x_154', 'x_155', 'x_156', 
               'x_157', 'x_16', 'x_17', 'x_18', 'x_19', 'x_2', 'x_20', 'x_21', 'x_22', 
               'x_23', 'x_24', 'x_25', 'x_26', 'x_27', 'x_28', 'x_29', 'x_3', 'x_30', 
               'x_31', 'x_32', 'x_33', 'x_34', 'x_35', 'x_36', 'x_37', 'x_38', 'x_39', 
               'x_4', 'x_40', 'x_41', 'x_42', 'x_43', 'x_44', 'x_45', 'x_46', 'x_47', 
               'x_48', 'x_49', 'x_5', 'x_50', 'x_51', 'x_52', 'x_53', 'x_54', 'x_55', 
               'x_56', 'x_57', 'x_58', 'x_59', 'x_6', 'x_60', 'x_61', 'x_62', 'x_63', 
               'x_64', 'x_65', 'x_66', 'x_67', 'x_68', 'x_69', 'x_7', 'x_70', 'x_71', 
               'x_72', 'x_73', 'x_74', 'x_75', 'x_76', 'x_77', 'x_78', 'x_79', 'x_8', 
               'x_80', 'x_81', 'x_82', 'x_83', 'x_84', 'x_85', 'x_86', 'x_87', 'x_88', 
               'x_89', 'x_9', 'x_90', 'x_91', 'x_92', 'x_93', 'x_94', 'x_95', 'x_96', 
               'x_97', 'x_98', 'x_99']
ONEHOT_COL = []
VECTOR_COL = []

LR = NUMERIC_COL + ONEHOT_COL
LR_COL = [col + '_lr' for col in LR]

NUMERIC_COL = ['x_1', 'x_10', 'x_100', 'x_101', 'x_102', 'x_103', 'x_104', 'x_105', 
               'x_106', 'x_107', 'x_108', 'x_109', 'x_11', 'x_110', 'x_111', 'x_112', 
               'x_113', 'x_114', 'x_115', 'x_116', 'x_117', 'x_118', 'x_119', 'x_12', 
               'x_120', 'x_121', 'x_122', 'x_123', 'x_124', 'x_125', 'x_126', 'x_127', 
               'x_128', 'x_129', 'x_13', 'x_130', 'x_131', 'x_132', 'x_133', 'x_134', 
               'x_135', 'x_136', 'x_137', 'x_138', 'x_139', 'x_14', 'x_140', 'x_141', 
               'x_142', 'x_143', 'x_144', 'x_145', 'x_146', 'x_147', 'x_148', 'x_149', 
               'x_15', 'x_150', 'x_151', 'x_152', 'x_153', 'x_154', 'x_155', 'x_156', 
               'x_157', 'x_16', 'x_17', 'x_18', 'x_19', 'x_2', 'x_20', 'x_21', 'x_22', 
               'x_23', 'x_24', 'x_25', 'x_26', 'x_27', 'x_28', 'x_29', 'x_3', 'x_30', 
               'x_31', 'x_32', 'x_33', 'x_34', 'x_35', 'x_36', 'x_37', 'x_38', 'x_39', 
               'x_4', 'x_40', 'x_41', 'x_42', 'x_43', 'x_44', 'x_45', 'x_46', 'x_47', 
               'x_48', 'x_49', 'x_5', 'x_50', 'x_51', 'x_52', 'x_53', 'x_54', 'x_55', 
               'x_56', 'x_57', 'x_58', 'x_59', 'x_6', 'x_60', 'x_61', 'x_62', 'x_63', 
               'x_64', 'x_65', 'x_66', 'x_67', 'x_68', 'x_69', 'x_7', 'x_70', 'x_71', 
               'x_72', 'x_73', 'x_74', 'x_75', 'x_76', 'x_77', 'x_78', 'x_79', 'x_8', 
               'x_80', 'x_81', 'x_82', 'x_83', 'x_84', 'x_85', 'x_86', 'x_87', 'x_88', 
               'x_89', 'x_9', 'x_90', 'x_91', 'x_92', 'x_93', 'x_94', 'x_95', 'x_96', 
               'x_97', 'x_98', 'x_99']

CROSS_COL = []
if len(CROSS_COL) != 0:
    for cols in CROSS_COL:
        LR_COL.append(cols[0]+'_'+cols[1])

N_BINS = 10
MAX_LEN = 30

fold = 5
round_cv = 10

is_print = True


'''
加上直接当数值输入的part（在ffm边上额外加，而不是取代替换）
'''