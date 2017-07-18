import pandas as pd
import numpy as np

ana_list = ['credit_total'
    ,'credit_baitiao'
    ,'zm_score'
    ,'d1_plus_capital_overdue'
    ,'d4_plus_capital_overdue'
    ,'d10_plus_capital_overdue'
    ,'d31_plus_capital_overdue'
    ,'capital_total'
    ,'cum_origin_amount'
    ,'profit'
    ]

df = pd.read_csv('tmp_wd_qd_credit_success_das_ana',sep='\t')
for item in ana_list:
    if item in ['credit_total','credit_baitiao','zm_score']:
        print item,df[df['type']=='NODAS'][item].mean(),df[df['type']=='DAS'][item].mean()
    else:
        print item,df[df['type']=='NODAS'][item].sum(),df[df['type']=='DAS'][item].sum()
print 'num',(df['type']=='NODAS').sum(),(df['type']=='DAS').sum()
print 'bad_num',((df['type']=='NODAS')&(df['d1_plus_capital_overdue']>0)).sum(),((df['type']=='DAS')&(df['d1_plus_capital_overdue']>0)).sum()
print 'order_user_num',((df['type']=='NODAS')&(df['cum_origin_amount']>0)).sum(),((df['type']=='DAS')&(df['cum_origin_amount']>0)).sum()