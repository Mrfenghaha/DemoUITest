# -*- coding: utf-8 -
import numpy


# 循环次数默认方法
def default_option(way, *param):
    if way == 'blacklist_type':
        id_type = param[0]
        n = blacklist_type_default_option(id_type)
    elif way == 'approve_rejected_reason':
        reason = param[0]
        n = approve_rejected_reason_default_option(reason)
    elif way == 'approve_return_reason':
        reason = param[0]
        approve_return_reason_default_option(reason)
    elif way == 'approve_cancel_reason':
        reason = param[0]
        n = approve_cancel_reason_default_option(reason)
    return n


# 选择黑名单的循环次数默认方法
def blacklist_type_default_option(blacklist_type):
    blacklist_list = ['BlackList1', 'BlackList2']
    n = blacklist_list.index(blacklist_type)  # 获取blacklist_type在列表中对应的下标位置即为n
    return n


# 选择审批拒绝原因的循环次数默认方法
def approve_rejected_reason_default_option(reason):
    reason_list = ['R101', 'R102', 'R103', 'R104', 'R105', 'R106', 'R107', 'R108', 'R109', 'R201', 'R202', 'R203',
                   'R204', 'R205', 'R301', 'R302', 'R303', 'R304', 'R305', 'R306', 'R401', 'R402', 'R403', 'R404',
                   'R405', 'R501', 'R502', 'R503', 'R504', 'R505', 'R506', 'R507', 'R508', 'R509', 'R601', 'R602',
                   'R603', 'R701', 'R702', 'R703']
    n = reason_list.index(reason[0]['reason_code'])  # 获取reason在列表中对应的下标位置即为n
    return n


# 选择审批退回原因的循环次数默认方法
def approve_return_reason_default_option(reason):
    reason_list = ['RT01', 'RT03', 'RT04', 'RT05', 'RT06', 'RT07']
    n = reason_list.index(reason[0]['reason_code'])  # 获取reason在列表中对应的下标位置即为n
    return n


# 选择审批取消原因的循环次数默认方法
def approve_cancel_reason_default_option(reason):
    reason_list = ['C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C11', 'C12']
    n = reason_list.index(reason[0]['reason_code'])  # 获取reason在列表中对应的下标位置即为n
    return n
