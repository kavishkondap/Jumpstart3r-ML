import pandas as pd
import numpy as np

data = pd.read_excel ('machineLearningData16.xlsx')

old_data = pd.read_excel ('OtherDataExcel.xlsx')
old_id = old_data ['id']
# old_locations = old_data ['location']
# old_locations = old_locations.str.strip ().str.replace ('\n', '')

curr_titles = data ['titles']
curr_blurbs = data ['blurbs']
curr_ids = data ['ids']

# id_positive_emotion = []
# id_negative_emotion = []
# id_sadness = []
# id_word_count = []

# id_count_unique_pos = []
# id_count_total_pos = []
# id_count_unique_neg = []
# id_count_total_neg = []
# id_count_total = []

# id_WC = []
# id_Analytic = []
# id_Clout = []
# id_Authentic = []
# id_Tone = []
# id_WPS = []
# id_Sixltr = []
# id_Dic = []
# id_function = []
# id_pronoun = []
# id_ppron = []
# id_i = []
# id_we = []
# id_you = []
# id_shehe = []
# id_they = []
# id_ipron = []
# id_article = []
# id_prep = []
# id_auxverb = []
# id_adverb = []
# id_conj = []
# id_negate = []
# id_verb = []
# id_adj = []
# id_compare = []
# id_interrog = []
# id_number = []
# id_quant = []
# id_affect = []
# id_posemo = []
# id_negemo = []
# id_anx = []
# id_anger = []
# id_sad = []
# id_social = []
# id_family = []
# id_friend = []
# id_female = []
# id_male = []
# id_cogproc = []
# id_insight = []
# id_cause = []
# id_discrep = []
# id_tentat = []
# id_certain = []
# id_differ = []
# id_percept = []
# id_see = []
# id_hear = []
# id_feel = []
# id_feel = []
# id_bio = []
# id_body = []
# id_health = []
# id_sexual = []
# id_ingest = []
# id_drives = []
# id_affiliation = []
# id_achieve = []
# id_power = []
# id_reward = []
# id_risk = []
# id_focuspast = []
# id_focuspresent = []
# id_focusfuture = []
# id_relativ = []
# id_motion = []
# id_space = []
# id_time = []
# id_work = []
# id_leisure = []
# id_home = []
# id_money = []
# id_relig = []
# id_death = []
# id_informal = []
# id_swear = []
# id_netspeak = []
# id_assent = []
# id_nonflu = []
# id_filler = []
# id_AllPunc = []
# id_Period = []
# id_Comma = []
# id_Colon = []
# id_SemiC = []
# id_QMark = []
# id_Exclam = []
# id_Dash = []
# id_Quote = []
# id_Apostro = []
# id_Parenth = []
# id_OtherP = []
# id_help = []

id_to_value = {
    'id_positive_emotion': {},
    'id_negative_emotion': {},
    'id_sadness': {},
    'id_wordcount': {},
    'id_count_unique_pos': {},
    'id_count_total_pos': {},
    'id_count_unique_neg': {},
    'id_count_total_neg': {},
    'id_count_total': {},
    'id_WC': {},
    'id_Analytic': {},
    'id_Clout': {},
    'id_Authentic': {},
    'id_Tone': {},
    'id_WPS': {},
    'id_Sixltr': {},
    'id_Dic': {},
    'id_function': {},
    'id_pronoun': {},
    'id_ppron': {},
    'id_i': {},
    'id_we': {},
    'id_you': {},
    'id_shehe': {},
    'id_they': {},
    'id_ipron': {},
    'id_article': {},
    'id_prep': {},
    'id_auxverb': {},
    'id_adverb': {},
    'id_conj': {},
    'id_negate': {},
    'id_verb': {},
    'id_adj': {},
    'id_compare': {},
    'id_interrog': {},
    'id_number': {},
    'id_quant': {},
    'id_affect': {},
    'id_posemo': {},
    'id_negemo': {},
    'id_anx': {},
    'id_anger': {},
    'id_sad': {},
    'id_social': {},
    'id_family': {},
    'id_friend': {},
    'id_female': {},
    'id_male': {},
    'id_cogproc': {},
    'id_insight': {},
    'id_cause': {},
    'id_discrep': {},
    'id_tentat': {},
    'id_certain': {},
    'id_differ': {},
    'id_percept': {},
    'id_see': {},
    'id_hear': {},
    'id_feel': {},
    'id_feel': {},
    'id_bio': {},
    'id_body': {},
    'id_health': {},
    'id_sexual': {},
    'id_ingest': {},
    'id_drives': {},
    'id_affiliation': {},
    'id_achieve': {},
    'id_power': {},
    'id_reward': {},
    'id_risk': {},
    'id_focuspast': {},
    'id_focuspresent': {},
    'id_focusfuture': {},
    'id_relativ': {},
    'id_motion': {},
    'id_space': {},
    'id_time': {},
    'id_work': {},
    'id_leisure': {},
    'id_home': {},
    'id_money': {},
    'id_relig': {},
    'id_death': {},
    'id_informal': {},
    'id_swear': {},
    'id_netspeak': {},
    'id_assent': {},
    'id_nonflu': {},
    'id_filler': {},
    'id_AllPunc': {},
    'id_Period': {},
    'id_Comma': {},
    'id_Colon': {},
    'id_SemiC': {},
    'id_QMark': {},
    'id_Exclam': {},
    'id_Dash': {},
    'id_Quote': {},
    'id_Apostro': {},
    'id_Parenth': {},
    'id_OtherP': {},
    'id_help': {}
}

# count = 0
# for i in range (len (old_id)):
#     if (old_id [i] )

# curr_id = data ['ids']
# old_id = old_data ['id']

# id_to_location = {}
count = 0
for i in range (len (old_id)):
    for key in id_to_value.keys ():
        id_to_value[key]
        id_to_value[key][old_id[i]] = old_data[key[3:]][i]
        # print (id_to_location)
    count+=1
    print (count)

values_to_df = {
    'id_positive_emotion': [],
    'id_negative_emotion': [],
    'id_sadness': [],
    'id_wordcount': [],
    'id_count_unique_pos': [],
    'id_count_total_pos': [],
    'id_count_unique_neg': [],
    'id_count_total_neg': [],
    'id_count_total': [],
    'id_WC': [],
    'id_Analytic': [],
    'id_Clout': [],
    'id_Authentic': [],
    'id_Tone': [],
    'id_WPS': [],
    'id_Sixltr': [],
    'id_Dic': [],
    'id_function': [],
    'id_pronoun': [],
    'id_ppron': [],
    'id_i': [],
    'id_we': [],
    'id_you': [],
    'id_shehe': [],
    'id_they': [],
    'id_ipron': [],
    'id_article': [],
    'id_prep': [],
    'id_auxverb': [],
    'id_adverb': [],
    'id_conj': [],
    'id_negate': [],
    'id_verb': [],
    'id_adj': [],
    'id_compare': [],
    'id_interrog': [],
    'id_number': [],
    'id_quant': [],
    'id_affect': [],
    'id_posemo': [],
    'id_negemo': [],
    'id_anx': [],
    'id_anger': [],
    'id_sad': [],
    'id_social': [],
    'id_family': [],
    'id_friend': [],
    'id_female': [],
    'id_male': [],
    'id_cogproc': [],
    'id_insight': [],
    'id_cause': [],
    'id_discrep': [],
    'id_tentat': [],
    'id_certain': [],
    'id_differ': [],
    'id_percept': [],
    'id_see': [],
    'id_hear': [],
    'id_feel': [],
    'id_feel': [],
    'id_bio': [],
    'id_body': [],
    'id_health': [],
    'id_sexual': [],
    'id_ingest': [],
    'id_drives': [],
    'id_affiliation': [],
    'id_achieve': [],
    'id_power': [],
    'id_reward': [],
    'id_risk': [],
    'id_focuspast': [],
    'id_focuspresent': [],
    'id_focusfuture': [],
    'id_relativ': [],
    'id_motion': [],
    'id_space': [],
    'id_time': [],
    'id_work': [],
    'id_leisure': [],
    'id_home': [],
    'id_money': [],
    'id_relig': [],
    'id_death': [],
    'id_informal': [],
    'id_swear': [],
    'id_netspeak': [],
    'id_assent': [],
    'id_nonflu': [],
    'id_filler': [],
    'id_AllPunc': [],
    'id_Period': [],
    'id_Comma': [],
    'id_Colon': [],
    'id_SemiC': [],
    'id_QMark': [],
    'id_Exclam': [],
    'id_Dash': [],
    'id_Quote': [],
    'id_Apostro': [],
    'id_Parenth': [],
    'id_OtherP': [],
    'id_help': []
}

# total_wrong = 0
# count = 0
# for id in curr_id:
#     locations.append (id_to_location[id])
#     count+=1
#     print (count)

count = 0
for id in curr_ids:
    for key in id_to_value.keys ():
        values_to_df [key].append (id_to_value[key][id])
    count+=1
    print (count)

for key in values_to_df.keys ():
    data [key] = values_to_df[key]

data.to_excel ('machineLearningData17.xlsx')

# data ['locations'] = locations
# data.to_excel ('machineLearningData9.xlsx', index = False)