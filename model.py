def calculate_score(top_class, non_Abuse):
    score_class = {"Abusive Image":0, "Non Abusive Image":0}
    for k, v in top_class.items():
        if k in non_Abuse:
            score_class["Non Abusive Image"] += v
        else:
            score_class["Abusive Image"] += v
    return score_class

def destroy_widget(label_text1):
    if label_text1 is not None:
        label_text1.destroy()