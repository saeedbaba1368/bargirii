from django.shortcuts import render
from loading.models import BargiriForm
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import numpy as np
import pandas as pd
import itertools

from django.http import HttpResponse
@csrf_exempt
def bargiri(request):
    if request.method == 'POST':
        form = BargiriForm(request.POST)
        if form.is_valid():
            obj= form.save()
            trans_name=obj.trans_name
            F1_1 = obj.F1_1
            
            F1_2 = obj.F1_2
            F1_3 = obj.F1_3
            F2_1 = obj.F2_1
            F2_2 = obj.F2_2
            F2_3 = obj.F2_3
            F3_1 = obj.F3_1 
            F3_2 = obj.F3_2
            F3_3 = obj.F3_3
            F4_1 = obj.F4_1
            F4_2 = obj.F4_2
            F4_3 = obj.F4_3
            cat1_1 = [F1_1, F1_2, F1_3]
            cat1_2 = [F1_1, F1_3, F1_2]
            cat1_3 = [F1_2, F1_1, F1_3]
            cat1_4 = [F1_2, F1_3, F1_1]
            cat1_5 = [F1_3, F1_1, F1_2]
            cat1_6 = [F1_3, F1_2, F1_1]

            cat2_1 = [F2_1, F2_2, F2_3]
            cat2_2 = [F2_1, F2_3, F2_2]
            cat2_3 = [F2_2, F2_1, F2_3]
            cat2_4 = [F2_2, F2_3, F2_1]
            cat2_5 = [F2_3, F2_1, F2_2]
            cat2_6 = [F2_3, F2_2, F2_1]

            cat3_1 = [F3_1, F3_2, F3_3]
            cat3_2 = [F3_1, F3_3, F3_2]
            cat3_3 = [F3_2, F3_1, F3_3]
            cat3_4 = [F3_2, F3_3, F3_1]
            cat3_5 = [F3_3, F3_1, F3_2]
            cat3_6 = [F3_3, F3_2, F3_1]

            cat4_1 = [F4_1, F4_2, F4_3]
            cat4_2 = [F4_1, F4_3, F4_2]
            cat4_3 = [F4_2, F4_1, F4_3]
            cat4_4 = [F4_2, F4_3, F4_1]
            cat4_5 = [F4_3, F4_1, F4_2]
            cat4_6 = [F4_3, F4_2, F4_1]
            cat1 = [cat1_1, cat1_2, cat1_3, cat1_4, cat1_5, cat1_6]
            cat2 = [cat2_1, cat2_2, cat2_3, cat2_4, cat2_5, cat2_6]
            cat3 = [cat3_1, cat3_2, cat3_3, cat3_4, cat3_5, cat3_6]
            cat4 = [cat4_1, cat4_2, cat4_3, cat4_4, cat4_5, cat4_6]
            combinations = list(itertools.product(cat1, cat2, cat3, cat4))
            pd.set_option('display.max_columns', None)
            df2 = pd.DataFrame(columns=['combination','index', 'R', 'S', 'T'])
            for combo in combinations:
                row = [combo,
                (cat1.index(combo[0])+1, cat2.index(combo[1])+1, cat3.index(combo[2])+1, cat4.index(combo[3])+1),
                combo[0][0]+combo[1][0]+combo[2][0]+combo[3][0],
                combo[0][1]+combo[1][1]+combo[2][1]+combo[3][1],
                combo[0][2]+combo[1][2]+combo[2][2]+combo[3][2],
                ]

            df2.loc[len(df2)] = row
            std_dev = df2[['R', 'S', 'T']].std(axis=1)
            df3 = pd.concat([df2, std_dev.rename('stddev')], axis=1)
            filtered_df = df3.sort_values('stddev').head(10)

            input_list = filtered_df[['index']]

            df4 = pd.DataFrame(input_list, columns=['index'])

            # separate the tuples into four columns
            df4[['F1', 'F2', 'F3', 'F4']] = df4['index'].apply(lambda x: pd.Series(x))
            df5=df4.iloc[:, -4:]
            df6 = pd.concat([filtered_df, df5], axis=1)
            # view the resulting dataframe
            arr = df6.iloc[:, 6:10].to_numpy()

            max_ones_count = -1
            row_with_max_ones = None

            # loop through each row in the database
            for i in range(len(arr)):
                # count the number of ones in this row
                ones_count = np.count_nonzero(arr[i] == 1)

                # if this count is greater than the current max count, update the row with maximum ones
                if ones_count > max_ones_count:
                    max_ones_count = ones_count
                    row_with_max_ones = i
            n=row_with_max_ones+1
            specialcols = filtered_df[['combination', 'R', 'S', 'T']]

            
            out=specialcols.iloc[n-1]
           
            F1_1_new=out[0][0][0]
            F1_2_new=out[0][0][1]
            F1_3_new=out[0][0][2]
            F2_1_new=out[0][1][0]
            F2_2_new=out[0][1][1]
            F2_3_new=out[0][1][2]
            F3_1_new=out[0][2][0]
            F3_2_new=out[0][2][1]
            F3_3_new=out[0][2][2]
            F4_1_new=out[0][3][0]
            F4_2_new=out[0][3][1]
            F4_3_new=out[0][3][2]
            R1=F1_1_new+F2_1_new+F3_1_new+F4_1_new
            R2=F1_2_new+F2_2_new+F3_2_new+F4_2_new
            R3=F1_3_new+F2_3_new+F3_3_new+F4_3_new
            context={
                "trans_name":trans_name,
                "F1_1":F1_1,
                "F1_2":F1_2,
                "F1_3":F1_3,
                "F2_1":F2_1,
                "F2_2":F2_2,
                "F2_3":F2_3,
                "F3_1":F3_1,
                "F3_2":F3_2,
                "F3_3":F3_3,
                "F4_1":F4_1,
                "F4_2":F4_2,
                "F4_3":F4_3,
                
                "F1_1_new":F1_1_new,
                "F1_2_new":F1_2_new,
                "F1_3_new":F1_3_new,
                "F2_1_new":F2_1_new,
                "F2_2_new":F2_2_new,
                "F2_3_new":F2_3_new,
                "F3_1_new":F3_1_new,
                "F3_2_new":F3_2_new,
                "F3_3_new":F3_3_new,
                "F4_1_new":F4_1_new,
                "F4_2_new":F4_2_new,
                "F4_3_new":F4_3_new,
                "R1":R1,
                "R2":R2,
                "R3":R3,
                
            }
            
            return render(request, 'badebargiri.html', {'context': context})
    else:
        form = BargiriForm()

    return render(request, 'ghablebargiri.html', {'form': form})