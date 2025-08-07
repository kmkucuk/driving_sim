import pandas as pd
from pathlib import Path
import random
def getClutterOrderCounterbalanceGroup(order_file = "clutter_change_order_cb.xlsx", cb_group = "1", practice_change_count = 10):
    if not isinstance(cb_group, str):
        raise ValueError(f"Counterbalance group is not entered as string {cb_group}, its type is instead {type(cb_group)}")

    xlsx_path = Path(order_file)

    df = pd.read_excel(xlsx_path)

    df.columns = [str(c).strip().lower() for c in df.columns]

    df.head(), df.columns.tolist()
    required = {"blocks", "block_trial_#", "gr1", "gr2", "gr3", "gr4"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    def block_num(s):
        try:
            return int(str(s).split()[-1])
        except Exception:
            return str(s)

    grouped = sorted(df.groupby("blocks"), key=lambda kv: block_num(kv[0]))

    gr_lists = {"gr1": [], "gr2": [], "gr3": [], "gr4": []}
    block_labels = []

    for block_label, g in grouped:
        block_labels.append(block_label)
        for gr in gr_lists.keys():
            idx = g.loc[g[gr].astype(int) == 1, "block_trial_#"].astype(int).tolist()
            gr_lists[gr].append(idx)

    random_practice_indices = random.sample(range(0, 40), practice_change_count)
    random_practice_indices.sort()
    gr_lists["gr" + cb_group].insert(0, random_practice_indices)
    selected_list = gr_lists["gr" + cb_group]
    print(f"Selected clutter change order group {cb_group} indices are: {selected_list}")
    return selected_list
    



    
a=0