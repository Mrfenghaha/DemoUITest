# -*- coding: utf-8 -
import numpy


# 循环次数默认方法
def default_option(way, *param):
    if way == 'id_type':
        id_type = param[0]
        n = id_type_default_option(id_type)
    elif way == 'gender':
        gender = param[0]
        n = gender_default_option(gender)
    elif way == 'educational':
        educational = param[0]
        n = educational_default_option(educational)
    elif way == 'marital':
        marital = param[0]
        n = marital_default_option(marital)
    elif way == 'purpose':
        purpose = param[0]
        n = purpose_default_option(purpose)
    elif way == 'career':
        career = param[0]
        n = career_default_option(career)
    elif way == 'company_years':
        company_years = param[0]
        n = company_years_default_option(company_years)
    elif way == 'monthly_income':
        monthly_income = param[0]
        n = monthly_income_default_option(monthly_income)
    elif way == 'work_payday':
        payday = param[0]
        n = work_payday_default_option(payday)
    elif way == 'first_relation_ship':
        marital = param[0]
        first_relation_ship = param[1]
        n = first_relation_ship_default_option(marital, first_relation_ship)
    elif way == 'second_relation_ship':
        marital = param[0]
        second_relation_ship = param[1]
        n = second_relation_ship_default_option(marital, second_relation_ship)
    elif way == 'three_relation_ship':
        marital = param[0]
        career = param[1]
        three_relation_ship = param[2]
        n = three_relation_ship_default_option(marital, career, three_relation_ship)
    elif way == 'bank_name':
        bank_name = param[0]
        n = bank_name_default_option(bank_name)
    return n


# 选择银行的循环次数默认方法
def id_type_default_option(id_type):
    id_type_list = ["PRC", "SSS", "UMID", "Driver's license", "GSIS"]
    n = id_type_list.index(id_type)  # 获取id_type在列表中对应的下标位置即为n
    return n


def gender_default_option(gender):
    gender_list = ["Male", "Female", "Other"]
    n = gender_list.index(gender)  # 获取gender在列表中对应的下标位置即为n
    return n


def educational_default_option(educational):
    educational_list = ["Elementary School", "High School", "Technical School", "College Grad", "Master", "Doctor"]
    n = educational_list.index(educational)  # 获取educational在列表中对应的下标位置即为n
    return n


def marital_default_option(marital):
    marital_list = ["Single", "Married with children", "Married without children", "Widowed", "Divorced"]
    n = marital_list.index(marital)  # 获取marital在列表中对应的下标位置即为n
    return n


def purpose_default_option(purpose):
    purpose_list = ["Shopping", "Education", "Travel", "Accommodation", "Multi-purposes", "Pay off other debts"]
    n = purpose_list.index(purpose)  # 获取purpose在列表中对应的下标位置即为n
    return n


# 选择工作类型的循环次数默认方法
def career_default_option(career):
    career_list = ["BIR Employee", "Business Owner", "Contract Employee", "Collection Persinnel/Loan Salesman",
                   "Barangay/City Hall Employee", "Other Government Employee", "Driver", "DepEd Employee",
                   "Private Teacher", "Freelance", "Farmer", "Factory Worker", "Housewife",
                   "Lawyer/Prosecutor/Judge,etc.", "News Media Practitioner", "Office Worker", "OFW",
                   "Pensioner/Retiree", "Police/Military", "Professional Worker(Doctors,Engineers,etc.)",
                   "Religious Figure", "Student", "SEC Staff", "Self-employed", "Unemployed"]
    n = career_list.index(career)  # 获取career在列表中对应的下标位置即为n
    return n


# 选择工作年限的循环次数默认方法
def company_years_default_option(company_years):
    company_years_list = ["Within 3 months", "3-6 months", "6 months-1 year", "1-2 years", "2-5 years", "5 years above"]
    n = company_years_list.index(company_years)  # 获取company_years在列表中对应的下标位置即为n
    return n


# 选择月收入的循环次数默认方法
def monthly_income_default_option(monthly_income):
    monthly_income_list = ["0-10000", "10001-20000", "20001-25000", "25001-30000", "30001-40000", "40001 above"]
    n = monthly_income_list.index(monthly_income)  # 获取monthly_income在列表中对应的下标位置即为n
    return n


# 选择发薪日的循环次数默认方法
def work_payday_default_option(date):
    n = int(date) - 1
    return n


# 选择第一联系人关系的循环次数默认方法
def first_relation_ship_default_option(marital, first_relation_ship):
    marital_list = numpy.array(['Widowed', 'Divorced'])

    if first_relation_ship == "Father":
        n = 0
    elif first_relation_ship == "Mother":
        n = 1
    else:
        if marital == 'Single':
            if first_relation_ship == "Brother":
                n = 2
            elif first_relation_ship == "Sister":
                n = 3
        elif marital == 'Married with children':
            if first_relation_ship == "Spouse":
                n = 2
            elif first_relation_ship == "Children":
                n = 3
            elif first_relation_ship == "Brother":
                n = 4
            elif first_relation_ship == "Sister":
                n = 5
        elif marital == 'Married without children':
            if first_relation_ship == "Spouse":
                n = 2
            elif first_relation_ship == "Brother":
                n = 3
            elif first_relation_ship == "Sister":
                n = 4
        # 如果marital值存在于marital_list中
        elif (marital_list == marital).any() == True:
            if first_relation_ship == "Children":
                n = 2
            elif first_relation_ship == "Brother":
                n = 3
            elif first_relation_ship == "Sister":
                n = 4
            else:
                print('first_relation_ship值错误')
    return n


# 选择第二联系人关系的循环次数默认方法
def second_relation_ship_default_option(marital, second_relation_ship):
    marital_list = numpy.array(['Widowed', 'Divorced'])

    if second_relation_ship == "Father":
        n = 0
    elif second_relation_ship == "Mother":
        n = 1
    elif second_relation_ship == "Brother":
        n = 2
    elif second_relation_ship == "Sister":
        n = 3
    else:
        if marital == 'Single':
            if second_relation_ship == "Other Relative":
                n = 4
            elif second_relation_ship == "Co-worker":
                n = 5
            elif second_relation_ship == "Friend":
                n = 6
            elif second_relation_ship == "Classmate":
                n = 7
            else:
                print('second_relation_ship值错误')
        elif marital == 'Married with children':
            if second_relation_ship == "Spouse":
                n = 4
            elif second_relation_ship == "Children":
                n = 5
            elif second_relation_ship == "Other Relative":
                n = 6
            elif second_relation_ship == "Co-worker":
                n = 7
            elif second_relation_ship == "Friend":
                n = 8
            elif second_relation_ship == "Classmate":
                n = 9
            else:
                print('second_relation_ship值错误')
        elif marital == 'Married without children':
            if second_relation_ship == "Spouse":
                n = 4
            elif second_relation_ship == "Other Relative":
                n = 5
            elif second_relation_ship == "Co-worker":
                n = 6
            elif second_relation_ship == "Friend":
                n = 7
            elif second_relation_ship == "Classmate":
                n = 8
            else:
                print('second_relation_ship值错误')
        # 如果marital值存在于marital_list中
        elif (marital_list == marital).any() == True:
            if second_relation_ship == "Children":
                n = 4
            elif second_relation_ship == "Other Relative":
                n = 5
            elif second_relation_ship == "Co-worker":
                n = 6
            elif second_relation_ship == "Friend":
                n = 7
            elif second_relation_ship == "Classmate":
                n = 8
            else:
                print('second_relation_ship值错误')
    return n


# 选择第三联系人关系的循环次数默认方法
def three_relation_ship_default_option(marital, career, three_relation_ship):
    career_list = numpy.array(['Business Owner', 'Freelance', 'Farmer', 'Housewife', 'Pensioner/Retiree',
                               'Religious Figure', 'Student', 'Self-employed', 'Unemployed'])
    marital_list = numpy.array(['Widowed', 'Divorced'])

    # 如果career值存在于career_list中
    if (career_list == career).any() == True:
        if three_relation_ship == "Father":
            n = 0
        elif three_relation_ship == "Mother":
            n = 1
        elif marital == 'Single':
            if three_relation_ship == "Brother":
                n = 2
            elif three_relation_ship == "Sister":
                n = 3
            else:
                print('three_relation_ship值错误')
        elif marital == 'Married with children':
            if three_relation_ship == "Spouse":
                n = 2
            elif three_relation_ship == "Children":
                n = 3
            elif three_relation_ship == "Brother":
                n = 4
            elif three_relation_ship == "Sister":
                n = 5
            else:
                print('second_relation_ship值错误')
        elif marital == 'Married without children':
            if three_relation_ship == "Spouse":
                n = 2
            elif three_relation_ship == "Brother":
                n = 3
            elif three_relation_ship == "Sister":
                n = 4
            else:
                print('second_relation_ship值错误')
        # 如果marital值存在于marital_list中
        elif (marital_list == marital).any() == True:
            if three_relation_ship == "Children":
                n = 2
            elif three_relation_ship == "Brother":
                n = 3
            elif three_relation_ship == "Sister":
                n = 4
            else:
                print('second_relation_ship值错误')
    else:
        n = 0
    return n


# 选择银行的循环次数默认方法
def bank_name_default_option(bank_name):

    bank_name_list = ["BDO", "BPI", "MBTC", "UBP", "CBC", "EWB", "SBC", "LBP", "PNB", "AUB"]
    n = bank_name_list.index(bank_name)  # 获取bank_name在列表中对应的下标位置即为n
    return n
